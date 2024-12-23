
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://hyperskill.org/courses")


# Задание 2
LOGO = ('xpath', "//ul[@class='navbar-nav']/li/a")  # логотип ссылка
NAV_BTN_EXPLORE = ('xpath', "//div[@id='nav-collapse']//ul//li[@click-event-target='explore']/a")  # меню explore
NAV_BTN_PRICING = ('xpath', "//div[@id='nav-collapse']//ul//li[@click-event-target='pricing']/a")  # меню pricing
NAV_BTN_FOR_BUSINESS = ('xpath', "//div[@id='nav-collapse']//ul//li[@click-event-target='join_as_organization']/a")  # меню for busines
BTN_SIGN_IN = ('xpath', "//nav[@data-component-name='BNavbar']//button[contains(span, 'Sign in')]")  # кнопка sign in
BTN_START_FOR_FREE = ('xpath', "//nav[@data-component-name='BNavbar']//button[contains(span, 'Start for free')]")  # кнопка start for free
HEADER_H1 = ('xpath', "//h1")  # заголовок h1
PROJECTS_PYTHON = ('xpath', "//section[1]/div[3]/div")  # список курсов python (костыли)
PROJECT_PYTHON = ('xpath', "//section[1]/div[3]/div[1]")  # список курсов python (костыли)
PROJECT_PYTHON_TITLE = ('xpath', "//section[1]/div[3]/div[1]/div/div/div/div[1]")  # заголовок первого курса (костыли)
PROJECT_PYTHON_RATING = ('xpath', "//section[1]/div[3]/div[1]/div/div/div/div[2]/span/span")  # рейтинг первого курса
PROJECT_PYTHON_TEXT = ('xpath', "//section[1]/div[3]/div[1]/div/div/div/div[3]//p")  # описание первого курса
PROJECT_PYTHON_IMG = ('xpath', "//section[1]/div[3]/div[1]//img")  # изображение первого курса
PROJECT_PYTHON_LVL = ('xpath', "//section[1]/div[3]/div[1]/div/div/div/div[2]/span[3]/span[2]")  # уровень первого курса
PROJECT_PYTHON_LINK = ('xpath', "//section[1]/div[3]/div[1]//a")  # ссылку на первый курс
# LOGO = ('xpath', "")  # кнопка load more
# LOGO = ('xpath', "")  # футер all courses
# LOGO = ('xpath', "")  # футер top courses
# LOGO = ('xpath', "")  # футер python
# LOGO = ('xpath', "")  # футер java
# LOGO = ('xpath', "")  # футер JavaScript
# LOGO = ('xpath', "")  # футер Kotlin
# LOGO = ('xpath', "")  # футер Go
# LOGO = ('xpath', "")  # футер Android
# LOGO = ('xpath', "")  # футер full catalog
# LOGO = ('xpath', "")  # футер blog
# LOGO = ('xpath', "")  # футер university
# LOGO = ('xpath', "")  # футер about
# LOGO = ('xpath', "")  # футер careers
# LOGO = ('xpath', "")  # футер help center
# LOGO = ('xpath', "")  # футер terms

driver.find_element(*LOGO)
driver.find_element(*NAV_BTN_EXPLORE)
driver.find_element(*NAV_BTN_PRICING)
driver.find_element(*NAV_BTN_FOR_BUSINESS)
driver.find_element(*BTN_SIGN_IN)
driver.find_element(*BTN_START_FOR_FREE)
driver.find_element(*HEADER_H1)
driver.find_elements(*PROJECTS_PYTHON)
driver.find_element(*PROJECT_PYTHON_TITLE)
driver.find_element(*PROJECT_PYTHON_RATING)
driver.find_element(*PROJECT_PYTHON_TEXT)
driver.find_element(*PROJECT_PYTHON_LVL)
res = driver.find_element(*PROJECT_PYTHON_LINK)
res.click()










