import time
import math
import pytest
from selenium import webdriver

l = 'https://stepik.org/lesson/236895/step/1 https://stepik.org/lesson/236896/step/1 https://stepik.org/lesson/236897/step/1 https://stepik.org/lesson/236898/step/1 https://stepik.org/lesson/236899/step/1 https://stepik.org/lesson/236903/step/1 https://stepik.org/lesson/236904/step/1 https://stepik.org/lesson/236905/step/1'
l = l.split()

def timenow():
    return str(math.log(int(time.time())))

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize("list_link", l)
def test_check_feedback(browser, list_link):
    link = f'{list_link}'
    browser.get(link)

    textarea = browser.find_element_by_tag_name('textarea')

    answer = timenow()

    textarea.send_keys(answer)

    button = browser.find_element_by_css_selector("[class='attempt__actions'] > button[type='button']")
    button.click()

    check = browser.find_element_by_css_selector('pre[class="smart-hints__hint"]')
    assert 'Correct!' in check.text