import pytest
from app.models.truck import Truck
from app.models.ship import Ship
from app.models.plane import Plane

def test_road_logistics():
    truck = Truck()
    assert truck.deliver() == "Delivering by road in a truck"

def test_sea_logistics():
    ship = Ship()
    assert ship.deliver() == "Delivering by sea in a ship"

def test_air_logistics():
    plane = Plane()
    assert plane.deliver() == "Delivering by air in a plane"