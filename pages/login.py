from data.login import loginelements as el
from data.login import logintestdata as td
from base.basepage import BasePage
from utilities import customlogger as cl


class Login(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    log = cl.custom_logger()

    def enter_username(self, username):
        self.sendKeys(username, *el.user_name)

    def enter_password(self, password):
        self.sendKeys(password, *el.password)

    def click_login_button(self):
        self.elementClick(*el.login_link)

    def verify_mandara_app_load(self):
        result = self.isElementPresent(*el.sigtuple_logo)
        return result

    def verify_login_text(self):
        result = self.verify_text_match_from_element(td.login_btn_text, *el.login_link)
        return result

    def verify_username_text(self):
        result = self.verify_text_match_from_element(td.usr_ghost_text, *el.user_ghost)
        return result

    def verify_password_text(self):
        result = self.verify_text_match_from_element(td.pwd_ghost_text, *el.pwd_ghost)
        return result

    def verify_fgt_pwd_text(self):
        result = self.verify_text_match_from_element(td.fgt_pwd_text, *el.forgot_password)
        return result

    def verify_back_to_login_text(self):
        result = self.verify_text_match_from_element(td.back_to_login, *el.back_to_login)
        return result

    def verify_reset_text(self):
        result = self.verify_text_match_from_element(td.reset_password_text, *el.reset_password)
        return result

    def verify_disabled_login_button(self):
        self.log.info("Verifying if the login button is disabled")
        self.log.debug("Checking the enabled returns: " + str(self.verify_if_button_enabled(*el.login_link)))
        if self.verify_if_button_enabled(*el.login_link):
            return True
        else:
            return False

    def username_input_alert(self):
        self.log.info("Verifying the alert text for the username input field")
        self.util.sleep(2)
        self.elementClick(*el.user_name)
        self.elementClick(*el.login_container)
        self.util.sleep(2)
        return self.verify_text_match_from_element(td.username_input_alert, *el.username_input_alert)

    def password_input_alert(self):
        self.log.info("Verifying the alert text for the password input field")
        self.elementClick(*el.user_name)
        self.elementClick(*el.login_container)
        self.util.sleep(2)
        return self.verify_text_match_from_element(td.password_input_alert, *el.password_input_alert)

    def login(self, username, password):
        self.clearField(*el.user_name)
        self.clearField(*el.password)
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def verify_login_failed(self):
        self.util.sleep(1, "Waiting for the invalid creds message")
        expected_invalid_header = self.getText(*el.error_invalid_login)
        expected_invalid_message = self.getText(*el.error_invalid_login1)
        if self.util.verifyTextMatch(td.invalid_creds_header, expected_invalid_header) and self.util.verifyTextMatch(
                td.invalid_creds_message, expected_invalid_message):
            return True
        else:
            return False

    def verify_login_success(self):
        self.util.sleep(2, "user icon")
        result = self.elementPresenceCheck(*el.user_icon)
        return result

    def verify_login_page_title(self, titleToVerify):
        result = self.verifyPageTitle(titleToVerify)
        return result

    def verify_enter_valid_email(self):
        self.util.sleep(2, "Forgot Password")
        self.elementClick(*el.forgot_password)
        self.elementClick(*el.fgtpasswdemail)
        self.moveOffsetToElement(10, 30, *el.fgtpasswdemail)
        self.util.sleep(2, "Message for entering valid email")
        return self.verify_text_match_from_element(td.forgot_password_input_alert, *el.forgot_password_alert)

    def forgot_password_invalid(self, email):
        self.sendKeys(email, *el.fgtpasswdemail)
        self.elementClick(*el.reset_password)
        self.util.sleep(1)
        result = self.elementPresenceCheck(*el.invalid_forgot_email)
        self.util.sleep(2)
        return result

    def forgot_password_valid(self, email):
        self.clearField(*el.fgtpasswdemail)
        self.elementClick(*el.fgtpasswdemail)
        self.sendKeys(email, *el.fgtpasswdemail)
        self.elementClick(*el.reset_password)
        self.util.sleep(1, "Confirmation Message for Email sent")
        confirmation_message = self.getText(*el.confirmation_messgforgtpasswd, "xpath")
        self.log.info("Verifying the successful email send for password reset")
        result = self.util.verifyTextMatch(confirmation_message, td.success_email_send_message)
        return result

    def presence_back_to_login(self):
        result = self.elementPresenceCheck(*el.back_to_login)
        return result

    def back_to_login(self):
        self.elementClick(*el.back_to_login)
        result = self.elementPresenceCheck(*el.password)
        return result

    def copyright(self):
        result = self.verify_text_match_from_element(td.copy_right_text, *el.copyright)
        return result
