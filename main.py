from fastapi import FastAPI, HTTPException

from nba_service import get_random_player_season


app = FastAPI(
    title="NBA API",
    description="Backend NBA pour application Android",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "NBA API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }

///TEMPORARY
import requests
@app.get("/test-nba")
def test_nba():
    url = "https://stats.nba.com/stats/playercareerstats?PlayerID=2544"

    headers = {
        "Host": "stats.nba.com",
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/131.0.0.0 Safari/537.36"
        ),
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.nba.com/",
        "Origin": "https://www.nba.com",
        "Connection": "keep-alive",
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=60,
    )

    return {
        "status_code": response.status_code,
        "length": len(response.text),
        "data": response.json(),
    }
////  
@app.get("/random-player-season")
def random_player_season():

    try:
        result = get_random_player_season()

        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
