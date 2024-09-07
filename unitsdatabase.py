from unitclass import Unit, Kodo_Beast, Dire_Wolf, Treant
from siegeclass import Siege
from mageclass import Mage, SpiritWalker, DruidOfTheClaw
from wariorclass import Warior, Mortar_team, Dragonhawk_Rider, Knight, Grunt, Archer, Ghoul
from hybridclass import Hybrid, Flying_Machine, Siege_Engine, Gryphon_rider, Mountain_Giant

units = {
    "peasant":Unit("Peasant",240,4,"normal",0,"medium",2.0,1,2,"melee",["melee","range"]),
    "footman":Warior("Footman",420,11,"normal",2,"heavy",1.35,1,2,"melee",["melee","range"]),
    "rifleman":Warior("Rifleman",535,16,"piercing",0,"medium",1.35,2,4,"range",["melee","range","air"]),
    "priest":Mage("Priest",290,7,"magic",0,"unarmored",2.0,1,2,"range",["melee","range","air"]),
    "sorceress":Mage("Sorceress",325,9,"magic",0,"unarmored",1.75,1,3,"range",["melee","range","air"]),
    "spellbreaker":Warior("Spell Breaker",600,12,"normal",3,"medium",1.9,1,3,"range",["melee","range"]),
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
    "militia":Warior("Militia",240,11,"normal",4,"heavy",1.2,1,2,"melee",["melee","range"]),
    
}

units2 = {
    "peasant":Unit("Peasant",240,4,"normal",0,"medium",2.0,1,2,"melee",["melee","range"]),
    "footman":Warior("Footman",420,11,"normal",2,"heavy",1.35,1,2,"melee",["melee","range"]),
    "rifleman":Warior("Rifleman",535,16,"piercing",0,"medium",1.35,2,4,"range",["melee","range","air"]),
    "priest":Mage("Priest",290,7,"magic",0,"unarmored",2.0,1,2,"range",["melee","range","air"]),
    "sorceress":Mage("Sorceress",325,9,"magic",0,"unarmored",1.75,1,3,"range",["melee","range","air"]),
    "spellbreaker":Warior("Spell Breaker",600,12,"normal",3,"medium",1.9,1,3,"range",["melee","range"]),
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
    "militia":Warior("Militia",240,11,"normal",4,"heavy",1.2,1,2,"melee",["melee","range"]),
    
}