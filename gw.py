# Games Workshop Store Paint Scraper
# Dry, Base, Layer, Wash, Technical, Texture, etc

import os
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class GamesWorkshopInventory:
    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path="C:\\Apps\\Geckodriver\\chromedriver.exe")

    def engage_driver(self):
        driver = self.driver
        driver.get(
            "https://www.games-workshop.com/en-US/Painting-Modelling?N=1088720681+865704738&Nr=AND(sku.siteId%3AUS_gw%2Cproduct.locale%3Aen_US_gw)&Nrs=collection()%2Frecord[product.startDate+%3C%3D+1589888760000+and+product.endDate+%3E%3D+1589888760000]&view=all")

        time.sleep(2)

        source = driver.page_source

        data = bs(source, 'html.parser')

        print(data.find_all('a', class_='product-item__name'))

        self.disengage_driver()

    def disengage_driver(self):
        return self.driver.close()


if __name__ == "__main__":
    G = GamesWorkshopInventory()
    G.engage_driver()
