from playwright.sync_api import Page, expect
from core.data import base_url
import allure 

class Header:
    def __init__(self, page: Page):
        self.page = page


    @allure.step("Открываем Хэдер на главной странице")
    def visit(self):
        self.page.goto(base_url)

    @allure.step("Нажимаем на кнопку регистрации")
    def click_on_registration_button(self):
        self.page.get_by_test_id("signup").click()

    @allure.step("Проверяем видимость кнопки создания объявления")
    def create_listing_button_should_be_visible(self):
        expect(self.page.get_by_test_id("create-listing")).to_be_visible()

    