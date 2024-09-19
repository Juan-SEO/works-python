#BINGO
# Realiza un programa que simule un bingo. El programa tiene que permitirte elegir 1, 2, o 3 cartones. 
# El progama finalizará cuando consigas "bingo", recuerda que puedes cantar línea.


import random


class Carton:
    def __init__(self, n_lines):
        self.lines = [Linea() for x in range(n_lines)]

    def check_win(self):
        for line in self.lines:
            if line.check_win():
                print("Linea")
        if all():
            print("Bingo")
        
class Linea:
    def __init__(self,size=6):
        self.size = size
        self.numbers = self.create_list()

    def create_list(self):
        return [1,2,3,4]
    
    def check_win(self):
        for n in self.numbers:
            if n not in shown_numbers:
                return False
        return True
