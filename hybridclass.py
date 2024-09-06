from wariorclass import Warior
import time
import random

class Hybrid(Warior):
    def __init__(self, name, health, damage, second_damage, damage_type, second_damage_type, armor, armor_type, attack_speed, second_attack_speed, dice_sides, second_dice_sides, unit_type, valid_targets):
        super().__init__(name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides, unit_type, valid_targets)
        self.second_damage = second_damage
        self.second_damage_type = second_damage_type
        self.second_attack_speed = second_attack_speed
        self.second_dice_sides = second_dice_sides

    def enemy_is_air_unit(self, target):
        if target.unit_type == "air":
            self.damage = self.second_damage
            self.damage_type = self.second_damage_type
            self.attack_speed = self.second_attack_speed
            self.dice_sides = self.second_dice_sides
            self.update_damage_multiplier(target)
            self.calculate_damage_reduction()

class Flying_Machine(Hybrid):
    def __init__(self, name, health, damage, second_damage, damage_type, second_damage_type, armor, armor_type, attack_speed, second_attack_speed, dice_sides, second_dice_sides, unit_type, valid_targets):
        super().__init__(name, health, damage, second_damage, damage_type, second_damage_type, armor, armor_type, attack_speed, second_attack_speed, dice_sides, second_dice_sides, unit_type, valid_targets)
        self.Flying_Machine_Bombs_upgrade()

    def Flying_Machine_Bombs_upgrade(self):
        upgrade = input(f"Do you want flying machine bombs upgrade for {self.name}? [y/n] --> ")

        if upgrade == "y":
            self.valid_targets.extend(["melee","range"])
        else:
            return
        
class Siege_Engine(Hybrid):
    def __init__(self, name, health, damage, second_damage, damage_type, second_damage_type, armor, armor_type, attack_speed, second_attack_speed, dice_sides, second_dice_sides, unit_type, valid_targets):
        super().__init__(name, health, damage, second_damage, damage_type, second_damage_type, armor, armor_type, attack_speed, second_attack_speed, dice_sides, second_dice_sides, unit_type, valid_targets)
        self.Barrage_upgrade()

    def Barrage_upgrade(self):
        upgrade = input(f"Do you want Barrage upgrade for {self.name}? [y/n] --> ")

        if upgrade == "y":
            self.valid_targets.append("air")
        else:
            return
        
class Gryphon_rider(Hybrid):
    def __init__(self, name, health, damage, second_damage, damage_type, second_damage_type, armor, armor_type, attack_speed, second_attack_speed, dice_sides, second_dice_sides, unit_type, valid_targets):
        super().__init__(name, health, damage, second_damage, damage_type, second_damage_type, armor, armor_type, attack_speed, second_attack_speed, dice_sides, second_dice_sides, unit_type, valid_targets)
        self.Animal_War_Training_upgrade()

    def Animal_War_Training_upgrade(self):
        upgrade = input(f"Do you want Animal War Training upgrade for {self.name}? [y/n] --> ")

        if upgrade == "y":
            self.health += 100
        elif upgrade == "n":
            return
        else:
            print("Invalid input for Animal War Training upgrade. Choose from: [y/n].")
            self.Animal_War_Training_upgrade()