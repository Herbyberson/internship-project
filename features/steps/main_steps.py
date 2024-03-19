from behave import given, when, then
from time import sleep


@given('Open the registration page')
def open_reelly_registration_page(context):
    context.app.main_page.open_page()


@when('Enter some test information in the input fields')
def enter_some_test_information(context):
    name = 'James Mcdaniel'
    phone = '123456789'
    email = name.replace(" ", "") + '@GMAIL.COM'
    password = "qwerty"
    context.app.registration_page.element_visible()
    context.app.registration_page.name_information(name)
    context.app.registration_page.phone_number_information(phone)
    context.app.registration_page.email_address_information(email)
    context.app.registration_page.password_information(password)

    sleep(7)


@then('Verify the right information is present')
def verify_right_information(context):
    name = 'James Mcdaniel'
    phone = '123456789'
    email = name.replace(" ", "") + '@GMAIL.COM'
    password = "qwerty"
    expected_information = {'name': name, 'phone': phone, 'email': email, 'password': password}
    context.app.registration_page.verify_information(expected_information['email'])
