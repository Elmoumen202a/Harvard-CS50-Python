# I use this in is_valid_url() for check url is valid
from urllib.parse import urlparse
# I use those in text_to_audio() for convert text to audio
import nltk
from newspaper import Article
from gtts import gTTS
# I use it in count_words() for cont words in artical web
import requests
from bs4 import BeautifulSoup



def main():
    url = input("Link of article: ")
    urltest = is_valid_url(url)  # Test link
    # print( is_valid_url(url))
    # run the code is url work/ isn't break \\ url = True or url = Flase
    if urltest ==True:
        num_words = count_words(url)
        print(f"The number of words in the article is: {num_words}")
        yesORno =input("Did you want continue to convert in mp3 (yes or no): ").lower()
        if yesORno == "yes":
            text_to_audio(url )
        elif yesORno == "no":
            print("OK!,thanks for visiting")

    elif urltest == False:
        print("The link is not valid")


# creat a function to check valid url
def is_valid_url(url):
  try:
    result = urlparse(url)
    return all([result.scheme, result.netloc])
  except ValueError:
    return False


# creat a function that count words in web
def count_words(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()
    words = text.split()
    return len(words)


#creat a function the conver text to speech
def text_to_audio(url):
   essay = Article(url)
   essay.download()
   essay.parse()
   nltk.download('punkt')
   essay.nlp()
   article_text =  essay.text
   language = 'en'
   _obj = gTTS(text=article_text, lang=language, slow=False)
   _obj.save("audioArticle.mp3")
   print("The txt is convert in mp3 sucssfully")


if __name__ == '__main__':
    main()
