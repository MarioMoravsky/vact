attacks = {
    # normal attacks
    "tackle": {
        "name": "Tackle",
        "factor": 3/2,
        "action": "",
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.2,
        "min_lvl": 0,
        "desc": "Tackles the enemy very hard.",
        "type": "normal",
        "effect": None,
        "is_generic": True,
        "ap": 30,
    },
    "cry": {
        "name": "Cry",
        "factor": 0,
        "action": "enem.miss_chance += 1",
        "world_action": "",
        "move": ["downgrade"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "So loud, it confuses the enemy.",
        "type": "normal",
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
    "bite": {
        "name": "Bite",
        "factor": 1.75,
        "action": "",
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.1,
        "min_lvl": 0,
        "desc": "A hard bite the sharp teeth.",
        "type": "normal",
        "effect": None,
        "is_generic": False,
        "ap": 30,
    },
    "power_bite": {
        "name": "Power bite",
        "factor": 8,
        "action": "",
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.1,
        "min_lvl": 30,
        "desc": "The hardest bite you can think of.",
        "type": "normal",
        "effect": None,
        "is_generic": False,
        "ap": 5,
    },
    "chocer": {
        "name": "Choker",
        "factor": 1,
        "action": "enem.atc -= 1",
        "world_action": "",
        "move": ["attack", "downgrade"],
        "miss_chance": 0.2,
        "min_lvl": 0,
        "desc": "Chokes the enemy and makes it weaker.",
        "type": "normal",
        "effect": "EffectParalyzation",
        "is_generic": False,
        "ap": 15,
    }, 
    "tail_wipe": {
        "name": "Tail wipe",
        "factor": 2.5,
        "action": "",
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.5,
        "min_lvl": 10,
        "desc": "Wipes through the enemy's face.",
        "type": "normal",
        "effect": None,
        "is_generic": False,
        "ap": 10,
    },
    "meat_skewer": {
        "name": "Meat skewer",
        "factor": 3.5,
        "action": "",
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.7,
        "min_lvl": 0,
        "desc": "Drills the horn deep in the enemy's flesh.",
        "type": "normal",
        "effect": None,
        "is_generic": False,
        "ap": 10,
    },
    "snooze": {
        "name": "Snooze",
        "factor": 0,
        "action": "enem.miss_chance += 0.5; enem.atc -= 1; enem.defense -= 1",
        "world_action": "",
        "move": ["downgrade"],
        "miss_chance": 0.2,
        "min_lvl": 15,
        "desc": "Makes the enemy sleepy.",
        "type": "normal",
        "effect": "EffectSleep",
        "is_generic": False,
        "ap": 15,
    },
    # poison attacks
    "poison_bite": {
        "name": "Poison bite",
        "factor": 1,
        "action": "",
        "world_action": "",
        "move": ["attack", "downgrade"],
        "miss_chance": 0.3,
        "min_lvl": 0,
        "desc": "Makes the enemy weaker.",
        "type": "poison",
        "effect": "EffectPoison",
        "is_generic": False,
        "ap": 10,
    },
    # stone attacks
    "pepple_fire": {
        "name": "Pepple fire",
        "factor": 1,
        "action": "enem.miss_chance += 1",
        "world_action": "",
        "move": ["attack", "downgrade"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Fires pepples at the enemy and makes it blind.",
        "type": "stone",
        "effect": None,
        "is_generic": True,
        "ap": 5,
    },
    "politure": {
        "name": "Politure",
        "factor": 0,
        "action": "self.defense += 1; self.atc += 1",
        "world_action": "",
        "move": ["shine"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Upgrades defense and attack points.",
        "type": "stone",
        "effect": None,
        "is_generic": True,
        "ap": 15,
    },
    "brick_throw": {
        "name": "Brick throw",
        "factor": 2,
        "action": "",
        "world_action": "",
        "move": ["throw"],
        "miss_chance": 0.3,
        "min_lvl": 15,
        "desc": "Throws an euler brick at the enemy.",
        "type": "stone",
        "effect": None,
        "is_generic": True,
        "ap": 20,
    },
    "rock_smash": {
        "name": "Rock smash",
        "factor": 5,
        "action": "",
        "world_action": "",
        "move": ["pound"],
        "miss_chance": 0.1,
        "min_lvl": 15,
        "desc": "Pounds the enemy with the Poketes full weight.",
        "type": "stone",
        "effect": None,
        "is_generic": True,
        "ap": 5,
    },
    "dia_stab": {
        "name": "Dia stab",
        "factor": 5,
        "action": "",
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.1,
        "min_lvl": 15,
        "desc": "Stabs the enemy with an giant diamond spike.",
        "type": "stone",
        "effect": None,
        "is_generic": False,
        "ap": 5,
    },
    "dazzle": {
        "name": "Dazzle",
        "factor": 1.5,
        "action": "",
        "world_action": "",
        "move": ["attack", "downgrade"],
        "miss_chance": 0.2,
        "min_lvl": 10,
        "desc": "Shines a bright light at the enemy and dazzles them.",
        "type": "stone",
        "effect": "EffectParalyzation",
        "is_generic": False,
        "ap": 20,
    },
    "dia_spikes": {
        "name": "Dia spikes",
        "factor": 2,
        "action": "",
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0,
        "min_lvl": 20,
        "desc": "Throws a heck lot of diamond spikes at the enemy.",
        "type": "stone",
        "effect": None,
        "is_generic": False,
        "ap": 20,
    },

    # ground attacks
    "earch_quake": {
        "name": "Earch quake",
        "factor": 4,
        "action": "",
        "world_action": "",
        "move": ["pound"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Brings the earth to shift.",
        "type": "ground",
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
    "power_roll": {
        "name": "Power roll",
        "factor": 2.5,
        "action": "",
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.2,
        "min_lvl": 0,
        "desc": "Rolls over the enemy.",
        "type": "ground",
        "effect": None,
        "is_generic": True,
        "ap": 15,
    },
    "toe_breaker": {
        "name": "Toe Breaker",
        "factor": 2.5,
        "action": "",
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.3,
        "min_lvl": 0,
        "desc": "Breaks the enemys toes.",
        "type": "ground",
        "effect": None,
        "is_generic": True,
        "ap": 20,
    },
     "ground_hit": {
        "name": "Ground hit",
        "factor": 3,
        "action": "",
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.1,
        "min_lvl": 0,
        "desc": "Damages the enemy with an unpredictable hit out of the ground.",
        "type": "ground",
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
     "dick_energy": {
        "name": "Dick energy",
        "factor": 0,
        "action": "self.atc += 2",
        "world_action": "",
        "move": ["shine"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Collects a great amount of energy in the Poketes tip.",
        "type": "ground",
        "effect": None,
        "is_generic": False,
        "ap": 15,
    },
     "hiding": {
        "name": "Hiding",
        "factor": 0,
        "action": "self.defense += 2",
        "world_action": "",
        "move": ["shine"],
        "miss_chance": 0,
        "min_lvl": 20,
        "desc": "Makes the Pokete hide under the ground to minimize damage.",
        "type": "ground",
        "effect": None,
        "is_generic": False,
        "ap": 15,
    },

    # Fire attacks
    "fire_bite": {
        "name": "Fire bite",
        "factor": 2,
        "action": "",
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.2,
        "min_lvl": 0,
        "desc": "Burns and bites the enemy at the same time.",
        "type": "fire",
        "effect": "EffectBurning",
        "is_generic": True,
        "ap": 15,
    },
    "ash_throw": {
        "name": "Ash throw",
        "factor": 0.5,
        "action": "enem.miss_chance += 1",
        "world_action": "",
        "move": ["attack", "downgrade"],
        "miss_chance": 0,
        "min_lvl": 15,
        "desc": "Throws ashes in the enemy's eyes.",
        "type": "fire",
        "effect": None,
        "is_generic": True,
        "ap": 15,
    },
    "flame_throw": {
        "name": "Flame throw",
        "factor": 2.5,
        "action": "",
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0,
        "min_lvl": 15,
        "desc": "Hans get ze Flammenwerfer!",
        "type": "fire",
        "effect": "EffectBurning",
        "is_generic": True,
        "ap": 10,
    },

    "fire_ball": {
        "name": "Fire ball",
        "factor": 4,
        "action": "",
        "world_action": "",
        "move": ["fireball"],
        "miss_chance": 0,
        "min_lvl": 25,
        "desc": "Casts a fireball at the enemy.",
        "type": "fire",
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
    # flying attacks
     "flying": {
        "name": "Flying",
        "factor": 1.5,
        "action": "",
        "world_action": "teleport()",
        "move": ["attack"],
        "miss_chance": 0.1,
        "min_lvl": 0,
        "desc": "Gives the Pokete the abbility to fly you around.",
        "type": "flying",
        "effect": None,
        "is_generic": False,
        "ap": 30,
    },
    "pick": {
        "name": "Pick",
        "factor": 1.7,
        "action": "",
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.1,
        "min_lvl": 0,
        "desc": "A pick at the enemy's weakest spot.",
        "type": "flying",
        "effect": None,
        "is_generic": True,
        "ap": 30,
    },
    "wind_blow": {
        "name": "Wind blow",
        "factor": 2,
        "action": "",
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Casts a wind blow at the enemy.",
        "type": "flying",
        "effect": None,
        "is_generic": True,
        "ap": 20,
    },
    "storm_gust": {
        "name": "Storm gust",
        "factor": 6,
        "action": "",
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Casts a strong and fast storm gust full of rain and hail that hits the enemy at it's weakest spots and makes it wanting to die.",
        "type": "flying",
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
    "schmetter": {
        "name": "Schmetter",
        "factor": 1.7,
        "action": "",
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.1,
        "min_lvl": 0,
        "desc": "Schmetters the enemy away.",
        "type": "flying",
        "effect": None,
        "is_generic": False,
        "ap": 30,
    },
    "eye_pick": {
        "name": "Eye pick",
        "factor": 2.5,
        "action": "enem.miss_chance += 2",
        "world_action": "",
        "move": ["attack", "downgrade"],
        "miss_chance": 0.6,
        "min_lvl": 0,
        "desc": "Picks out one of the enemy's eyes.",
        "type": "flying",
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
    "wing_hit": {
        "name": "Wing hit",
        "factor": 2.5,
        "action": "",
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.5,
        "min_lvl": 0,
        "desc": "Hits the enemy with a wing.",
        "type": "flying",
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
    "brooding": {
        "name": "Brooding",
        "factor": 0,
        "action": "self.hp += 2 if self.hp+2 <= self.full_hp else 0",
        "world_action": "",
        "move": ["shine"],
        "miss_chance": 0,
        "min_lvl": 15,
        "desc": "Regenerates 2 HP.",
        "type": "flying",
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
    "power_pick": {
        "name": "Power pick",
        "factor": 2,
        "action": "",
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.4,
        "min_lvl": 0,
        "desc": "A harsh picking on the enemy's head.",
        "type": "flying",
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
    # water attacks
    "bubble_gun": {
        "name": "Bubble gun",
        "factor": 2,
        "action": "",
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.2,
        "min_lvl": 0,
        "desc": "Fires some bubbles at the enemy.",
        "type": "water",
        "effect": None,
        "is_generic": True,
        "ap": 20,
    },
    "bubble_bomb": {
        "name": "Bubble bomb",
        "factor": 6,
        "action": "enem.miss_chance += 1",
        "world_action": "",
        "move": ["attack", "downgrade"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "A deadly bubble.",
        "type": "water",
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
    "bubble_shield": {
        "name": "Bubble shield",
        "factor": 0,
        "action": "self.defense += 2",
        "world_action": "",
        "move": ["shine"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Creates a giant bubble that protects the Pokete.",
        "type": "water",
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
    "wet_slap": {
        "name": "Wet slap",
        "factor": 2.5,
        "action": "",
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.1,
        "min_lvl": 10,
        "desc": "Gives the enemy a wet and cold slap in the face.",
        "type": "water",
        "effect": None,
        "is_generic": True,
        "ap": 15,
    },
    "shell_pinch": {
        "name": "Shell pinch",
        "factor": 2.5,
        "action": "",
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.1,
        "min_lvl": 15,
        "desc": "Pinches the enemy with its strong shells.",
        "type": "water",
        "effect": None,
        "is_generic": False,
        "ap": 20,
    },
    # undead attacks
    "heart_touch": {
        "name": "Heart touch",
        "factor": 4,
        "action": "enem.defense -= 4",
        "world_action": "",
        "move": ["attack", "downgrade"],
        "miss_chance": 0,
        "min_lvl": 20,
        "desc": "Touches the enemy's heard with its' cold ghost claws.",
        "type": "undead",
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
    "confusion": {
        "name": "Confusion",
        "factor": 0,
        "action": "",
        "world_action": "",
        "move": ["downgrade"],
        "miss_chance": 0.2,
        "min_lvl": 0,
        "desc": "Confuses the enemy.",
        "type": "undead",
        "effect": "EffectConfusion",
        "is_generic": True,
        "ap": 40,
    },
    "mind_blow": {
        "name": "Mind blow",
        "factor": 0,
        "action": "",
        "world_action": "",
        "move": ["downgrade"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Causes confusion deep in the enemy's mind.",
        "type": "undead",
        "effect": "EffectConfusion",
        "is_generic": True,
        "ap": 15,
    },
    # electro attacks
    "shock": {
        "name": "Shock",
        "factor": 3/2,
        "action": "",
        "world_action": "",
        "move": ["arch"],
        "miss_chance": 0.2,
        "min_lvl": 0,
        "desc": "Gives the enemy a shock.",
        "type": "electro",
        "effect": None,
        "is_generic": True,
        "ap": 30,
    },
    "charging": {
        "name": "Charging",
        "factor": 0,
        "action": "self.atc += 2",
        "world_action": "",
        "move": ["shine"],
        "miss_chance": 0,
        "min_lvl": 10,
        "desc": "Charges the Pokete.",
        "type": "electro",
        "effect": None,
        "is_generic": True,
        "ap": 15,
    },
    "mega_arch": {
        "name": "Mega arch",
        "factor": 5,
        "action": "",
        "world_action": "",
        "move": ["arch"],
        "miss_chance": 0,
        "min_lvl": 15,
        "desc": "Gives the enemy heavy a shock.",
        "type": "electro",
        "effect": "EffectParalyzation",
        "is_generic": True,
        "ap": 10,
    },
    # plant attacks
    "apple_drop": {
        "name": "Apple drop",
        "factor": 1.7,
        "action": "",
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.3,
        "min_lvl": 0,
        "desc": "Lets an apple drop on the enemy's head.",
        "type": "plant",
        "effect": None,
        "is_generic": False,
        "ap": 30,
    },
    "super_sucker": {
        "name": "Super sucker",
        "factor": 0,
        "action": "enem.hp -=2; self.hp +=2 if self.hp+2 <= self.full_hp else 0",
        "world_action": "",
        "move": ["downgrade", "shine"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Sucks 2 HP from the enemy and adds it to it's own.",
        "type": "plant",
        "effect": None,
        "is_generic": False,
        "ap": 10,
    },
    "sucker": {
        "name": "Sucker",
        "factor": 0,
        "action": "enem.hp -=1; self.hp +=1 if self.hp+1 <= self.full_hp else 0",
        "world_action": "",
        "move": ["downgrade", "shine"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Sucks 1 HP from the enemy and adds it to it's own.",
        "type": "plant",
        "effect": None,
        "is_generic": False,
        "ap": 20,
    },
    "root_strangler": {
        "name": "Root strangler",
        "factor": 1,
        "action": "",
        "world_action": "",
        "move": ["attack", "downgrade"],
        "miss_chance": 0.2,
        "min_lvl": 20,
        "desc": "Uses old and crusty roots to strangle the enemy.",
        "type": "plant",
        "effect": "EffectParalyzation",
        "is_generic": True,
        "ap": 15,
    },
    "root_slap": {
        "name": "Root slap",
        "factor": 1.5,
        "action": "",
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.2,
        "min_lvl": 0,
        "desc": "Uses old and crusty roots to slap the enemy.",
        "type": "plant",
        "effect": None,
        "is_generic": True,
        "ap": 30,
    },
    "leaf_storm": {
        "name": "Leaf storm",
        "factor": 5,
        "action": "",
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0,
        "min_lvl": 20,
        "desc": "Blasts a bunch of spiky leafs at the enemy.",
        "type": "plant",
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
    "bark_hardening": {
        "name": "Bark hardening",
        "factor": 0,
        "action": "self.defense += 1",
        "world_action": "",
        "move": ["shine"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Hardens the bark to protect it better.",
        "type": "plant",
        "effect": None,
        "is_generic": True,
        "ap": 15,
    },
    "poison_spores": {
        "name": "Poison spores",
        "factor": 0,
        "action": "",
        "world_action": "",
        "move": ["downgrade"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Ejects some poisonous spores onto the enemy.",
        "type": "plant",
        "effect": "EffectPoison",
        "is_generic": False,
        "ap": 15,
    },
    "branch_stab": {
        "name": "Branch stab",
        "factor": 4,
        "action": "enem.miss_chance += 1",
        "world_action": "",
        "move": ["attack", "downgrade"],
        "miss_chance": 0.2,
        "min_lvl": 15,
        "desc": "Stabs the enemy with a branch, preferably in the enemy's eyes.",
        "type": "plant",
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
    # ice attacks
    "freeze": {
        "name": "Freeze",
        "factor": 0,
        "action": "",
        "world_action": "",
        "move": ["downgrade"],
        "miss_chance": 0.1,
        "min_lvl": 10,
        "desc": "Freezes the enemy.",
        "type": "ice",
        "effect": "EffectFreezing",
        "is_generic": True,
        "ap": 10,
    },
    "snow_storm": {
        "name": "Snow storm",
        "factor": 2.5,
        "action": "",
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Summons a snow storm full of ice spikes onto the enemy.",
        "type": "ice",
        "effect": None,
        "is_generic": True,
        "ap": 20,
    },
    "sword_of_ice": {
        "name": "Sword of ice",
        "factor": 5,
        "action": "",
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0.3,
        "min_lvl": 20,
        "desc": "Stabs a giant ice spike into the enemy.",
        "type": "ice",
        "effect": None,
        "is_generic": True,
        "ap": 10,
    },
    "spikes": {
        "name": "Spikes",
        "factor": 1.75,
        "action": "",
        "world_action": "",
        "move": ["attack"],
        "miss_chance": 0,
        "min_lvl": 0,
        "desc": "Stabs the enemy with an some ice spikes.",
        "type": "ice",
        "effect": None,
        "is_generic": True,
        "ap": 30,
    },
}

if __name__ == "__main__":
    print("\033[31;1mDo not execute this!\033[0m")
