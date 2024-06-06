from .logistics import Logistics
from models.truck import Truck

class RoadLogistics(Logistics):
    def create_transport(self):
        return Truck()