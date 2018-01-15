import pytest

import mantis_commands as mc
import settings


@pytest.yield_fixture(scope="function")
def go_to_signup_and_return(driver_up):
    print("Переходим на страницу авторизации")
    mc.go_to_url(driver_up)
    print("Вводим логин")
    mc.go_to_signup_page(driver_up)
    yield driver_up
    print("Возвращаемся на страницу авторизации")
    mc.go_to_url(driver_up)
    print("Возвращаемся на страницу регистрации")
    mc.go_to_signup_page(driver_up)


@pytest.mark.parametrize("user", [settings.USER_LOGIN_DEFAULT])
@pytest.mark.parametrize("email", settings.EMAIL_LIST[1:])
@pytest.mark.parametrize("captcha", settings.CAPTCHA_DEFAULT)
def test_user_already_registered(go_to_signup_and_return, user, email, captcha):
    """
        Тест проверяет условие: если пользователь уже зарегестрирован, выводить
            ошибку APPLICATION ERROR  # 800
        Остальные поля заполненны верно.

        Для успешного прохождения нужно создать пользователя с логином
        "administrator" или подставить логин любого другого, уже созданного
        пользователя.

        По хорошему, пользователя нужно создать автоматически...
        Но я не успел победить API gmail.
        И не успел подключить БД для получения логина автоматически.

    """
    mc.set_login(go_to_signup_and_return, user)
    mc.set_email(go_to_signup_and_return, email)
    mc.set_captcha(go_to_signup_and_return, captcha)
    mc.apply_signup(go_to_signup_and_return)
    error = mc.get_signup_error(go_to_signup_and_return)
    assert error == 'APPLICATION ERROR #800'


@pytest.mark.parametrize("user", settings.USER_LOGIN_LIST[1:])
@pytest.mark.parametrize("email", settings.EMAIL_DEFAULT)
@pytest.mark.parametrize("captcha", settings.CAPTCHA_DEFAULT)
def test_email_already_registered(go_to_signup_and_return, user, email, captcha):
    """
        Тест проверяет условие: если email уже зарегестрирован, выводить
            ошибку APPLICATION ERROR  # 813
        Остальные поля заполненны верно.

        Для успешного прохождения нужно создать пользователя с логином
        "administrator" или подставить логин любого другого, уже созданного
        пользователя.

    """
    mc.set_login(go_to_signup_and_return, user)
    mc.set_email(go_to_signup_and_return, email)
    mc.set_captcha(go_to_signup_and_return, captcha)
    mc.apply_signup(go_to_signup_and_return)
    error = mc.get_signup_error(go_to_signup_and_return)
    assert error == 'APPLICATION ERROR #813'


@pytest.mark.parametrize("user", [settings.USER_LOGIN_LIST[2]])
@pytest.mark.parametrize("email", settings.EMAIL_LIST[1:])
@pytest.mark.parametrize("captcha", settings.CAPTCHA_DEFAULT)
def test_invalid_user_name(go_to_signup_and_return, user, email, captcha):
    """
        Тест проверяет условие: если в имени пользователя указать недопустимый символ,
            то должна отобразится ошибка APPLICATION ERROR  # 805
        Остальные поля заполненны верно.

    """
    mc.set_login(go_to_signup_and_return, user)
    mc.set_email(go_to_signup_and_return, email)
    mc.set_captcha(go_to_signup_and_return, captcha)
    mc.apply_signup(go_to_signup_and_return)
    error = mc.get_signup_error(go_to_signup_and_return)
    assert error == 'APPLICATION ERROR #805'


@pytest.mark.parametrize("user", [settings.USER_LOGIN_DEFAULT])
@pytest.mark.parametrize("email", settings.EMAIL_DEFAULT)
@pytest.mark.parametrize("captcha", settings.CAPTCHA_LIST[1:])
def test_input_error_for_captcha(go_to_signup_and_return, user, email, captcha):
    """
        Тест проверяет условие: если при вводе каптчи была допущена,
            то должна отобразится ошибка APPLICATION ERROR  # 1904
        Остальные поля заполненны верно.

    """
    mc.set_login(go_to_signup_and_return, user)
    mc.set_email(go_to_signup_and_return, email)
    mc.set_captcha(go_to_signup_and_return, captcha)
    mc.apply_signup(go_to_signup_and_return)
    error = mc.get_signup_error(go_to_signup_and_return)
    assert error == 'APPLICATION ERROR #1904'
