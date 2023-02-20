import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


def registration_page_test(url: str) -> str:
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        driver.find_element(By.XPATH, '//label[text()="First name*"]/following::input[1]').send_keys("test")
        driver.find_element(By.XPATH, '//label[text()="Last name*"]/following::input[1]').send_keys("test")
        driver.find_element(By.XPATH, '//label[text()="Email*"]/following::input[1]').send_keys("test")

        driver.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

        return driver.find_element(By.TAG_NAME, "h1").text

    except Exception as e:
        print(e)

    finally:
        driver.quit()


class TestRegistration(unittest.TestCase):
    def test_first_page(self):
        h1 = registration_page_test("https://suninjuly.github.io/registration1.html")
        self.assertEqual("Congratulations! You have successfully registered!", h1, "Registration failed")

    def test_second_page(self):
        h1 = registration_page_test("https://suninjuly.github.io/registration2.html")
        self.assertEqual("Congratulations! You have successfully registered!", h1, "Registration failed")


if __name__ == '__main__':
    unittest.main()
