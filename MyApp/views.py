__author__ = 'vivek'

from django.http import HttpResponse
from django.shortcuts import render
import datetime
import json
from django.shortcuts import render_to_response
from . import Forms
from django.http import JsonResponse
from django.shortcuts import render, redirect
from MyApp.models import *
import thread
#import queue
from multiprocessing import *
from scheduler import *
import sys

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

import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Application_ROOT = os.path.join(BASE_DIR,'MyApp')
SCHEDULER_FILE = os.path.join(Application_ROOT,'scheduler.py')

try:
    # Import the Database Module
    print "Starting Scheduler"
    #pid = subprocess.Popen([sys.executable, "python","scheduler.py"]) # C
    #subprocess.call(['python', SCHEDULER_FILE])
    #subprocess.run(["python", "scheduler.py"])


except Exception:
    print "Error in processing. Error starting scheduler"
    print traceback.format_exc()

def base(request):
    #Test Base HTML Page
    return render(request,'base.html')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def main_page(request):
    output = "<html><body>It is now</body></html>"
    return HttpResponse(output)

def hello(request):
    return HttpResponse("Hello world")

def index(request):
    return render(request,'index.html')

def logout(request):
    return render(request,'login_simple.html')

def login(request):
    print None

def addtoqueue(request):
    print "Added City,State and Site to Scrape to Queue!"
    q.put(1)
    schedule(q.put(1))

def startScraping(request):
    print None


def stopScraping(request):
    print None