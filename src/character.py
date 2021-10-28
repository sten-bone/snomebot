import discord
import src.item

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
    def get_sheet(self, dice):
        sheet = discord.Embed(title=self.name, url='')
        sheet.set_thumbnail(url='')
        sheet.add_field(name="HP", value=f"{self.hp}/{self.max_hp}", inline=False)
        sheet.add_field(name="Level", value=self.level, inline=True)
        sheet.add_field(name="Gold", value=self.gold, inline=True)
        sheet.add_field(name=f"EXP ({self.exp}/10)", value=":star:" * self.exp, inline=False)
        sheet.add_field(name="Muscle :crossed_swords:", value=self.muscle, inline=False)
        sheet.add_field(name="Vision :eye:", value=self.vision, inline=False)
        sheet.add_field(name="Stealth :boot:", value=self.stealth, inline=False)
        sheet.add_field(name="Agility :runner:", value=self.agility, inline=False)
        sheet.add_field(name="Weapon", value=self.weapon, inline=False)
        sheet.add_field(name="Armor", value=self.armor, inline=False)
        sheet.add_field(name="Items", value="Use `sb items`", inline=False)
        sheet.add_field(name="Reckless Reactions", value=self.list_reactions(dice), inline=False)
        return sheet
    
    # returns a list of reactions and dice emoji
    def list_reactions(self, dice):
        react = []
        for i in range(len(self.reactions)):
            r = self.reactions[i]
            react.append(f"{dice[i]} " 
                + (":flushed:" if r[0] == 'mild' else (":fearful:" if r[0] == 'bad' else ":scream:")) 
                + f" {r[1]}")
        return '\n'.join(react)

    # gives the character a certain amount of exp
    def give_exp(self, exp_to_add):
        self.exp += exp_to_add

    # deals damage to the character, but will not go below 0
    def deal_damage(self, damage):
        self.hp -= damage
        if (self.hp < 0): self.hp = 0

    # heals the character, but will 
    def heal(self, health):
        self.hp += health
        if (self.hp > self.max_hp): self.hp = self.max_hp