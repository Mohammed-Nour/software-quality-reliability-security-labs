import app.hangman as hangman 
from unittest.mock import patch
import os


def test_get_random_word():
    word = hangman.get_random_word()
    assert word in hangman.WORDS


def test_clear_screen():
    with patch("os.system") as mock_system:
        hangman.clear_screen()
        # Ensure the correct command is called based on the OS
        expected_command = "cls" if os.name == "nt" else "clear"
        mock_system.assert_called_once_with(expected_command)


def test_splash_screen():
    with patch("builtins.print") as mock_print, \
         patch("builtins.input", return_value="") as mock_input, \
         patch("app.hangman.clear_screen") as mock_clear_screen:
        hangman.splash_screen()

        # Verify print was called (output validation is tricky, so just check if print was used)
        assert mock_print.call_count > 0  

        # Ensure input was called once
        mock_input.assert_any_call("Press enter to continue...")
        # Ensure `clear_screen` was called
        mock_clear_screen.assert_called_once()


def test_hangman_win():
    with patch("app.hangman.get_random_word", return_value="python") as mock_get_random_word, \
        patch("builtins.input", side_effect=["p", "y", "t", "h", "o", "n", "n"]) as mock_input, \
        patch("builtins.print") as mock_print, \
        patch("app.hangman.clear_screen") as mock_clear_screen:
        hangman.hangman()
        mock_print.assert_any_call("You win!")


def test_hangman_lose():
    with patch("app.hangman.get_random_word", return_value="python") as mock_get_random_word, \
        patch("builtins.input", side_effect=["z", "q", "c", "e", "g", "w", "n", "!", "u", "z", "n"]) as mock_input, \
        patch("builtins.print") as mock_print, \
        patch("app.hangman.clear_screen") as mock_clear_screen:

        hangman.hangman()
        mock_print.assert_any_call("You lose!")


def test_hangman_win_and_play_again():
    with patch("app.hangman.get_random_word", return_value="python") as mock_get_random_word, \
        patch("builtins.input", side_effect=["p", "y", "t", "h", "o", "n", "y","p", "y", "t", "a", "a", "h", "o", "n", "n"]) as mock_input, \
        patch("builtins.print") as mock_print, \
        patch("app.hangman.clear_screen") as mock_clear_screen:
        hangman.hangman()
        mock_print.assert_any_call("You win!")
