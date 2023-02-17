Файлы
----------------
[conftest.py](conftest.py) содержит код настройки браузера перед запуском тестов

[constants.py](constants.py) содержит константы для тестов (перед запуском тестов в данном файле необходмо ввести валидные данные, после уточнения критериев ввода в поля необходимо дополнить словари)

[locators.py](locators.py) содержит локаторы

[tests](tests) папка с тестами

[pages](pages) папка с классами для веб-страниц


Как запусить тесты
----------------

1) Установить библиотеки:

    ```bash
    pip3 install -r requirements.txt
    ```

2) Скачать Selenium WebDriver https://chromedriver.chromium.org/downloads (выберите нужную вам версию драйвера)

3) Запуск тестов:

    ```bash
    python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
    ```
