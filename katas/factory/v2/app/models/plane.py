from app.models.transport import Transport


class Plane(Transport):
    def deliver(self):
        return "Delivering by air in a plane"