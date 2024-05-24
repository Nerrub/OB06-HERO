import random

class Hero:
    def __init__(self, name, health=100,attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        other.health -= damage
        print(f"{self.name} наносит {other.name} {damage} урона")
    def is_alive(self):
        return self.health > 0
class Game:
    def __init__(self):
        self.player = Hero("Игрок")
        self.computer = Hero("Компьютер")
    def start(self):
        print("Бой начинается")
        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            print(f"У {self.computer.name} осталось {self.computer.health} здоровья \n")
            if not self.computer.is_alive():
                print("Игрок победил!")
                break
            self.computer.attack(self.player)
            print(f"У {self.player.name} осталось {self.player.health} здоровья \n")
            if not self.player.is_alive():
                print("Комьютер победил!")
                break
game = Game()
game.start()