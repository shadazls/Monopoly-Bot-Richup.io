from typing import Optional

from selenium import webdriver
from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class MainActions:
    """
    A collection of static methods to perform common actions on web elements using Selenium.
    """

    @staticmethod
    def init_player(profile_path: str, url: str, window_position: Optional[str] = None) -> webdriver:
        """
        Initializes a new WebDriver instance for a player with the specified profile and navigates to the given URL.

        Args:
            profile_path (str): The path to the Firefox profile to be used for the new player.
            url (str): The URL to navigate the new player to.
            window_position (Optional[str], optional): The position of the browser window for the new player.
                Can be "right", "left", or None. Defaults is None.

        Returns:
            webdriver: A WebDriver instance for the new player.

        """

        new_player_firefox_options = webdriver.FirefoxOptions()
        new_player_firefox_options.profile = profile_path

        new_player = webdriver.Firefox(options=new_player_firefox_options)
        new_player.get(url)

        if window_position == "left":
            new_player.set_window_position(0, 0)
            new_player.set_window_size(960, 1200)
        elif window_position == "right":
            new_player.set_window_position(960, 0)
            new_player.set_window_size(960, 1200)
        else:
            new_player.maximize_window()

        new_player.implicitly_wait(3)

        return new_player

    @staticmethod
    def click_element(driver: webdriver, locator: tuple[any, str]) -> bool:
        """
        Clicks on a web element located by the specified locator.

        Args:
            driver: A webdriver instance.
            locator: A tuple containing the locator strategy and value to locate the web element.

        Returns:
            bool: True if the element is successfully clicked.

        """
        element = WebDriverWait(driver, 3).until(ec.element_to_be_clickable(locator))
        element.click()
        return True

    @staticmethod
    def send_keys_to_element(driver: webdriver, locator: tuple[any, str], keys: str) -> bool:
        """
        Sends keys to a web element located by the specified locator.

        Args:
            driver: A webdriver instance.
            locator: A tuple containing the locator strategy and value to locate the web element.
            keys: The keys to be sent to the web element.

        Returns:
            bool: True if the keys are successfully sent to the element, False otherwise.
        """
        try:
            element = WebDriverWait(driver, 4).until(ec.visibility_of_element_located(locator))
            element.send_keys(keys)
            return True
        except TimeoutException:
            return False
