from competitor import Competitor

class SportsEventSimulator:
    def __init__(self):
        self.participants = []

    def add_participant(self, participant):
        self.participants.append(participant)

    def start_event(self):
        for participant in self.participants:
            print(participant.display())
            if isinstance(participant, Competitor):
                print(participant.compete())