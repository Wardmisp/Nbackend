import random

from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats


def get_eligible_players():
    """
    Retourne les joueurs ayant au moins une saison
    dans les statistiques de saison régulière.
    """

    all_players = players.get_players()

    eligible_players = []

    for player in all_players:
        if player["id"] is not None:
            eligible_players.append(player)

    return eligible_players


def get_player_seasons(player_id: int):
    """
    Récupère les saisons de saison régulière
    disponibles pour un joueur.
    """

    career = playercareerstats.PlayerCareerStats(
        player_id=player_id
    )

    df = career.season_totals_regular_season.get_data_frame()

    if df.empty:
        return []

    return df.to_dict(orient="records")


def get_random_player_season():
    """
    Choisit :
    1. un joueur aléatoire
    2. une saison aléatoire parmi ses saisons disponibles
    """

    # Joueur aléatoire
    all_players = get_eligible_players()

    if not all_players:
        raise Exception("Aucun joueur disponible")

    player = random.choice(all_players)

    # Ses saisons
    seasons = get_player_seasons(player["id"])

    if not seasons:
        raise Exception(
            f"Aucune saison disponible pour {player['full_name']}"
        )

    # Saison aléatoire
    season = random.choice(seasons)

    return {
        "player": {
            "id": player["id"],
            "name": player["full_name"],
        },
        "season": season,
    }
