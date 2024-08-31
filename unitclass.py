import time
import random

class Unit:
    def __init__(self, name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides,
                can_attack_ground=False, can_attack_air=False, air_unit=False):

        self.name = name
        self.health = health
        self.damage = damage
        self.damage_type = damage_type
        self.armor = armor
        self.armor_type = armor_type
        self.attack_speed = attack_speed
        self.dice_sides = dice_sides
        self.can_attack_ground = can_attack_ground
        self.can_attack_air = can_attack_air
        self.air_unit = air_unit
        self.dice_rolls = 1
        self.dice_dmg = 0
        self.damage_reduction = 0.0
        self.dmgmult = 1.0
        self.total_damage = 0

    def update_damage_multiplier(self, target):
        damage_multipliers = {("normal", "medium"): 1.5,
                            ("normal", "fortified"): 0.7,
                            ("piercing", "medium"): 0.75,
                            ("piercing", "light"): 2,
                            ("piercing", "unarmored"): 1.5,
                            ("piercing", "fortified"): 0.35,
                            ("magic", "heavy"): 2,
                            ("magic", "medium"): 0.75,
                            ("magic", "light"): 1.25,
                            ("magic", "fortified"): 0.35,
                            ("siege", "medium"): 0.5,
                            ("siege", "unarmored"): 1.5,
                            ("siege", "fortified"): 2
                            }

        key = (self.damage_type, target.armor_type)
        self.dmgmult = damage_multipliers.get(key, 1.0)

    def calculate_damage(self):
        new_damage = 0
        num_of_rolls = self.dice_rolls
        while num_of_rolls > 0:
            roll = random.randrange(1,self.dice_sides+1)
            new_damage += roll
            num_of_rolls -= 1
        return new_damage
    
    def calculate_damage_reduction(self):
        self.damage_reduction = (self.armor * 0.06) / (1 + 0.06 * self.armor)

    def can_attack_unit(self, target):
        if self.can_attack_ground == False and target.air_unit == False:
            return False
        elif self.can_attack_air == False and target.air_unit == True:
            return False
        return True
    
    def attack_unit(self,target):
        while self.is_alive() and target.is_alive():
            time.sleep(self.attack_speed)
            if not self.is_alive():
                return
            elif not target.is_alive():
                return
            new_damage = self.calculate_damage()
            if not self.can_attack_unit(target):
                print(f"{self.name} can't attack {target.name}.")
                return
            self.total_damage = round((self.damage + new_damage) * self.dmgmult * (1 - target.damage_reduction))
            target.health -= self.total_damage
            print(f"{self.name} does {self.total_damage} damage, leaving {target.name} with {target.health} health.")

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def fight(self,target):
        while self.is_alive() and target.is_alive():
            self.attack_unit(target,new_damage=self.calculate_damage())
            if not target.is_alive():
                print(f"{self.name} has won with {self.health} left.")
            else:
                target.attack_unit(self,new_damage=target.calculate_damage())
                if not self.is_alive():
                    print(f"{target.name} has won with {target.health} left.")