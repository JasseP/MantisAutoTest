import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.remote_connection import LOGGER

import logging

import settings


def get_element_when_loaded(browser, text, search_by=By.ID, timeout=5):
    """
        Проверяет нахождение элемента на странице перед взаимодействием с ним.

            :param search_by: тип поиска (точно работает поиск по id и xpath)
            :param browser: текущий процесс
            :param text: ключ по которому нужно произвести поиск
            :param timeout: время ожидания

            :return: Элемент или если в течении 5 секунд не появился на
                        странице возвращает ошибку TimeoutException
    """
    try:
        element = WebDriverWait(browser, timeout)
        element = element.until(ec.presence_of_element_located((search_by, text)))
    except TimeoutException:
        print("Элемент {} не найден".format(text))
        assert False
    return element


def driver_connection(browser_name):
    """
        Выбор драйвера
        !!!Поддерживается только Chrome и FireFox!!!
            :param browser_name: Название браузера (Chrome, FireFox)
            :return: Драйвер
    """
    if browser_name.lower() == 'firefox':
        browser = webdriver.Firefox(settings.GECKODRIVER_PATH)
    elif browser_name.lower() == 'chrome':
        browser = webdriver.Chrome(settings.CHROMEDRIVER_PATH)
    else:
        raise ValueError(f"Браузер {browser_name} не поддерживается")
    LOGGER.setLevel(logging.FATAL)
    return browser


def go_to_url(browser, site_url=settings.SITE_URL):
    """
        Переход по заданному URL. По умолчанию использует URL сайта
        указанный в файле Settings.py

            :param browser: текущий процесс
            :param site_url: URL для перехода
    """
    browser.get(site_url)


def set_login(browser, user_login=settings.USER_LOGIN_DEFAULT):
    """
        Ввод логина пользователя. По умолчанию использует логин
        указанный в файле Settings.py

            :param browser: текущий процесс
            :param user_login: Существующий логин
    """
    login = get_element_when_loaded(browser, "username")
    login.send_keys(user_login)


def apply_login_input(browser):
    """
        Нажает на кнопку подтверждающую ввод логина

            :param browser: текущий процесс

    """
    btn_xpath = "//form[@id='login-form']/fieldset/input[2]"
    btn_accept = get_element_when_loaded(browser, btn_xpath, search_by=By.XPATH)
    btn_accept.click()


def apply_password_input(browser, user_pass=settings.USER_PASS):
    """
        Ввод логина пользователя. По умолчанию использует пароль
        указанный в файле Settings.py

            :param browser: текущий процесс
            :param user_pass: Существующий пароль

    """
    password = get_element_when_loaded(browser, "password")
    btn_xpath = "//form[@id='login-form']/fieldset/input[3]"
    btn_accept = get_element_when_loaded(browser, btn_xpath, search_by=By.XPATH)
    password.send_keys(user_pass)
    btn_accept.click()


def apply_page_create_bug(browser):
    """
        Переход на страницу создания Ошибки. Работает только после авторизации

            :param browser: текущий процесс

    """
    xpath = "//div[@class='btn-group btn-corner padding-right-8 padding-left-8']/a[@href='bug_report_page.php']"
    add_new_bug = get_element_when_loaded(browser, xpath, search_by=By.XPATH)
    add_new_bug.click()


def set_category(browser, user_category=settings.CATEGORY_DEFAULT[0]):
    """
        Выбор категории ошибки. По умолчанию использует значение переменной
        CATEGORY_DEFAULT в файле Settings.py.

            :param browser: текущий процесс
            :param user_category: Пользовательское значение (список доступных можно узнать в
            файле Settings.py --> CATEGORY_LIST

    """
    category = get_element_when_loaded(browser, "category_id")
    select = Select(category)
    select.select_by_visible_text(user_category)


def set_reproducibility(browser, text=settings.REPRODUCIBILITY_DEFAULT[0]):
    """
        Выбор "воспроизводимости" ошибки. По умолчанию использует значение переменной
        REPRODUCIBILITY_DEFAULT в файле Settings.py.

            :param browser: текущий процесс
            :param text: Пользовательское значение(список доступных можно узнать в
            файле Settings.py --> REPRODUCIBILITY_LIST
    """
    reproducibility = get_element_when_loaded(browser, "reproducibility")
    select = Select(reproducibility)
    select.select_by_visible_text(text)


def set_summary(browser, text=settings.SUMMARY_DEFAULT[0]):
    """
        Заполнение "Темы" ошибки. По умолчанию использует значение переменной
        SUMMARY_DEFAULT в файле Settings.py.

            :param browser: текущий процесс
            :param text: Пользовательское значение(список доступных можно узнать в
            файле Settings.py --> SUMMARY_LIST
    """
    summary = get_element_when_loaded(browser, "summary")
    summary.send_keys(text)


def set_description(browser, text=settings.DESCRIPTION_DEFAULT[0]):
    """
        Заполнение "Описания" ошибки. По умолчанию использует значение переменной
        DESCRIPTION_DEFAULT в файле Settings.py.

            :param browser: текущий процесс
            :param text: Пользовательское значение(список доступных можно узнать в
            файле Settings.py --> DESCRIPTION_LIST
    """
    description = get_element_when_loaded(browser, "description")
    description.send_keys(text)


