from pages.login_page import LoginPage


def test_Check_the_login_correctly_to_site(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.enter_username('standard_user')
    login_page.enter_password('secret_sauce')
    login_page.check_privacy_policy()
    login_page.click_submit_button()
    assert login_page.get_title() == 'Products'

def test_Missing_username(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.enter_username('')
    login_page.enter_password('secret_sauce')
    login_page.check_privacy_policy()
    login_page.click_submit_button()
    assert login_page.get_alert_message() == 'Epic sadface: Username is required'
    assert login_page.get_title() != 'Products'

def test_Missing_password(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.enter_username('standard_user')
    login_page.enter_password('')
    login_page.check_privacy_policy()
    login_page.click_submit_button()
    assert login_page.get_alert_message() == 'Epic sadface: Password is required'
    assert login_page.get_title() != 'Products'

def test_Privacy_policy_checkbox_not_checked(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.enter_username('standard_user')
    login_page.enter_password('secret_sauce')
    assert login_page.get_alert_message() == 'Username, Password, and Privacy Policy Check are required'
    login_page.click_submit_button()
    assert login_page.get_title() != 'Products'

def test_Valid_username_and_password(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.enter_username('standard_user')
    login_page.enter_password('secret_sauce')
    login_page.check_privacy_policy()
    login_page.click_submit_button()
    assert login_page.get_title() == 'Products'

def test_Invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.enter_username('standard_user')
    login_page.enter_password('erronea')
    login_page.check_privacy_policy()
    login_page.click_submit_button()
    assert login_page.get_alert_message() == 'Epic sadface: Username and password do not match any user in this service'
    assert login_page.get_title() != 'Products'

def test_Active_user(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.enter_username('standard_user')
    login_page.enter_password('secret_sauce')
    login_page.check_privacy_policy()
    login_page.click_submit_button()
    assert login_page.get_title() == 'Products'

def test_Inactive_user(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.enter_username('locked_out_user')
    login_page.enter_password('secret_sauce')
    login_page.check_privacy_policy()
    login_page.click_submit_button()
    assert login_page.get_alert_message() == 'Epic sadface: Sorry, this user has been locked out.'
    assert login_page.get_title() != 'Products'