# File: phahy039_test.py
# Description: test all methods from main file except the inistiliser and getters or setters.
# Author: Huyen Thi Thu Pham
# StudentID: 110369293
# EmailID: phahy039
# This is my own work as defined by the University's Academic Misconduct Policy.


import unittest
from phahy039_main import *


class WorkshopTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the dependencies
        self.forge = Forge()
        self.enchanter = Enchanter()
        self.workshop = Workshop(self.forge, self.enchanter)

    def test_addWeapon(self):
        # Create a weapon
        weapon = Weapon("Sword", Steel, Maple)
        # Add a weapon to the workshop
        self.workshop.addWeapon(weapon)
        # Check if the weapon is added to the workshop's list of weapons
        self.assertIn(weapon, self.workshop.weapons)

    def test_removeWeapon(self):
        # Add a weapon to the workshop
        weapon = Weapon("Shield", Bronze, Oak)
        self.workshop.addWeapon(weapon)
        # Remove the weapon from the workshop
        self.workshop.removeWeapon(weapon)
        # Verify that the weapon is no longer in the workshop's list of weapons
        self.assertNotIn(weapon, self.workshop.weapons)

    def test_addEnchantment(self):
        # Create materials
        diamond = Diamond(strength=3.0, magicPower=4.5)
        # Create a enchantment
        enchantment = Enchantment("Holy", diamond, diamond, "pulses a blinding beam of light")
        # Add an enchantment to the workshop
        self.workshop.addEnchantment(enchantment)
        # Check if the enchantment is added to the workshop's list of enchantments
        self.assertIn(enchantment, self.workshop.enchantments)

    def test_removeEnchantment(self):
        # Create materials
        diamond = Diamond(strength=3.0, magicPower=4.5)
        # Create a enchantment
        enchantment = Enchantment("Holy", diamond, diamond, "pulses a blinding beam of light")
        # Remove an enchantment to the workshop
        self.workshop.removeEnchantment(enchantment)
        # Check if the enchantment is removed from the workshop's list of enchantments
        self.assertNotIn(enchantment, self.workshop.enchantments)
    def test_addMaterial(self):
        # Choose a material and quantity to add
        material = Steel()
        quantity = 10
        # Add the material to the workshop
        self.workshop.addMaterial(material, quantity)
        # Check if the material and quantity are added to the workshop's materials
        self.assertEqual(self.workshop.materials.get(material.__class__.__name__), quantity)

    def test_removeMaterial(self):
        # Add a material to the workshop
        steel = Steel(strength=10, purity=1.8)
        self.workshop.addMaterial(steel, 10)

        # Remove a quantity of material from the workshop
        quantity = 5
        self.workshop.removeMaterial(steel, quantity)

        # Assert that the quantity of material in the workshop is decreased by the specified amount
        expectedQuantity = 10 - quantity
        self.assertEqual(self.workshop.materials[steel.__class__.__name__], expectedQuantity)

        # Try to remove a larger quantity than what is available
        invalidQuantity = 10
        with self.assertRaises(ValueError):
            self.workshop.removeMaterial(steel, invalidQuantity)

    def test_displayWeapons(self):
        # Create some weapons and add them to the workshop
        steel = Steel()
        maple =Maple()
        bronze = Bronze()
        oak = Oak()
        iron =Iron()
        ash = Ash()
        weapon1 = Weapon("Sword", steel, maple)
        weapon2 = Weapon("Shield", bronze, oak)
        weapon3 = Weapon("Axe", iron, ash)
        weapon4 = Weapon("Scythe", steel, ash)

        # Add enchantments to some weapons
        diamond = Diamond()
        ruby = Ruby()
        onyx = Onyx()
        enchantment1 = Enchantment("Holy", diamond, diamond, "pulses a blinding beam of light")
        enchantment2 = Enchantment("Lava", ruby, onyx, "melts the armour off an enemy")
        weapon1.enchantment = enchantment1
        weapon2.enchantment = enchantment2
        # Add weapons and enchantments to the workshop
        self.workshop.addWeapon(weapon1)
        self.workshop.addWeapon(weapon2)
        self.workshop.addWeapon(weapon3)
        self.workshop.addWeapon(weapon4)
        self.workshop.addEnchantment(enchantment1)
        self.workshop.addEnchantment(enchantment2)

        # Define the expected output for stored enchantments
        expectedStoredEnchantments = "A Holy enchantment is stored in the workshop.\n" \
                                     "A Lava enchantment is stored in the workshop.\n"

        # Define the expected output for enchanted weapons
        expectedEnchantedWeapons = "The Holy Greatsword is imbued with a Holy enchantment and pulses a blinding beam of light. It deals 831.60 damage.\n" \
                                   "The Molten Defender is imbued with a Lava enchantment and melts the armour off an enemy. It deals 35.26 damage.\n"

        # Assert that the actual output for stored enchantments matches the expected output
        self.assertEqual(self.workshop.displayEnchantments(), expectedStoredEnchantments)

        # Assert that the actual output for enchanted weapons contains the expected output
        self.assertIn(expectedEnchantedWeapons, self.workshop.displayWeapons())

    def test_displayEnchantments(self):
        diamond = Diamond()
        ruby = Ruby()
        onyx = Onyx()
        enchantment1 = Enchantment("Holy", diamond, diamond, "pulses a blinding beam of light")
        enchantment2 = Enchantment("Lava", ruby, onyx, "melts the armour off an enemy")
        self.workshop.addEnchantment(enchantment1)
        self.workshop.addEnchantment(enchantment2)
        expectedOutput = "A Holy enchantment is stored in the workshop.\n" \
                          "A Lava enchantment is stored in the workshop.\n"
        self.assertEqual(self.workshop.displayEnchantments(), expectedOutput)

    def test_displayMaterials(self):
        iron = Iron()
        steel = Steel()
        self.workshop.addMaterial(iron,5)
        self.workshop.addMaterial(iron,2)
        self.workshop.addMaterial(steel,3)
        expectedOutput = "Iron: 7 remaining.\n"\
                         "Steel: 3 remaining.\n"
        self.assertEqual(self.workshop.displayMaterials(), expectedOutput)


