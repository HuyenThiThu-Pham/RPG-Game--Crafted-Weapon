# File: phahy039_main.py
# Description: designing and implementing a crafting system
# that allows a user to create weapons and enchantments,
# and then imbue those enchantments into the crafted weapons.
# Author: Huyen Thi Thu Pham
# StudentID: 110369293
# EmailID: phahy039
# This is my own work as defined by the University's Academic Misconduct Policy.



from abc import ABC, abstractmethod



class Material(ABC):
    def __init__(self, strength):
        self.strength = strength


class Wood(Material):
    def __init__(self, strength):
        super().__init__(strength)


class Metal(Material):
    def __init__(self, strength, purity):
        super().__init__(strength)
        self.purity = purity


class Gemstone(Material):
    def __init__(self, strength, magicPower):
        super().__init__(strength)
        self.magicPower = magicPower


class Maple(Wood):
    def __init__(self, strength=5):
        super().__init__(strength)


class Ash(Wood):
    def __init__(self, strength=3):
        super().__init__(strength)


class Oak(Wood):
    def __init__(self, strength=4):
        super().__init__(strength)


class Bronze(Metal):
    def __init__(self, strength=3, purity=1.3):
        super().__init__(strength, purity)


class Iron(Metal):
    def __init__(self, strength=6, purity=1.1):
        super().__init__(strength, purity)


class Steel(Metal):
    def __init__(self, strength=10, purity=1.8):
        super().__init__(strength, purity)


class Ruby(Gemstone):
    def __init__(self, strength=1, magicPower=1.8):
        super().__init__(strength, magicPower)


class Sapphire(Gemstone):
    def __init__(self, strength=1.2, magicPower=1.6):
        super().__init__(strength, magicPower)


class Emerald(Gemstone):
    def __init__(self, strength=1.6, magicPower=1.1):
        super().__init__(strength, magicPower)


class Diamond(Gemstone):
    def __init__(self, strength=2.1, magicPower=2.2):
        super().__init__(strength, magicPower)


class Amethyst(Gemstone):
    def __init__(self, strength=1.8, magicPower=3.2):
        super().__init__(strength, magicPower)


class Onyx(Gemstone):
    def __init__(self, strength=0.1, magicPower=4.6):
        super().__init__(strength, magicPower)


class Workshop:
    """
    A main class to store enchanter and forge for later uses.

    Attributes
    ----------
        forge (Forge): The forge used for weapon crafting.
        enchanter (Enchanter): An instance of the Enchanter class associated with the workshop.
        weapons (list): A list to store crafted weapons.
        enchantments (list): A list to store crafted enchantments.
        materials (list): A list to store available materials.

    Methods
    -------
        addWeapon(self, weapon):
            Add a weapon created to the workshop.
        removeWeapon(self, weapon):
            Remove a weapon from workshop.
        addEnchantment(self, enchantment):
            Add an enchantment to the workshop.
        removeEnchantment(self, enchantment):
            Remove an enchantment from the workshop.
        addMaterial(self, material, quantity):
            Add a quantity of material to the workshop.
        removeMaterial(self, material, quantity):
            Remove a quantity of material from the workshop.
        displayWeapons(self):
            Display information of the Weapon in the workshop with being enchanted or not.
        displayEnchantments(self):
            Display information of the enchantment in the workshop
        displayMaterials(self):
            Display quantity of material remaining in the workshop.
    """
    def __init__(self, forge, enchanter):
        self.forge = forge
        self.enchanter = enchanter
        self.weapons = []
        self.enchantments = []
        self.materials = {}

    def addWeapon(self, weapon):
        """ Adds a weapon to the workshop."""

        self.weapons.append(weapon)

    def removeWeapon(self, weapon):
        """Removes a weapon from the workshop."""
        if weapon in self.weapons:
            self.weapons.remove(weapon)

    def addEnchantment(self, enchantment):
        """Adds an enchantment to the workshop."""
        self.enchantments.append(enchantment)

    def removeEnchantment(self, enchantment):
        """Removes an enchantment from the workshop. """
        if enchantment in self.enchantments:
            self.enchantments.remove(enchantment)

    def addMaterial(self, material, quantity):
        """Adds the specified quantity of the material to the workshop."""
        if isinstance(material, str):
            materialName = material
        else:
            materialName = material.__class__.__name__

        if materialName in self.materials:
            self.materials[materialName] += quantity
        else:
            self.materials[materialName] = quantity

    def removeMaterial(self, material, quantity):
        """Removes a quantity of material from the workshop."""
        material = material.__class__.__name__
        if material in self.materials:
            if self.materials[material] > quantity:
                self.materials[material] -= quantity
                if self.materials[material] == 0:
                    del self.materials[material]
            else:
                raise ValueError("Insufficient quantity of material in the workshop.")
        else:
            raise ValueError("Material not found in the workshop.")

    def displayWeapons(self):
        """Display information of the Weapons in the workshop, whether enchanted or not."""

        enchantedWeapons = ["Holy Greatsword", "Molten Defender", "Berserker Axe", "Soul Eater",
                            "Twisted Bow", "Wand of the Deep", "Venemous Battlestaff"]
        weaponInfo =""
        for i in range(len(self.weapons)):
            weapon = self.weapons[i]
            if weapon.enchantment:
                enchantmentEffect = weapon.enchantment.useEffect()
                enchantedDamage = weapon.calculateDamage() * weapon.enchantment.calculateMagicDamage()
                weaponInfo += f"The {enchantedWeapons[i]} is imbued with a {enchantmentEffect}. "\
                              f"It deals {enchantedDamage:.2f} damage.\n"
            elif i < len(enchantedWeapons):
                weaponDamage = weapon.calculateDamage()
                weaponInfo += f"The {weapon.name} is not enchanted. It deals {weaponDamage:.2f} damage.\n"
        return weaponInfo

    def displayEnchantments(self):
        enchantmentInfo = ""
        for enchantment in self.enchantments:
            enchantmentInfo += f"A {enchantment.name} enchantment is stored in the workshop.\n"
        return enchantmentInfo

    def displayMaterials(self):
        """Displays the current materials in the workshop."""
        materialInfo = ""
        for material, quantity in self.materials.items():
            materialInfo += f"{material}: {quantity} remaining.\n"
        return materialInfo


