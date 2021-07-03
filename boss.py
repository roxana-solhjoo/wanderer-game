from maps import Map
from hero import Hero

class Boss(Hero):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.HP = 2 * self.level * Map.get_random() + Map.get_random()
        self.DP = self.level / 2 * Map.get_random() + Map.get_random() / 2
        self.SP = self.level * Map.get_random() + self.level
        self.maxHP = 38
