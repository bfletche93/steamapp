import logging
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from models import Base

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)

logger.info("Starting app")
db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://steamapp_user:example@db:5432/steamapp"
# initialize the app with the extension
db.init_app(app)

with app.app_context():
    db.create_all()

logger.info("Completed app")