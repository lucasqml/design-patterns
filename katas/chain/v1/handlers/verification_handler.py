from handlers.handler import Handler
from exceptions.order_processing_exception import OrderProcessingException

class ValidationHandler(Handler):
    def handle(self, order):
        if order.valid:
            print("Order details are valid.")
        else:
            print("Order validation failed.")
            raise OrderProcessingException("Order validation failed.")
        super().handle(order)