from datetime import datetime
class Spy:  #initialising details in class
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:  #initialising message details
    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy
friends = []


Spy.name = raw_input("What is your name : ")
if len(Spy.name) > 0:
    Spy.salutation = raw_input("Are you Mr or Mrs : ")
    Spy.name = Spy.salutation + ". " + Spy.name
    if len(Spy.name) > 0:  # checking length of spy_name
        print "Welcome " + Spy.name + " glad to have you back"
    else:
        print 'Please enter valid name'
    Spy.age = 0
    Spy.rating = 0.0
    Spy.is_online = False
    Spy.age = raw_input("What is your age : ")
    Spy.age = int(Spy.age)
    if Spy.age > 12 and Spy.age < 50:
        Spy.rating = raw_input("What is your spy rating : ")
        Spy.rating = float(Spy.rating)
    else:
        print "You are not of the correct age to be a spy"
    if Spy.rating > 4.5:
        print 'You have the good ratings '
    elif Spy.rating > 3.5 and Spy.rating <= 4.5:
        print 'You have the average rating'
    elif Spy.rating >= 2.5 and Spy.rating <= 3.5:
        print 'You can improve it'
    else:
        print 'We can always use somebody for the help.'
else:
    print "Please enter something!!"