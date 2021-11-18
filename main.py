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

from datetime import datetime
from random import randint
import os
import time
import json

class Ticket:

    def __init__(self, name, number, defaultPrice, eventName, eventDate):
        self.name = name
        self.number = number
        self.defaultPrice = defaultPrice
        self.eventName = eventName
        self.eventDate = eventDate
        self.writeTicket()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number

    @property
    def defaultPrice(self):
        return self.__defaultPrice

    @defaultPrice.setter
    def defaultPrice(self, defaultPrice):
        self.__defaultPrice = defaultPrice

    @property
    def eventName(self):
        return self.__eventName

    @eventName.setter
    def eventName(self, eventName):
        self.__eventName = eventName

    @property
    def eventDate(self):
        return self.__eventDate

    @eventDate.setter
    def eventDate(self, eventDate):
        self.__eventDate = eventDate

    # write ticket into json file
    def writeTicket(self):
        f = open(self.number + '.json', 'w')
        json.dump(self.__dict__, f)
        f.close()
    # get ticket from json file
    def getTicket(Task1):
        if not os.path.exists(Task1 + '.json'):
                raise FileNotFoundError
        f = open(Task1 + '.json', "r")
        input = json.load(f)
        name = input['_Ticket__name']
        eventName = input['_Ticket__eventName']
        eventDate = input['_Ticket__eventDate']
        if '_StudentTicket__price' in input:
                defaultPrice = input['_StudentTicket__defaultPrice']
        elif '_LateTicket__price' in input:
                defaultPrice = input['_LateTicket__defaultPrice']
        else:
                defaultPrice = input['_AdvanceTicket__defaultPrice']
        f.close()
        return f"{Task1}\n{name}\nevent: {eventName}\ntotal price: {round(defaultPrice)}\ndate: {eventDate}"

    # creates our ticket in the json file
    def createTicket(Task1):
        if not os.path.exists(Task1):
            raise FileNotFoundError
        f = open(Task1, "r")
        input = json.load(f)
        name = input['name']
        defaultPrice = input['defaultPrice']
        eventName = input['eventName']
        eventDate = input['eventDate']
        is_student = False
        if 'is_student' in input:
            is_student = input['is_student']
        f.close()
        return Ticket.generateTicket(name, eventName, eventDate, defaultPrice, is_student)

    # makes ticket depending on the input
    def generateTicket(name, eventName, eventDate, defaultPrice, is_student=False):
        if (
                not isinstance(eventDate, str)
                and not isinstance(eventName, str)
                and not isinstance(defaultPrice, int)
                and not isinstance(name, str)
                and not isinstance(is_student, bool)
        ):
            raise TypeError("Incorrect type")
        ans = input("Enter the number of days until the event: ")

        if not isinstance(ans, int):
            raise TypeError("Incorrect input")

        if is_student == True:
            return StudentTicket(name, eventName, defaultPrice, eventDate)
        elif ans >= 60:
            return AdvancedTicket(name, eventName, defaultPrice, eventDate)
        elif ans <= 10:
            return LateTicket(name, eventName, defaultPrice, eventDate)
        else:
            return Ticket(name, eventName, defaultPrice, eventDate)

    def generateNumber(self):
        newnum = ''.join(["{}".format(randint(0, 9)) for num in range(0, 10)])
        return newnum

# derived classes which are subtypes of our ticket
class AdvancedTicket(Ticket):
    def __init__(self, person, event, modifiedPrice, eventDate):
        super().__init__(person, event, modifiedPrice, eventDate)

    @property
    def modifiedPrice(self):
        return self.__modifiedPrice

    @modifiedPrice.setter
    def modifiedPrice(self, modifiedPrice):
        self.__modifiedPrice = modifiedPrice * 0.60

class LateTicket(Ticket):
    def __init__(self, person, event, modifiedPrice, eventDate):
        super().__init__(person, event, modifiedPrice, eventDate)

    @property
    def modifiedPrice(self):
        return self.__modifiedPrice

    @modifiedPrice.setter
    def modifiedPrice(self, modifiedPrice):
        self.__modifiedPrice = modifiedPrice * 1.10

class StudentTicket(Ticket):
    def __init__(self, person, event, modifiedPrice, eventDate):
        super().__init__(person, event, modifiedPrice, eventDate)

    @property
    def modifiedPrice(self):
        return self.__modifiedPrice

    @modifiedPrice.setter
    def modifiedPrice(self, modifiedPrice):
        self.__modifiedPrice = modifiedPrice * 0.50

def main():
    print(Ticket.createTicket("Task1.json"))

main()