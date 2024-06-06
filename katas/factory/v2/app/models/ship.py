from app.models.transport import Transport


class Ship(Transport):
    def deliver(self):
        return "Delivering by sea in a ship"