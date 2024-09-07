import threading
import sys
import os
from unitclass import Kodo_Beast
from hybridclass import Hybrid
from wariorclass import Mortar_team, Knight
from unitsdatabase import units, units2


def main():
    print("\nAvailable units:")
    for key in units.keys():
        print(f"- {key}")
        
    unit1_name = input("Choose the first unit (or 'quit' to exit): ").lower()
    if unit1_name == 'quit':
        sys.exit("You chose to quit.")
        
    unit2_name = input("Choose the second unit (or 'quit' to exit): ").lower()
    if unit2_name == 'quit':
        sys.exit("You chose to quit.")
        
    if unit1_name not in units or unit2_name not in units2:
        print("Invalid unit name(s). Please try again.")
        main()
        
    unit1 = units[unit1_name]
    unit2 = units2[unit2_name]
    os.system("clear")
    unit1.upgrades()
    unit2.upgrades()

    if isinstance(unit1,Hybrid):
        unit1.enemy_is_air_unit(unit2)
    if isinstance(unit2,Hybrid):
        unit2.enemy_is_air_unit(unit1)

    if isinstance(unit1,Mortar_team):
        unit1.Fragmentation_Shards_upgrade(unit2)
    if isinstance(unit2,Mortar_team):
        unit2.Fragmentation_Shards_upgrade(unit1)

    unit1.update_damage_multiplier(unit2)
    unit2.update_damage_multiplier(unit1)

    if isinstance(unit1,Knight):
        unit1.Sundering_Blades_upgarde(unit2)
    if isinstance(unit2,Knight):
        unit2.Sundering_Blades_upgarde(unit1)

    if isinstance(unit1,Kodo_Beast):
        unit1.War_Drums_upgrade()
    if isinstance(unit2,Kodo_Beast):
        unit2.War_Drums_upgrade()

    unit1.calculate_damage_reduction()
    unit2.calculate_damage_reduction()

    t1 = threading.Thread(target=unit1.attack_unit, args=(unit2,))
    t2 = threading.Thread(target=unit2.attack_unit, args=(unit1,))

    os.system("clear")

    print("Combat begins!!!")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    os.system("clear")

    if not unit1.is_alive():
            print(f"{unit2.name} has won with {unit2.health} health.")
    if not unit2.is_alive():
        print(f"{unit1.name} has won with {unit1.health} health.")


    print(f"{unit1.name} has {unit1.damage} damage, {unit1.damage_type} type, {unit1.dmgmult} multyplier, {unit1.attack_speed} speed, {unit1.dice_rolls} dice rolls, {unit1.armor} armor.")
    print(f"{unit2.name} has {unit2.damage} damage, {unit2.damage_type} type, {unit2.dmgmult} multyplier, {unit2.attack_speed} speed, {unit2.dice_rolls} dice rolls, {unit2.armor} armor.")

    print("Thanks for playing!")

if __name__ == "__main__":
    main()