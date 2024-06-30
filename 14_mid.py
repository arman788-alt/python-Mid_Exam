class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list = []
    
        Star_Cinema.entry_hall(self)

    def entry_show(self, show_id, movie_name, time):

        show_info = (show_id, movie_name, time)
        self.__show_list.append(show_info)
        self.__seats[show_id] = [['Free' for _ in range(self.__cols)] for _ in range(self.__rows)]

    def book_seats(self, show_id, seats_to_book):

        if show_id not in self.__seats:
            print(f"This id {show_id} do not exist.")

        for row, col in seats_to_book:

            if row >= self.__rows or col >= self.__cols:
                print(f"Seat ({row}, {col}) is invalid.")
            if self.__seats[show_id][row][col] == 'Booked':

                print(f"Seat ({row}, {col}) is already booked.")
            self.__seats[show_id][row][col] = 'Booked'

    def view_show_list(self):

        for show in self.__show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):

        if show_id not in self.__seats:
            print(f"Show ID {show_id} do not exist.")
        
        seats = self.__seats[show_id]
        for row in range(self.__rows):
            for col in range(self.__cols):
                if seats[row][col] == 'Free':
                    print(f"Seat ({row}, {col}) is available")


# Example usage:
h1 = Hall(6, 8, '02')
h1.entry_show('c1', 'TOFAN', '03:00 AM')
h1.entry_show('c1', 'JAWAN', '12:00 AM')

print("Show list in h1:")
h1.view_show_list()

print("\nAvailable seats for show c1 in 02:")
h1.view_available_seats('c1')

print("\nBooking seats (1, 1), (2, 2) for show c1:")
h1.book_seats('c1', [(1, 1), (2, 2)])



