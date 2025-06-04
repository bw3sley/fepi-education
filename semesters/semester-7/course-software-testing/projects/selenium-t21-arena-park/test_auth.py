import pytest

import time 

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

URL = "https://t21-arena-park.com/"

@pytest.fixture
def driver():
    options = Options()

    options.add_argument("--no-sandbox")
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()

def login(driver):
    driver.get(URL)

    driver.find_element(By.ID, "email").send_keys("bw3sley@gmail.com")
    driver.find_element(By.ID, "password").send_keys("T21-ARENA-PARK")
    
    driver.find_element(By.CSS_SELECTOR, ".items-center:nth-child(1)").click()

    time.sleep(1)

def test_it_should_be_able_to_login(driver):
    login(driver)

    assert driver.current_url == URL + "home"

def test_it_should_be_able_to_logout(driver):
    login(driver)

    driver.execute_script("""
        const el = document.querySelector('span[aria-haspopup="menu"]');
        if (el) {
            el.dispatchEvent(new PointerEvent('pointerdown', { bubbles: true }));
        }
    """)

    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Sair']/ancestor::button"))
    )
    
    logout_button.click()

    assert driver.current_url == URL

def test_it_should_return_an_error_if_credentials_are_invalid(driver):
    driver.get(URL)

    driver.find_element(By.ID, "email").send_keys("bw3sley@gmail.com")
    driver.find_element(By.ID, "password").send_keys("t21-arena-park")
    
    driver.find_element(By.CSS_SELECTOR, ".items-center:nth-child(1)").click()

    time.sleep(1)

    error_message = driver.find_element(By.CSS_SELECTOR, "[data-sonner-toast] [data-title]").text

    assert error_message == "Credenciais inválidas"