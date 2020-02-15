from tkinter import *
import bs4
import json
from urllib.request import urlopen as uOpen
from bs4 import BeautifulSoup as soup
from selenium import webdriver
import requests

def websiteScraping():
    # here we are simply accesing the website and taking all the data from the html
    browser = webdriver.Chrome(executable_path='/chromedriver.exe')
    browser.get("https://www.bovada.lv/sports/basketball")

    # here is where the html is parsed
    page_soup = soup(aClient.page_source, "html.parser")
    print(page_soup)

    # here we will find and all the games (basketball) that have not yet occurred
    for entry in page_soup.find_all("span", attrs="market-line.bet-handicap"):
        print(entry + '.')





websiteScraping()
