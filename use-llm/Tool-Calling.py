from llama_index.core.tools import FunctionTool
from llama_index.llms.ollama import Ollama
from typing import TypedDict


class Song(TypedDict):
    name: str
    artist: str

def generate_song(name: str, artist: str) -> Song:
    """Generates a song with provided name and artist."""
    return {"name": name, "artist": artist}


tool = FunctionTool.from_defaults(fn=generate_song)

# 初始化 Ollama
llm = Ollama(model="qwen2.5:7b", request_timeout=60.0)
response = llm.predict_and_call(
    [tool],
    "Pick a random chinese song for me",
)
print(str(response))