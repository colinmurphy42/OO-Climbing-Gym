import abc  # Python's abstract class library
import numpy as np


class SettingBehavior(object):
    # This is how an abstract class is defined
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def setRoutes(self, wallSize):
        """Required Method"""


# Unique behavior for setting the routes in bouldering and big walls
class SettingBoulder(SettingBehavior):

    def __init__(self):
        self.grades = ["V0", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10"]

    def setRoutes(self, wallSize):
        # Get a sample of grades for size of area
        routes = np.random.choice(self.grades, wallSize, True)
        # Sorts by taking away first character(ex V10 -> 10)
        return sorted(routes, key=lambda x: int(x[1:]))


class SettingBigWall(SettingBehavior):

    def __init__(self):
        self.grades = ["5.6", "5.7", "5.8", "5.9", "5.10", "5.11", "5.12", "5.13", "5.14"]

    def setRoutes(self, wallSize):
        # Get a sample of grades for size of area
        routes = np.random.choice(self.grades, wallSize, True)
        # Sorts by taking away first two characters(ex. 5.10 -> 10)
        return sorted(routes, key=lambda x: int(x[2:]))