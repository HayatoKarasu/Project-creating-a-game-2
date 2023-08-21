from utils import randcell
import os

class Helicopter:
    def __init__(self, w, h):
        rc = randcell(w, h)
        rx, ry = rc[0], rc[1]
        self.h = h
        self.w = w
        self.x = rx
        self.y = ry
        self.mxtank = 1
        self.tank = 0
        self.score = 0
        self.lives = 20

    def move(self, dx, dy):
        nx = dx + self.x
        ny = dy + self.y
        if (nx >= 0 and ny >= 0 and nx < self.h and ny < self.w):
            self.x, self.y = nx, ny

    def print_stats(self):
        print('✅ ', self.tank, '/', self.mxtank, sep="", end = "|")
        print('⚡️', self.score, end = "|")
        print('❤️ ', self.lives)

    def game_over(self):
        os.system("clear")
        print("ИГРА ОКОНЧЕНА! Вы набрали: ", self.score, "очков")
        exit(0)

    def export_data(self):
        return {"score": self.score,
                "lives": self.lives, 
                "x": self.x, 
                "y": self.y, 
                "tank": self.tank, 
                "mxtank": self.mxtank}
    
    def import_data(self, data):
        self.x = data["x"] or 0
        self.y = data["y"] or 0
        self.tank = data["tank"] or 0
        self.mxtank = data["mxtank"] or 1
        self.lives = data["lives"] or 20
        self.score = data["score"] or 0
