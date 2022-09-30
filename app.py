from shiny import App

from server import app_server
from ui import app_ui


app = App(app_ui, app_server, debug=True)