from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from helpers import retrieve_phone_code

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    phone_input = (By.ID, "phone")
    phone_code_input = (By.ID, "code")
    card_number_input = (By.ID, "card_number")
    card_code_input = (By.ID, "card_code")
    confirm_card_label = (By.ID, "card_confirmed")
    comment_input = (By.ID, "driver_comment")
    confirm_comment_label = (By.ID, "comment_submitted")
    blanket_toggle = (By.ID, "blanket_toggle")
    ice_cream_button = (By.ID, "add_ice_cream")
    ice_cream_quantity_label = (By.ID, "ice_cream_count")
    comfort_tariff = (By.ID, "tariff_comfort")
    request_button = (By.ID, "request_button")
    message_input = (By.ID, "driver_message")
    confirmation_popup = (By.ID, "search_popup")
    taxi_option_locator = (By.XPATH, '//button[contains(text(),"chamar")]')
    comfort_icon_locator = (By.XPATH, '//img[@src="/static/media/kids.075fd8d4.svg"]')
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

    def get_to_location_value(self):
        return self.driver.find_element(*self.to_field).get_attribute('value')

    def click_taxi_option(self):
        self.driver.find_element(*self.taxi_option_locator).click()

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

    def click_number_text(self, number):
        self.driver.find_element(*self.phone_input).send_keys(number)
        code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.phone_code_input).send_keys(code)

    def confirm_number(self):
        return self.driver.find_element(*self.phone_input).get_attribute("value")

    def click_add_card(self, number, cvv):
        self.driver.find_element(*self.card_number_input).send_keys(number)
        self.driver.find_element(*self.card_code_input).send_keys(cvv)
        self.driver.find_element(By.TAG_NAME, "body").click()
        self.driver.find_element(By.ID, "add_card_button").click()

    def confirm_card(self):
        return self.driver.find_element(*self.confirm_card_label).text

    def add_comment(self, comment):
        self.driver.find_element(*self.comment_input).send_keys(comment)

    def confirm_comment(self):
        return self.driver.find_element(*self.confirm_comment_label).text

    def toggle_blanket(self):
        self.driver.find_element(*self.blanket_toggle).click()

    def toggle_blanket_active(self):
        return "active" in self.driver.find_element(*self.blanket_toggle).get_attribute("class")

    def add_ice_cream(self):
        self.driver.find_element(*self.ice_cream_button).click()

    def order_ice_cream(self, quantity):
        for _ in range(quantity):
            self.add_ice_cream()

    def ice_cream_quantity(self):
        return self.driver.find_element(*self.ice_cream_quantity_label).text

    def show_popup(self):
        return self.driver.find_element(*self.confirmation_popup).text