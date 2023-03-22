import pytest
import time
import math

from config import STEPIK_LOGIN, STEPIK_PASSWORD
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize('url', ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1',
                                 'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
                                 'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
                                 'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1'])
def test_auth(browser, url):
    browser.implicitly_wait(10)
    browser.get(url)
    browser.find_element(By.CSS_SELECTOR, "#ember33").click()
    browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys(STEPIK_LOGIN)
    browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys(STEPIK_PASSWORD)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    WebDriverWait(browser, 10).until(EC.invisibility_of_element((By.CSS_SELECTOR, ".box")))
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea")))
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea")))\
        .send_keys(str(math.log(int(time.time()))))
    browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".attempt-message_correct")))
    result = browser.find_element(By.CSS_SELECTOR, ".attempt__message div p").text
    print(result)
    assert "Correct!" in result
