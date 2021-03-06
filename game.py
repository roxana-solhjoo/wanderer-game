from tkinter import *
import random

from tiles import Floor, Wall
from hero import Hero
from boss import Boss
from skeleton import Skeleton
from maps import Map

class Game():
    def __init__(self, hero):
        self.hero = hero
        self.tiles = []
        self.characters = []
        floor = PhotoImage(file="images/floor.png")
        wall = PhotoImage(file="images/wall.png")

        for i in range(0,10):
            if Map.matrix[0][i] == 0:
                tile = Floor(i*72,0, floor)
                self.add_tiles(tile)
            else:
                tile = Wall(i*72,0, wall)
                self.add_tiles(tile)
            for j in range(1,10):
                if Map.matrix[j][i] == 0:
                    tile = Floor(i*72,j*72, floor)
                    self.add_tiles(tile)
                else:
                    tile = Wall(i*72,j*72, wall)
                    self.add_tiles(tile)
        self.create_monsters()


    def create_monsters(self):  
        skeleton = PhotoImage(file="images/skeleton.png")
        boss = PhotoImage(file="images/boss.png") 
        count = 0
        while count < random.randint(3,6):
            i = random.randint(0,9)
            j = random.randint(0,9)
            if Map.matrix[j][i] == 0:
                skelet = Skeleton(i, j, skeleton)
                self.characters.append(skelet)
                count +=1

        count2 = 0
        while count2 < 1:
            i = random.randint(0,9)
            j = random.randint(0,9)
            if Map.matrix[j][i] == 0:
                boss = Boss(i, j, boss)
                self.characters.append(boss)
                count2 +=1

    def draw(self, canvas):
        canvas.create_rectangle(0, 0, 720, 720)
        for tile in self.tiles:
            canvas.create_image(tile.x, tile.y, anchor=NW, image = tile.image)
    
    def add_tiles(self, tiles):
        self.tiles.append(tiles)
        return self.tiles

    def draw_character(self,canvas):
        for char in self.characters:
            canvas.create_image(char.x, char.y, anchor=NW, image = char.image)

    def remove_character(self, character):
        self.characters.remove(character)

    def get_characters(self):
        return self.characters

    def get_char_length(self):
        return len(self.characters)

    def level_up_chars(self, amount):
        for i in self.characters:
            i.set_level(amount)







    
    





    
    