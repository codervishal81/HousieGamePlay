'''
    Represents cell on the housie ticket.
    Cell has number and a state that says whether cell is marked or unmarked
'''

class TicketCell:

    def __init__(self, number) -> None:
        self.number = number
        self.is_marked = False

    def mark(self):
        self.is_marked = True

    def __str__(self) -> str:
        return self.number + " " + ("X" if self.is_marked else " ")

        

class EmptyCell(TicketCell):

    def __init__(self) -> None:
        super().__init__(None)

    def __str__(self) -> str:
        return "E" + " " + " "

