from wariorclass import Warior

class Hybrid(Warior):
    def __init__(self, name, health, damage, second_damage, damage_type, second_damage_type, armor, armor_type, attack_speed, second_attack_speed, dice_rolls, second_dice_rolls, dice_sides, second_dice_sides, unit_type, valid_targets):
        super().__init__(name, health, damage, damage_type, armor, armor_type, attack_speed, dice_rolls, dice_sides, unit_type, valid_targets)
        self.second_damage = second_damage
        self.second_damage_type = second_damage_type
        self.second_attack_speed = second_attack_speed
        self.second_dice_rolls = second_dice_rolls
        self.second_dice_sides = second_dice_sides

    def enemy_is_air_unit(self, target):
        if target.unit_type == "air":
            self.damage = self.second_damage
            self.damage_type = self.second_damage_type
            self.attack_speed = self.second_attack_speed
            self.dice_rolls = self.second_dice_rolls
            self.dice_sides = self.second_dice_sides

class Flying_Machine(Hybrid):
    def __init__(self, name, health, damage, second_damage, damage_type, second_damage_type, armor, armor_type, attack_speed, second_attack_speed, dice_rolls, second_dice_rolls, dice_sides, second_dice_sides, unit_type, valid_targets):
        super().__init__(name, health, damage, second_damage, damage_type, second_damage_type, armor, armor_type, attack_speed, second_attack_speed, dice_rolls, second_dice_rolls, dice_sides, second_dice_sides, unit_type, valid_targets)

    def upgrades(self):
        self.armor_update()
        self.get_dice_rolls()
        self.Flying_Machine_Bombs_upgrade()

    def Flying_Machine_Bombs_upgrade(self):
        upgrade = input(f"Do you want flying machine bombs upgrade for {self.name}? [y/n] --> ")

        if upgrade == "y":
            self.valid_targets.extend(["melee","range"])
        else:
            return
        
class Siege_Engine(Hybrid):
    def __init__(self, name, health, damage, second_damage, damage_type, second_damage_type, armor, armor_type, attack_speed, second_attack_speed, dice_rolls, second_dice_rolls, dice_sides, second_dice_sides, unit_type, valid_targets):
        super().__init__(name, health, damage, second_damage, damage_type, second_damage_type, armor, armor_type, attack_speed, second_attack_speed, dice_rolls, second_dice_rolls, dice_sides, second_dice_sides, unit_type, valid_targets)

    def upgrades(self):
        self.armor_update()
        self.get_dice_rolls()
        self.Barrage_upgrade()

    def Barrage_upgrade(self):
        upgrade = input(f"Do you want Barrage upgrade for {self.name}? [y/n] --> ")

        if upgrade == "y":
            self.valid_targets.append("air")
        else:
            return
        
class Gryphon_rider(Hybrid):
    def __init__(self, name, health, damage, second_damage, damage_type, second_damage_type, armor, armor_type, attack_speed, second_attack_speed, dice_rolls, second_dice_rolls, dice_sides, second_dice_sides, unit_type, valid_targets):
        super().__init__(name, health, damage, second_damage, damage_type, second_damage_type, armor, armor_type, attack_speed, second_attack_speed, dice_rolls, second_dice_rolls, dice_sides, second_dice_sides, unit_type, valid_targets)

    def upgrades(self):
        self.armor_update()
        self.get_dice_rolls()
        self.Animal_War_Training_upgrade()

class Mountain_Giant(Hybrid):
    def __init__(self, name, health, damage, second_damage, damage_type, second_damage_type, armor, armor_type, attack_speed, second_attack_speed, dice_rolls, second_dice_rolls, dice_sides, second_dice_sides, unit_type, valid_targets):
        super().__init__(name, health, damage, second_damage, damage_type, second_damage_type, armor, armor_type, attack_speed, second_attack_speed, dice_rolls, second_dice_rolls, dice_sides, second_dice_sides, unit_type, valid_targets)

    def enemy_is_air_unit(self, target):
        pass

    def upgrades(self):
        self.armor_update()
        self.War_Club()
        self.get_dice_rolls()

    def War_Club(self):
        upgrade = input(f"Do you want {self.name} to use War Club? [y/n] --> ")

        if upgrade == "y":
            self.damage = self.second_damage
            self.damage_type = self.second_damage_type
            self.attack_speed = self.second_attack_speed
            self.dice_rolls = self.second_dice_rolls
            self.dice_sides = self.second_dice_sides
        elif upgrade == "n":
            return
        else:
            print("Invalid input for War Club. Choose from: [y/n].")
            self.War_Club()


    def Hardened_Skin(self, total_damage):
        total_damage -= 8
        return 3 if total_damage < 3 else total_damage