from .logistics import Logistics
from app.models.ship import Ship

class SeaLogistic(Logistics):
    def create_transport(self):
        return Ship()