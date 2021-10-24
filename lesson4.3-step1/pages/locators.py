from selenium.webdriver.common.by import By


class MainPageLocators():
    BASKET_PAGE_URL = ("http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear")
    BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PROD_NAME  = (By.CSS_SELECTOR, ".product_main h1")
    PROD_PRICE = (By.CSS_SELECTOR, "p.price_color")
    FIND_NAME = (By.CSS_SELECTOR, ".alert-success div strong")
    PROD_TMP  = (By.XPATH, './/*[@id="messages"]/div[1]/div/strong')
    PRICE_TMP = (By.XPATH, './/*[@id="messages"]/div[3]/div/p[1]/strong')


#.//*[contains(@class, 'success')]      # Просто заметка на будущее