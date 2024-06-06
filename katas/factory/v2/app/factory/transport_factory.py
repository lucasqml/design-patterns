from app.models.truck import Truck
from app.models.ship import Ship
from app.models.plane import Plane

class TransportFactory:
    def create_transport(self, transport_type):
        if transport_type == "truck":
            return Truck()
        elif transport_type == "ship":
            return Ship()
        elif transport_type == "plane":
            return Plane()
        else:
            raise ValueError(f"Invalid transport type")