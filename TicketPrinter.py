class TicketPrinter:

    def __init__(self):
        pass

    def print(self, ticket):
        print("================== Ticket : " + str(ticket.id) + " ==========================")
        print("-" * 55)
        for i in range(3):           
            row_str = ''
            for cell in ticket.rows[i]:
                row_str = row_str + "|" + ("{:03d}".format(cell.number) if cell.number != None else "   ") + (" X" if cell.is_marked else "  ")
            row_str = row_str + "|"
            print(row_str)
        print("-" * 55)