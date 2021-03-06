# Author: Amir Mohammadi
# @amiremohamadi
# Cheater for https://grandedesafio.com
# Usage: python cheater.py {url} {name}

from sys import argv
from time import sleep
from selenium import webdriver

# Set webdriver
driver = webdriver.Firefox(executable_path='path/to/your/webdriver')

website_url, name = argv[1], argv[2]
driver.get(website_url)

name_field = driver.find_element_by_id('name')
name_field.clear()
name_field.send_keys(name)

start_button = driver.find_element_by_id('start')
start_button.click()

for _ in range(20):
    sleep(1.5)
    correct_item = driver.find_element_by_class_name('correct')
    correct_item.click()