class Crafter(ABC):
    """Abstract base class representing a crafter.
    Methods
    -------
        craft(self):
        disassemble(self)"""

    @abstractmethod
    def craft(self):
        """Abstract method to craft an item."""
        pass

    @abstractmethod
    def disassemble(self):
        """Abstract method to disassemble an item."""
        pass


class Forge(Crafter):
    """
    A type of Crafter class, implements the craft and disassemble methods.
    Attributes
    ----------
        workshop (Workshop): The workshop instance associated with the forge.
    Methods
    -------
        craft(self, name, primaryMaterial, catalystMaterial,materials):
            Crafts a weapon, instantiated weapon and return the instantiated weapon to workshop.
        disassemble(self, weapon, materials):
            Disassembles a previously crafted weapon and returns it.
    """
    def __init__(self, workshop=None):
        super().__init__()
        self.__workshop = workshop

    def craft(self, name, primaryMaterial, catalystMaterial, materials):
        """  Crafts a weapon, instantiated weapon perform calculations of damage on the weapon and return the instantiated weapon to workshop """

        # Check if the required materials are available in the material store
        if (
            primaryMaterial.__class__.__name__ not in materials
            or catalystMaterial.__class__.__name__ not in materials
        ):
            raise ValueError("Insufficient materials for crafting.")

        if (
            materials[primaryMaterial.__class__.__name__] < 1
            or materials[catalystMaterial.__class__.__name__] < 1
        ):
            raise ValueError("Insufficient materials for crafting.")

        # Create a new instance of the Weapon class
        weapon = Weapon(name, primaryMaterial, catalystMaterial)

        # Calculate the damage for the weapon
        weapon.calculateDamage()

        if self.__workshop is not None:
            # Add the weapon to the workshop
            self.__workshop.addWeapon(weapon)
        # Update the material store by consuming the required materials
        materials[primaryMaterial.__class__.__name__] -= 1
        materials[catalystMaterial.__class__.__name__] -= 1

        # Return the crafted weapon
        return weapon

    def disassemble(self, weapon, materials):
        """ Disassembles a previously crafted weapon and returns it."""

        if self.__workshop is not None:
            # Remove the weapon from the workshop
            self.__workshop.removeWeapon(weapon)

        # Update the material store with the disassembled weapon's materials
        materials[weapon.getPrimaryMaterial().__class__.__name__] += 1
        materials[weapon.getCatalystMaterial().__class__.__name__] += 1

        # Return the weapon being disassembled.
        return weapon


