from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):

    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Akshay Kathpalia\\Documents\\Manjima\\chromedriver_win32\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\\Akshay Kathpalia\\Documents\\Manjima\\geckodriver-v0"
                                                   ".27.0-win64\\geckodriver.exe")
    else:
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Akshay Kathpalia\\Documents\\Manjima\\chromedriver_win32\\chromedriver.exe")

    driver.get("https://qa.sigtuple.com")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
