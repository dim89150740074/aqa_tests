from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=1)
driver.get("https://demoqa.com/radio-button")
A_LOCATOR = ("xpath", "//div[@id='content']//a")

# открыть новую вкладку
driver.switch_to.new_window('tab')
driver.get('https://the-internet.herokuapp.com/')
driver.find_element(*A_LOCATOR).click()

# открыть новое окно
driver.switch_to.new_window('window')
driver.get('https://the-internet.herokuapp.com/')
driver.find_element(*A_LOCATOR).click()

# ссылка которая открывается в новой вкладке (нюансы)
driver.get('https://the-internet.herokuapp.com/windows')
# если мы кликнем по ссылке, и потом попробуем найти элемент в новой вкладке, (ищем по текту)то мы элемент не сможем найти
# а если сразу перейдем по нужной нам ссылке, то элемент будет айден
driver.get('https://the-internet.herokuapp.com/windows/new')
# чтобы не возникало таких ошибок, нам нужно явно указывать какую вкладку/окно открыть

# дескриптор это айдишник окна или вкладки
# получить дескриптор
current_window_id = driver.current_window_handle
# в селениум нет назницы между табами и окнами (id-шники выглядят одинаковл) т.е. если у меня открыто 3 окна и в каждом по 2 вкладки, селениум будет видеть это как 6 вкладок
# если открылась вкладка по клику на ссылку, то мы не сможем получить ее id, так как контекст не был переключен, дл\ этого нам нужно получить список всех id
all_tabs = driver.window_handles
# и если мы хотим обратиться к последнему открытому табу, нам нужно сделать так
driver.switch_to.window(all_tabs[-1])

# проверяем что новая вкладка открылась
wait.until(EC.number_of_windows_to_be(len(all_tabs + 1)))
for window_handle in driver.window_handles:
    if window_handle != original_tab:
        driver.switch_to.window(window_handle)
        break


# или такой вариант
wait.until(EC.new_window_is_opened()) # не работает!

# Закрытие определенных вкладок
driver.close()
# если нам нужно закрыть определенную вкладку, то вначале мы ее открываем (переключаевмся на нее) а потом уже закрываем

# если вкладка закрылась, на что будет переключен контекст селениума? он останется на закрытой вкладке, поэтому после закрытия нам нужно переключить контекст на другую вкладку

# чтобы закрыть все вкладке нужно
driver.quit()

# при работе с табами для лучшей читабельности нам нужносохранять id каждого таба после открытия, это сделает код более читабельным и с ним легчяе будет работать
time.sleep(3)

# IFRAMES
# https://testautomationpractice.blogspot.com/
# если у нас код, которым мы хотим работать, находится в iframe, то нам нужно прежде чем мы начтем с ним взаимодействовать, перключиться на него
# он может отображаться как iframe или как frame

# вначалек мы находим на странице элемент frame или же iframe а уже потом переключаться
widget_iframe = driver.find_element(*IFRAME_LOCATOR)
driver.switch_to.frame(widget_iframe)
# и после этого мы уже можем взаимодействовать с полями внутри айфрейма: получчать элементы, кликать, вводить данные и пр
# еще можно овводить код айфрейма
driver.switch_to.frame("frame-012312i")
# или можно переключаться по индексу
driver.switch_to.frame(0)

# помимо одного айфрейма на странице может быть несклько айфреймов, а еще может быть такое, что внутри одного iframe могут быть вложены другие iframe
# перключение с айфрейма обратно к странице
driver.switch_to.default_content()

# https://the-internet.herokuapp.com/nested_frames
# вначале мы  находим родительский фрейм, потом мы находим вложенные в него фреймы. /Чтобы удобно переключаться между фреймами, нужно сохранять их в переменную
widget_iframe = driver.find_element(*IFRAME_LOCATOR)
driver.switch_to.frame(widget_iframe)

# если много фреймов, то можно создать словарь и через него переключаться между ними



