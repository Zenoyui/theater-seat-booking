# Система бронирования мест в театре

Это приложение — консольная система бронирования мест, предназначенная для использования в театрах. Приложение позволяет пользователям бронировать места, просматривать доступные или забронированные места и отменять бронирование.

## Особенности

- **Бронирование мест**: Пользователи могут забронировать место, выбрав его номер.
- **Отображение зала**: Визуальное представление зала с обозначением забронированных и доступных для бронирования мест.
- **Просмотр бронирований**: Выводит список всех забронированных мест.
- **Отмена бронирования**: Предоставляет возможность отменить бронирование.
- **Файл состояния**: При выполнении программы создается файл theater_state.json, в котором содержатся данные о всех забронированных и доступных местах.
- **Цветовая дифференциация**: Использует библиотеку colorama для отображения забронированных мест красным цветом и свободных - зеленым.

## Установка

Перед запуском приложения, необходимо установить библиотеку colorama. Это можно сделать с помощью пакетного менеджера pip, введя следующую команду в командной строке:


pip install colorama

Убедитесь, что у вас установлен pip. Если нет, вы можете установить его, следуя официальной документации Python.

## Интерфейс приложения


Выберите действие:
1. Забронировать место
2. Посмотреть забронированные места
3. Отменить бронирование
4. Показать зал
5. Выйти
Введите номер действия: 4

  1  2  3  4  5  6  7  8  9 10
 11 12 13 14 15 16 17 18 19 20
 21 22 23 24 25 26 27 28 29 30
 31 32 33 34 35 36 37 38 39 40
 41 42 43 44 45 46 47 48 49 50

Выберите действие:
1. Забронировать место
2. Посмотреть забронированные места
3. Отменить бронирование
4. Показать зал
5. Выйти
Введите номер действия:

## Запуск приложения

Чтобы запустить систему бронирования, откройте командную строку или терминал и выполните следующую команду:

python theaterseatbooking.py

Следуйте инструкциям на экране для управления бронированием мест.

## Лицензионное соглашение

Это программное обеспечение распространяется под [MIT License](LICENSE).
