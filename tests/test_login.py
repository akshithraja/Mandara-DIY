from pages.login import Login
from utilities.BaseClass import BaseClass
import pytest
from utilities import customlogger as cl
from data.login import logintestdata as td
from utilities.teststatus import StatusTest


class TestLogin(BaseClass):
    log = cl.custom_logger()

    @pytest.fixture(autouse=True)
    # loading all the objects in the test class
    def objectsetup(self, setup):
        self.log.info("Setting up the objects")
        self.lp = Login(self.driver)
        self.ts = StatusTest(self.driver)

    # Checks if the Mandara page has loaded by verifying the availability of the logo.
    def test_mandara_app_load(self):
        self.log.info("Verifying if the Mandara App loaded")
        result = self.lp.verify_mandara_app_load()
        self.ts.markFinal("Mandara app load verification", result, "Verification of Mandara load with logo appearance")

    # Verifies the title of the loaded Mandara Page
    def test_title(self):
        self.log.info("Checking the title of the Mandara login Page")
        result1 = self.lp.verify_login_page_title(td.page_title)
        self.ts.markFinal("Page title", result1, "Verification of the Page Title")

    # Verifies the copyright info with the current year
    def test_copyright(self):
        self.log.info("Checking the copyright presence and year correctness")
        result = self.lp.copyright()
        self.ts.markFinal("Copyright Info", result, "Verification of the presence and year correctness for copyright")

    # Verifies the text in the username field, password field, and the text in the buttons of login page
    def test_text(self):
        self.log.info("Verification of the text available in the buttons")
        result1 = self.lp.verify_username_text()
        result2 = self.lp.verify_password_text()
        result3 = self.lp.verify_fgt_pwd_text()
        result4 = self.lp.verify_login_text()
        self.ts.mark(result1, "Verifying the text in the username field")
        self.ts.mark(result2, "Verifying the text in the password field")
        self.ts.mark(result3, "Verifying the text in the forgot_password button")
        self.ts.markFinal("Verifying the text in the Login page", result4, "Verification of all text in login button")

    # Verifies the input alert for username and password when clicked and no data is entered
    def test_login_input_field_alert(self):
        self.log.info("Checking the alert messages for the username and password")
        result1 = self.lp.username_input_alert()
        result2 = self.lp.password_input_alert()
        self.ts.mark(result1, "Verifying the username input alert when no text is given")
        self.ts.markFinal(
            "Login page alert message check", result2, "Verifying the username input alert when no text is given"
        )

    # Verifies the login button being disabled when no value is entered in both username and password fields
    def test_login_button_disabled(self):
        self.log.info("Verifying if the login button is disabled when no value is entered to both login fields")
        result = self.lp.verify_disabled_login_button()
        self.ts.markFinal("Login button disable check", result, "Verifying disabled login button on start")

    # Verifies the invalid log with wrong username
    def test_invalid_login_user(self):
        self.log.info("Verifying Invalid login with wrong username")
        self.lp.login(td.wrongusername, td.password)
        result2 = self.lp.verify_login_failed()
        self.ts.markFinal("Invalid Login", result2, "Verification of Invalid Login with wrong username")

    # Verifies the invalid log with wrong password
    def test_invalid_login_pass(self):
        self.log.info("Verifying Invalid login with wrong password")
        self.lp.login(td.username, td.wrongpassword)
        result2 = self.lp.verify_login_failed()
        self.ts.markFinal("Invalid Login", result2, "Verification of Invalid Login with wrong password")

    # Verifies the forgot password feature
    def test_forgotpassword(self):
        result3 = self.lp.verify_enter_valid_email()
        result4 = self.lp.forgot_password_invalid(td.wrongemail)
        result5 = self.lp.forgot_password_valid(td.email)
        self.ts.mark(result3, "Checking valid Email message")
        self.ts.mark(result4, "Sending wrong Email and verifying the error thrown")
        self.ts.markFinal("Valid Email check", result5, "Verification of forgot password feature")

    # Verifies the text for the buttons in the forgot password page.
    def reset_pwd_page_text(self):
        result1 = self.lp.verify_back_to_login_text()
        result2 = self.lp.verify_reset_text()
        self.ts.mark(result1, "Verification of back_to_login_text")
        self.ts.markFinal("Verification of text in reset password field", result2,
                          "Verification of reset password text ")

    # Verifies the presence and functionality of the "back to login" feature
    def test_back_to_login(self):
        result1 = self.lp.presence_back_to_login()
        result2 = self.lp.back_to_login()
        self.ts.mark(result1, "Verifying the presence of back to login button")
        self.ts.markFinal("Back to login", result2, "Verification of back to login button")

    # Verifies the valid login
    def test_valid_login(self):
        self.lp.login(td.username, td.password)
        result3 = self.lp.verify_login_success()
        self.ts.markFinal("Valid Login", result3, "Verification of Valid Login")
