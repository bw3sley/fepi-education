# Wesley Bernardes - 020321

import pytest

import time 

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait, Select 

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC

URL = "https://demoqa.com/automation-practice-form"

@pytest.fixture()
def driver():
  options = Options()

  options.add_argument("--no-sandbox")
  # options.add_argument("--headless")

  driver = webdriver.Chrome(options=options)

  yield driver

  driver.quit()

def test_form_sign_up(driver):
    driver.get(URL)

    result_dict = {}

    # Evitar que as propagandas fiquem sobrepondo os campos do formulário

    driver.set_window_size(1920, 1080)

    driver.find_element(By.ID, "firstName").click()
    driver.find_element(By.ID, "firstName").send_keys("João")
    driver.find_element(By.ID, "lastName").send_keys("Santos")
    driver.find_element(By.ID, "userEmail").send_keys("joao.santos@teste.com")
    driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']").click()
    driver.find_element(By.ID, "userNumber").send_keys("9988776655")

    btn_submit = driver.find_element(By.ID, "submit")

    # Scrollar até o botão para evitar que a propaganda o cubra o botão

    driver.execute_script("arguments[0].scrollIntoView(true);", btn_submit)
    
    time.sleep(1)

    btn_submit.click()

    time.sleep(1)

    # Isso é frescura

    message = driver.find_element(By.ID, "example-modal-sizes-title-lg").text

    assert message == "Thanks for submitting the form"