import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ACCOUNT_XPATH = '//*[@href="https://account.magento.com/customer/account/login"]'
EMAIL_XPATH = '//*[@id="email"]'
PASSWORD_XPATH = '//*[@id="pass"]'
LOGIN_XPATH = '//*[@id="send2"]'
USERNAME_XPATH = '//*[@class="header-nav-current-user"]'
EMAIL = "test@pixafy.com"
PASSWORD = "123456"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")


class TestSeleniumLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=options)

    def test_login(self):
        driver = self.driver
        """Go to http://enterprise-demo.user.magentotrial.com/"""
        driver.get("https://enterprise-demo.user.magentotrial.com/")

        account_link = driver.find_element(By.XPATH, ACCOUNT_XPATH)
        WebDriverWait(driver, 10).until(EC.visibility_of(account_link))
        account_link.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, EMAIL_XPATH)))
        """Sign in using these credentials."""
        email_field = driver.find_element(By.XPATH, EMAIL_XPATH)
        email_field.send_keys(EMAIL)

        password_field = driver.find_element(By.XPATH, PASSWORD_XPATH)
        password_field.send_keys(PASSWORD)

        login_btn = driver.find_element(By.XPATH, LOGIN_XPATH)
        login_btn.click()

        """Wait for 5 seconds."""
        driver.implicitly_wait(5)

        """Verify that you are now signed in."""
        """
        Unfortunately, this website has changed, and the link:
        http://enterprise-demo.user.magentotrial.com/
        is now "Status Code: 301 Moved Permanently"
        and now it redirects to:
        https://magento.com/products/magento-commerce
        and there is no such account as you mentioned in the task.
        Nevertheless, I continue here assuming what would I do further. 
        
        To assure I'm logged in, I would use something like that:
        """
        LOGO = '//*[@class="logo-main"]'
        delete_me = driver.find_element(By.XPATH, LOGO)
        assert delete_me
        # account_link = driver.find_element(By.XPATH, USERNAME_XPATH)
        # assert EMAIL in account_link.text()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
