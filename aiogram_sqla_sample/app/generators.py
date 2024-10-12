import asyncio
from mistralai import Mistral
import os

from config import AI_TOKEN

async def generate(content):
    s = Mistral(
        api_key=AI_TOKEN,
    )
    res = await s.chat.complete_async(model="mistral-small-latest", messages=[
        {
            "content": content,
            "role": "user",
        },
    ])
    if res is not None:
        return res