import requests
from bs4 import BeautifulSoup


class InvalidWord(Exception):
    pass


try:
    word = input("Enter a word: ")
    url = requests.get('https://en.oxforddictionaries.com/definition/' + word)
    print("Finding information.....\n "
          "This might take some time based upon your internet speed.\n")
    data = url.content
    soup = BeautifulSoup(data, features="lxml")
    
    tag = soup.find_all("span", "ind")
    
    if not tag:
        raise InvalidWord
    
    for i in range(len(tag)):
        print(f"{i + 1})  {tag[i].text}")

except InvalidWord as e:
    print("Please enter a valid word")
