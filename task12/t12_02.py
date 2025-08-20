from __future__ import annotations
import sys, os, requests
from dataclasses import dataclass
from typing import Any
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY_ID = os.getenv("OPENWEATHER_CITY_ID")
UNITS = os.getenv("OPENWEATHER_UNITS", "metric")

if not API_KEY:
    print("OPENWEATHER_API_KEY puuttuu", file=sys.stderr)
    sys.exit(1)

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@dataclass
class Weather:
    place: str
    description: str
    temp_c: float

    @classmethod
    def from_openweather(cls, payload: dict[str, Any]) -> "Weather":
        name = payload.get("name") or "Tuntematon"
        weather_list = payload.get("weather") or []
        description = (weather_list[0]["description"] if weather_list else "n/a").capitalize()

        main = payload.get("main") or {}
        if "temp" in main:
            temp_c = float(main["temp"])
        elif "temp_k" in main:
            temp_c = float(main["temp_k"]) - 273.15
        else:
            temp_k = float(main.get("temp", 0.0))
            temp_c = temp_k - 273.15

        return cls(place=name, description=description, temp_c=temp_c)

def fetch_weather_by_city_name(city_name: str) -> Weather:
    params = {
        "appid": API_KEY,
        "q": city_name,
        "units": UNITS,
        "lang": "fi",
    }
    r = requests.get(BASE_URL, params=params, timeout=10)
    _raise_for_openweather(r)
    return Weather.from_openweather(r.json())

def fetch_weather_by_city_id(city_id: str) -> Weather:
    params = {
        "appid": API_KEY,
        "id": city_id,
        "units": UNITS,
        "lang": "fi",
    }
    r = requests.get(BASE_URL, params=params, timeout=10)
    _raise_for_openweather(r)
    return Weather.from_openweather(r.json())

def _raise_for_openweather(resp: requests.Response) -> None:
    try:
        resp.raise_for_status()
    except requests.HTTPError as e:
        try:
            msg = resp.json().get("message")
        except Exception:
            msg = None
        if msg:
            raise SystemExit(f"{msg} (HTTP {resp.status_code})") from e
        raise

def main() -> None:
    if CITY_ID:
        weather = fetch_weather_by_city_id(CITY_ID)
    else:
        city = input("Anna paikkakunta: ").strip()
        if not city:
            print("Ei paikkakuntaa annettu, heippa.")
            sys.exit(0)
        weather = fetch_weather_by_city_name(city)

    print(f"Sää – {weather.place}: {weather.description}, {weather.temp_c:.1f} °C")

if __name__ == "__main__":
    main()
