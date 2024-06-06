import pytest
from app.logistics.road_logistic import RoadLogistic
from app.logistics.sea_logistic import SeaLogistic
from app.logistics.air_logistic import AirLogistic

def test_road_logistics():
    logistics = RoadLogistic()
    transport = logistics.create_transport()
    assert transport.deliver() == "Delivering by road in a truck"

def test_sea_logistics():
    logistics = SeaLogistic()
    transport = logistics.create_transport()
    assert transport.deliver() == "Delivering by sea in a ship"

def test_air_logistics():
    logistics = AirLogistic()
    transport = logistics.create_transport()
    assert transport.deliver() == "Delivering by air in a plane"