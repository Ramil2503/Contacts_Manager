import json

class Contact:
    count_id = 1

    def __init__(self, name: str, phone: str, comment: str):
        self.name = name
        self.phone = phone
        self.comment = comment
        self.uid = Contact.count_id
        Contact.count_id += 1

    def __str__(self):
        return f'{self.uid:>3}. {self.name:<20} {self.phone:<20} {self.comment:<20}'
    
    def __repr__(self):
        return f'{self.uid:>3}. {self.name:<20} {self.phone:<20} {self.comment:<20}'

    def for_search(self):
        return f'{self.name} {self.phone} {self.comment}'.lower()

class PhoneBook:
    
    def __init__(self, path: str):
        self.contacts: list[Contact] = []
        self.path = path


    def open_file(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for contact in data:
            _, name, phone, comment, *_ = contact.strip().split(':')
            self.contacts.append(Contact(name, phone, comment))


    def add_contact(self, new: Contact):
        self.contacts.append(new)


    def search(self, word: str) -> list[Contact]:
        result = []
        for contact in self.contacts:
            if word.lower() in contact.for_search():
                result.append(contact)
                break
        return result


    def change(self, index: int, new: Contact):
        for contact in self.contacts:
            if index == contact.uid:
                contact.name = new.name if new.name else contact.name
                contact.phone = new.phone if new.phone else contact.phone
                contact.comment = new.comment if new.comment else contact.comment


    def delete(self, index: int):
        # del self.contacts[index]
        for contact in self.contacts:
            if contact.uid == index:
                self.contacts.remove(contact)
                break


    def save_file(self):
        with open('phones.txt', 'r+', encoding='utf-8') as file:
            file.truncate()
            for contact in self.contacts:
                id = contact.uid
                name = contact.name
                phone = contact.phone
                comment = contact.comment

                line = f"{id}:{name}:{phone}:{comment}"
                file.write(line + '\n')

    def phonebook_length(self):
        return len(self.contacts)
