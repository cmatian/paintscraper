# Games Workshop Store Paint Scraper
# Dry, Base, Layer, Wash, Technical, Texture, etc

import os
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

'''
Selenium is used instead of traditional, headless scraping techniques due to GW's use of Endeca (e-commerce toolkit from Oracle). They inject their inventory data into the window after it has finished loading. From my experimentation, I could technically parse the document without BS4, but that would take a long time to figure out an algorithm (most likely RegEx) that can accurately pull the correct data points from their manifest.

Selenium is used as a driver for navigating to a specific URL, and quickly pulling the source after they inject it into the browser window. A headless browser window can be used but I would need to overcomplicate the code with overrides to hide the fact that it's a bot scraping their site. Recaptcha will otherwise block access.

A viewable window gets around both of the above issues and is a lot simpler for my needs.
'''


class GamesWorkshopInventory:
    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path="C:\\Apps\\Geckodriver\\chromedriver.exe")

    def engage_driver(self):
        driver = self.driver
        driver.get(
            "https://www.games-workshop.com/en-US/Painting-Modelling?N=1088720681+865704738&Nr=AND(sku.siteId%3AUS_gw%2Cproduct.locale%3Aen_US_gw)&Nrs=collection()%2Frecord[product.startDate+%3C%3D+1589888760000+and+product.endDate+%3E%3D+1589888760000]&view=all")

        source = driver.page_source

        '''
        Parse the source which returns an array containing the text values of each paint.
        '''
        air_paints = bs(source, 'html.parser').find_all(
            'a', class_='product-item__name').text

        '''
        Produce a text file containing the name of the information for now. Later on we will transfer this to a CSV format.
        '''
        paint_type = 'air'
        with open(f'{paint_type}.txt', 'w') as file:
            for air_paint in air_paints:
                file.write(f'{air_paint}')

        # Close out the driver
        self.disengage_driver()

    def disengage_driver(self):
        return self.driver.close()


if __name__ == "__main__":
    G = GamesWorkshopInventory()
    G.engage_driver()
