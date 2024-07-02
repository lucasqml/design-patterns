# Creating the handlers
from exceptions.order_processing_exception import OrderProcessingException
from handlers.inventory_check_handler import InventoryCheckHandler
from handlers.payment_verification_handler import PaymentVerificationHandler
from handlers.shipping_confirmation_handler import ShippingConfirmationHandler
from handlers.verification_handler import ValidationHandler
from models.order import Order


validation_handler = ValidationHandler()
inventory_handler = InventoryCheckHandler()
payment_handler = PaymentVerificationHandler()
shipping_handler = ShippingConfirmationHandler()

validation_handler.set_next(inventory_handler).set_next(payment_handler).set_next(shipping_handler)

order = Order(valid=True, in_stock=True, payment_info=True, shipping_details=True)

try:
    validation_handler.handle(order)
    print("Order processed successfully.")
except OrderProcessingException as e:
    print(f"Order processing failed: {e}")


orderWithoutPayment = Order(valid=True, in_stock=True, payment_info=False, shipping_details=True)

try:
    validation_handler.handle(orderWithoutPayment)
    print("Order processed successfully.")
except OrderProcessingException as e:
    print(f"Order processing failed: {e}")