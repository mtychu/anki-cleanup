import asyncio
import json
from typing import Dict, Iterable, Optional

from openai import AsyncOpenAI
from openai.helpers import LocalAudioPlayer

openai = AsyncOpenAI()


async def fetch_example_and_definition(
    vocab: str,
    target_language: str = "Chinese",
    translation_language: str = "English",
    model: str = "gpt-4o-mini",
    max_tokens: int = 200,
    temperature: float = 0.2,
) -> Optional[Dict[str, str]]:
    """Fetch one example sentence in `language` for `vocab` and its translation.

    Returns a dict: {"example": str, "translation": str, "raw": str} on
    success, or None on failure. The assistant MUST return strict JSON with
    the keys "example" and "translation". Non-JSON responses are rejected to
    keep parsing predictable.
    """

    prompt = (
        f"Provide exactly one natural example sentence that uses the word '{vocab}' "
        f"in {target_language}. Also provide a concise translation of that example into "
        f'{translation_language}. Return valid JSON with two keys: "example" '
        f'(the example in {target_language}) and "translation" (the translation in '
        f"{translation_language}). The example must be exactly one sentence."
    )

    try:
        resp = await openai.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature,
        )
    except Exception as e:
        # Let the caller decide how to handle connectivity/auth errors
        print(f"OpenAI request failed: {e}")
        return None

    # The SDK returns a structure with choices -> message -> content
    try:
        content = resp.choices[0].message.content
    except Exception:
        # Fallback: try to stringify the whole response
        content = str(resp)

    # Parse the assistant content strictly as JSON. If parsing fails, return None.
    try:
        parsed = json.loads(content)
    except Exception:
        # Non-JSON responses are rejected for now to keep parsing simple.
        return None

    if not isinstance(parsed, dict):
        return None

    # Validate required keys
    required_keys = ["example", "translation"]

    missing = [k for k in required_keys if k not in parsed or not parsed.get(k)]
    if missing:
        # missing required keys -> reject
        return None

    return {
        "example": parsed.get("example"),
        "translation": parsed.get("translation"),
        "raw": content,
    }


async def tts_demo() -> None:
    """Small demo that plays a short sentence using the TTS helper in the SDK."""
    async with openai.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="nova",
        input="彼女は背の高い男性を好みますね。",
        instructions="use a neutral tone",
        response_format="pcm",
    ) as response:
        await LocalAudioPlayer().play(response)


if __name__ == "__main__":
    # Simple demo: run the TTS demo and then an example fetch if an API key is set.
    asyncio.run(tts_demo())
