import random

from HousieTicket import HousieTicket
from NumberDraw import NumberDraw

class HousieGame:
    def __init__(self, no_of_players) -> None:
        if no_of_players <= 0:
            raise Exception("Player count should be greater than 0")

        self.no_of_players = no_of_players
        self.is_game_started = False
        self.is_game_completed = False
        self.tickets = []
        self.announced_numbers = []
        self.first_row_winners = []
        self.second_row_winners = []
        self.third_row_winners = []
        self.number_draw = NumberDraw(1, 100)

    def distribute_tickets(self):
        if self.is_game_started or self.is_game_completed:
            raise Exception("Can not distribute ticket at this stage")

        self.tickets = []
        for i in range(self.no_of_players):
            numbers = random.sample(range(1, 101), HousieTicket.numbers_in_one_ticket)
            self.tickets.append(HousieTicket(i, numbers))

    def play(self):       
        self.is_game_started = True
        while not self.is_game_over() and self.number_draw.is_number_available():   
            number = self.number_draw.draw()         
            self.announced_numbers.append(number)
            for ticket in self.tickets:
                ticket.mark_number_if_present(number)

            # check first row full tickets
            if len(self.first_row_winners) == 0:
                for ticket in self.tickets:
                    if 0 in ticket.get_full_row_ids():
                         ticket.surrender()
                         self.first_row_winners.append(ticket)
            
             # check second row full tickets
            if len(self.second_row_winners) == 0:
                for ticket in self.tickets:
                    if 1 in ticket.get_full_row_ids():
                         ticket.surrender()
                         self.second_row_winners.append(ticket)

             # check third row full tickets
            if len(self.third_row_winners) == 0:
                for ticket in self.tickets:
                    if 2 in ticket.get_full_row_ids():
                         ticket.surrender()
                         self.third_row_winners.append(ticket)              

        self.is_game_completed = True

    def is_game_over(self):
        return any(x.is_full_housie() for x in self.tickets)

    def get_winners(self):
        return [ticket for ticket in self.tickets if ticket.is_full_housie()]

    def get_full_row_tickets(self):
        return self.first_row_winners + self.second_row_winners + self.third_row_winners

