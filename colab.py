from selenium import webdriver

# for explicit wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#for action keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

#utils
import webbrowser
from datetime import datetime
import time


# user options
email=""
colab_url = 'https://colab.research.google.com' # colab link to execute
open_url='https://console.clouderizer.com/projects'


# Using Chrome to access web
browser = webdriver.Chrome()
# Open the website
browser.get(colab_url)

# waiting for login to show up
try:
  element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, 'input'))
  )
finally:
  email_form = browser.find_element_by_tag_name('input')
  email_form.send_keys(email)
  email_form.send_keys('\n')

print("Enter your google credentials in the browser")

# wait for colab to start

try:
  element = WebDriverWait(browser, 30).until(
      EC.presence_of_element_located((By.ID, "runtime-menu-button"))
  )
finally:
  # execute all cells
  ActionChains(browser).send_keys(Keys.CONTROL+Keys.F9).perform()

#open new tab
if open_url:
  webbrowser.open_new_tab(open_url)

start_time = datetime.now()

#loop for making sure colab is connected
while True:
  try:
    WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "icon-error")))
  except TimeoutException:
    print("time: {} | waiting for disconnect...".format(datetime.now()-start_time),end='\r')
    continue
  except Exception as e:
    print('error',e)
    time.sleep(5)
    continue
  print('reconnecting...')
  er = browser.find_element_by_class_name('icon-error')
  er.click()

