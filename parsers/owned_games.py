from typing import Dict

from models import SteamApp, User

def process_games(session, games: Dict, user_id: int):
    user = session.get(User, user_id)
    if user is None:
        user = User(user_id=user_id)
        session.add(user)

    user.owned_games.clear()

    for game in games:
        steamapp_id = game.get("appid")
        steamapp = session.get(SteamApp, steamapp_id)
        if not steamapp:
            name = game.get("name")
            steamapp = SteamApp(appid=steamapp_id, name=name)
            session.add(steamapp)
        user.owned_games.add(steamapp)

    session.commit()