class Enchanter(Crafter):
    """
    A type of Crafter and implements the craft and disassemble methods.

    Attributes
    ----------
        __workshop (Workshop): The workshop instance associated with the enchanter.
        __enchantment(list): A list to store enchantments.
        __materials(dict): A dictionary to track the quantity of different materials.
        __recipes (enchantmentName, effect): dict

    Methods
    -------
        craft(self, name, primaryMaterial, catalystMaterial, materials):
            Instantiated and return an enchantment.
        disassemble(self, enchantment, materials):
            Return the enchantment being disassembled.
        enchant(self, weapon, enchantmentName, enchantment):
            Imbue the weapons with a created enchantment.
    """
    def __init__(self, workshop=None):
        super().__init__()
        self.__workshop = workshop
        self.__enchantment = []
        self.__materials = {
            "Maple": 0,
            "Oak": 0,
            "Ash": 0,
            "Bronze": 0,
            "Iron": 0,
            "Steel": 0,
            "Ruby": 0,
            "Sapphire": 0,
            "Emerald": 0,
            "Diamond": 0,
            "Amethyst": 0,
            "Onyx": 0
        }
        self.__recipes = {
            "Holy": "pulses a blinding beam of light",
            "Lava": "melts the armour off an enemy",
            "Pyro": "applies a devastating burning effect",
            "Darkness": "binds the enemy in dark vines",
            "Cursed": "causes the enemy to become crazed",
            "Hydro": "envelops the enemy in a suffocating bubble",
            "Venomous": "afflicts a deadly, fast-acting toxin"
        }

    def craft(self, name, primaryMaterial, catalystMaterial, materials):
        """Creating an enchantment, instantiated and returned to Workshop"""
        # Check if the required materials are available in the material store
        if (
            primaryMaterial.__class__.__name__ not in materials
            or catalystMaterial.__class__.__name__ not in materials
        ):
            raise ValueError("Insufficient materials for crafting.")

        if (
            materials[primaryMaterial.__class__.__name__] < 1
            or materials[catalystMaterial.__class__.__name__] < 1
        ):
            raise ValueError("Insufficient materials for crafting.")

        # Create a new instance of the Enchantment class
        effect = self.__recipes.get(name)
        if effect is None:
            # Choose a default recipe when the requested recipe is not found
            effect = "Default Effect"

        enchantment = Enchantment(name, primaryMaterial, catalystMaterial, effect)

        if self.__workshop is not None:
            # Add the enchantment to the workshop
            self.__workshop.addEnchantment(enchantment)
        # Update the material store by consuming the required materials
        materials[primaryMaterial.__class__.__name__] -= 1
        materials[catalystMaterial.__class__.__name__] -= 1

        # Return the crafted enchantment
        return enchantment

    def disassemble(self, enchantment, materials):
        """ Remove and disassembles a previously crafted enchantment from Workshop
        and returns it to material store."""
        # Remove the enchantment from the workshop
        if self.__workshop is not None:
            self.__workshop.removeEnchantment(enchantment)

        materials[enchantment.getPrimaryMaterial().__class__.__name__] += 1
        materials[enchantment.getCatalystMaterial().__class__.__name__] += 1
        # Return the enchantment being disassembled.
        return enchantment

    def enchant(self, weapon, enchantmentName, enchantment):
        """Enchants a weapon with the specified enchantment."""
        # The weapons attributes are updated to reflect the attached enchantment.
        weapon.setEnchantment(enchantment)
        weapon.setDamage(weapon.getDamage() * enchantment.magicDamage)
        weapon.enchantmentName = enchantmentName


