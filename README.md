# MantisAutoTes

Результат работы: https://youtu.be/Q2cxZWIFYvA

Для корректной работы тестов авторизации, помимо инструкций указанных в тестах нужно
изменить файл Mantis:
mantis\vendor\dapphp\securimage\securimage_show.php
Требуется добавить команду: $img->charset = '0';

Настройка производится через файл settings.py

