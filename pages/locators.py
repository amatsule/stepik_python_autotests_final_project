from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    EMAIL_LOGIN_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD_LOGIN_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")
    EMAIL_REGISTER_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REGISTRATION_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_CONFIRM_REGISTRATION_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    HAS_BEEN_ADDED_TO_BASKET_MESSAGE = (By.XPATH, "//div[@id='messages']//strong")
    BASKET_TOTAL_MESSAGE = (By.XPATH, "//p[contains(text(),'Your basket total')]//strong ")
    PRODUCT_NAME_STRING = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_STRING = (By.CSS_SELECTOR, ".product_main .price_color")

