import time
import logging
import os

from dotenv import load_dotenv
from selenium.common import WebDriverException
from selenium.webdriver.common.by import By

from locators import LoginLocators
from locators import MainLocators
from locators import GameLocators

from utils import MainActions

from selenium import webdriver

# Remise à 0 du fichier de logs s'il existe
if os.path.exists('app.log'):
    open('app.log', 'w').close()

# Configuration du système de journalisation
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Variables contenant les informations de connexion à discord
load_dotenv()
discord_username = os.getenv("DISCORD_USERNAME")
discord_password = os.getenv("DISCORD_PASSWORD")

firefox_main_player_profile_path = r"C:\Users\shada\AppData\Roaming\Mozilla\Firefox\Profiles\czvd66c6.Selenium_Main_Player"
firefox_secondary_player_profile_path = r"C:\Users\shada\AppData\Roaming\Mozilla\Firefox\Profiles\av9xb8wf.Selenium_Secondary_Player"

main_player = MainActions.init_player(firefox_main_player_profile_path, "https://richup.io/", "left")


def discord_login(username: str, password: str) -> None:
    """
    Logs into Discord using the provided username and password.

    Args:
        username (str): The username to log in with Discord.
        password (str): The password to log in with Discord.

    Returns:
        None
    """
    logging.info("Attempting to log in to Discord with username: %s", username)

    MainActions.click_element(main_player, LoginLocators.LOGIN_MENU_BUTTON)
    MainActions.click_element(main_player, LoginLocators.DISCORD_LOGIN_BUTTON)

    MainActions.send_keys_to_element(main_player, LoginLocators.DISCORD_USERNAME_INPUT, username)
    MainActions.send_keys_to_element(main_player, LoginLocators.DISCORD_PASSWORD_INPUT, password)
    MainActions.click_element(main_player, LoginLocators.DISCORD_LOGIN_FORM_SUBMIT_BUTTON)

    MainActions.click_element(main_player, LoginLocators.DISCORD_AUTHORIZE_BUTTON)

    logging.info("Successfully logged in to Discord as user: %s", username)


def create_farm_game() -> str:
    """
    Creates a new game.

    This function creates a new game with two players: the main player, who is logged in, and the secondary player, who is not logged in.
    The players will roll dices and ending their turns without making any other actions.
    The game will automatically end after 9 minutes for it to be counted.
    This mode is typically used for earning in-game coins, increasing karma score, and winrate.

    Returns:
        str: The created game's url.
    """
    logging.info("Initiating the creation of a new game (farm type).")

    time.sleep(2)
    MainActions.click_element(main_player, MainLocators.CREATE_GAME_BUTTON)

    MainActions.click_element(main_player, MainLocators.JOIN_GAME_BUTTON)
    logging.info("Successfully created and joined the game (main player).")

    new_game_url = main_player.current_url

    return new_game_url


def join_farm_game() -> None:
    """
    Joins an already created game as the second player.

    The function initiates the creation of a second player and joins them to a game already created by the first player.
    It opens a new browser window for the second player, handles popups and cookies,
    then clicks on the "Play" button followed by the "Join Game" button.

    """
    # TODO : Optimiser le code au niveau des popup/cookies pour gagner du temps (beaucoup de temps à gagner)
    logging.info("Joining an already created game as the second player.")
    time.sleep(2)
    MainActions.click_element(secondary_player, MainLocators.PLAY_GAME_BUTTON)
    MainActions.click_element(secondary_player, MainLocators.JOIN_GAME_BUTTON)
    logging.info("Successfully joined the game (secondary player).")


def start_farm_game() -> None:
    """
    Starts a farm type game.

    This function attempts to start the game of farm type. It clicks on the "Start Game" button
    and logs the success of starting the game.

    Returns:
        None
    """
    logging.info("Attempting to start the game (farm type).")
    MainActions.click_element(main_player, MainLocators.START_GAME_BUTTON)
    logging.info("Successfully started the game (farm type).")


