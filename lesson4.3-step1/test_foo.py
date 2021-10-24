from .pages.main_page import MainPage
from .pages.locators import MainPageLocators

def test_guest_can_add_product_to_basket(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page = MainPage(browser, MainPageLocators.BASKET_PAGE_URL)   
    page.open()                         # Переход на выбранную страницу
    page.go_to_basket_page()            # Найти и нажать кнопку ДОБАВИТЬ В КОРЗИНУ
    page.solve_quiz_and_get_code()      # Проверочный код
    page.check_basket_page(1)           # Проверка товара
    page.check_basket_page(2)           # Проверка цены товара
    
    