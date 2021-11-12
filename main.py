#Task 1.
#Write a program for selling tickets to IT-events. Each ticket has a unique number and a price.
#There are four types of tickets: regular ticket, advance ticket (purchased 60 or more days before the event),
#late ticket (purchased fewer than 10 days before the event) and student ticket.
#Additional information:
#-advance ticket - discount 40% of the regular ticket price;
#-student ticket - discount 50% of the regular ticket price;
#-late ticket - additional 10% to the reguler ticket price.
#All tickets must have the following properties:
#-the ability to construct a ticket by number;
#-the ability to ask for a ticket’s price;
#-the ability to print a ticket as a String.

# main program blueprint
import json

f = open('Task1.json', )

data = json.load(f)

for i in data['ticket_details']:
    print(i)

ans1 = input("Do you already have a ticket? Press y for yes, press n for no ")
if ans1 == "Y" or "y":
    ticket_id = input("Enter your ticket number: ")
    # search by id in json
elif ans1 == "N" or "n":
    input("Enter a ticket you'd like to buy: ")
    # asking for ticket details



class Ticket():

    def __init__(self, number, price):
        self.number = number
        self.price = price

    def get_price(self):
        return self.price
    def set_price(self,value1):
        self.price = value1

    def get_number(self):
        return self.number
    def set_number(self,value2):
        self.number = value2

class RegularTicket(Ticket):
    pass
class AdvancedTicket(Ticket):
    pass
class LateTicket(Ticket):
    pass
class StudentTicket(Ticket):
    pass
try:
    ans2 = input("Are you a student? Press y for yes, press n for no ")
    if ans2 == "y" or "Y":
        a = StudentTicket(a.set_number("Enter your ticket number"))
    elif ans2 == "n" or "N":
        pass
    else:
        print("Incorrect answer, please try again")
except TypeError:
    print("Incorrect input")
    exit(1)


f.close()