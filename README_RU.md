## Пример организации автотестирования для cервиса бронирования Ostrovok.ru
> Ostrovok.ru — российский сервис онлайн-бронирования отелей.

<img src="resources/Ostrovok_logo.png" alt="Ostrovok_logo" border="0" />

## Реализованы тесты:
* UI
  * ✅ Результатов поиска
  * ✅ Логина с помощью e-mail
  * ✅ Изменения языка
  * ✅ Локализации заголовка
  * ✅ Поиска и изменения валюты
  * ✅ Поиска неизвестной валюты
    
* API
  * ✅ Получения списка популярных направлений
  * ✅ Получения ограничений в связи с COVID-19 \
  С  параметрами:
    > country_code: ['us', 'ru'] \
    > lang: ['en', 'ru']
  * ✅ Списка возвращаемых праздников
  * ✅ Истории поиска
  * ✅ Проверка результатов поиска \
    С  параметрами:
    > query: ['Moscow, Russia', 'Istanbul, Turkiye'] \
    > locale: ['en', 'ru']

* Android
  * ✅ Результат поиска отелей для популярного города
  * ✅ Логина пользователя с помощью e-mail
  * ✅ Отображения телефонов поддержки


## Технологический стек
Python, Pytest, Selene, PyCharm, Requests, Appium, Jenkins, Selenoid, Github, Telegram

<p  align="center">
  <img src="resources/python.png" width="40" height="40"  alt="Python"/>
  <img src="resources/pytest.png" width="40" height="40"  alt="Pytest"/>
  <img src="resources/selene.png" width="50" height="40"  alt="Selene"/>
  <img src="resources/pysharm.png" width="40" height="40"  alt="PyCharm"/>
  <img src="resources/request.png" width="50" height="40"  alt="Requests"/>
  <img src="resources/appium.png" width="40" height="40"  alt="Appium"/>
  <img src="resources/Jenkins.jpg" width="40" height="40"  alt="Jenkins"/>
  <img src="resources/selenoid.png" width="40" height="40"  alt="Selenoid"/>
  <img src="resources/telegram-logo.png" width="40" height="40"  alt="Telegram"/>
</p>

## Как запустить
Перед выполением необходимо:
* В .env определить параметры конфигурации:
    - login, password for selenoid в .env  
    SELENOID_LOGIN=user  
    SELENOID_PASSWORD=password
    - credentials пользователя ostrovok.ru в .env  
    TEST_USER_EMAIL=some_mail@gmail.com  
    TEST_USER_PASSWORD=password
    - в config.personal.env добавить browserstack userName и accessKey
    browserstack.userName='userName'
    browserstack.accessKey='accessKey'

### Локально
```bash
pip install poetry
poetry install
source .venv/bin/activate
env context=$CONTEXT pytest $TESTS_FOLDER
```

### Переменные для запуска
* TESTS_FOLDER - папка с тестами\
tests/API\
tests/Mobile\
tests/UI\
Default value: . (run all tests)

* CONTEXT - контекст для запуска мобильного приложения\
local - run via Appium on localhost\
personal - run via BrowserStack\
Default value: personal

### Удаленно
```bash
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install
env context=$CONTEXT pytest $TESTS_FOLDER
```

### Видео о прохождении тестов
* UI browser tests  
<img src="resources/test_run.gif" alt="video test" border="0" />

* Mobile  
<img src="resources/mobile.gif" alt="video test" border="0" />

### Запуск в Jenkins
Статистика по запускам <br >
<img src="resources/allure_stats.png" alt="Статистика по запускам" border="0">

### Параметры запуска <br >
<img src="resources/jenkins_params.png" alt="Jenkins" border="0">

### Отчёт о прохождении автотестов в Allure Report
<img src="resources/allure_report.png" alt="Allure-Report" border="0">

### Уведомления о прохождении автотестов в Telegram
<img src="resources/telegram_notification.png" alt="telegram-bot" border="0">