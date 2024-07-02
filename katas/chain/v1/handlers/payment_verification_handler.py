from handlers.handler import Handler
from exceptions.order_processing_exception import OrderProcessingException

class PaymentVerificationHandler(Handler):
    def handle(self, order):
        if order.payment_info:
            print("Payment verified.")
        else:
            print("Payment verification failed.")
            raise OrderProcessingException("Payment verification failed.")
        super().handle(order)
