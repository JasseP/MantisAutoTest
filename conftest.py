import pytest

import mantis_commands as mc
import settings


@pytest.yield_fixture(scope="module", params=settings.BROWSERS)
def driver_up(request):
    """
        Фикстура открывает браузер

    """
    print("Запускаем браузер")
    driver = mc.driver_connection(request.param[0])
    yield driver
    print("Закрываем процесс")
    driver.quit()


@pytest.fixture(scope="module")
def authorization(driver_up):
    """
        Переход на страницу авторизации и последующий вход
        пользователя заданного по умолчанию в файле settings.py

    """
    print("Переходим на странице авторизации")
    mc.go_to_url(driver_up)
    print("Вводим логин")
    mc.set_login(driver_up)
    mc.apply_login_input(driver_up)
    print("Вводим пароль")
    mc.apply_password_input(driver_up)
    return driver_up
