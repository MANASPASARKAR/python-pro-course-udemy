import card
import seat
import random
import string
from ticket import Ticket

class User:

    def __init__(self, name):
        self.name = name


    def buy_ticket(self, seat_id, user_card):

        chosen_seat = seat.Seat(seat_id)
        chosen_seat.occupy()

        balance = user_card.get_balance()
        price = chosen_seat.get_price()

        if(balance < price):
            return "Low balance"

        user_card.deduct_price(price)
        ticket_id = ''.join(random.choices(string.ascii_letters, k=8))
        ticket = Ticket(ticket_id, self.name, price, seat_id)
        ticket.to_pdf()

        return "bought ticket successfully! Check out the pdf!"




