import unittest
from Distributions.NormalDistribution import NormalDistribution
from Runtimes import ApplicationRuntime


class TestReceivedWeightEvent(unittest.TestCase):
    """
    A class to test received weight events.
    """

    def setUp(self) -> None:
        self.options: dict = {
            "passenger_weight_distribution": NormalDistribution(80, 10),
            "passenger_mean_weight": 80,
            "passenger_speed_range": range(5, 10),
            "passenger_loading_time_range": range(1, 3),
            "passenger_regular_size": 0.5,
            "passenger_max_walk_range": range(0, 6),
            "passenger_compliance": 0.8,
            "train_capacity": 75,
            "train_fullness": range(40, 80),
            "train_unload_percent": range(30, 50),
            "train_set_setup": 4,
            "train_amount_of_sets": 2,
            "train_park_at_index": None,
            "station_sector_count": 16,
            "station_distance": 3.0,
            "station_stairs_placement": [3],
            "station_sector_passenger_max_count": 25,
            "station_sector_fullness": range(20, 50),
            "station_stair_factor": 1.5,
            "station_light_thresholds": {"green": .5, "yellow": .75},
            "time_arrive_event": 60,
            "time_depart_event": 0,
            "time_load_passenger_event": 1,
            "time_unload_passenger_event": 1,
            "time_passenger_decision_event": 5,
            "time_receive_weight_event": 10,
            "time_send_weight_event": 0,
            "time_weigh_train_event": 3,
            "time_door_action": 4
        }
        self.runtime = ApplicationRuntime.ApplicationRunTime(self.options)

    def test_station_lights(self):
        """
        Test whether the non-marginal station sectors have light.
        """
        self.runtime.run()
        for sector in self.runtime.environment.station.sectors:
            if sector.train_car:
                self.assertIsNotNone(sector.light.status)
            else:
                self.assertIsNone(sector.light.status)

    def test_station_has_passengers(self):
        """
        Test whether the station has passengers on it.
        """
        self.options['station_sector_passenger_max_count'] = 100
        self.options['station_sector_fullness'] = range(10, 10)
        self.runtime.run()

        # for loop for sectors, check passengers
        for sector in self.runtime.environment.station.sectors:
            print("amount: ", sector.amount)

    def tearDown(self) -> None:
        pass