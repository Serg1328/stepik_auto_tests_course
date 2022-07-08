import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    driver = webdriver.Chrome()  # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
    driver.get(link)             # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке

    # метод find_element_by возвращает только первый из всех элементов, которые подходят под условия поиска.

    input1 = driver.find_element(By.TAG_NAME, "input") # находим на сайте поле "First name" по тегу: input
    #input1 = driver.find_element_by_tag_name("input")
    input1.send_keys("Serg")     # вводим имя Serg в поле "First name"
    input2 = driver.find_element(By.NAME, "last_name") # находим на сайте поле "Last name" по атрибуту [name="last_name"] элемента
    #input2 = driver.find_element_by_name("last_name")
    input2.send_keys("Plakhin")  # вводим имя Plakhin в поле "Last name"
    input3 = driver.find_element(By.CLASS_NAME, "city") # находим на сайте поле "City" по атрибуту [class="form-control city"](.city) элемента
    #input3 = driver.find_element_by_class_name("city")
    input3.send_keys("Moscow")   # вводим название города Moscow в поле "City"
    input4 = driver.find_element(By.ID, "country")   # находим на сайте поле "Country" по атрибуту ID (#country) элемента
    #input4 = driver.find_element_by_id("country")
    input4.send_keys("Russia")   # вводим название страны "Russia" в поле "Country"
    button = driver.find_element(By.CSS_SELECTOR, "button.btn") # Найдем кнопку:"Submit",которая отправляет введенные данные
    #button = driver.find_element_by_css_selector(".btn")
    button.click() # кликнем по ней

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла