import pytest
import requests
from bs4 import BeautifulSoup
from project import  is_valid_url , text_to_audio , count_words



def test_is_valid_url():
    assert is_valid_url("https://coffeeandjunk.com/articles/") == True
    assert is_valid_url("examplecom") == False

def test_count_words():
    url = "https://coffeeandjunk.com/articles/"
    num_words = count_words(url)
    print(f"The number of words in the article is: {num_words}")

def test_text_to_audio():
    url = "https://coffeeandjunk.com/articles/"
    text = BeautifulSoup(requests.get(url).text, "html.parser").get_text()
    audio_file = text_to_audio.text_to_audio(text)
    assert audio_file.is_valid_audio_file()

