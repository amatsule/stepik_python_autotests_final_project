from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION_FIELD)
        password_field.send_keys(password)
        password_confirmation_field = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM_REGISTRATION_FIELD)
        password_confirmation_field.send_keys(password)
        register = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.EMAIL_LOGIN_FIELD), "Email Login field not found"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_LOGIN_FIELD), "Password Login field not found"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button not found"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.EMAIL_REGISTER_FIELD), "Email Registration field not found"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_REGISTRATION_FIELD), "Password Registration field not found"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_CONFIRM_REGISTRATION_FIELD), "Password Registration Confirmation field not found"
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "Register Button not found"
