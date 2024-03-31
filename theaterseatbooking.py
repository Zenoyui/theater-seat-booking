import json
from colorama import Fore, Style
import threading
import time
import os

class Theater:
    def init(self, rows, seats_per_row):
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seats = [[str(i + 1 + j * seats_per_row) for i in range(seats_per_row)] for j in range(rows)]  # Номера мест
        self.bookings = {}
        self.filename = 'theater_state.json'
        self.load_bookings_from_file()

    def display_seating_chart(self):
        for i, row in enumerate(self.seats, start=1):
            for seat in row:
                if seat in self.bookings:
                    print(Fore.RED + f'{seat:>3}', end='')
                else:
                    print(Fore.GREEN + f'{seat:>3}', end='')
            print(Style.RESET_ALL)

    def book_seat(self):
        seat = int(input("Введите номер места: ")) - 1
        row = seat // self.seats_per_row

        if seat < 0 or seat >= self.rows * self.seats_per_row:
            print("Неправильно указан номер места.")
            return False

        if self.seats[row][seat % self.seats_per_row] not in self.bookings:
            self.bookings[self.seats[row][seat % self.seats_per_row]] = 'booked'
            print(f"Место {row + 1}/{seat % self.seats_per_row + 1} успешно забронировано.")
            self.display_seating_chart()  # Отображение зала после бронирования
            return True
        else:
            print("Извините, место уже занято.")
            return False

    def cancel_booking(self, seat):
        if seat in self.bookings:
            del self.bookings[seat]
            print("Бронирование успешно отменено.")
        else:
            print("Бронирование не найдено.")

    def display_bookings(self):
        print("Список забронированных мест:")
        for seat in self.bookings.keys():
            row = (int(seat) - 1) // self.seats_per_row
            print(f"Ряд {row + 1}, Место {seat}")

    def save_bookings_to_file(self):
        data = {
            'bookings': self.bookings,
            'seats': self.seats
        }
        with open(self.filename, 'w') as f:
            json.dump(data, f)

    def load_bookings_from_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.bookings = data['bookings']
                self.seats = data['seats']

    def auto_save(self):
        while True:
            self.save_bookings_to_file()
            time.sleep(1)

# Пример использования:

theater = Theater(rows=5, seats_per_row=10)
auto_save_thread = threading.Thread(target=theater.auto_save)
auto_save_thread.daemon = True
auto_save_thread.start()

while True:
    print("\nВыберите действие:")
    print("1. Забронировать место")
    print("2. Посмотреть забронированные места")
    print("3. Отменить бронирование")
    print("4. Показать зал")
    print("5. Выйти")

    choice = input("Введите номер действия: ")

    if choice == '1':
        theater.book_seat()
    elif choice == '2':
        theater.display_bookings()
    elif choice == '3':
        seat = input("Введите номер места, которое хотите отменить: ")
        theater.cancel_booking(seat)
    elif choice == '4':
        theater.display_seating_chart()
    elif choice == '5':
        break
    else:
        print("Неправильный ввод. Попробуйте снова.")
