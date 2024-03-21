from selenium.webdriver.common.by import By


class GameLocators:
    """
    Locators for elements related to actions that can be performed during the game.
    """

    ROLL_DICES_BUTTON = By.CSS_SELECTOR, ".zrAsGo65 > div:nth-child(1) > button:nth-child(1)"
    ROLL_DICES_AGAIN_BUTTON = (By.CSS_SELECTOR, ".s3FE4qke")
    BUY_PROPERTY_BUTTON = (By.CSS_SELECTOR, "div._YZ7dkIA:nth-child(2) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)")
    END_TURN_BUTTON = (By.CSS_SELECTOR, "div._YZ7dkIA:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)")
    AUCTION_BUTTON = (By.CSS_SELECTOR, "div._YZ7dkIA:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)")
    AUCTION_CURRENT_BID = (By.CSS_SELECTOR, ".LJ72TaNX > span:nth-child(2)")
    AUCTION_BID_2_BUTTON = (By.CSS_SELECTOR, "div._YZ7dkIA:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)")
    AUCTION_BID_10_BUTTON = (By.CSS_SELECTOR, "div._YZ7dkIA:nth-child(2) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)")
    AUCTION_BID_100_BUTTON = (By.CSS_SELECTOR, "div._YZ7dkIA:nth-child(3) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)")
    CREATE_TRADE_BUTTON = (By.CLASS_NAME, "yCokhJwL")
    LIST_PLAYER_TRADE_DIV = (By.CLASS_NAME, "qS3VjzBC")
    SELECT_PLAYER_TRADE_BUTTON = (By.TAG_NAME, "button")
    BANKRUPT_BUTTON = (By.CLASS_NAME, "r44rmzzs")
    BANKRUPT_CONFIRM_BUTTON = (By.CSS_SELECTOR, "button.erpKMsiA:nth-child(6)")
    VOTEKICK_BUTTON = (By.CLASS_NAME, ".Gfj962li")


class MainLocators:
    """
    Locators for elements not related to authentication or playing the game.
    """

    CONNECTION_STATUS = (By.CLASS_NAME, 'zXywqvFA')
    CREATE_GAME_BUTTON = By.XPATH, "//div[@class='vSsot1FM']//button[2]"
    CREATE_GAME_BUTTON_ALT = (By.CSS_SELECTOR, "button.erpKMsiA:nth-child(2)")  # A tester
    PLAYER_USERNAME_INPUT = (By.CLASS_NAME, "bqnTeikf")
    PLAY_GAME_BUTTON = (By.CLASS_NAME, "UeVPCIu4")
    JOIN_GAME_BUTTON = (By.CLASS_NAME, "KDf8glTM")
    LIST_SKIN_DIV = (By.XPATH, "/html/body/div[1]/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[1]")
    SELECT_SKIN_BUTTON = (By.TAG_NAME, "button")
    START_GAME_BUTTON = (By.CSS_SELECTOR, ".zrAsGo65 > div:nth-child(1) > button:nth-child(1)")
    LIST_PLAYER_DIV = (By.CLASS_NAME, "WfhNQqdL")
    PLAYER_DIV = (By.TAG_NAME, "div")
    BACK_TO_LOBBY_BUTTON = (By.XPATH, ".//div[@class='f23yMqdp']//button[2]")


class LoginLocators:
    """
    Locators for elements related to the authentication.
    """

    LOGIN_MENU_BUTTON = (By.CLASS_NAME, "X2UE01gz")
    DISCORD_LOGIN_BUTTON = (By.CLASS_NAME, "mBWkZ6KB")
    DISCORD_USERNAME_INPUT = (By.NAME, "email")
    DISCORD_PASSWORD_INPUT = (By.NAME, "password")
    DISCORD_LOGIN_FORM_SUBMIT_BUTTON = (By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/button[2]")
    DISCORD_LOGIN_FORM_SUBMIT_BUTTON_ALT = (By.CSS_SELECTOR, "button.marginBottom8_f4aae3")  # A tester
    DISCORD_AUTHORIZE_BUTTON = (By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/div/div/div[2]/button[2]")
    DISCORD_AUTHORIZE_BUTTON_ALT = (By.CSS_SELECTOR, "button.button_afdfd9:nth-child(2)")  # A tester


class PopupLocators:
    """
    Locators for elements related to pop-up interfaces.
    """

    POPUP_BUTTON = (By.CLASS_NAME, "css-47sehv")


class CookieLocators:
    """
    Locators for elements related to cookie consent interfaces.
    """

    COOKIE_BUTTON = (By.CLASS_NAME, "cmpboxbtnyes")
