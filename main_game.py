from errors import *
from Character import *

class Menu:
    def __init__(self,):
        self.heroes_names = []

    def print_menu(self):
        print("1. Create new character")
        print("2. Create gun")
        print("3. Extra object")
        print("4. Print all character`s names")
        print("5. Delete a character")
        print("6. Exit")
    
    def command_create_character(self, name, sex, ch_class):
        # input
        # validate
        # create hero
        self.naem = name
        self.sex = sex
        self.ch_class = ch_class

        # hero = Character(name, sex, ch_class)
    
    def choice(self, gun, extra_object):
        self.gun = gun
        self.extra_object = extra_object

    def run(self):
        while True:
            self.print_menu()
            choice = input("Choose an item from the menu: \n> ")

            if choice == "1":
                self.command_create_character(input("Enter the character name (alpha-numeric): "), input("Give sex for the character: "), input("Give ch_class: "))
                if self.ch_class != 'Warrior' and self.ch_class != 'Mage':
                    raise InvalidCh_class()
                self.heroes_names.append(self.command_create_character)

            elif choice == "2":
                name = input("Character name")
                if name in self.heroes_names:
                    pass

            elif choice == "3":
                name = input("Character name")
                if name.__contains__(self.heroes_names):
                    pass

            elif choice == "4":
                print(self.heroes_names)
      
            elif choice == "5": 
                name = input("Character name")
                if name.__contains__(self.heroes_names):
                    self.heroes_names.pop(name)

            elif choice == "6": 
                break

            else:
                raise InvalidDataFormat()
            print(self.heroes_names)
                
if __name__ == '__main__':
    menu = Menu()
    menu.run()
