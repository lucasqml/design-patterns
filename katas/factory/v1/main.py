from logistics.sea_logistic import SeaLogistics
from logistics.road_logistic import RoadLogistics
# Importe a classe AirLogistics se você a tiver implementado

class Main:
    @staticmethod
    def run_logistics():
        logistics_type = input("Enter logistics type (sea, road): ")

        if logistics_type == 'sea':
            logistics = SeaLogistics()
        elif logistics_type == 'road':
            logistics = RoadLogistics()
        # Adicione uma condição para AirLogistics se você a tiver implementado
        else:
            raise ValueError("Invalid logistics type")

        transport = logistics.create_transport()
        print(transport.deliver())

# Para usar
if __name__ == "__main__":
    Main.run_logistics()