**ЯндексПрактикум. Курс "Автоматизатор тестирования на Python".** 
---
**Спринт 7 "Тестирование API"**
***
В проекте спроектированы тесты для API сервиса [Яндекс.Самокат](https://qa-scooter.praktikum-services.ru/).
Прикреплен отчет о результатах прохождения тестов.

### Тестируемые эндпоинты:

* `POST /api/v1/courier` - создание курьера
* `POST /api/v1/orders` - создание заказа
* `POST /api/v1/courier/login` - авторизация курьера
* `GET /api/v1/orders` - получение списка заказов


***
### Структура проекта

Пакет `tests`: модули с тестами
* test_create_courier.py
* test_create_order.py
* test_list_orders.py
* test_login_courier.py

Модуль `conftest.py` с фикстурами:

* payload_create_courier - наполнение словаря тестовыми данными для создания курьера
* create_new_courier - создание нового курьера

Модуль `data.py`:
* тестовые данные для классов Courier, Login, Order

Модуль `url.py`:
* URL сервиса

Модуль `endpoints.py`:
* эндпоинты

Модуль `helpers.py`:
* генераторы данных

Модуль `source.py`:
* вспомогательные функции
***
Отчёты в формате JSON хранятся в директории `allure_results`

Зависимости в файле requirements.txt
***
### Для запуска тестов
* Установить pytest
```
pip install pytest
```
* Запуск всех тестов с сохранением отчета
```
pytest -vs --alluredir=allure_results
```
* Сгенерировать отчет о тестировании в формате веб-страницы
```
allure serve allure_results
```

