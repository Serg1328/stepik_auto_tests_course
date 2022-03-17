import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
l = 'https://stepik.org/lesson/236895/step/1 https://stepik.org/lesson/236896/step/1 https://stepik.org/lesson/236897/step/1 https://stepik.org/lesson/236898/step/1 https://stepik.org/lesson/236899/step/1 https://stepik.org/lesson/236903/step/1 https://stepik.org/lesson/236904/step/1 https://stepik.org/lesson/236905/step/1'
l = l.split()
@pytest.mark.parametrize('language', l)
def test_guest_should_see_login_link(browser, language):
    link = f"{language}"
    browser.get(link)




#link = 'https://stepik.org/lesson/237240/step/3?unit=209628'

#browser = webdriver.Chrome()
#browser.implicitly_wait(5)
#browser.get(link)

#list_link = browser.find_element(By.CSS_SELECTOR, 'div[class="html-content rich-text-viewer ember-view"] >span > p:nth-child(9)')
#l = list_link.text
#print(l)

