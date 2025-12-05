import asyncio
from typing import Dict, Iterable, Optional
from pydantic import BaseModel

from openai import OpenAI, AsyncOpenAI
from openai.helpers import LocalAudioPlayer

openai = AsyncOpenAI()


class ExampleSentence(BaseModel):
    target_language_sentence: str
    source_language_translation: str


# Sample BaseModel - TODO make the requested data dynamic
class Glyph(BaseModel):
    vocab: str
    target_language_definition: str
    source_language_definition: str
    example_sentences: list[ExampleSentence]


client = OpenAI()

# TODO: get data from dictionaries as well as AI.
# https://platform.openai.com/docs/guides/structured-outputs


def fetch_ai_vocab_data(
    vocab: str, target_language: str, source_language: str, example_count: int = 2
) -> Glyph:

    # OpenAI call for fetching AI vocab data
    response = client.responses.parse(
        model="gpt-5-nano-2025-08-07",
        input=[
            {
                "role": "system",
                "content": f"""You are a {target_language} language learning assistant.
                The student speaks {source_language}. Only the required structured
                output.""",
            },
            {
                "role": "user",
                "content": f"""
                For "{vocab}" in {target_language}, please return the following:
                - definition in {target_language}, key: target_language_definition
                - equivalent word(s) in {source_language}, key: source_language_definition
                - {example_count} example sentence(s) using "{vocab}", key: example_sentences
                  Each example sentence should have:
                  - the sentence in {target_language}, key: target_language_sentence
                  - the translation in {source_language}, key: source_language_translation""",
            },
        ],
        text_format=Glyph,
    )

    event = response.output_parsed
    print(event)
    return event


# TODO find alternative to OpenAI - This doesn't sound good or natural
# async def open_ai_tts() -> None:
#     """Small demo that plays a short sentence using the TTS helper in the SDK."""
#     async with openai.audio.speech.with_streaming_response.create(
#         model="gpt-4o-mini-tts",
#         voice="nova",
#         input="彼女は背の高い男性を好みますね。",
#         instructions="use a neutral tone",
#         response_format="pcm",
#     ) as response:
#         await LocalAudioPlayer().play(response)


if __name__ == "__main__":
    fetch_ai_vocab_data("鼻水", "Japanese", "English")