class ForgeTestCase(unittest.TestCase):
    def setUp(self):
        self.forge = Forge(workshop=None)
        self.enchanter = Enchanter()
        self.workshop = Workshop(self.forge, self.enchanter)

    def test_craft(self):
        maple = Maple(strength=5)
        steel = Steel(strength=10, purity=1.8)
        materials = {"Maple": 5, "Steel": 3}
        weapon = self.forge.craft("Sword", maple, steel, materials)

        # Check the attributes of the crafted weapon:
        self.assertEqual(weapon.name, "Sword")
        self.assertEqual(weapon.getPrimaryMaterial(), maple)
        self.assertEqual(weapon.getCatalystMaterial(), steel)
        # Check if the weapon is added to the workshop (assuming self.__workshop is not None):
        # Call the addWeapon method
        self.workshop.addWeapon(weapon)
        # Assert that the weapon is added to the workshop
        self.assertIn(weapon, self.workshop.weapons)
        # Check if the required materials are consumed from the material store:
        self.assertEqual(materials["Steel"], 2)
        self.assertEqual(materials["Maple"], 4)
        # Test for insufficient primary material:
        with self.assertRaises(ValueError):
            self.forge.craft("Sword", maple, steel, {"Maple": 3})
        # Test for insufficient catalyst material:
        with self.assertRaises(ValueError):
            self.forge.craft("Sword", maple, steel, {"Steel": 5})

    def test_disassemble(self):
        weapon = Weapon("Sword", Maple(strength=5), Steel(strength=10, purity=1.8))
        # Create a materials dictionary representing the available materials in the workshop
        materials = {"Maple": 5, "Steel": 3}
        # Call the disassemble method
        disassembled_weapon = self.forge.disassemble(weapon, materials)
        # Verify that the weapon is removed from the workshop
        self.assertNotIn(weapon, self.workshop.weapons)
        # Verify that the method returns the weapon object being disassembled
        self.assertEqual(disassembled_weapon, weapon)


