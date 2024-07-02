from handlers.handler import Handler
from exceptions.order_processing_exception import OrderProcessingException

class ShippingConfirmationHandler(Handler):
    def handle(self, order):
        if order.shipping_details:
            print("Shipping confirmed.")
        else:
            print("Shipping confirmation failed.")
            raise OrderProcessingException("Shipping confirmation failed.")
        super().handle(order)