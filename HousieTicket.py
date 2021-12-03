'''
    Represents a housie game ticket.
    This ticket has 3 rows and 9 columns
    Each row contains 5 numbers and 4 empty cells
    So ticket has total 15 (3 X 5) unique numbers and 12 (3 X 4) empty cells
    All 15 numbers are unique, no number is repeated
'''
import random

from TicketCell import EmptyCell, TicketCell

class HousieTicket:
    no_of_rows = 3
    no_of_columns = 9
    empty_cells_in_row = 4
    numbers_in_one_ticket = 15
    numbers_in_one_row = 5

    def __init__(self, id, unique_numbers) -> None:
        if len(unique_numbers) != HousieTicket.numbers_in_one_ticket:
            raise Exception('There should be exact 15 numbers')

        self.__ensure_numbers_are_unique(unique_numbers)
        self.id = id
        self.rows = []
        for _ in range(HousieTicket.no_of_rows):
            row = self.__generate_row(unique_numbers[:HousieTicket.numbers_in_one_row])
            self.rows.append(row)
            unique_numbers = unique_numbers[HousieTicket.numbers_in_one_row:]
        self.ticket_surrendered = False

    def __generate_row(self, numbers):
        if len(numbers) != HousieTicket.numbers_in_one_row:
            raise Exception(f'There should be exact {HousieTicket.numbers_in_one_row} numbers in a row')

        row = []
        empty_cell_indexes = random.sample(range(HousieTicket.no_of_columns), HousieTicket.empty_cells_in_row)
        for i in range(HousieTicket.no_of_columns):
            row.append(EmptyCell() if i in empty_cell_indexes else TicketCell(numbers.pop()))
        return row

    def __ensure_numbers_are_unique(self, numbers) -> None:
        if len(numbers) != len(set(numbers)):
            raise Exception('Numbers should be unique')

    def get_full_row_ids(self):
        full_rows = []
        for i in range(HousieTicket.no_of_rows):
            if all(x.number == None or x.is_marked for x in self.rows[i]):
                full_rows.append(i)
        return full_rows

    def is_full_housie(self):
        return len(self.get_full_row_ids()) == 3

    def mark_number_if_present(self, number):
        if self.ticket_surrendered:
            return
            
        for i in range(HousieTicket.no_of_rows):
            for j in range(HousieTicket.no_of_columns):
                if self.rows[i][j].number == number:
                    self.rows[i][j].mark()

    def surrender(self):
        self.ticket_surrendered = True

    def __str__(self) -> str:
        str = ''
        for i in range(HousieTicket.no_of_rows):
            for j in range(HousieTicket.no_of_columns):
                str += " " + self.rows[i][j]

                




        

        

    

    