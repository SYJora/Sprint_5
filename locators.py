from selenium.webdriver.common.by import By

class BurgerLocators:

    BUTTON_LOGIN_IN_ACCOUNT = (By.XPATH, "//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']") # Кнопка для в хода на главной странице
    BUTTON_LOGIN = (By.XPATH, "//button[contains(text(), 'Войти')]") #Текст кнопки входа
    REDISTRATION_LINK = (By.XPATH, "//a[starts-with(@href, '/re')]") #Сылка на регестрацию

    ACCOUNT_NAME = (By.XPATH, "(//input[@type = 'text'])[1]") #Поле ввода имени
    ACCOUNT_EMAIL = (By.XPATH, "(//input[@type = 'text'])[1]") #Поле ввода электроной почты
    REGIDTER_ACCOUNT_EMAIL = (By.XPATH, "(//input[@type = 'text'])[2]") #Поле вода электроной почты на странице регестраций
    ACCOUNT_PASSWORD = (By.XPATH, "//input[@type = 'password']") #Поле ввода пароля
    ERROR_TEXT_INCORRECT_PASSWORD = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]") #текст ошибки прине коректном воде пароля

    BUTTON_REGISTRATION = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]") #Кнопка Регистраций
    BUTTON_MAKE_ORDER = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]") #Кнопка Сделать заказ
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]") #Кнопка входа в личный кабинет
    BUTTON_DESIGNER = (By.XPATH, "//p[contains(text(), 'Конструктор')]") #Кнопка перехода в конструктор
    BUTTON_LOGOUT = (By.XPATH, "//button[contains(text(), 'Выход')]") #Кнопка выхода из личного кабинета

    LINK_LOGIN = (By.XPATH, "//a[contains(@href,'/login')]") #Ссылка на регистрацию
    LINK_FORGOT_PASSWORD = (By.XPATH, "//a[contains(@href, '/forgot')]") #Ссылка востановление пароля

    TAB_PROFAIL = (By.XPATH, "//a[contains(@href, '/account/profile')]") #Кнопка профиль в личном кабинете
    TAB_DESIGNER_FILLING = (By.XPATH, "//span[text()= 'Начинки']") #Вкладка начинки в конструкторе
    TAB_DESIGNER_SAUCES = (By.XPATH, "//span[text()= 'Соусы']") #Вкладка соусы в конструкторе
    TAB_DESIGNER_BURGERS = (By.XPATH, "//span[text()= 'Булки']") #Вкладка булки в конструкторе

    TEXT_DESIGNER = (By.XPATH, "//h1[@class]") #Текст кнопки Конструктор
    TEXT_LOGIN_PAGE = (By.XPATH, "//h2[text() = 'Вход']") #Текст надписи на странице входа
    TEXT_SECTION_DESIGNER_FILLING = (By.XPATH, "//h2[contains(text(), 'Начинки')]") #Текст раздела в конструкторе начинка
    TEXT_SECTION_DESIGNER_SAUCES = (By.XPATH, "//h2[contains(text(), 'Соусы')]") #Текст раздела в конструкторе соусы
    TEXT_SECTION_DESIGNER_BURGERS = (By.XPATH, "//h2[contains(text(), 'Булки')]") #Текст раздела в конструкторе булки

    LOGO = (By.XPATH, "//div[@class = 'AppHeader_headerlogo2D0X2']") #Логотип на главной страницы

