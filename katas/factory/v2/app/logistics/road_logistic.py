from .logistics import Logistics
from app.models.truck import Truck

class RoadLogistic(Logistics):
    def create_transport(self):
        return Truck()