from HousieGame import HousieGame
from TicketPrinter import TicketPrinter

players_count = input("Enter number of players : ")
game = HousieGame(int(players_count))
game.distribute_tickets()
game.play()

print("###############GAME OVER#################################")
print("Total Number Announced: " + str(len(game.announced_numbers)))
print(game.announced_numbers)

print("=======================FULL ROWS============================")
full_row_tickets = game.get_full_row_tickets()
for ticket in full_row_tickets:
    TicketPrinter().print(ticket)
    print('')
    print('')

print("=======================WINNER============================")
full_housie_tickets = game.get_winners()
for ticket in full_housie_tickets:
    TicketPrinter().print(ticket)
print('')
print('')

print_all = input("Do you want to print all tickets? (y/n)")
if print_all.lower() == 'y':
    print("=======================ALL TICKETS============================")
    for ticket in game.tickets:
        TicketPrinter().print(ticket)
    print('')
    print('')    

