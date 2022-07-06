import psycopg2
from datetime import datetime

class DashboardController():
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def initial_values(self, parent):
        self.model.initial_values(parent)
