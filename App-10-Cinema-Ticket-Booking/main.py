import sys
from user import User
from seat import Seat
from card import Card

name = input("Enter your name: ")
chosen_seat = input(f"Select seat you want to choose ({Seat.get_empty_seats()}): ")

seat = Seat(chosen_seat)
if not seat.is_free():
    sys.exit(f"Sorry The Seat {chosen_seat} is Occupied!")

while True:

    confirm = input(f"The price of the seat is {seat.get_price()}Do you want to continue? (enter yes / no): ")
    if confirm.lower() == 'no' or confirm.lower() == 'no':
        sys.exit()
        break

    elif confirm.lower() == 'yes' or confirm.lower() == 'y':
        break

    print("Invalid input try again")

card_no = input("Enter card number: ")
card_holder_name = input("Enter Card Holder name: ")
card_cvc = input("Enter card cvc: ")
card_type = input("Enter card type: ")

card = Card(type=card_type, number=card_no, cvc=card_cvc, holder=card_holder_name)
if not card.validate():
    sys.exit("Invalid card info!")

user = User(name)
print(user.buy_ticket(seat.seat_id, card))
