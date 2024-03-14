from behave import given, when, then
from time import sleep


@given('Open the registration page')
def open_reelly_registration_page(context):
    context.app.main_page.open_page()


@when('Enter some test information in the input fields')
def enter_some_test_information(context):
    information = 'James Mcdaniel'
    context.app.registration_page.element_visible()
    context.app.registration_page.enter_information(information)
    sleep(7)


@then('Verify the right information is present')
def verify_right_information(context):
    expected_information = 'James Mcdaniel'
    context.app.registration_page.verify_information(expected_information)