class EnchanterTestCase(unittest.TestCase):
    def setUp(self):
        self.enchanter = Enchanter()

    def test_craft(self):
        name = "Holy"
        diamond = Diamond(strength=2.1, magicPower=2.2)
        materials = {"Diamond": 3, "Ruby": 1}
        # Call the "craft" method of the enchanter object.
        enchantment = self.enchanter.craft(name, diamond, diamond, materials)
        #Verify that the enchantment object is an instance of the Enchantment class
        self.assertIsInstance(enchantment, Enchantment)
        self.assertEqual(enchantment.name, name)
        self.assertEqual(enchantment.getPrimaryMaterial(), diamond)
        self.assertEqual(enchantment.getCatalystMaterial(), diamond)
        # Verify that the material store was updated
        self.assertEqual(materials["Diamond"], 1)
        self.assertEqual(materials["Ruby"], 1)

    def test_disassemble(self):
        enchantment = Enchantment("Holy", Diamond(strength=2.1, magicPower=2.2), Diamond(strength=2.1, magicPower=2.2), "pulses a blinding beam of light")
        materials = {"Diamond": 2, "Ruby": 0}
        disassembled_enchantment = self.enchanter.disassemble(enchantment, materials)
        #Verify that the disassembled enchantment returned from the disassemble method is the same as the original one.
        self.assertEqual(disassembled_enchantment, enchantment)
        # Verify the materials dictionary was updated.
        self.assertEqual(materials["Diamond"], 4)
        self.assertEqual(materials["Ruby"], 0)

    def test_enchant(self):
        diamond = Diamond(strength=2.1, magicPower=2.2)
        maple = Maple(strength=5)
        steel = Steel(strength=10, purity=1.8)
        weapon = Weapon("Sword", maple, steel)
        enchantment =Enchantment("Holy", diamond, diamond, "pulses a blinding beam of light")

        # Enchant the weapon using the enchant method
        self.enchanter.enchant(weapon, "Holy", enchantment)
        # Verify the weapon's attributes after enchantment
        self.assertEqual(weapon.getEnchantment(), enchantment)
        self.assertEqual(weapon.calculateDamage() * weapon.enchantment.calculateMagicDamage(), 5 * (10*1.8) *((2.1*2.2)+(2.1*2.2)))
        self.assertEqual(weapon.enchantmentName, "Holy")


class WeaponTestCase(unittest.TestCase):

    def test_calculateDamage(self):
        # Test case 1: Two pieces of wood
        self.primaryMaterial = Oak(strength=4)
        self.catalystMaterial = Maple(strength=5)
        self.weapon = Weapon("Bow", self.primaryMaterial, self.catalystMaterial)
        # Verify the calculateDamage
        self.assertEqual(self.weapon.calculateDamage(), 20)

        # Test case 2: Two pieces of metal
        primaryMaterial = Bronze(strength=3, purity=1.3)
        catalystMaterial = Bronze(strength=3, purity=1.3)
        weapon = Weapon("Dagger", primaryMaterial, catalystMaterial)
        self.assertEqual(round(weapon.calculateDamage(), 2), 7.8)

        # Test case 3: Wood and metal combination
        primaryMaterial = Steel(strength=10, purity=1.8)
        catalystMaterial = Maple(strength=5)
        weapon = Weapon("Sword", primaryMaterial, catalystMaterial)
        self.assertEqual(round(weapon.calculateDamage(), 2), 90)

    def test_attack(self):
        # Verify that when a weapon is created
        # the attack method returns a string indicating that it deals 20.00 damage.
        primaryMaterial = Oak(strength=4)
        catalystMaterial = Maple(strength=5)
        weapon = Weapon("Bow", primaryMaterial, catalystMaterial)
        self.assertEqual(weapon.attack(), "It deals 20.00 damage.")


class EnchantmentTestCase(unittest.TestCase):

    def setUp(self):
        diamond = Diamond(strength=2.1, magicPower=2.2)
        self.enchantment = Enchantment("Holy", diamond, diamond, "pulses a blinding beam of light")

    def test_calculateMagicDamage(self):
        magicDamage = self.enchantment.calculateMagicDamage()
        self.assertEqual(round(magicDamage, 2), 9.24)

    def test_useEffect(self):
        effect = self.enchantment.useEffect()
        expected_effect = "Holy enchantment and pulses a blinding beam of light"
        self.assertEqual(effect, expected_effect)

if __name__ == '__main__':
    unittest.main()