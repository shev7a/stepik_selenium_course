from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from math import log, sin


def calc(x: int) -> str:
    return str(log(abs(12 * sin(x))))


url = "https://suninjuly.github.io/explicit_wait2.html"

driver = webdriver.Chrome()

try:
    driver.get(url)
    WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    driver.find_element(By.ID, "book").click()
    x = int(driver.find_element(By.ID, "input_value").text)
    driver.find_element(By.ID, "answer").send_keys(calc(x))
    driver.find_element(By.ID, "solve").click()

    print(f'Answer: {driver.switch_to.alert.text.split(":")[-1].strip()}')

except Exception as e:
    print(e)
finally:
    driver.quit()
