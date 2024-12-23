from selenium import webdriver

from selenium.webdriver.chrome.options import Options

# /Импорт
from selenium.webdriver import ActionChains # 1 вариант (предпочтительный, более простой вариант)
from selenium.webdriver.common.action_chains import ActionChains # 2 вариант

# как работает экшн | экшн.перемести.кликни.заверши

#
driver = webdriver.Chrome()
action = ActionChains(driver)
button = |(*BTN_LOCATOR)
action.click(button).perform() # perform() \команда на выполнеие экшена
action.double_click(button).perform()
action.context_click(button).perform() # context_click() клик правой кнопкой мыши

# работа с выпадающим меню
# http://demoqa.com/menu
#находим нужные нам элементы
action.move_to_element(nav_step_1).move_to_element(nav_step_2).click(nav_step_3).perform()

# работа с сочетаниями клавишь
# не всеч сочетания клавишь разрешены/, например запрещены/: открытие/закрытие новой вкладки
action.key_down(Keys.TAB).perform() # но клавиша остается зажатой/, чтобы ее отжать нужно
action.key_down(Keys.TAB).key_up(Keys.TAB).perform()

# DRAG AND DROP (простой, встречается чаще всего)
# https://demoqa.com/droppable
# есть 2 элемента в драг энд дроп это: сорс (ято перетгиваем) и таргет (куда)
# сохраняем элементы в переменные source, target
action.drag_and_drop(source, target).perform()

# явное управление перетаскиванием
action.click_and_hold(source).move_to_element(target).release().perform()

# DRAG AND DROP (сортировки)
# https://demoqa.com/sortable

def sorting(source_index, target_index):
    SOURCE_LOCATOR = ("xpath", f"//div[contains(@class, 'vertical-list-container')]/div[{source_index}]")
    TARGET_LOCATOR = ("xpath", f"//div[contains(@class, 'vertical-list-container')]/div[{target_index}]")
    source_elem = driver.find_element(*SOURCE_LOCATOR)
    target_elem = driver.find_element(*TARGET_LOCATOR)
    action.drag_and_drop(source_elem, target_elem).perform()





