from .text import *
#from model import phonebook_length
from model import PhoneBook, Contact

def menu() -> int:
    print(main_menu)
    while True:
        choice = input(menu_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        print(input_error)


def print_message(message: str):
    length = len(message)
    print('\n' + '=' * length)
    print(message)
    print('=' * length + '\n')


def show_contacts(book: PhoneBook):
    if book.contacts:
        print('\n' + '=' * 67)
        for contact in book.contacts:
            print(contact)
        print('=' * 67 + '\n')
    else:
        print(book_error)


# def show_contact(book: PhoneBook):
#     if book:
#         print('\n' + '=' * 67)
#         for contact in book:
#             print(contact)
#         print('=' * 67 + '\n')
#     else:
#         print(book_error)


def show_contact(contact: Contact):
    print(contact)


def input_contact(message: str) -> dict[str, str]:
    print(message)
    new = Contact(input(new_contact[0]), input(new_contact[1]), input(new_contact[2]))
    return new


def input_return(message: str) -> str:
    return input(message)

def input_id(message: str, book: PhoneBook) -> str:
    while True:
        choice = int(input(message))
        # if choice and 0 < choice <= book.phonebook_length():
        #     return choice
        # print(delete_error)
        # if book.contacts[choice] != None:
        #     return choice
        # print(delete_error)
        for contact in book.contacts:
            if contact.uid == choice:
                book.contacts.remove(contact)
                return choice
        print(delete_error)
