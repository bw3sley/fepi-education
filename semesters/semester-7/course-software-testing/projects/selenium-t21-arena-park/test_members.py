import pytest

import time 

import uuid

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

def generate_unique_email():
    unique_id = uuid.uuid4().hex[:8]
    return f"teste_{unique_id}@example.com"

def login(driver):
    driver.get(URL)

    driver.find_element(By.ID, "email").send_keys("bw3sley@gmail.com")
    driver.find_element(By.ID, "password").send_keys("T21-ARENA-PARK")
    
    driver.find_element(By.CSS_SELECTOR, ".items-center:nth-child(1)").click()

    time.sleep(1)

def create_member(driver):
    driver.get(URL + "members")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".bg-lime-600"))
    ).click()

    driver.find_element(By.ID, "name").send_keys("teste")

    email = generate_unique_email()
    driver.find_element(By.ID, "email").send_keys(email)
    
    driver.find_element(By.ID, "phone").send_keys("99999999999")

    Select(driver.find_element(By.CSS_SELECTOR, ".flex:nth-child(4) > select")).select_by_visible_text("Voluntário")

    driver.find_element(By.NAME, "areas").click()
    driver.find_element(By.CSS_SELECTOR, '[data-value="(Selecionar todos)"]').click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[form="new-member-form"]'))
    ).click()

    time.sleep(1)

def test_it_should_be_able_to_create_member(driver):
    login(driver)

    create_member(driver)

    success_message = driver.find_element(By.CSS_SELECTOR, "[data-sonner-toast] [data-title]").text

    assert success_message == "Voluntário cadastrado com sucesso!"

def test_it_should_be_able_to_warn_errors_when_creating_an_athlete(driver):
    login(driver)

    driver.get(URL + "members")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".bg-lime-600"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[form="new-member-form"]'))
    ).click()

    error_span = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span.text-red-500"))
    )

    assert error_span is not None

def test_it_should_be_able_to_delete_an_athlete(driver):
    login(driver)

    time.sleep(1)

    driver.get(URL + "members?athleteName=teste&role=all&page=1")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//tr[.//td//span[text() = 'teste']]")
        )
    )

    remaining = driver.find_elements(By.XPATH, "//tr[.//td//span[text() = 'teste']]")

    while (len(remaining) > 0):
        row_action = driver.find_element(By.CSS_SELECTOR, 'table [title="Delete o usuário"]')
        row_action.click()

        confirm_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".flex-col-reverse > .border-transparent"))
        )

        confirm_button.click()

        time.sleep(1)

        success_message = driver.find_element(By.CSS_SELECTOR, "[data-sonner-toast] [data-title]").text

        assert success_message == "Voluntário removido com sucesso!"

        remaining = driver.find_elements(By.XPATH, "//tr[.//td//span[text() = 'teste']]")
    
    assert len(remaining) == 0

def test_it_should_be_able_to_cancel_a_deletion_of_an_athlete(driver):
    login(driver)

    create_member(driver)

    driver.get(URL + "members?athleteName=teste&role=all&page=1")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//tr[.//td//span[text() = 'teste']]")
        )
    )

    row_action = driver.find_element(By.CSS_SELECTOR, 'table [title="Delete o usuário"]')
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

    create_member(driver)

    driver.get(URL + "members?athleteName=teste&role=all&page=1")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//tr[.//td//span[text() = 'teste']]")
        )
    )

    row_action = driver.find_element(By.CSS_SELECTOR, 'table [title="Editar o usuário"]')
    row_action.click()

    name_field = driver.find_element(By.ID, "name")
    name_field.clear()
    name_field.send_keys("Teste do teste")

    time.sleep(1)

    save_button = driver.find_element(By.CSS_SELECTOR, "[role='dialog'] button[type='submit']")
    save_button.click()

    time.sleep(1)

    success_message = driver.find_element(By.CSS_SELECTOR, "[data-sonner-toast] [data-title]").text

    assert success_message == "Voluntário atualizado com sucesso!"