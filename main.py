from asyncio import timeout

import data
import helpers
from pages import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    def teardown_method(self):
        self.driver.quit()

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_from_location(data.ADDRESS_FROM)
        routes_page.enter_to_location(data.ADDRESS_TO)
        assert routes_page.get_from_location_value() == data.ADDRESS_FROM
        assert routes_page.get_to_location_value() == data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        assert routes_page.click_comfort_active()

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        routes_page.click_number_text(data.PHONE_NUMBER)
        assert data.PHONE_NUMBER in routes_page.confirm_number()

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        routes_page.click_add_card(data.CARD_NUMBER, data.CARD_CODE)
        assert "Cartão" in routes_page.confirm_card()

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        routes_page.add_comment(data.MESSAGE_FOR_DRIVER)
        assert data.MESSAGE_FOR_DRIVER in routes_page.confirm_comment()

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        routes_page.toggle_blanket()
        assert routes_page.toggle_blanket_active() is True

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        routes_page.order_ice_cream(2)
        assert int(routes_page.ice_cream_quantity()) == 2

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        routes_page.click_number_text(data.PHONE_NUMBER)
        routes_page.click_add_card(data.CARD_NUMBER, data.CARD_CODE)
        routes_page.add_comment(data.MESSAGE_FOR_DRIVER)
        assert "Buscar carro" in routes_page.show_popup()