class Weapon:
    """
    Creating a weapon using 2 materials.

    Attributes
    ----------
        __name (str): The name of the weapon.
        __damage (float): The damage value of the item (initialized as 0).
        __enchanted (bool): A boolean indicating whether the item is enchanted (initialized as False).
        __primaryMaterial (Material): The primary material used for the weapon.
        __catalystMaterial (Material): The catalyst material used for the weapon.
        __enchantment: The enchantment applied to the item (initialized as None).

    Methods
    -------
        getName(self):
        setName(self, value):
        getDamage(self):
        setDamage(self, value):
        isEnchanted(self):
        setEnchanted(self, value):
        getPrimaryMaterial(self):
        getCatalystMaterial(self):
        getEnchantment(self):
        setEnchantment(self, enchantment):
        calculateDamage(self):
            Calculates the damage of the weapon based on the materials used and return it.
        attack(self):
            Returns a string describing the attack of the weapon.
    """

    def __init__(self, name, primaryMaterial, catalystMaterial):

        self.__name = name
        self.__damage = 0
        self.__enchanted = False
        self.__primaryMaterial = primaryMaterial
        self.__catalystMaterial = catalystMaterial
        self.__enchantment = None

    # Getter and setter for name attribute
    def getName(self):
        return self.__name

    def setName(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self.__name = value

    # Getter and setter for damage attribute
    def getDamage(self):
        return self.__damage

    def setDamage(self, value):
        if not isinstance(value, float):
            raise ValueError("Damage must be a float.")
        self.__damage = value

    # Getter and setter for enchanted attribute
    def isEnchanted(self):  # Check if the weapon is enchanted.
        return self.__enchanted

    def setEnchanted(self, value):
        if not isinstance(value, bool):
            raise ValueError("Enchanted status must be a boolean.")
        self.__enchanted = value

    # Getter and setter for primaryMaterial attribute
    def getPrimaryMaterial(self):
        return self.__primaryMaterial

    # Getter and setter for secondaryMaterial attribute
    def getCatalystMaterial(self):
        return self.__catalystMaterial

    # Getter and setter for enchantment attribute
    def getEnchantment(self):
        return self.__enchantment

    def setEnchantment(self, enchantment):
        if not isinstance(enchantment, Enchantment):
            raise TypeError("Enchantment must be an instance of the Enchantment class.")
        self.__enchantment = enchantment
        self.setEnchanted(True)

    # Properties for all attributes
    name = property(getName, setName)
    damage = property(getDamage, setDamage)
    enchanted = property(isEnchanted, setEnchanted)
    primaryMaterial = property(getPrimaryMaterial)
    secondaryMaterial = property(getCatalystMaterial)
    enchantment = property(getEnchantment, setEnchantment)

    def calculateDamage(self):
        """
        Calculates the damage of the weapon based on the materials used and return it.
        """
        primaryStrength = self.__primaryMaterial.strength
        catalystStrength = self.__catalystMaterial.strength
        # If a weapon is made of two pieces of wood:
        if (
                isinstance(self.__primaryMaterial, Wood)
                and isinstance(self.__catalystMaterial, Wood)
        ):
            self.__damage = primaryStrength * catalystStrength
        # If a weapon is made of two pieces of metal:
        elif (
                isinstance(self.__primaryMaterial, Metal)
                and isinstance(self.__catalystMaterial, Metal)
        ):
            primaryPurity = self.__primaryMaterial.purity
            catalystPurity = self.__catalystMaterial.purity
            self.__damage = (primaryStrength * primaryPurity) + (catalystStrength * catalystPurity)
        # If a weapon is made of a piece of wood and a piece of metal:
        elif (
                isinstance(self.__primaryMaterial, Metal)
                and isinstance(self.__catalystMaterial, Wood)
        ):
            primaryPurity = self.__primaryMaterial.purity
            self.__damage = (primaryStrength * catalystStrength) * primaryPurity
        elif (
                isinstance(self.__primaryMaterial, Wood)
                and isinstance(self.__catalystMaterial, Metal)
        ):
            catalystPurity = self.__catalystMaterial.purity
            self.__damage = primaryStrength * (catalystStrength * catalystPurity)
        else:
            raise ValueError("Invalid combination of material.")
        return self.__damage

    def attack(self):  # used in the workshops displayArmory method.
        """Returns a string describing the attack of the weapon."""

        damage = self.calculateDamage()
        return f"It deals {damage:.2f} damage."


class Enchantment:
    """
    Creating an enchantment and imbued onto a weapon.

    Attributes
    ----------
        __name (str): The name of the enchantment.
        __primaryMaterial (Material): The primary material used for the enchantment.
        __catalystMaterial (Material): The catalyst material used for the enchantment.
        __effect (str): The effect of the enchantment.
        __magicDamage (float): The additional magic damage provided by the enchantment.

    Methods
    -------
        getName(self):
        getMagicDamage(self):
        setMagicDamage(self, value):
        getEffect(self):
        setEffect(self, value):
        getPrimaryMaterial(self):
        getCatalystMaterial(self):
        calculateMagicDamage(self):
            Calculate the additional magic damage provided by the enchantment
            based on the primary and catalyst materials.
        useEffect(self):
            Use the enchantment and return a string representation of the enchantment and its effect.
    """
    def __init__(self, name, primaryMaterial, catalystMaterial, effect):

        self.__name = name
        self.__primaryMaterial = primaryMaterial
        self.__catalystMaterial = catalystMaterial
        self.__effect = effect
        self.__magicDamage = 0
        self.calculateMagicDamage()

    # Getter for name attribute
    def getName(self):
        return self.__name

    # Getter and setter for magicDamage attribute
    def getMagicDamage(self):
        return self.__magicDamage

    def setMagicDamage(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("The magicDamage must be a number.")
        self.__magicDamage = value

    # Getter and setter for effect attribute
    def getEffect(self):
        return self.__effect

    def setEffect(self, value):
        if not isinstance(value, str):
            raise TypeError("The effect must be a string.")
        self.__effect = value

    # Getter for primaryMaterial attribute
    def getPrimaryMaterial(self):
        return self.__primaryMaterial

    # Getter for catalystMaterial attribute
    def getCatalystMaterial(self):
        return self.__catalystMaterial

    # Property for name attribute
    name = property(getName)

    # Property for magicDamage attribute
    magicDamage = property(getMagicDamage, setMagicDamage)

    # Property for effect attribute
    effect = property(getEffect, setEffect)

    def calculateMagicDamage(self):
        """
        Calculate the additional magic damage provided by the enchantment based on the primary and catalyst materials.
        """
        primary_strength = self.__primaryMaterial.strength
        primary_magic_power = self.__primaryMaterial.magicPower
        catalyst_strength = self.__catalystMaterial.strength
        catalyst_magic_power = self.__catalystMaterial.magicPower

        self.__magicDamage = (primary_strength * primary_magic_power) + (catalyst_strength * catalyst_magic_power)
        return self.__magicDamage

    def useEffect(self):  # used in the workshops methods when displaying your armoury of enchanted weapons.
        """
        Use the enchantment and return a string representation of the enchantment and its effect.
        """
        return f"{self.__name} enchantment and {self.__effect}"


# Create a workshop, forge, enchanter.
workshop = Workshop(Forge(), Enchanter())
# Create a set of materials and lists for testing.
materials = [Maple(), Oak(), Ash(), Bronze(), Iron(), Steel(),
             Ruby(), Sapphire(), Emerald(), Diamond(), Amethyst(), Onyx()]
weaponBlueprints = {
    "Sword": [Steel(), Maple()],
    "Shield": [Bronze(), Oak()],
    "Axe": [Iron(), Ash()],
    "Scythe": [Steel(), Ash()],
    "Bow": [Oak(), Maple()],
    "Wand": [Ash(), Oak()],
    "Staff": [Bronze(), Maple()],
    "Dagger": [Bronze(), Bronze()]}
enchantmentBlueprints = {
    "Holy": [Diamond(), Diamond()],
    "Lava": [Ruby(), Onyx()],
    "Pyro": [Ruby(), Diamond()],
    "Darkness": [Onyx(), Amethyst()],
    "Cursed": [Onyx(), Onyx()],
    "Hydro": [Sapphire(), Emerald()],
    "Venomous": [Emerald(), Amethyst()],
    "Earthly": [Emerald(), Emerald()]}
enchantedWeapons = ["Holy Greatsword", "Molten Defender", "Berserker Axe", "Soul Eater",
    "Twisted Bow", "Wand of the Deep", "Venemous Battlestaff"]
# Adds a number of materials to use for crafting.
for material in materials:
    if isinstance(material, Wood):
        workshop.addMaterial(material.__class__.__name__, 20)
    elif isinstance(material, Metal):
        workshop.addMaterial(material.__class__.__name__, 10)
    else:
        workshop.addMaterial(material.__class__.__name__, 5)
print("--------------------------------Material Store--------------------------------")
print(workshop.displayMaterials())
# Crafts the following: Sword, Shield, Axe, Scythe, Bow, Wand and Staff weapons.
for weapon, materials in weaponBlueprints.items():
    craftedWeapon = workshop.forge.craft(
        weapon, materials[0], materials[1], workshop.materials)
    workshop.addWeapon(craftedWeapon)
# Disassemble the extra weapon.
workshop.removeWeapon(workshop.forge.disassemble(
    workshop.weapons[7], workshop.materials))
print("------------------------------------Armoury-----------------------------------")
print(workshop.displayWeapons())
# Crafts the following: Holy, Lava, Pyro, Darkness, Cursed, Hydro and Venomous enchantments.

for enchantment, materials in enchantmentBlueprints.items():
    craftedEnchantment = workshop.enchanter.craft(
        enchantment, materials[0], materials[1], workshop.materials)
    workshop.addEnchantment(craftedEnchantment)
# Disassemble the extra enchantment.
workshop.removeEnchantment(workshop.enchanter.disassemble(
    workshop.enchantments[7], workshop.materials))
print("------------------------------------Enchantments------------------------------------")
print(workshop.displayEnchantments())
print("-----------------------------------Material Store-----------------------------------")
print(workshop.displayMaterials())
# Enchant the following weapons: Sword, Shield, Axe, Scythe, Bow, Wand and Staff.
for i in range(len(enchantedWeapons)):
    workshop.enchanter.enchant(
        workshop.weapons[i], enchantedWeapons[i], workshop.enchantments[i])
print("-----------------------------------Enchanted Armoury----------------------------------")
print(workshop.displayWeapons())
