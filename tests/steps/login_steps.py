from behave import given, when, then
from pages.login_page import LoginPage

@given("user is at the login page")
def step_user_at_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate()

@when("user enter the '{username}'")
def step_user_enter_username(context, username):
    context.login_page.enter_username(username)

@when("user enter a '{password}'")
def step_user_enter_password(context, password):
    context.login_page.enter_password(password)

@when("user check the Privacy Policy checkbox")
def step_user_check_privacy_policy(context):
    context.login_page.check_privacy_policy()

@when("user click on submit button")
def step_user_click_submit_button(context):
    context.login_page.click_submit_button()

@then("should display a title is '{title}'")
def step_should_display_title(context, title):
    assert context.login_page.get_title() == title

@then('should display the message alert as "{alert_message}"')
def step_should_display_alert_message(context, alert_message):
    assert context.login_page.get_alert_message() == alert_message

@then("should not display the title '{title}'")
def step_should_not_display_title(context, title):
    assert context.login_page.get_title() != title


