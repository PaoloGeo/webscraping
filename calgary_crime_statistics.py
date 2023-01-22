# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 09:33:50 2022

@author: Paolo
"""

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/webscraping/chromedriver.exe')

driver.get('https://data.calgary.ca/')

#button = driver.find_element(By.XPATH, '//*[@id="content-body"]/div/div/div[2]/ul/li[1]/a')
#button.click()

box = driver.find_element(By.NAME, 'search')
box.send_keys('Community Crime Statistics')
box.send_keys(Keys.ENTER)

link = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/div/div[4]/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/h2/a')
link.click()

export = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/div/div[2]/div/div[2]/button')
export.click()

saveas = driver.find_element(By.XPATH, '//*[@id="export-flannel"]/section/ul/li[1]/a').click()






#saveas.send_keys(Keys.CONTROL + Keys.ENTER)

#driver.switchTo().alert().sendKeys("Text");

#download = driver.find_element(By.XPATH, '//*[@id="export-flannel"]/section/div[3]/ul[1]/li[1]/a')
#download.click()
