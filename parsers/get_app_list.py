from sqlalchemy import update

from datetime import datetime
from typing import Dict

from models import SteamApp

def make_steam_app(app_list_entry: Dict, now: datetime) -> SteamApp:
    app = SteamApp(**app_list_entry)
    app.in_app_list = True
    app.last_seen_in_app_list = now
    return app

def process_app_list(session, app_list: Dict):
    update_in_app_list_stmt = update(SteamApp).values(in_app_list=False)
    session.execute(update_in_app_list_stmt)

    now = datetime.now()

    for item in app_list:
        steam_app = make_steam_app(item, now)
        session.merge(steam_app)

    session.commit()