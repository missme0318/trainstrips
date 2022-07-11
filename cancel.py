from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select


def cancel_train(cancelinfo):

    IDnum = cancelinfo.split('\n')[0]
    ticketnum = = cancelinfo.split('\n')[1]
    
    return IDnum