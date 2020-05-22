# Games Workshop Store Paint Scraper
# Dry, Base, Layer, Wash, Technical, Texture, etc

import os
import sys
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

'''
Selenium is used instead of traditional, headless scraping techniques due to GW's use of Endeca (e-commerce toolkit from Oracle). They inject their inventory data into the window after it has finished loading. From my experimentation, I could technically parse the document without BS4, but that would take a long time to figure out and overly complicate the code.

Selenium is used as a driver for navigating to a specific URL, and quickly pulling the source after they inject it into the browser window. A headless browser window can be used but I would need to overcomplicate the code with overrides to hide the fact that it's a bot scraping their site. Recaptcha will otherwise block access.

A viewable window gets around both of the above issues and is a lot simpler for my needs.
'''

# Structure of the Inventory Object produced by the GamesWorkshopInventory class
'''
inventory = {
    '<type>': {
        '<paint_name>': {
            'colour': '<colour>'
            'price': '<price>'
            'type': '<type>'
        }
    }
}
'''


class GamesWorkshopInventory:
    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path="C:\\Apps\\Geckodriver\\chromedriver.exe")
        self.initial_url = "https://www.games-workshop.com/en-US/detail?Ndi=3184893862&Ndn=GW_Painting_and_Modelling_Browse_Paint_by_Colour.dyn.dimensionPaintColour"
        self.colour_keys = []
        self.inventory = {}  # Storage

    # This will review the page and add the names of colours we need to visit. We use the colours as a key which is used to determine which link Selenium will visit next.
    def generate_colour_key(self):
        items = bs(self.driver.page_source, 'html.parser').find_all(
            'div', class_='hgn__filterButtonName')

        for item in items:
            self.colour_keys.append(item.text.strip().lower())

    def visit_next_colour(self, colour_key):
        colour_title = colour_key.title()
        # Find the button using the class and the colour_key (title case). Then use that element as the click target
        # to go to then next page of paints (filtered by color)
        try:
            # Syntax - Select div that has the class and text
            target = self.driver.find_element_by_xpath(
                f"//div[contains(@class, 'hgn__filterButtonName') and contains(text(), '{colour_title}')]")
        except NoSuchElementException as error:
            print(f"Exception caught in <fn visit_next_colour>: {error}")
            sys.exit(0)

        # Click the element to load the next page
        target.click()

        time.sleep(2)

        # text = bs(self.driver.page_source, 'html.parser').find(class_=)

    def get_page_source(self):
        return self.driver.page_source

    def engage_driver(self):
        self.driver.get(self.initial_url)  # Opens the initial page

        self.generate_colour_key()

        self.visit_next_colour('brown')

        self.disengage_driver()

    def disengage_driver(self):
        return self.driver.close()


if __name__ == "__main__":
    G = GamesWorkshopInventory()
    G.engage_driver()
