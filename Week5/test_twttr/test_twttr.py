from twttr import shorten

# words Upper and lower
def test_short_words():
        assert shorten("somthing") == "smthng"
        assert shorten("Twitter") == "Twttr"
        assert shorten("My tweEet") == "My twt"
# punctuation
def test_short_punctuation():
        assert shorten(",?!.") == ",?!."
# numbers
def test_short_number():
        assert shorten("987") == "987"
        assert shorten("00") == "00"
