from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver = webdriver.Chrome('C:/webscraping/chromedriver.exe')

driver.get('https://data.calgary.ca/')

box = driver.find_element(By.NAME, 'search')
box.send_keys('Community Crime Statistics')
box.send_keys(Keys.ENTER)

link = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/div/div[4]/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/h2/a')
link.click()

export = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/div/div[2]/div/div[2]/button')
export.click()

driver.find_element(By.XPATH, '//*[@id="export-flannel"]/section/ul/li[1]/a').click()

filename = (r'C:\Users\Paolo\Downloads\Community_Crime_Statistics.csv')

df = pd.read_csv(filename)

df = pd.read_csv(filename, usecols=['Category', 'Year', 'Crime Count'])

pivot = df.pivot_table(index='Year', columns='Category', values='Crime Count', aggfunc='count')

pivot.plot(title="Crimes over the years (2017 - 2022)", kind='line', figsize=(18, 9), ylabel='Number of crimes', style='o-')


