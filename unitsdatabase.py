import copy
from unitclass import Unit, Kodo_Beast, Dire_Wolf, Treant
from mageclass import Mage, SpiritWalker, DruidOfTheClaw
from wariorclass import Warrior, Siege, Mortar_team, Dragonhawk_Rider, Knight, Grunt, Archer, Ghoul, Mountain_Giant, Crypt_Fiend
from hybridclass import Hybrid, Flying_Machine, Siege_Engine, Gryphon_rider

#Spell Breaker and Huntress are classified as melee because their attack range seems so small, that siege units can't attack them.
#The reason behind this big dict of units is that I couldn't find a way to get unit data from the game itself and there wasn't a webpage that would list all the stats. Namely: dice_rolls, dice_sides.
#stormcrowm has druid of the talon master training increasing its healt by 40.
#If I try to have a mirror match like footman vs footman they will share upgrades I give them. 
# Example: Footman1 gets basic upgrades and footman2 gets expert upgrades. They will both end up with basic and expert upgrades.
# Same probably goes for other upgrades and updates.
# That is why I created a deepcopy of units1.

units1 = {
    "peasant":Unit("Peasant",240,4,"normal",0,"medium",2.0,1,2,"melee",["melee","range"]),
    "footman":Warrior("Footman",420,11,"normal",2,"heavy",1.35,1,2,"melee",["melee","range"]),
    "rifleman":Warrior("Rifleman",535,16,"piercing",0,"medium",1.35,2,4,"range",["melee","range","air"]),
    "priest":Mage("Priest",290,7,"magic",0,"unarmored",2.0,1,2,"range",["melee","range","air"]),
    "sorceress":Mage("Sorceress",325,9,"magic",0,"unarmored",1.75,1,3,"range",["melee","range","air"]),
    "spellbreaker":Warrior("Spell Breaker",600,12,"normal",3,"medium",1.9,1,3,"melee",["melee","range"]),
    "flyingmachine":Flying_Machine("Flying Machine",250,6,17,"siege","piercing",2,"heavy",2.5,2.0,1,1,2,2,"air",["air"]),
    "mortarteam":Mortar_team("Mortar Team",360,51,"siege",0,"heavy",3.5,1,13,"range",["range"]),
    "dragonhawkrider":Dragonhawk_Rider("Dragonhawk Rider",625,19,"piercing",1,"light",1.75,1,3,"air",["melee","range","air"]),
    "knight":Knight("Knight",885,28,"normal",5,"heavy",1.4,2,5,"melee",["melee","range"]),
    "siegeengine":Siege_Engine("Siege Engine",700,44,16,"siege","piercing",2,"fortified",2.1,2.0,1,1,11,2,"melle",[]),
    "gryphonrider":Gryphon_rider("Gryphon Rider",875,44,44,"magic","magic",0,"light",2.2,2.4,1,1,11,11,"air",["melee","range","air"]),
    "waterelemental1":Unit("Water Elemental 1",500,18,"piercing",0,"heavy",1.5,1,5,"range",["melee","range","air"]),
    "waterelemental2":Unit("Water Elemental 2",625,31,"piercing",1,"heavy",1.5,2,5,"range",["melee","range","air"]),
    "waterelemental3":Unit("Water Elemental 3",825,42,"piercing",2,"heavy",1.5,2,5,"range",["melee","range","air"]),
    "phoenix":Unit("Phoenix",1250,60,"magic",1,"light",1.4,1,15,"air",["melee","range","air"]),
    "militia":Warrior("Militia",240,11,"normal",4,"heavy",1.2,1,2,"melee",["melee","range"]),
    "peon":Unit("Peon",250,6,"normal",0,"medium",3.0,1,2,"melee",["melee","range"]),
    "grunt":Grunt("Grunt",700,17,"normal",1,"heavy",1.6,1,4,"melee",["melee","range"]),
    "trollheadhunter":Warrior("Troll Headhunter",375,22,"piercing",0,"medium",2.31,1,5,"range",["melee","range","air"]),
    "demolisher":Warrior("Demolisher",425,71,"siege",2,"heavy",4.5,1,18,"range",["range"]),
    "shaman":Mage("Shaman",350,9,"magic",0,"unarmored",2.1,1,2,"range",["melee","range","air"]),
    "trollwitchdoctor":Mage("Troll Witch Doctor",315,9,"magic",0,"unarmored",1.75,1,5,"range",["melee","range","air"]),
    "raider":Warrior("Raider",610,22,"siege",1,"medium",1.85,1,5,"melee",["melee","range","air"]),
    "windrider":Warrior("Wind Rider",570,34,"piercing",0,"light",2.0,2,5,"air",["melee","range","air"]),
    "kodobeast":Kodo_Beast("Kodo Beast",1000,15,"piercing",1,"unarmored",1.44,1,5,"range",["melee","range","air"]),
    "trollbatrider":Warrior("Troll Batrider",325,15,"siege",0,"light",1.8,1,3,"air",["melee","range","air"]),
    "spiritwalker":SpiritWalker("Spirit Walker",500,16,"magic",0,"unarmored",1.75,1,6,"range",["melee","range","air"]),
    "tauren":Warrior("Tauren",1300,29,"normal",3,"heavy",1.9,1,7,"melee",["melee","range"]),
    "spiritwolf":Unit("Spirit Wolf",250,10,"normal",0,"heavy",1.0,1,2,"melee",["melee","range"]),
    "direwolf":Dire_Wolf("Dire Wolf", 350,15,"normal",0,"heavy",1.0,1,2,"melee",["melee","range"]),
    "shadowwolf":Dire_Wolf("Shadow Wolf",500,20,"normal",0,"heavy",1.0,1,2,"melee",["melee","range"]),
    "serpentward1":Unit("Serpent Ward 1",90,13,"piercing",0,"heavy",1.5,1,3,"range",["melee","range","air"]),
    "serpentward2":Unit("Serpent Ward 2",165,26,"piercing",0,"heavy",1.5,1,4,"range",["melee","range","air"]),
    "serpentward3":Unit("Serpent Ward 3",200,45,"piercing",0,"heavy",1.5,1,5,"range",["melee","range","air"]),
    "trollberserker":Warrior("Troll Berserker",475,22,"piercing",0,"medium",2.31,1,5,"range",["melee","range","air"]),
    "wisp":Unit("Wisp",125,0,"normal",0,"medium",0.0,0,0,"melee",[]),
    "archer":Archer("Archer",255,15,"piercing",0,"medium",1.5,1,3,"range",["melee","range","air"]),
    "huntress":Warrior("Huntress",600,15,"normal",2,"unarmored",1.8,1,3,"melee",["melee","range"]),
    "glaivethrower":Siege("Glaive Thrower",300,44,"siege",2,"heavy",3.5,1,18,"range",["range"]),
    "hippogryph":Warrior("Hyppogryphe",525,49,"normal",0,"unarmored",1.05,1,8,"air",["air"]),
    "druidofthetalon":Mage("Druid of the Talon",300,10,"magic",0,"unarmored",1.6,1,3,"range",["melee","range","air"]),
    "faeriedragon":Warrior("Faerie Dragon",450,12,"piercing",0,"light",1.75,1,3,"air",["melee","range","air"]),
    "dryad":Warrior("Dryad",435,16,"piercing",0,"unarmored",2.0,1,3,"range",["melee","range","air"]),
    "druidoftheclaw":DruidOfTheClaw("Druid of the Claw",430,18,"normal",1,"heavy",1.5,1,4,"melee",["melee","range"]),
    "mountaingiant":Mountain_Giant("Mountain Giant",1600,26,"normal",6,"medium",2.5,2,7,"melee",["melee","range"]),
    "chimaera":Warrior("Chimaera",1000,66,"magic",2,"light",2.5,1,17,"air",["melee","range"]),
    "hippogryphrider":Archer("Hippogryph Rider",780,15,"piercing",1,"light",1.1,1,3,"air",["melee","range","air"]),
    "stormcrow":Warrior("Storm Crow",340,26,"pierce",0,"unarmored",1.75,1,7,"air",["air"]),
    "stormcrowm":Warrior("Storm Crow M",380,26,"pierce",0,"unarmored",1.75,1,7,"air",["air"]),
    "dotcbear":Warrior("DotC Bear",960,25,"normal",3,"heavy",1.5,3,6,"melee",["melee","range"]),
    "treant":Treant("Treant",300,14,"normal",0,"heavy",1.75,1,3,"melee",["melee","range"]),
    "avatarofvengeance":Unit("Avatar of Vengeance",1200,24,"normal",2,"heavy",1.35,1,12,"range",["melee","range","air"]),
    "acolyte":Unit("Acolyte",230,8,"normal",1,"medium",2.5,1,2,"melee",["melee","range"]),
    "ghoul":Ghoul("Ghoul",340,10,"normal",0,"heavy",1.3,2,2,"melee",["melee","range"]),
    "cryptfiend":Crypt_Fiend("Crypt Fiend",550,25,"piercing",0,"medium",2.0,1,6,"range",["melee","range"]),
    "gargoyle":Hybrid("Gargoyle",410,17,60,"piercing","normal",3,"unarmored",2.2,1.4,1,1,4,10,"air",["melee","range","air"]),
    "necromancer":Mage("Necromancer",315,9,"magic",0,"unarmored",1.8,1,2,"range",["melee","range","air"]),
    "banshee":Mage("Banshee",285,8,"magic",0,"unarmored",1.5,1,5,"range",["melee","range","air"]),
    "meatwagon":Siege("Meat Wagon",380,70,"siege",2,"heavy",4.0,1,18,"range",["range"]),
    "obsidianstatue":Unit("Obsidian Statue",500,6,"magic",4,"heavy",2.1,1,2,"range",["melee","range","air"]),
    "abomination":Warrior("Abomination",1175,34,"normal",2,"heavy",1.9,1,7,"melee",["melee","range"]),
    "frostwyrm":Hybrid("Frost Wyrm",1350,91,83,"magic","magic",1,"light",3.0,3.0,2,1,12,11,"air",["melee","range","air"]),
    "skeletonwarrior":Warrior("Skeleton Warrior",180,13,"normal",1,"heavy",2.0,1,2,"melee",["melee","range","air"]),
    "skeletalmage":Warrior("Skeletal Mage",240,10,"piercing",0,"medium",1.5,1,2,"range",["melee","range","air"]),
    "carrionbeetle1":Unit("Carrion Beetle 1",170,7,"normal",2,"heavy",1.5,1,2,"melee",["melee","range"]),
    "carrionbeetle2":Unit("Carrion Beetle 2",300,14,"normal",2,"heavy",1.5,1,4,"melee",["melee","range"]),
    "carrionbeetle3":Unit("Carrion Beetle 3",440,21,"normal",2,"heavy",1.5,1,6,"melee",["melee","range"]),
    "shade":Unit("Shade",125,0,"normal",0,"medium",0.0,0,0,"melee",[]),
    "destroyer":Warrior("Destroyer",850,18,"magic",3,"light",1.35,1,3,"air",["melee","range","air"])
}

units2 = copy.deepcopy(units1)