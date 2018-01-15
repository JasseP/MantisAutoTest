import os

"""
    Основные настройки
    ---------------------------------------------------------------------------------------------"""
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
# Расположение драйвера для использования Firefox
GECKODRIVER_PATH = CURRENT_PATH
# Расположение драйвера для использования Chrome
CHROMEDRIVER_PATH = os.path.join(CURRENT_PATH, "chromedriver.exe")

# Браузеры в которых осуществлять прогон
BROWSERS = [['chrome'], ['FireFox']]

# Данные используемые для авторизации пользователя, под которым будет происходить основной пул "внутренних проверок"
USER_LOGIN_DEFAULT = "administrator"
USER_PASS = "root"

# URL для доступа к тестируемому сайту
SITE_URL = r"http://localhost/mantis/"
# Страница со всеми созданными ошибками
ALL_BUG_PAGE = SITE_URL + 'view_all_bug_page.php'

"""
    Параметры для прогона. 
    !!!Требуется перенести в более подходящее место. Напрмер в БД!!!
    ---------------------------------------------------------------------------------------------"""
CATEGORY_LIST = ["[все проекты] Не General", "[все проекты] General"]
CATEGORY_DEFAULT = [CATEGORY_LIST[0]]

REPRODUCIBILITY_LIST = ["всегда", "иногда", "произвольно", "не проверялась", "не воспроизводится", "неприменимо"]
REPRODUCIBILITY_DEFAULT = [REPRODUCIBILITY_LIST[0]]

SEVERITY_LIST = ["нововведение", "пустяк", "тест/опечатка", "настройка",
                 "малое", "большое", "критическое", "блокирующее"]
SEVERITY_DEFAULT = [SEVERITY_LIST[0]]

SUMMARY_LIST = ["Ростелеком-Интеграция", "Ростелеком", "Интеграция"]
SUMMARY_DEFAULT = [SUMMARY_LIST[0]]

DESCRIPTION_LIST = ["Входит в группу компаний ПАО «Ростелеком»",
                    "Специализируется на проектировании и автоматизации процессов продаж и \
                     обслуживания телекоммуникационной компании в В2С, В2В, B2O сегментах.",
                    "Успешной работе компании способствует выбранная стратегия развития – курс \
                     на инновации, собственная экспертиза по всему спектру программных решений \
                     национального оператора связи."]
DESCRIPTION_DEFAULT = [DESCRIPTION_LIST[0]]

# Первый элемент 'Верный' или уже сужествующий.
USER_LOGIN_LIST = ["administrator", "Ant-on", "Антон", "Ant10"]

EMAIL_LIST = ["root@localhost", "123@", "asd.231"]
EMAIL_DEFAULT = [EMAIL_LIST[0]]

CAPTCHA_LIST = ["000000", "132000"]
CAPTCHA_DEFAULT = [CAPTCHA_LIST[0]]
