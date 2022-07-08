import time
from selenium import webdriver

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:

    driver = webdriver.Chrome() # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера

    driver.get(link)
    time.sleep(2)
    button = driver.find_element(By.ID, "submit_button")
    button.click()
    time.sleep(1)

finally:
    # закрываем браузер после всех манипуляций
    driver.quit()
