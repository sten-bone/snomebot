import discord

class Character:

    def __init__(self, name, level, hp, max_hp, gold,
                 exp, muscle, vision, stealth, agility, 
                 weapon, armor, items, reactions):
        self.name = name
        self.level = level
        self.hp = hp
        self.max_hp = max_hp
        self.gold = gold
        self.exp = exp
        self.muscle = muscle
        self.vision = vision
        self.stealth = stealth
        self.agility = agility
        self.weapon = weapon
        self.armor = armor
        self.items = items
        self.reactions = reactions
        
    # returns the character sheet as an embed object
    def get_sheet(self):
        sheet = discord.Embed(title=self.name, url='')
        return sheet