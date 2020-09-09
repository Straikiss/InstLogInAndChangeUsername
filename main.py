from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

def parser_configs():
  configs = []
  with open('configs.txt', 'r') as data:
    for line in data:
      line = line.strip()
      parser_configs = line.split('=')
      configs.append(parser_configs)
  return configs

NAMES = parser_configs()[0][1]
SURNAMES = parser_configs()[1][1]
ACCOUNTS = parser_configs()[2][1]
ACCOUNT_PATH = parser_configs()[3][1]
NAME_PATH = parser_configs()[4][1]
SURNAME_PATH = parser_configs()[5][1]
NEW_ACCOUNT_PATH = parser_configs()[6][1]

MIN_NUM = 3 
MAX_NUM = 9 
INSTAGRAM_INDEX_PATH = 'https://www.instagram.com/'
INSTAGRAM_EDIT_PATH = 'https://www.instagram.com/accounts/edit/'
INSTAGRAM_SAVE_PATH = '//*[@id="react-root"]/section/main/div/article/form/div[11]/div/div/button'

def parser_name():
  name = []
  with open(NAME_PATH, 'r') as data:
    for line in data:
      parser_name = line[:-1]
      name.append(parser_name)
  return name[random.randint(0, int(NAMES))]

def parser_surname():
  surname = []
  with open(SURNAME_PATH, 'r') as data:
    for line in data:
      parser_surname = line[:-1]
      surname.append(parser_surname)
  return surname[random.randrange(0, int(SURNAMES))]

def create_new_account():
  random_list = []
  for i in range(0, int(MIN_NUM)):
    number = random.randint(1, int(MAX_NUM))
    random_list.append(number)
  return parser_name().lower() + '_' + parser_surname().lower() + str(random_list[0]) + str(random_list[1]) + str(random_list[2])
  
def parser_account():
  username = []
  password = []
  with open(ACCOUNT_PATH, 'r') as data:
    for line in data:
      line = line.strip()
      parser_username, parser_password = line.split(':')
      username.append(parser_username)
      password.append(parser_password)
  return username, password

def save(new_account, password):
  data_account = open(NEW_ACCOUNT_PATH, 'a')
  data_account.write(new_account + ':' + str(password) + '\n')
  data_account.close()

def login():
  username, password = parser_account()
  
  for i in range(int(ACCOUNTS)):
    new_account = create_new_account()

    browser = webdriver.Chrome('chromedriver')

    browser.get(INSTAGRAM_INDEX_PATH)

    time.sleep(2)
    
    print('Username: ' + str(username[i]))
    username_input = browser.find_element_by_name('username')
    username_input.clear()
    username_input.send_keys(username[i])
  
    time.sleep(2)

    print('Password: ' + str(password[i]))
    password_input = browser.find_element_by_name('password')
    password_input.clear()
    password_input.send_keys(password[i])
    password_input.send_keys(Keys.ENTER)

    time.sleep(2)

    browser.get(INSTAGRAM_EDIT_PATH)

    print('New username: ' + str(new_account))
    input_new_second_username = browser.find_element_by_id('pepUsername')
    input_new_second_username.clear()
    input_new_second_username.send_keys(new_account)

    time.sleep(2)

    print('New accout: ' + new_account + ':' + str(password[i]) + ' saved to [' + str(NEW_ACCOUNT_PATH) + ']')

    save(new_account, password[i])

    time.sleep(2)

    browser.find_element_by_xpath(INSTAGRAM_SAVE_PATH).click()

    browser.close()

def main():
  login()
  
main()