from selenium import webdriver
import time

from selenium.webdriver.chrome.webdriver import WebDriver

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

import unittest

class TestReg(unittest.TestCase):
    def test_reg1(self):
        driver = webdriver.Chrome()
        driver.get(link1)

        input1 = driver.find_element_by_css_selector('input.first[required]')
        input1.send_keys("Serg")

        input2 = driver.find_element_by_css_selector('[placeholder="Input your last name"]')
        input2.send_keys("Serg")

        input3 = driver.find_element_by_css_selector('[placeholder="Input your email"]')
        input3.send_keys("serg.ru")

        # Отправляем заполненную форму
        button = driver.find_element_by_css_selector(".btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = driver.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Registration check')

    def test_reg2(self):
        driver = webdriver.Chrome()
        driver.get(link2)

        input1 = driver.find_element_by_css_selector('input.first[required]')
        input1.send_keys("Serg")

        input2 = driver.find_element_by_css_selector('[placeholder="Input your last name"]')
        input2.send_keys("Serg")

        input3 = driver.find_element_by_css_selector('[placeholder="Input your email"]')
        input3.send_keys("serg.ru")

        # Отправляем заполненную форму
        button = driver.find_element_by_css_selector(".btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = driver.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Registration check')

if __name__ == "__main__":
    unittest.main()