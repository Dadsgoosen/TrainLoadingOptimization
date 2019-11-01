import datetime
from typing import List

from Events.Event import Event
from Events.ReceiveWeightEvent import ReceiveWeightEvent
from Events.SendWeightEvent import SendWeightEvent
from Runtimes.Configuration import Configuration
from Runtimes.Environment import Environment


class WeighTrainEvent(Event):
    """
    Event when the train gets weighed.
    The train is weighed by summing all the passenger weights together
    """
    def __init__(self, timestamp: datetime, configuration: Configuration):
        super().__init__(timestamp, configuration)

    def fire(self, environment: Environment) -> List[Event]:
        # Adding all the passengers weights together
        # and storing it in the train weight property
        super().log_event()
        for train_set in environment.train.train_sets:
            for train_car in train_set.cars:
                for passenger in train_car.passengers:
                    train_car.weight += passenger.weight
                environment.train.weight += train_car.weight
        return {SendWeightEvent(self.timestamp + datetime.timedelta(seconds= + self.configuration.time_send_weight_event), self.configuration)}