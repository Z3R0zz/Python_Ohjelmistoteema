import requests
from dataclasses import dataclass

@dataclass
class Joke:
    id: str
    value: str
    icon_url: str
    url: str
    categories: list[str]
    created_at: str
    updated_at: str

resp = requests.get("https://api.chucknorris.io/jokes/random")
resp.raise_for_status()

data = resp.json()

joke = Joke(**data)

print(joke.value)
