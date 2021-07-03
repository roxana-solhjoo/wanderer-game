from maps import Map
from hero import Hero

class Skeleton(Hero):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.HP = 2 * self.level * Map.get_random()
        self.DP = self.level / 2 * Map.get_random()
        self.SP = self.level * Map.get_random()
        self.maxHP = 38




