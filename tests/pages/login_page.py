from selenium.webdriver.common.by import By



class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.URL = 'https://www.saucedemo.com/'
        self.input_username = 'user-name'
        self.input_password = 'password'
        self.button_submit = 'login-button'
        self.title = '//*[@class="title"]'
        self.alert_message = '//*[@class="error-message-container error"]'

    def navigate(self):
        self.driver.get(self.URL)

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.input_username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.input_password).send_keys(password)

    def click_submit_button(self):
        self.driver.find_element(By.ID, self.button_submit).click()

    def get_title(self):
        return self.driver.find_element(By.XPATH, self.title).text

    def get_alert_message(self):
        return self.driver.find_element(By.XPATH, self.alert_message).text