import os
import imaplib
import time

print("""

  /$$$$$$              /$$                                         /$$     /$$                                                   /$$ /$$      
 /$$__  $$            | $$                                        | $$    |__/                                                  |__/| $$      
| $$  \ $$ /$$   /$$ /$$$$$$    /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$$$$$   /$$  /$$$$$$$        /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$| $$      
| $$$$$$$$| $$  | $$|_  $$_/   /$$__  $$| $$_  $$_  $$ |____  $$|_  $$_/  | $$ /$$_____/       /$$__  $$| $$_  $$_  $$ |____  $$| $$| $$      
| $$__  $$| $$  | $$  | $$    | $$  \ $$| $$ \ $$ \ $$  /$$$$$$$  | $$    | $$| $$            | $$$$$$$$| $$ \ $$ \ $$  /$$$$$$$| $$| $$      
| $$  | $$| $$  | $$  | $$ /$$| $$  | $$| $$ | $$ | $$ /$$__  $$  | $$ /$$| $$| $$            | $$_____/| $$ | $$ | $$ /$$__  $$| $$| $$      
| $$  | $$|  $$$$$$/  |  $$$$/|  $$$$$$/| $$ | $$ | $$|  $$$$$$$  |  $$$$/| $$|  $$$$$$$      |  $$$$$$$| $$ | $$ | $$|  $$$$$$$| $$| $$      
|__/  |__/ \______/    \___/   \______/ |__/ |__/ |__/ \_______/   \___/  |__/ \_______/       \_______/|__/ |__/ |__/ \_______/|__/|__/      


""")

imap_server = "imap.gmail.com" #or another imap seerver
email_adress = "" # your email
password = "" # your password
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_adress, password)

def inbox():

    imap.select("Inbox", readonly=False)
    what_email = input("What sender from your email want to delete ? \n")
    status, message = imap.search(None, f'(FROM "{what_email}")')
    emails = message[0].split()
    count = len(emails)

    for emailss in emails:
        count = count -1
        print(count)
        imap.store(emailss, '+FLAGS', '(\Deleted)')
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')

    input("All Unread emails deleted , press any key to exit !")


def trash():

    imap.select("[Gmail]/Trash")
    status, message = imap.search(None, 'ALL')
    emails = message[0].split()
    count = len(emails)

    for emailss in emails:
        count = count - 1
        print(count)
        imap.store(emailss, '+FLAGS', '(\Deleted)')
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')

    imap.expunge()
    input("All Unread emails deleted , press any key to exit !")


def spam():

    imap.select("[Gmail]/Spam")
    status, message = imap.search(None, 'ALL')
    emails = message[0].split()
    count = len(emails)

    for emailss in emails:
        count = count - 1
        print(count)
        imap.store(emailss, '+FLAGS', '(\Deleted)')
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')

    imap.expunge()

    input("All Unread emails deleted , press any key to exit !")


def unreaded():

    imap.select("Inbox", readonly=False)
    status, message = imap.search(None, 'UNSEEN')
    emails = message[0].split()
    count = len(emails)


    for emailss in emails:
        count = count -1
        print(count)
        imap.store(emailss, '+FLAGS', '(\Deleted)')
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')

    input("All Unread emails deleted , press any key to exit !")


while True:
    steps = input("Choose one of the steps : \n[1] Delete one sender from your email\n[2] Empty the Trash\n"
                  "[3] Delete all Unread emails\n[4] Empty the Spam folder\n[5] To exit !\n")
    if steps == "1":
        inbox()
    elif steps == "2":
        trash()
    elif steps == "3":
        unreaded()
    elif steps == "4":
        spam()
    elif steps == "5":
        break
    else:
        print("Choose the right step !")


