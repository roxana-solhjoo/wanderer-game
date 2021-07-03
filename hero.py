from tkinter import *

from maps import Map

class Hero():

    def __init__(self, x, y, image):
        self.x = x *72
        self.y = y *72
        self.image = image
        self.HP = 20 + 3 * Map.get_random()
        self.maxHP = 38
        self.DP = 2 * Map.get_random()
        self.SP = 5 + Map.get_random()
        self.level = 1
        self.count = 0

    def draw_character(self, canvas):
        canvas.create_image(self.x, self.y, anchor=NW, image = self.image)

    def move(self, x=0, y=0 ):
        self.x += x
        self.y += y
        self.count += 1
    def get_coordinates(self):
        return self.x, self.y

    def set_coordinatesX(self, x):
        self.x += x

    def set_coordinatesY(self, y):
        self.y += y

    def set_image(self, image):
        self.image = image

    def level_up(self):
        self.level += 1
    
    def set_level(self, level):
        self.level = level

    def increase_HP(self, hp):
        self.HP += hp

    def set_HP(self, hp):
        self.HP = hp
        
    def strike(self, opponent):
        if isinstance(self, Hero):
            SV = 2 * self.SP + Map.get_random()
            if (SV) > opponent.DP:
                opponent.HP -= SV-opponent.DP
        else:
            SV = opponent.SV + Map.get_random()
            if ((2 * Map.get_random()) + SV) > self.DP:
                self.HP -= SV-self.DP

    def battle(self, opponent):
        if self.HP and opponent.HP > 0:
            self.strike(opponent)
            opponent.strike(self)
        else:
            if isinstance(self, Hero) and opponent.HP < self.HP:
                self.maxHP += Map.get_random()
                self.DP += Map.get_random()
                self.SP += Map.get_random()
                return opponent
            else:
                print("Hero died")

