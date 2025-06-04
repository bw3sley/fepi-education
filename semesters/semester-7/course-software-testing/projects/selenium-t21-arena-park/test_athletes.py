import pytest

import time 

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait, Select 

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC

URL = "https://t21-arena-park.com/"

@pytest.fixture
def driver():
    options = Options()

    options.add_argument("--no-sandbox")
    # options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()

def login(driver):
    driver.get(URL)

    driver.find_element(By.ID, "email").send_keys("bw3sley@gmail.com")
    driver.find_element(By.ID, "password").send_keys("T21-ARENA-PARK")
    
    driver.find_element(By.CSS_SELECTOR, ".items-center:nth-child(1)").click()

    time.sleep(1)

def create_athlete(driver):
    driver.get(URL + "athletes")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".bg-lime-600"))
    ).click()

    driver.find_element(By.ID, "name").send_keys("teste")
    driver.find_element(By.ID, "birthDate").send_keys("10/10/2024")

    Select(driver.find_element(By.NAME, "handedness")).select_by_visible_text("Destro")
    Select(driver.find_element(By.CSS_SELECTOR, ".flex:nth-child(4) > select")).select_by_visible_text("Masculino")
    Select(driver.find_element(By.NAME, "bloodType")).select_by_visible_text("A+")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[form="new-athlete-form"]'))
    ).click()

def test_it_should_be_able_to_create_athlete(driver):
    login(driver)

    create_athlete(driver)

    time.sleep(1)

    success_message = driver.find_element(By.CSS_SELECTOR, "[data-sonner-toast] [data-title]").text

    assert success_message == "Atleta criado com sucesso!"

def test_it_should_be_able_to_warn_errors_when_creating_an_athlete(driver):
    login(driver)

    driver.get(URL + "athletes")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".bg-lime-600"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[form="new-athlete-form"]'))
    ).click()

    error_span = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span.text-red-500"))
    )

    assert error_span is not None

def test_it_should_be_able_to_delete_an_athlete(driver):
    login(driver)

    time.sleep(1)

    driver.get(URL + "athletes?athleteName=teste&gender=all&page=1")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//tr[.//td//span[text() = 'teste']]")
        )
    )

    remaining = driver.find_elements(By.XPATH, "//tr[.//td//span[text() = 'teste']]")

    while (len(remaining) > 0):
        row_action = driver.find_element(By.CSS_SELECTOR, ".border-b:nth-child(1) .gap-2")
        row_action.click()

        confirm_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".flex-col-reverse > .border-transparent"))
        )

        confirm_button.click()

        time.sleep(1)

        success_message = driver.find_element(By.CSS_SELECTOR, "[data-sonner-toast] [data-title]").text

        assert success_message == "Atleta removido com sucesso!"

        remaining = driver.find_elements(By.XPATH, "//tr[.//td//span[text() = 'teste']]")
    
    assert len(remaining) == 0

def test_it_should_be_able_to_cancel_a_deletion_of_an_athlete(driver):
    login(driver)

    create_athlete(driver)

    driver.get(URL + "athletes?athleteName=teste&gender=all&page=1")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//tr[.//td//span[text() = 'teste']]")
        )
    )

    row_action = driver.find_element(By.CSS_SELECTOR, ".border-b:nth-child(1) .gap-2")
    row_action.click()

    cancel_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space(span/text())='Cancelar']")
        )
    )

    cancel_button.click()

    time.sleep(1)

    remaining = driver.find_elements(By.XPATH, "//tr[.//td//span[text() = 'teste']]")
    
    assert len(remaining) == 1

def test_it_should_be_able_to_edit_an_athlete(driver):
    login(driver)

    create_athlete(driver)

    driver.get(URL + "athletes?athleteName=teste&gender=all&page=1")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//tr[.//td//span[text() = 'teste']]")
        )
    )

    edit_button = driver.find_element(By.CSS_SELECTOR, ".flex > .size-9")
    edit_button.click()

    time.sleep(1)

    open_modal_button = driver.find_element(By.CSS_SELECTOR, ".h-8.px-3").click()

    name_field = driver.find_element(By.CSS_SELECTOR, "#athlete-form #name")
    name_field.clear()
    name_field.send_keys("Teste do teste")

    time.sleep(1)

    save_button = driver.find_element(By.CSS_SELECTOR, "[role='dialog'] button[type='submit']")
    save_button.click()

    time.sleep(1)

    success_message = driver.find_element(By.CSS_SELECTOR, "[data-sonner-toast] [data-title]").text

    assert success_message == "Os dados do atleta foram atualizados com sucesso!"