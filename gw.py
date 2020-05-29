# Games Workshop Store Paint Scraper
# Dry, Base, Layer, Wash, Technical, Texture, etc

# Full Imports
import os
import sys
import time
import json
import re
import pprint  # just for testing and viewing objects in a legible format

# Selective Imports
from paint_manifest import data as URL_MANIFEST
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

'''
Selenium is used instead of traditional, headless scraping techniques due to GW's use of Endeca (e-commerce toolkit from Oracle). They inject their inventory data into the window after it has finished loading. From my experimentation, I could technically parse the document without BS4, but that would take a long time to figure out and overly complicate the code.

Selenium is used as a driver for navigating to a specific URL, and quickly pulling the source after they inject it into the browser window. A headless browser window can be used but I would need to overcomplicate the code with overrides to hide the fact that it's a bot scraping their site. Recaptcha will otherwise block access.

A viewable window gets around both of the above issues and is a lot simpler for my needs. One of those cases where testing modules are useful for gathering data.
'''

# Structure of the Inventory Object produced by the GamesWorkshopInventory class
'''
inventory = {
    '<type>': {
        '<paint_name>': {
            'colour': '<colour>'
            'price': '<price>'
            'type': '<type>'
            'size': '<size>'
        }
    }
}
'''


class GamesWorkshopInventory:
    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path="C:\\Apps\\Geckodriver\\chromedriver.exe")
        self.initial_url = "https://www.games-workshop.com/en-US/Black-Templar-2019?Ndn=GW_Painting_and_Modelling_Browse_Paint_by_Colour.dyn.dimensionPaintColour&Ndi=3184893862"
        self.fragment_url = "https://www.games-workshop.com/en-US/detail?"
        self.links = URL_MANIFEST
        self.colour_keys = {}
        self.inventory = {}  # Storage

    # This will review the page and add the names of colours we need to visit. We use the colours as a key which is used to determine which link Selenium will visit next.
    def generate_colour_key(self):
        items = bs(self.driver.page_source, 'html.parser').find_all(
            'div', class_='hgn__filterButtonName')

        for item in items:
            nav_color_text = item.text.strip().lower()
            nav_query_string = item['data-name']

            self.colour_keys[nav_color_text] = nav_query_string

        # self.colour_keys.append(item.text.strip().lower())

    def visit_next_colour(self, colour_key):
        colour_title = colour_key.title()

        # This needs to be refactored completely because recaptcha is interfering

    def get_page_source(self):
        return self.driver.page_source

    # Function will handle the main task of grabbing the paints from each page and placing them into the correct structure
    def get_paints(self, paint_colour):
        paints = bs(self.driver.page_source,
                    'html.parser').find_all('span', class_='recordItem')

        filtered_list = [paint['data-gtm-productfieldobject']
                         for paint in paints]

        for item in filtered_list:
            # This is an object produced from the json
            paint = json.loads(item)

            # We use the paint['name'] key and run its value through a regex to grab the type and name
            paint_re = re.search(
                r"(\w*):\s([^\(]*)", paint['name'])

            paint_price = paint['price']
            paint_type = paint_re.group(1)  # type -> used as our key in the
            paint_name = paint_re.group(2)  # name
            paint_size = None

            paint_name, paint_size = self.normalize_colors(
                paint_type, paint_name)

            # Append the paint dictionary to the inventory dictionary (classified by type)
            if paint_type not in self.inventory:
                self.inventory[paint_type] = {}  # Initialize

            self.inventory[paint_type].update({
                paint_name: {
                    'price': paint_price,
                    'colour': paint_colour,
                    'type': paint_type,
                    'size': paint_size
                }
            })

    '''
    The data provided from scraping shows inconsistency across the board with regards to naming conventions. Over the years
    GW has added newer products with slightly different naming systems. For example, Citadel Death Guard Spray v.s Chaos Black Spray. To make up for this inconsistency, the data needs to be further filtered through a function and normalized to a standard convention.

    Older colors (pre/circa 2019) use a different convention compared to recently added colors. The date is now preceded by the size of the paint on recent colors. The regex we have supplied

    #>ml sizes. I will add in the sizes after normalizing the names because the naming conventions are so wildly different in some cases.
    Key words to remove from the name include "Citadel", "Global", "Spray", and various <

    Also to note, there are a few technicals that are not 24ml. These need to be checked manually by the code and assigned the correct values.
    '''

    def normalize_colors(self, paint_type, paint_name) -> tuple:

        words_to_filter = (
            'Citadel',
            'Global',
            'Spray',
            '12ml',
            '18ml',
            '24ml',
            '400ml'
        )

        paint_sizes = {
            'base': '12ml',
            'layer': '12ml',
            'dry': '12ml',
            'contrast': '18ml',
            'air': '24ml',
            'technical': '24ml',
            'technical_2': '12ml',
            'shade': '24ml',
            'spray': '400ml',
        }

        '''
        This is tuple that contains the names of technical items that don't share the same size as the usual technical items.
        We check if the paint_name exists in this tuple and update the size based on that
        '''
        paint_size_overrides = (
            'Nurgles Rot',
            'Spiritstone Red',
            'Soulstone Blue',
            'Waystone Green',
            'Nihilakh Oxide',
            'Blood For The Blood God',
            'Typhus Corrosion'
        )

        new_name = ' '.join(
            filter(lambda x: x not in words_to_filter, paint_name.split()))
        new_size = paint_sizes[paint_type.lower()]

        # Run another check here for technicals that are not 24ml. Manually checked against the GW website.
        if paint_type == 'Technical' and paint_name in paint_size_overrides:
            new_size = paint_sizes['technical_2']

        return new_name, new_size

    def engage_driver(self):

        self.driver.get(self.initial_url)  # Opens the initial page

        self.generate_colour_key()

        for colour in self.colour_keys:
            print(self.links[colour])

        # self.get_paints('black')  # Initially start on the black page
        # for colour_key in self.colour_keys:
        #     self.visit_next_colour(colour_key)

        print(pprint.pprint(self.inventory))

        self.disengage_driver()

    def disengage_driver(self):
        return self.driver.close()


if __name__ == "__main__":
    G = GamesWorkshopInventory()
    G.engage_driver()
