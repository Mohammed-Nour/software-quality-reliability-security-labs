from app.hangman import get_random_word


def test_hangman():
    WORDS = ("python", "jumble", "easy", "difficult",
             "answer", "xylophone", "hangman", "computer",
             "science", "programming", "mathematics",
             "player", "condition", "reverse", "water",
             "board", "geeks", "keyboard", "laptop", "headphone",
             "mouse", "printer", "scanner", "software", "hardware",
             "network", "server")
    word = get_random_word()
    assert word in WORDS
