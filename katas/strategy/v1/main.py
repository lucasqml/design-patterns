from competitor import Competitor
from sports_event_simulator import SportsEventSimulator
from marathon_strategy import MarathonStrategy
from ten_km_strategy import TenKmStrategy
from triathlon_strategy import TriathlonStrategy
from marshal1 import Marshal1 # type: ignore

simulator = SportsEventSimulator()
simulator.add_participant(Competitor(MarathonStrategy()))
simulator.add_participant(Competitor(TenKmStrategy()))
simulator.add_participant(Competitor(TriathlonStrategy()))
simulator.add_participant(Marshal1())
simulator.start_event()