from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from helpers import retrieve_phone_code
import time

class UrbanRoutesPage:
    # Seção "De" e "Para"
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')


    def enter_phone_number(self, number):
        phone_input = self.driver.find_element(By.ID, "phone")
        phone_input.send_keys(number)

    def add_credit_card(self, number, name, expiry, cvv):
        self.driver.find_element(By.ID, "card_number").send_keys(number)
        self.driver.find_element(By.ID, "card_name").send_keys(name)
        self.driver.find_element(By.ID, "card_expiry").send_keys(expiry)
        cvv_input = self.driver.find_element(By.ID, "code")
        cvv_input.send_keys(cvv)
        self.driver.find_element(By.TAG_NAME, "body").click()  # simula perda de foco
        self.driver.find_element(By.ID, "add_card_button").click()

    def write_driver_comment(self, comment):
        comment_box = self.driver.find_element(By.ID, "driver_comment")
        comment_box.send_keys(comment)
        self.driver.find_element(By.ID, "submit_comment").click()

    def request_blanket_and_wipes(self):
        blanket_toggle = self.driver.find_element(By.ID, "blanket_toggle")
        blanket_toggle.click()
        assert "active" in blanket_toggle.get_attribute("class")

    def order_ice_cream(self, quantity):
        for _ in range(quantity):
            self.driver.find_element(By.ID, "add_ice_cream").click()

    def select_tariff_comfort(self):
        comfort_option = self.driver.find_element(By.ID, "tariff_comfort")
        if comfort_option.is_displayed():
            comfort_option.click()

    def send_request_with_message(self, message):
        message_box = self.driver.find_element(By.ID, "driver_message")
        message_box.send_keys(message)
        self.driver.find_element(By.ID, "request_button").click()


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


