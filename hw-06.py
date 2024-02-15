from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
     pass

class Phone(Field):

    def ten_digit_check(phone: str):
        if re.search("\d{10}", phone):
            return True
        else:
            print(f"incorrect phone number: {phone}")
            return False

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str):
        if Phone.ten_digit_check(phone):
            self.phones.append(Phone(phone))
            
    
    def remove_phone(self, deleted_phone: str):
        for phone in self.phones:
            if str(phone) == deleted_phone:
                self.phones.remove(phone)

    def edit_phone(self, old_number: str, new_number: str):
        for phone in self.phones:
            if str(phone) == old_number:
                if Phone.ten_digit_check(new_number):
                    self.phones[self.phones.index(phone)] = Phone(new_number)

    def find_phone(self, desired_phone: str):
        for phone in self.phones:
            if desired_phone == str(phone) :
                return(phone)
         
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name] = record

    def find(self, search_name: str):
        for name in self.data:
            if search_name == str(name):
                return(self.data.get(name))
            
    def delete(self, search_name: str):
        for name in self.data:
            if search_name == str(name):
                del self.data[name]
                break



# book = AddressBook()

# # Створення запису для John
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")

# # Додавання запису John до адресної книги
# book.add_record(john_record)

# # Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)

# # Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)

# # Знаходження та редагування телефону для John
# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")

# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# # Видалення запису Jane
# book.delete("Jane")

