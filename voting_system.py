from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Python libraries needed
# pip install selenium
# pip install webdriver-manager
# pip install requests


# In some cases, it's needed a proxy server to avoid getting banner
# ScrapeOps offers a limited but useful DEMO account.
# http://scrapeops.io/

SCRAPEOPS_API_KEY = ''
proxy_options = f"http://scrapeops.headless_browser_mode=true:{SCRAPEOPS_API_KEY}@proxy.scrapeops.io:5353"


def init_chrome():
    ip_proxy = proxy_options
    """Opciones de navegación"""
    options = webdriver.ChromeOptions()
    # comment this line if you don't need a proxy
    options.add_argument(f'--proxy-server={ip_proxy}')
    options.add_argument('--start-maximized')
    # options.add_argument('--window-size=1000,1000')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-web-security')  # Disable same-origin policy
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-notifications')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--no-sandbox')
    options.add_argument('--log-level=3')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--no-default-browser-check')
    options.add_argument('--no-first-run')
    options.add_argument('--disable-blink-features=AutomationControlled')

    exp_options = [
        'enable-automation',  # Remove the text "Chrome is being controlled by automated test software"
        'ignore-certificate-errors',
        'enable-logging'
    ]
    options.add_experimental_option("excludeSwitches", exp_options)
    prefs = {
        "profile.default_content_setting_values.notifications": 2,
        # Notifications 0=ask | 1=allow | 2=not allow
        "intl.accept_languages": ["es-ES", "es"],  # set browser language
        "credentials_enable_service": False
    }
    options.add_experimental_option("prefs", prefs)
    # Configurar el navegador
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver


""" MAIN ################################################ """

if __name__ == '__main__':

    driver = init_chrome()
    driver.maximize_window()
    # URL WITH THE VOTING SYSTEM
    url = "https://www.lacasadelosfamososmexico.tv/vota"
    driver.get(url)
    time.sleep(7)

    iframe = driver.find_element(By.XPATH,
                                 '//*[@id="main-web-app-00000188-0813-d082-a988-2b1f07950000"]/section/div[1]/div[2]/iframe')
    driver.switch_to.frame(iframe)
    try:
        wait = WebDriverWait(driver, 8)
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[2]/div/div/div[2]/div[1]/div[1]")))
        element.click()

    except Exception:
        print("An exception occurred")
        pass
    finally:

        time.sleep(random.randint(1, 4))
        driver.quit()
