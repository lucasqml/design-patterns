from handlers.handler import Handler
from exceptions.order_processing_exception import OrderProcessingException

class InventoryCheckHandler(Handler):
    def handle(self, order):
        if order.in_stock:
            print("Inventory check passed.")
        else:
            print("Inventory check failed.")
            raise OrderProcessingException("Inventory check failed.")
        super().handle(order)