import asyncio
import json
from typing import Dict, Iterable, Optional
from pydantic import BaseModel
import yaml

from openai import AsyncOpenAI
from openai.helpers import LocalAudioPlayer

openai = AsyncOpenAI()

# Load configuration from YAML
with open("config/openai_config.yaml", "r", encoding="utf8") as f:
    config = yaml.safe_load(f)

# Fields from YAML
fields = config["fields"]


class Glyph(BaseModel):
    vocab: str
    target_language_definition: str
    source_language_definition: str
    example_sentence: Optional[str] = None
    translation: Optional[str] = None


async def fetch_fields(
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

    for name, details in fields.items():
        if details.get("mvp"):
            print(f"MVP field: {name}")
            print(f"Description: {details['description']}")

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

    return {
        "example": parsed.get("example"),
        "translation": parsed.get("translation"),
        "raw": content,
    }


async def open_ai_tts() -> None:
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
    asyncio.run(open_ai_tts())
    # Simple demo: run the TTS demo and then an example fetch if an API key is set.
