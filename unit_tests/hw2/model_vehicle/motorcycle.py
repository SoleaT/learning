from unit_tests.hw2.model_vehicle.vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, company, model, release_year):
        wheels_num = 2
        speed = 0
        super().__init__(company, model, release_year, wheels_num, speed)

    def test_drive(self):
        self.speed = 75

    def park(self):
        self.speed = 0
