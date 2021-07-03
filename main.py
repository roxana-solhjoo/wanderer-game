from tkinter import *
import random

from game import Game
from hero import Hero
from maps import Map



def main():
    root = Tk()
    root.title("Wanderer Game")
    canvas = Canvas(root, width=720, height=720)

    hero_down = PhotoImage(file="images/hero-down.png")
    hero_up = PhotoImage(file="images/hero-up.png")
    hero_left = PhotoImage(file="images/hero-left.png")
    hero_right = PhotoImage(file="images/hero-right.png")

    hero = Hero(0, 0, hero_down)
    game = Game(hero)


    def battle(event):
        opponent = False
        for char in game.get_characters():
            if coords(hero) == coords(char):
                opponent = hero.battle(char)
        if opponent:
            game.remove_character(opponent)
        if game.get_char_length() < 1:
            new_level()
            game.create_monsters()
            game.level_up_chars(hero.level)
            hero.x = 0
            hero.y = 0
            hero.set_image(hero_down)

        canvas.delete("all")
        stats()
        draw_canvas()

    canvas.pack()

    m = Map.matrix
    def coords(char):
        x, y = char.get_coordinates()
        x, y = int(x / 72), int(y / 72)
        return x, y

    def leftKey(event):
        if m[coords(hero)[1]][coords(hero)[0] - 1] != 1 and coords(hero)[0] > 0:  # left
            hero.move(x=-72)
            hero.set_image(hero_left)
            draw_canvas()

    def rightKey(event):
        if m[coords(hero)[1]][coords(hero)[0] + 1] != 1 and coords(hero)[0] <= 9:  # right
            hero.move(x=72)
            hero.set_image(hero_right)
            draw_canvas()

    def upKey(event):
        if m[coords(hero)[1] - 1][coords(hero)[0]] != 1 and coords(hero)[1] > 0:  # up
            hero.move(y=-72)
            hero.set_image(hero_up)
            draw_canvas()

    def downKey(event):
        if m[coords(hero)[1] + 1][coords(hero)[0]] != 1 and coords(hero)[1] <= 9:  # down
          hero.move(y=72)
          hero.set_image(hero_down)
          draw_canvas()


    root.bind('<Left>', leftKey)
    root.bind('<Right>', rightKey)
    root.bind('<Up>', upKey)
    root.bind('<Down>', downKey)
    root.bind('<space>', battle)

    def draw_canvas():
        game.draw(canvas)
        game.draw_character(canvas)
        hero.draw_character(canvas)

    draw_canvas()
    canvas.focus_set()

    canvas2 = Canvas(root, width=600, height=30)
    def stats():
        canvas2.create_rectangle(0, 0, 600, 30, fill="grey")
        text = f"Hero (Level: {hero.level}) HP: {int(hero.HP)}/38 | DP: {hero.DP} | SP: {hero.SP}"
        canvas_text = canvas2.create_text(10, 10, text=text, font=('freemono bold', 11), anchor=NW)
        canvas2.pack()

    def new_level():
        hero.level_up()
        chance = random.random()
        if chance <= 0.1:
            hero.set_HP = hero.maxHP
        if 0.1 < chance <= 0.4:
            hero.set_HP = hero.maxHP / 3
        if chance >= 0.5:
            hero.set_HP = hero.maxHP * 0.1

    root.mainloop()

if __name__ == '__main__':
    main()
