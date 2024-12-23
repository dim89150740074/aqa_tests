from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
# options.add_argument("--headless=new")
options.page_load_strategy = "eager"
driver = webdriver.Chrome(options=options)

product_links = [
    {"url":"https://eleanboutique.ru/plate-smoking-dlinnoe-barhatnoe.html", "size":42, "count_product":1},
]

counter = 0
url = "https://eleanboutique.ru/plate-smoking-dlinnoe-barhatnoe.html"
size = 44
count_product = 1

SIZE_LOCATOR = ("xpath", f"//span[text()='{size}']")
ADD_TO_CART_BTN_LOCATOR = ("xpath", "//a[text()='ДОБАВИТЬ В КОРЗИНУ']")
COUNT_PRODUCT_TO_CART_LOCATOR = ("xpath", "//div[@class='header-top']//div[contains(@class, 'cardIcon')]/span")
PRODUCT_NAME_LOCATOR = ("xpath", "//h1") # добавить
PRODUCT_PRICE_LOCATOR = ("xpath", "//div[@class='card__info-price']") # добавить (если товар со скидкой, то будут проблемы)
BTN_CART_LOCATOR = ("xpath", "//div[@class='header-top']//div[contains(@class, 'cardIcon')]")
# локатор в корзине - название
# локатор в корзине - размер
# локатор в корзине - количество
# локатор в корзине - цена


driver.get(url)
driver.find_element(*SIZE_LOCATOR).click()
driver.find_element(*ADD_TO_CART_BTN_LOCATOR).click()
driver.refresh()
count = driver.find_element(*COUNT_PRODUCT_TO_CART_LOCATOR).text.strip()
product_name = driver.find_element(*PRODUCT_NAME_LOCATOR).text.strip()
product_price = driver.find_element(*PRODUCT_PRICE_LOCATOR).text.replace("₽", "").replace(" ", "")
print(count, product_name, product_price)
driver.find_element(*BTN_CART_LOCATOR).click()
time.sleep(10)

# Проверяю, что в корзину добавился товар, который я добавил и в размере, который я выбрал
# Заходить в корзину и сверять там название, размер, цену и количество














