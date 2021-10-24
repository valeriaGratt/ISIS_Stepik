from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage): 
    
    def go_to_basket_page(self):
        # Проверим наличие кнопки ДОБАВИТЬ В КОРЗИНУ
        assert self.is_element_present(*MainPageLocators.BASKET_BTN), "BASKET_BTN is not presented"
        basket_btn = self.browser.find_element(*MainPageLocators.BASKET_BTN)
        
        # Сохраним для сравнения имя выбранного товара
        self.tovar  = self.browser.find_element(*MainPageLocators.PROD_NAME).text
        # Сохраним для сравнения стоимость того же товара
        self.price = self.browser.find_element(*MainPageLocators.PROD_PRICE).text
        
        basket_btn.click()
        
    def check_basket_page(self, kod):
        if kod == 1:
            pr_rmp  = self.browser.find_element(*MainPageLocators.PROD_TMP).text
            print(f"   Наименование товара: {self.tovar}")
            assert pr_rmp == self.tovar, f"Другой товар - {pr_rmp} != {self.tovar}"
        else:
            pr_rmp  = self.browser.find_element(*MainPageLocators.PRICE_TMP).text
            print(f"   Цена для продажи: {self.price}")
            assert pr_rmp == self.price, f"Цена отличается от изначальной - {pr_rmp} != {self.price}"
