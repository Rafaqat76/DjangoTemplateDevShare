import pprint
import random
import re
import time
import traceback
from venv import logger

from bs4 import BeautifulSoup
from selenium import webdriver

p = pprint.PrettyPrinter(indent=4)
realtDictPagenumbers = {}
realtListPagenumbers = []
city = [('Detroit', 'MI')]
price = 300000
url = "https://www.realtor.com/realestateandhomes-search/Detroit_MI/price-300000-na"
# https://www.realtor.com/realestateandhomes-search/Detroit_MI/pg-2
# https://www.realtor.com/realestateandhomes-search/Detroit_MI/price-300000-na/pg-2

class Scraping:

    def realtor(self, city=None, state=None, price=None):
        print("Scraping realtor")

        try:
            f = open("realtor.csv", "w")
            f.close()
            driver = webdriver.Chrome(executable_path=r'C:\chromedriver\chromedriver.exe')
            driver.implicity_wait(20)
            base_url = url
            time.sleep(random.randrange(30, 130))
            driver.get(base_url)
            c = driver.page_source
            soup = BeautifulSoup(c, 'html.parser')
            pagelinks = soup.find_all('a', href=re.compile(r'/realestateandhomes-search/Detroit_MI/price-300000-na.*'),
                                      attrs={'title': re.compile(r'Page.*')})

            for pagenumber in pagelinks:

                try:
                    print(pagenumber.text)
                    realtListPagenumbers.append(int(pagenumber.text))

                except:
                    print("Cannot Collect All the Page")
                    logger.error('Cannot Collect All the Page', traceback.format_exc())

                minrealtor = min(realtListPagenumbers)
                maxrealtor = max(realtListPagenumbers)

            for i in range(minrealtor, maxrealtor):
                print("page %d") % i
                time.sleep(random.randrange(60, 120))
                intermediatePageurl = "https://www.realtor.com/realestateandhomes-search/Detroit_MI/price-300000-na" + str(
                    i) + '_p'

                driver.get(intermediatePageurl)
                time.sleep(random.randrange(5, 10))
                c = driver.page_source
                soup = BeautifulSoup(c, "html.parser")
                links = soup.find_all('div', class_=re.compile(r'jsx-3900997218 component_property-card broker-logo.*'))

                for listing in links:
                    try:
                        home_imagelist = []
                        datawriter = None
                        # home = listing.find_all('div', attrs={'data-label': re.compile(r'propertyFound.*')})
                        home_price = str(listing.find_all('li', attrs={'data-label': 'pc-price'})[0].text)
                        print(home_price)
                        home_bed = str(listing.find_all('li', attrs={'data-label': 'pc-meta-beds'})[0].text)
                        print(home_bed)
                        home_bath = str(listing.find_all('li', attrs={'data-label': 'pc-meta-baths'})[0].text)
                        print(home_bath)
                        home_space = str(listing.find_all('li', attrs={'data-label': 'pc-meta-sqft'})[0].text)
                        print(home_space)
                        home_address = str(listing.find_all('li', attrs={'data-label': 'pc-address'})[0].text)
                        print(home_address)
                        home_address2 = str(listing.find_all('li', attrs={'data-label': 'pc-address-second'})[0].text)
                        print(home_address2)
                        home_url = str(listing.find_all('a', attrs={'href': re.compile(r'.*')})[0].text)
                        print(home_url)
                        home_images = listing.find_all('img')
                        for im in home_images:

                            if 'image/gif' in im:
                                print("Update")
                            else:
                                home_imagelist.append(im.get('src'))

                        print(home_imagelist)

                        datawriter = home_price + " " + home_bed + " " + home_bath + " " + home_space + " " + home_address + " " + home_address2 + " ".join(
                            home_imagelist) + '\n'

                        f = open("realtor.csv", "a")
                        f.write(datawriter)
                        f.close()

                    except StandardError:
                        print("error")
                        print(traceback.format_exc())

                    finally:
                        pass

        except  StandardError:
            traceback.format_exc()
            print("We Have Excepting in processing!")

            if __name__ == "__main__":
                Scraping().realtor()
