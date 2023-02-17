


Как запусить тесты
----------------

1) Установить библиотеки:

    ```bash
    pip3 install -r requirements.txt
    ```

2) Скачать Selenium WebDriver https://chromedriver.chromium.org/downloads (выберите нужную вам версию драйвера)

3) зупуск тестов:

    ```bash
    python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
    ```