def play_farm_game() -> None:
    """
    Plays a Monopoly game (farm type).

    This function actively plays a Monopoly game by rolling dices and ending turns.
    The game lasts for a duration of 9 minutes. Each player takes their turn alternatively.
    After the game ends, bankruptcy is declared by the secondary player, and the players are returned to the lobby.

    Returns:
        None
    """
    logging.info("Starting the Monopoly game.")

    duree_partie = 9 * 60
    heure_debut = time.time()
    turns_completed = 0
    elapsed_minutes = 0

    try:

        # MainActions.click_element(main_player, GameLocators.ROLL_DICES_BUTTON)
        main_player.find_element(By.CSS_SELECTOR, ".zrAsGo65 > div:nth-child(1) > button:nth-child(1)")
        tour_actuel = 1

    except WebDriverException:

        tour_actuel = 2

    while time.time() - heure_debut < duree_partie:

        elapsed_time = time.time() - heure_debut
        current_elapsed_minutes = int(elapsed_time / 60)

        if current_elapsed_minutes > elapsed_minutes:
            elapsed_minutes = current_elapsed_minutes
            logging.info(f"{elapsed_minutes} minutes have elapsed.")
            logging.info(f"{turns_completed} turns has been completed.")

        if tour_actuel == 1:
            logging.info("Main player's turn.")
            turns_completed += 1
            play_turn(main_player)
            tour_actuel = 2

        else:
            logging.info("Secondary player's turn.")
            turns_completed += 1
            play_turn(secondary_player)
            tour_actuel = 1

    logging.info("Secondary player is declaring bankruptcy.")
    declare_bankruptcy()

    logging.info("Successfully ended the game, returning to the lobby.")
    MainActions.click_element(main_player, MainLocators.BACK_TO_LOBBY_BUTTON)


def play_turn(player: webdriver) -> None:
    """
    Plays a turn for the specified player.

    This function launch a player's turn in a Monopoly game (farm type) by performing actions such as rolling the dices and ending the turn.
    If necessary, the player may roll the dices multiple times.

    Args:
        player: The player for whom the turn is played.

    Returns:
        None
    """
    try:
        MainActions.click_element(player, GameLocators.ROLL_DICES_BUTTON)  # Lancer les dés une première fois
    except WebDriverException:
        return  # ???
    """
    if MainActions.click_element(player, GameLocators.END_TURN_BUTTON):  # Terminer son tour
        return  # 1
    elif MainActions.click_element(player, GameLocators.ROLL_DICES_AGAIN_BUTTON):  # Lancer les dés une deuxième fois (car terminer tour n'a pas fonctionné)
        if MainActions.click_element(player, GameLocators.END_TURN_BUTTON):  # Terminer son tour
            return  # 2
        elif MainActions.click_element(player, GameLocators.ROLL_DICES_AGAIN_BUTTON):  # Lancer les dés une troisième fois (car terminer tour n'a pas fonctionné)
            if MainActions.click_element(player, GameLocators.END_TURN_BUTTON):  # Terminer son tour
                return  # 3
            else:
                return  # 6
        else:
            return  # 4
    else:
        return  # 5
    """

    try:

        MainActions.click_element(player, GameLocators.END_TURN_BUTTON)
        return  # 1

    except WebDriverException:

        try:

            MainActions.click_element(player, GameLocators.ROLL_DICES_AGAIN_BUTTON)

            try:

                MainActions.click_element(player, GameLocators.END_TURN_BUTTON)
                return  # 2

            except WebDriverException:

                try:

                    MainActions.click_element(player, GameLocators.ROLL_DICES_AGAIN_BUTTON)

                    try:

                        MainActions.click_element(player, GameLocators.END_TURN_BUTTON)
                        return  # 3

                    except WebDriverException:
                        return  # 6

                except WebDriverException:

                    return  # 4

        except WebDriverException:

            return  # 5

    # 1 : Lancer les dés et finir tour PROBA : 5/6
    # 5 : Lancer les dés, et arriver sur prison/vacances
    # 2 : Lancer les dés (x2) et finir tour 1/6
    # 4 : Lancer les dés (x2), et arriver sur prison/vacances
    # 3 : Lancer les dés (x3) et finir tour
    # 6 : Lancer les dés (x3), et arriver sur prison/vacances ou double


def declare_bankruptcy():
    """
    Declares bankruptcy.

    Returns:
        None
    """
    logging.info("Attempting to declare bankruptcy.")

    MainActions.click_element(secondary_player, GameLocators.BANKRUPT_BUTTON)
    logging.info("Successfully clicked on bankrupt button.")

    MainActions.click_element(secondary_player, GameLocators.BANKRUPT_CONFIRM_BUTTON)
    logging.info("Successfully clicked on bankrupt confirm button.")


def farm_game_algorithm():
    farm_game_url = create_farm_game()
    secondary_player.get(farm_game_url)
    join_farm_game()
    start_farm_game()
    play_farm_game()


nb_parties = 80

game_url = create_farm_game()
secondary_player = MainActions.init_player(firefox_secondary_player_profile_path, game_url, "right")
join_farm_game()
start_farm_game()
play_farm_game()
for i in range(nb_parties):
    farm_game_algorithm()
