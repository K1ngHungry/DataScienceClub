from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.by import By


df = pd.DataFrame(columns=['Player','Salary']) # creates master dataframe 

driver = webdriver.Chrome('/Users/kevin/chromedriver')

url = 'https://hoopshype.com/salaries/players/'
driver.get(url)

players = driver.find_elements(By.XPATH, '//td[@class="name"]') # locate all player names and store in a list of web elements
salaries = driver.find_elements(By.XPATH, '//td[@class="hh-salaries-sorted"]') # locate all salaries and store in a list of web elements

# convert web elements to text
players_list = []
for p in range(len(players)):
    players_list.append(players[p].text)

salaries_list = []
for s in range(len(salaries)):
    salaries_list.append(salaries[s].text)

data_tuples = list(zip(players_list[1:],salaries_list[1:])) # list of each players name and salary paired together
temp_df = pd.DataFrame(data_tuples, columns=['Player','Salary']) # creates dataframe of each tuple in list
df = df.append(temp_df) # appends to master dataframe

print(df)
df.to_csv('nba.csv')

driver.close()
