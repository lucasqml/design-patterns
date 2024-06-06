from .logistics import Logistics
from app.models.plane import Plane

class AirLogistic(Logistics):
    def create_transport(self):
        return Plane()