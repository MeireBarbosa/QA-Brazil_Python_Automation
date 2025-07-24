from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from helpers import retrieve_phone_code
import time

class UrbanRoutesPage:
    # Seção "De" e "Para"
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Selecionar tarifa e chamar táxi
    taxi_option_locator = (By.XPATH, '//button[contains(text(),"chamar")]')
    comfort_icon_locator = (By.XPATH, '//img[@src=/static/media/kids.075fd8d4.svg]')
    comfort_active = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')

    def __init__(self, driver):
        self.driver = driver

    def enter_from_location(self, from_text):
        WebDriverWait(self.driver, timeout=3).until(
            EC.visibility_of_element_located(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(from_text)

    def enter_to_location(self, to_text):
        WebDriverWait(self.driver, timeout=3).until(
            EC.visibility_of_element_located(self.to_field))
        self.driver.find_element(*self.to_field).send_keys(to_text)

    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

    def get_from_location_value(self):
        return WebDriverWait(self.driver, timeout=3).until(
            EC.visibility_of_element_located(self.from_field)
        ).get_attribute('value')

    def click_taxi_option(self):
        self.driver.find_element(*self.comfort_icon_locator).click()

    def click_comfort_icon(self):
        self.driver.find_element(*self.comfort_icon_locator).click()

    def click_comfort_active(self):
        try:
            active_button = WebDriverWait(self.driver, timeout=10).until(
                EC.visibility_of_element_located(self.comfort_active)
            )
            return "active" in active_button.get_attribute("class")
        except Exception:
            return False