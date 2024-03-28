from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from support.logger import logger
from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, 15)
    context.app = Application(context.driver)

    # headless environment Google Chrome set up:

    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service, options=options)

    # headless environment Firefox set up:

    # options = webdriver.FirefoxOptions()
    # options.add_argument("--headless")
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service, options=options)

    ### BROWSERSTACK ENVIRONMENT ###

    # bs_username = # private-removed for privacy
    # bs_access_key = # private-removed for privacy
    # url = f'http://{bs_username}:{bs_access_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    #
    # bstack_options = {
    #     "browserName": "Safari",
    #     "os": "OS X",
    #     "osVersion": "Ventura",
    #     "browserVersion": "16.5",
    #     "sessionName": scenario_name
    # }
    #
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
