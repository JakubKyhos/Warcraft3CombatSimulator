from wariorclass import Warior
import time
import random

class Hybrid(Warior):
    def __init__(self, name, health, damage, second_damage, damage_type, second_damage_type, armor, armor_type, attack_speed, second_attack_speed, dice_sides, second_dice_sides,
                 weapon_upgrade=None, armor_upgrade=None,
                 can_attack_ground=False, can_attack_air=False, air_unit=False):
        super().__init__(name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides, weapon_upgrade, armor_upgrade, can_attack_ground, can_attack_air, air_unit)
        self.second_damage = second_damage
        self.second_damage_type = second_damage_type
        self.second_attack_speed = second_attack_speed
        self.second_dice_sides = second_dice_sides