def create_bug(browser):
    """
        Нажать на кнопку "Создать задачу".
        Отработает только после заполнения "Категории", "Темы", "Описания"

            :param browser: текущий процесс
    """
    xpath = "//input[@value='Создать задачу']"
    btn_add_bug = get_element_when_loaded(browser, xpath, search_by=By.XPATH)
    btn_add_bug.click()
    time.sleep(3)


def set_filter_field_summary(browser, text=settings.SUMMARY_DEFAULT[0]):
    """
        Заполнение поля "Поиск" для фильтрации ошибок. По умолчанию использует значение переменной
        SUMMARY_DEFAULT в файле Settings.py.

            :param browser: текущий процесс
            :param text: Указывается тема задачи. Пользовательское значение(список доступных можно узнать в
            файле Settings.py --> SUMMARY_LIST
    """
    tb_filter = get_element_when_loaded(browser, "filter-search-txt")
    tb_filter.send_keys(text)


def apply_filtr_summary(browser):
    """
        Применить фильтр на странице поиска задач.

            :param browser: текущий процесс
    """
    xpath = "//input[@value='Фильтровать']"
    apply_filter = get_element_when_loaded(browser, xpath, search_by=By.XPATH)
    apply_filter.click()


def get_summary_bug_from_table(browser):
    """
        Получить Тему созданной задачи для последующего сравнения ее с создаваемой темой.

            :param browser: текущий процесс
            :return: Тема задачи
    """

    xpath = "//table[@id='buglist']/tbody/tr/td[@class='column-summary']"
    table_summary = get_element_when_loaded(browser, xpath, search_by=By.XPATH)
    return table_summary.text


def apply_bug(browser):
    """
        Переход на страницу задачи для ее удаления.
            :param browser: текущий процесс

    """
    xpath = "//table[@id='buglist']/tbody/tr/td[@class='column-id']"
    bug = get_element_when_loaded(browser, xpath, search_by=By.XPATH)
    bug.click()

# FIXME Достаточно много практически одинаковых функций. Нужно объединить.


def apply_delete(browser):
    """
        Нажать на кнопку "Удалить". Работает только на странице просмотра ошибки.

            :param browser: текущий процесс

    """
    xpath = "//input[@value='Удалить']"
    apply_del = get_element_when_loaded(browser, xpath, search_by=By.XPATH)
    apply_del.click()


def apply_delete_confirm(browser):
    """
        Нажать на кнопку "Удалить задачу".
        Работает только на странице подтверждения удаления ошибки

            :param browser: текущий процесс

    """
    xpath = "//input[@value='Удалить задачи']"
    apply_del = get_element_when_loaded(browser, xpath, search_by=By.XPATH)
    apply_del.click()


def go_to_signup_page(browser):
    """
        Нажать на кнопку "зарегестрировать учетную запись".
        Работает только на странице авторизации.

    :param browser: текущий процесс
    """
    xpath = "//div[@class='toolbar center']/a[@href='signup_page.php']"
    apply_signup = get_element_when_loaded(browser, xpath, search_by=By.XPATH)
    apply_signup.click()


def set_email(browser, text=settings.EMAIL_DEFAULT):
    """
        Заполнение поля "Электронная почта".
        По умолчанию использует значение переменной SUMMARY_DEFAULT в файле Settings.py.

            :param browser: текущий процесс
            :param text: Указывается email для регистрации. Пользовательское значение(список
                        доступных можно узнать в файле Settings.py --> EMAIL_LIST)
    """
    email = get_element_when_loaded(browser, "email-field")
    email.send_keys(text)


def set_captcha(browser, text=settings.CAPTCHA_DEFAULT):
    """
        Заполнение поля "Электронная почта".
        По умолчанию использует значение переменной SUMMARY_DEFAULT в файле Settings.py.

            :param browser: текущий процесс
            :param text: Указывается email для регистрации. Пользовательское значение(список
                        доступных можно узнать в файле Settings.py --> EMAIL_LIST)
    """
    captcha = get_element_when_loaded(browser, "captcha-field")
    captcha.send_keys(text)


def apply_signup(browser):
    """
        Нажать на кнопку "зарегестрировать учетную запись".
        Работает только на странице авторизации.

    :param browser: текущий процесс
    """
    xpath = "//input[@value='Зарегистрироваться']"
    apply_signup = get_element_when_loaded(browser, xpath, search_by=By.XPATH)
    apply_signup.click()


def get_signup_error(browser):
    """
        Получить номер ошибки при регистрации.
        APPLICATION ERROR #800 - Это регистрационное имя пользователя уже задействовано
        APPLICATION ERROR #813 - Этот адрес электронной почты уже используется
        APPLICATION ERROR #805 - Недопустимое регистрационное имя пользователя
        APPLICATION ERROR #1904 - Ошибка ввода каптчи


    :param browser: текущий процесс
    """
    xpath = "//div[@class='alert alert-danger']/p[@class='bold']"
    error = get_element_when_loaded(browser, xpath, search_by=By.XPATH)
    return error.text
