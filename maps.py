import random

class Map():
    matrix = [[0,0,0,1,0,0,0,0,0,0],
          [0,0,0,1,0,1,0,1,1,0],
          [0,1,1,1,0,1,0,1,1,0],
          [0,0,0,0,0,1,0,0,0,0],
          [1,1,1,1,0,1,1,1,1,0],
          [0,1,0,1,0,0,0,0,0,0],
          [0,1,0,1,0,1,1,0,1,0],
          [0,0,0,0,0,1,1,0,1,0],
          [0,1,1,1,0,0,0,0,1,0],
          [0,0,0,1,0,1,1,0,0,0]]
    @staticmethod
    def get_random():
        return random.randint(1,6)
