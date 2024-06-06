from app.models.transport import Transport


class Truck(Transport):
    def deliver(self):
        return "Delivering by road in a truck"