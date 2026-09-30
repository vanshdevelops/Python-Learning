# Write a class train which has method to book a ticket, get status(no. of seats) and get fare information of train running under Indian Railways.

from random import randint 
class Train:
    def __init__(self, TrainNo):
        self.TrainNo = TrainNo
    def book(self, fro, to):
        print(f"ticket is booked in train no.: {self.TrainNo} from {fro} to {to}")
    def getstatus(self):
        print(f"train no.: {self.TrainNo} is running on time")
    def getfare(self, fro, to):
        print(f"Ticket fare in tarin no.: {self.TrainNo} from{ fro} to {to} is {randint(222, 5555)}")     


t = Train(123456)
t.book("Agra", "Meerut")
t.getstatus()
t.getfare("Agra", "Meerut")

