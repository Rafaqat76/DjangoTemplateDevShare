# -*- coding: utf-8 -*-
import random
import re
import traceback
from threading import Lock
# import SimpleHTTPServer
# import SocketServer
# import DBConnector as databaseconnection
from venv import logger

import alog
from bs4 import BeautifulSoup
from selenium import webdriver

lock = Lock()
import time

import pprint

pp = pprint.PrettyPrinter(indent=4)

truliaDictPageNumbers = {}
truliaListPageNumbers = []
cityList = [('Detroit', 'MI')]

price = 300000

urlTrulia = 'https://www.trulia.com/for_sale/Detroit,MI/300000p_price/'

logger = alog.alog('Scraping Engine')

# options = webdriver.ChromeOptions()


footageLinksToDownload = []


class Scraping:

    def trulia(self, city=None, state=None, price=None):
        print("Scraping Trulia")

        try:
            f = open("trulia.csv", "w")

            f.close()
            driver = webdriver.Chrome(executable_path=r'C:\chromedriver\chromedriver.exe')
            # driver = webdriver.Firefox()
            # driver = webdriver.Chrome()
            # webdriver.Firefox()
            # driver = webdriver.Firefox(executable_path=r'C:\firefoxdriver\geckodriver.exe')
            driver.implicitly_wait(30)

            base_url = urlTrulia

            verificationErrors = []
            accept_next_alert = True

            time.sleep(random.randrange(60, 130))
            # driver.get(base_url + "/" + str(item) + "/")
            driver.get(base_url)

            c = driver.page_source
            soup = BeautifulSoup(c, "html.parser")

            # Call Database Service to pick up the next city which has not been used today and

            pagelinks = soup.find_all('a', href=re.compile(r'/for_sale/Detroit,MI/300000p_price/.*'),
                                      attrs={'aria-label': re.compile(r'Page .*')})

            for pagenumber in pagelinks:

                try:
                    print(pagenumber.text)
                    truliaListPageNumbers.append(int(pagenumber.text))

                except:
                    print("Cannot Collect All the Page")
                    logger.error('Cannot Collect All the Page', traceback.format_exc())

            # So we have got the pages. Now do logic to get the min and max

            minTrulia = min(truliaListPageNumbers)
            maxTrulia = max(truliaListPageNumbers)

            for i in range(minTrulia, maxTrulia):
                print("page %d") % i
                time.sleep(random.randrange(60, 130))

                intermediatePageURL = 'https://www.trulia.com/for_sale/Detroit,MI/300000p_price/' + str(i) + '_p'

                driver.get(intermediatePageURL)
                time.sleep(random.randrange(6, 10))
                c = driver.page_source
                soup = BeautifulSoup(c, "html.parser")

                links = soup.find_all('div', class_=re.compile(r'Grid__CellBox-sc-5ig2n4-0 .*'))

                # print links
                # print len(links)

                for listing in links:

                    try:
                        tempHome_imageList = []
                        dataWriter = None
                        # Now get the House Details for each link
                        tempHome = listing.find_all('div', attrs={'data-testid': re.compile(r'property.*')})
                        tempHome_price = str(listing.find_all('div', attrs={'data-testid': 'property-price'})[0].text)
                        print(tempHome_price)
                        tempHome_bed = str(listing.find_all('div', attrs={'data-testid': 'property-beds'})[0].text)
                        print(tempHome_bed)
                        tempHome_bath = str(listing.find_all('div', attrs={'data-testid': 'property-baths'})[0].text)
                        print(tempHome_bath)
                        tempHome_floorspace = str(
                            listing.find_all('div', attrs={'data-testid': 'property-floorSpace'})[0].text)
                        print(tempHome_floorspace)
                        tempHome_street = str(listing.find_all('div', attrs={'data-testid': 'property-street'})[0].text)
                        print(tempHome_street)
                        tempHome_region = str(listing.find_all('div', attrs={'data-testid': 'property-region'})[0].text)
                        print(tempHome_region)
                        tempHome_homeURL = str(
                            listing.find_all('a', attrs={'href': re.compile(r'.*')})[0].attrs['href'])
                        print(tempHome_homeURL)
                        tempHome_images = listing.find_all('img')
                        for im in tempHome_images:
                            # print im.get('src')

                            if 'image/gif' in im:
                                print("Update")
                            else:
                                tempHome_imageList.append(im.get('src'))

                        print(tempHome_imageList)

                        # Start to Look into Database and see if the House is in the Database or not.
                        # If the house is not in the Database, insert it

                        dataWriter = tempHome_price + ',' + tempHome_bed + ',' + tempHome_bath + ',' + tempHome_floorspace + ',' + tempHome_street + ',' + tempHome_region + ','.join(
                            tempHome_imageList) + '\n'

                        f = open("trulia.csv", "a")

                        f.write(dataWriter)
                        f.close()

                        # Write to Database


                    except Exception:
                        print("Error in processing. An Ad may be?")
                        print(traceback.format_exc())
                        # or
                        # print(sys.exc_info()[2])
                    finally:
                        pass


        except  Exception:
            traceback.format_exc()
            print("We Have Excepting in processing!")

    def zillow(self, city, state, price):
        print("Scraping Zillow")

    def realtor(self, city, state, price):
        print("Scraping Relator")

    def redfin(self, city, state, price):
        print("Scraping Redfin")

    def homes(self, city, state, price):
        print("Scraping Homes")

    def ziprealty(self, city, state, price):
        # https://www.ziprealty.com/for-sale-homes/Dallas-TX-2419c/minprice_300000
        print("Scraping ZipRealty")

    def hotpads(self, city, state, price):
        print("Scraping Hotpads")

    def remax(self, city, state, price):
        print("Scraping Remax")

    def apartments(self, city, state, price):
        print(None)


if __name__ == "__main__":
    Scraping().trulia()
