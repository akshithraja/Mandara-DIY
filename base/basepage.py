from base.seleniumdriver import SeleniumDriver
from utilities.util import Util

class BasePage(SeleniumDriver):
    def __init__(self, driver):
        """
        Inits BasePage class

        Returns:
            None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()