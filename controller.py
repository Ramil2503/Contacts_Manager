from view import Console
from view import text
from model import PhoneBook

def start():
    pb = PhoneBook('phones.txt')
    while True:
        choice = Console.menu()
        match choice:
            case 1:
                pb.open_file()
                Console.print_message(text.open_successful)
            case 2:
                pb.save_file()
                Console.print_message(text.file_saved)
            case 3:
                Console.show_contacts(pb)
            case 4:
                new = Console.input_contact(text.input_new_contact)
                pb.add_contact(new)
                Console.print_message(text.contact_saved(new.name))
            case 5:
                word = Console.input_return(text.search_word)
                result = pb.search(word)
                Console.show_contact(result)
            case 6:
                word = Console.input_return(text.search_word)
                result = pb.search(word)
                Console.show_contact(result)
                index = Console.input_return(text.input_index)
                new = Console.input_contact(text.input_change_contact)
                pb.change(int(index), new)
                old_name = pb.contacts[int(index)-1].name
                Console.print_message(text.contact_changed(new.name if new.name else old_name))
            case 7:
                word = Console.input_return(text.search_word)
                result = pb.search(word)
                Console.show_contact(result)
                index = Console.input_delete_id(text.delete_contact, pb)
                pb.delete(index)
                Console.show_contacts(pb)
                Console.print_message(text.contact_deleted)
            case 8:
                break
