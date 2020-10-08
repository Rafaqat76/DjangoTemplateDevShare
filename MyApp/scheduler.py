__author__ = 'vivek'
#import queue
import os
import time
from scraping import *
import threading, Queue
import alog
import xml.dom.minidom as minidom
import xml.parsers.expat as xmlerr
import shutil,os,zipfile,socket,time
import json
import sys
import csv
import xml.etree.cElementTree as ET
import pprint
import requests
from collections import defaultdict
import datetime
import math
from decimal import Decimal
import os
import platform
import zipfile
import mmap
import SimpleHTTPServer
import SocketServer
import uuid
#import DBConnector as databaseconnection
import os
import alog
import traceback
from threading import Thread
from time import sleep
import subprocess
from subprocess import call
from subprocess import Popen, PIPE
import threading
import glob
from threading import Lock
lock = Lock()
import multiprocessing
import time

import pprint
pp = pprint.PrettyPrinter(indent=4)


import xml.dom.minidom as minidom
import xml.parsers.expat as xmlerr
import shutil,os,zipfile,socket,time
import json
import sys
import csv
import xml.etree.cElementTree as ET
import pprint
import requests
from collections import defaultdict
import datetime
import math
from decimal import Decimal
import os
import platform
import zipfile
import mmap
import SimpleHTTPServer
import SocketServer
import uuid
#import DBConnector as databaseconnection
import os
import alog
import traceback
from threading import Thread
from time import sleep
import subprocess
from subprocess import call
from subprocess import Popen, PIPE
import threading
import glob
from multiprocessing import Queue
from threading import Lock
lock = Lock()
import multiprocessing
import time

import pprint
from Queue import Empty
pp = pprint.PrettyPrinter(indent=4)




timeduration = 1


logger=alog.alog('Scheduler for Scraping Engine')
city = "Detroit"
state = "MI"


def schedule():
    print "I am inside Schedule"

    while 1:


        if Queue().empty():

            print "I am a scheduler"
            time.sleep(timeduration)



            ######### Trulia #########
            print "1. Scraping Trulia"




            logger.info('Will Scrape Site.','Trulia')
            logger.info('Starting to scrape after %s seconds for city %s and state %s ' %(timeduration,city,state),'Trulia at ')
            Scraping().trulia()

            ######### Zillow #########
            print "2. Scraping Zillow"

            ######### Redfin #########
            print "3. Scraping Redfin"

            ######### Realtor #########
            print "4. Scraping Realtor"

            ######### Homes #########
            print "5. Scraping Homes"

            ######### Hotpads #########
            print "6. Scraping Hotpads"

            ######### ZipRealty #########
            print "7. Scraping ZipRealty"

            ######### Trulia #########
            print "8. Scraping Trulia"


             ######### Trulia #########
            print "9. Scraping Trulia"

        else:
            print "The Queue in now empty so will process it"

if __name__ == "__main__":
     schedule()
