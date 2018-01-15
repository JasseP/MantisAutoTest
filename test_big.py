import pytest

import mantis_commands as mc
import settings


@pytest.yield_fixture(scope="function")
def go_to_create_and_del_bug(authorization):
    print("Переходим на страницу создания ошибки")
    mc.apply_page_create_bug(authorization)
    yield authorization
    print("Удалаем Cookie")
    authorization.delete_cookie('MANTIS_VIEW_ALL_COOKIE')
    print("Заходим на страницу редоктирования ошибки")
    mc.apply_bug(authorization)
    print("Удаляем ошибку")
    mc.apply_delete(authorization)
    print("Подтверждаем удаление")
    mc.apply_delete_confirm(authorization)
    print("Перезагрузка страницы")
    authorization.refresh()


@pytest.mark.parametrize("category", settings.CATEGORY_DEFAULT)
@pytest.mark.parametrize("reproducibility", settings.REPRODUCIBILITY_DEFAULT)
@pytest.mark.parametrize("summary", settings.SUMMARY_DEFAULT)
@pytest.mark.parametrize("description", settings.DESCRIPTION_DEFAULT)
def test_main(go_to_create_and_del_bug, category, reproducibility, summary, description):
    # FIXME Проведить проверку на совпадение текста не самый лучший подход.
    """
        Тест проверяющий полный цикл необходимый для создания ошибки.
        Авторизация -- Создание ошибки -- Проверка наличия -- Удаление

        Составляется декартово произведение передающихся параметров на вход.
        Каждое сочетание определяется, как отдельный тест.

        Если тест будет провален, система будет запускать новые, пока
        не пройдет все.
    """
    print("Устанавливаем категорию")
    mc.set_category(go_to_create_and_del_bug, category)
    print("Устанавливаем частоты повторов")
    mc.set_reproducibility(go_to_create_and_del_bug, reproducibility)
    print("Заполняем тему")
    mc.set_summary(go_to_create_and_del_bug, summary)
    print("Заполняем описание")
    mc.set_description(go_to_create_and_del_bug, description)
    print("Создаем ошибку")
    mc.create_bug(go_to_create_and_del_bug)
    print("Переходим на страницу со списком ошибок")
    mc.go_to_url(go_to_create_and_del_bug, settings.ALL_BUG_PAGE)
    print("Устанавливаем фильтр на свою ошибку")
    mc.set_filter_field_summary(go_to_create_and_del_bug, summary)
    print("Применяем фильтр")
    mc.apply_filtr_summary(go_to_create_and_del_bug)
    print("Получаем значение темы задачи")
    summary_text = mc.get_summary_bug_from_table(go_to_create_and_del_bug)
    assert summary_text == summary
    # FIXME --> Нужно перейти на страницу созданной ошибки и проверить введенные данные
