from selenium.webdriver.chrome.webdriver import WebDriver

driver = WebDriver()
driver.get("https://testautomationpractice.blogspot.com/")

# 1 Найти иконку Wikipedia по имени класса
wiki_icon = driver.find_element("class name", "wikipedia-icon")
print(wiki_icon)

# 2 Найти поле ввода Wikipedia по id
wiki_input = driver.find_element("id", "Wikipedia1_wikipedia-search-input")
print(wiki_input)

# 3 Найти кнопку поиска Wikipedia по css селектору (.имя класса)
wiki_btn = driver.find_element("css selector", "input.wikipedia-search-button")
print(wiki_btn)

# 4 Найти любой другой элемент на странице по тегу
input_phone = driver.find_element("id", "phone")
print(input_phone)