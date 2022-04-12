from flask import Flask
from app.routes.routes_leads import bp as bp_leads


def init_app(app: Flask):
   
    app.register_blueprint(bp_leads)