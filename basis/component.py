from utils.extending import AutoExtendingSelectors
from utils.log import trace


class BaseComponent(object):
    __metaclass__ = AutoExtendingSelectors

    def __init__(self, driver, element):
        """
        :type driver: ContestoDriver
        :type element: ContestoWebElement
        """
        self.driver = driver
        self.element = element
        trace(self.__class__)
