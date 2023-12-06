import unittest

from unit_tests.hw2.model_vehicle.car import Car
from unit_tests.hw2.model_vehicle.motorcycle import Motorcycle
from unit_tests.hw2.model_vehicle.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car('audi','6000',2033)
        self.motorcycle = Motorcycle('yamaha','black',1960)

    def test_car_instance(self):
        self.assertIsInstance(self.car,Vehicle)

    def test_car_wheels(self):
        self.assertEqual(self.car.wheels_num,4)

    def test_moto_wheels(self):
        self.assertEqual(self.motorcycle.wheels_num,2)

    def test_car_speed(self):
        self.car.test_drive()
        self.assertEqual(self.car.speed,60)

    def test_car_park(self):
        self.car.test_drive()
        self.car.park()
        self.assertEqual(self.car.speed,0)

    def test_moto_speed(self):
        self.motorcycle.test_drive()
        self.assertEqual(self.motorcycle.speed,75)

    def test_moto_park(self):
        self.motorcycle.test_drive()
        self.motorcycle.park()
        self.assertEqual(self.motorcycle.speed, 0)


if __name__ == '__main__':
    unittest.main()