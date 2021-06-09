from tkinter import *
import random
import math

root = Tk()
has_numbers = BooleanVar()
has_letters = BooleanVar()
has_symbols = BooleanVar()
quantity = IntVar()
quantity.set(8)
password = StringVar()

class Generator:
    def __init__(self, has_numbers, has_letters, has_symbols, quantity):
        self.has_numbers = has_numbers
        self.has_letters = has_letters
        self.has_symbols = has_symbols
        self.quantity = quantity
        self.password = ""
        self.letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'
                        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
        self.symbols = ('.', ',', '[', ']', '{', '}', '~', '^', '´', '`', ';', ':', '/',
                        '?', '°', '>', '<', '-', '_', '+', '=', '§', '!', '@', '#', '$',
                        '%', '¨', '&', '*', '(', ')', '"', "'", '\\', '|', '₢')
        self.password_generator()

    def password_generator(self):
        if self.has_numbers and not self.has_letters and not self.has_symbols:
            # Senha só com números.
            for time in range(0, quantity.get()):
                self.password = str(self.password) + str(random.randint(0, 9))
        elif self.has_letters and not self.has_numbers and not self.has_symbols:
            # Senha só com letras.
            for time in range(0, quantity.get()):
                self.password += random.choice(self.letters)
        elif self.has_symbols and not self.has_letters and not self.has_numbers:
            # Senha só com símbolos.
            for time in range(0, quantity.get()):
                self.password += random.choice(self.symbols)
        elif self.has_numbers and self.has_letters and not self.has_symbols:
            # Senha com números e letras
            for time in range(0, quantity.get()):
                if time % 2 == 0:
                    self.password += str(random.randint(0, 9))
                else:
                    self.password += random.choice(self.letters)
        elif self.has_numbers and self.has_symbols and not self.has_letters:
            # Senha com números e símbolos.
            for time in range(0, quantity.get()):
                if time % 2 == 0:
                    self.password += str(random.randint(0, 9))
                else:
                    self.password += random.choice(self.symbols)
        elif self.has_symbols and self.has_letters and not self.has_numbers:
            # Senha com símbolos e letras.
            for time in range(0, quantity.get()):
                if time % 2 == 0:
                    self.password += random.choice(self.symbols)
                else:
                    self.password += random.choice(self.letters)
        else:
            # Senha com tudo.
            for time in range(0, quantity.get()):
                if time % 3 == 0:
                    self.password += str(random.randint(0, 9))
                elif time % 2 == 0:
                    self.password += random.choice(self.symbols)
                else:
                    self.password += random.choice(self.letters)
        password.set(self.password)

def execute_generator():
    pword = Generator(has_numbers.get(), has_letters.get(), has_symbols.get(), quantity.get())

root.geometry("220x200")
root.title("Password generator")
entry_password = Entry(root, textvariable=password, width=35).grid(row=0, column=0)
Label(root, text="Would you like your password: ").grid(row=1, column=0)

ck_num = Checkbutton(root, text="Has numbers?", variable=has_numbers)
ck_num.grid(row=2, column=0)

ck_letter = Checkbutton(root, text="Has letters?", variable=has_letters)
ck_letter.grid(row=3, column=0)

ck_symbols = Checkbutton(root, text="Has symbols?", variable=has_symbols)
ck_symbols.grid(row=4, column=0)

Label(root, text="Num of characters: ").grid(row=5, column=0, sticky=W, pady=10)
Entry(root, textvariable=quantity, width=5, takefocus=True).grid(row=5, column=0, sticky=E, padx=60)

Button(root, text="Generate!", width=30, command=execute_generator).grid(row=6, column=0, sticky=W, pady=18)

root.mainloop()