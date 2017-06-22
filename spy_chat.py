from termcolor import colored
from spy_details import spy, Spy, ChatMessage, friends
from steganography.steganography import Steganography
from datetime import datetime

STATUS_MESSAGES = ['Hii whatsapp', 'Available.', 'Busy','Sleeping']

print "****WELCOME TO SPY CHAT!****"


Spy.current_status_message = None
def add_status(): #adding status to the spychat user
    updated_status_message=None
    status_position=0
    if Spy.current_status_message != None:
        print "Your current status message is : "+Spy.current_status_message
    else:
        print "You don't have any status message currently \n"
    default = raw_input("Do you want to select from the older status (y/n)? ")
    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")
        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message
        elif default.upper() == 'Y':
            status_position = 1
        for message in STATUS_MESSAGES:
            print +status_position, message
            status_position = status_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print "The option you chose is not valid! Press either y or n."

    if updated_status_message:
        print "Your updated status message is : "+updated_status_message
    else:
        print "You current don't have a status update"
    return updated_status_message


def add_friend():   #adding a new friend
    new_friend = Spy('','',0,0.0)
    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")
    new_friend.name = new_friend.salutation + " " + new_friend.name
    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)
    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)
    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print "Friend Added!"
    else:
        print "SORRY! We can't add spy with the details you provided"
        invalid_friend=1

    return len(friends)


def select_a_friend(): #selecting from a friendlist
    number_of_friend = 0
    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (number_of_friend +1, friend.salutation, friend.name,
                                                   friend.age,
                                                   friend.rating)
        number_of_friend = number_of_friend + 1
    friend_choice = raw_input("Choose from your friends")
    friend_choice_position = int(friend_choice) - 1
    return friend_choice_position


def send_message():
        if len(friends)==0: #checking that there is any friend or not
            add_friend()
            send_message()
        else:
            friend_choice=select_a_friend()
            original_image = raw_input("What is the name of the image?")
            output_path = "hello1.jpg"
            text = raw_input("Write your message ")
            if len(text)>0:
                Steganography.encode(original_image, output_path, text)
                new_chat = ChatMessage(text,True)
                friends[friend_choice].chats.append(new_chat)
                print "Your secret message image is ready!"
            elif len(text) > 150:
                print "Words are more.please delete something\n"

            else:
                print "Enter some message"



def read_message(): # read a message from list
    sender = select_a_friend()
    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)
    new_chat = ChatMessage(secret_text,False)
    friends[sender].chats.append(new_chat)
    print "Your secret message has been saved!"

def read_chat_history(): #read chats history from friends
    if len(friends) == 0:
        print "No friends and messages!"

    else:
        read_for = select_a_friend()

        print '\n'

        for chat in friends[read_for].chats:
             if chat.sent_by_me:
                print colored ("[%s]" , "blue") %(chat.time.strftime("%d,%B,%Y")), colored("you said ", "red")
                print chat.message
             else:
                print '(%s) [%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)

def start_chat(Spy):  #starting chat from the user

    Spy.name = Spy.salutation + " " + Spy.name
    if Spy.age > 10 and Spy.age < 60:
        print "Authentication complete. Welcome " + Spy.name + " age: " \
              + str(Spy.age) + " and rating of: " + str(Spy.rating) + " Proud to have you onboard"

        show_menu = True

        while show_menu:
            menu_choices = "choose your option \n 1. To Update status \n 2. TO add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)
               # choose from menu
                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print "Sorry you are NOT of the CORRECT AGE to be a spy"

start_chat(Spy) #caling method spy _chat