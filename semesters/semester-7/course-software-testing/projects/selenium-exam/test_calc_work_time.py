# Wesley Bernardes - 020321

import pytest

import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait, Select 

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys

URL = "https://www.calculadora.app/trabalhista/horas-trabalhadas"

@pytest.fixture
def driver():
    options = Options()

    options.add_argument("--no-sandbox")
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()

def test_calc_work_time(driver):
  driver.get(URL)

  driver.find_element(By.ID, "entrada-v-0").send_keys("09:00")
  driver.find_element(By.ID, "saída-v-1").send_keys("12:00")
  driver.find_element(By.ID, "entrada-v-2").send_keys("13:00")
  driver.find_element(By.ID, "saída-v-3").send_keys("18:00")
  
  driver.find_element(By.ID, "calcular").click()

  time.sleep(1)

  value = driver.find_element(By.CSS_SELECTOR, ".stat-value").text

  assert value == "08:00"