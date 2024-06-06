import pytest
from app.models.truck import Truck
from app.factory.transport_factory import TransportFactory
from app.models.ship import Ship
from app.models.plane import Plane

def test_create_truck():
    factory = TransportFactory()
    transport = factory.create_transport("truck")
    assert isinstance(transport, Truck)

def test_create_ship():
    factory = TransportFactory()
    transport = factory.create_transport("ship")
    assert isinstance(transport, Ship)

def test_create_plane():
    factory = TransportFactory()
    transport = factory.create_transport("plane")
    assert isinstance(transport, Plane)

def test_invalid_transport_type():
    factory = TransportFactory()
    with pytest.raises(ValueError):
        factory.create_transport("elephant")