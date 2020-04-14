import abc  # Python's abstract class library
import numpy as np


# Gets the route grading distribution for new sets
def routeDistr(str):
    # We can make this cooler later, right now just adds more moderate routes than easy or hard
    if str == "boulder":
        return [0.1, 0.1, 0.13, 0.14, 0.13, 0.12, 0.1, 0.08, 0.045, 0.025, 0.025, 0.005]
    if str == "bigwall":
        return [0.05, 0.05, 0.1, 0.1, 0.15, 0.15, 0.15, 0.15, 0.05, 0.05]

    print("Invalid input")
    return


class SettingBehavior(object):
    # This is how an abstract class is defined
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def setRoutes(self, wallSize):
        """Required Method"""


# Unique behavior for setting the routes in bouldering and big walls
class SettingBoulder(SettingBehavior):

    def __init__(self, gradesIn):
        self.grades = gradesIn

    def setRoutes(self, wallSize):
        # Get a sample of grades for size of area
        routes = np.random.choice(self.grades, wallSize, True, routeDistr('boulder'))
        # Sorts by taking away first character(ex V10 -> 10)
        return sorted(routes, key=lambda x: int(x[1:]))


class SettingBigWall(SettingBehavior):

    def __init__(self, gradesIn):
        self.grades = gradesIn

    def setRoutes(self, wallSize):
        # Get a sample of grades for size of area
        routes = np.random.choice(self.grades, wallSize, True, routeDistr('bigwall'))
        # Sorts by taking away first two characters(ex. 5.10 -> 10)
        return sorted(routes, key=lambda x: int(x[2:]))
