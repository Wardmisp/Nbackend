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