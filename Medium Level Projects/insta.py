import requests
from bs4 import BeautifulSoup

print("------------------------------------------")
username = input("Enter the username: ")
URL = "https://www.instagram.com/{}/"
try:
    r = requests.get(URL.format(username))
    s= BeautifulSoup(r.text,"html.parser")
    u = s.find("meta",property="og:image")
    url = u.attrs['content']

    with open(username+'.jpg',"wb") as pic:
        binary = requests.get(url).content
        pic.write(binary)

    print()
    print("Process completed. File saved as "+username+".jpg")
    print("------------------------------------------")
except:
    print()
    print("Sorry. Please check your connection or enter the right username")
    print("------------------------------------------")
