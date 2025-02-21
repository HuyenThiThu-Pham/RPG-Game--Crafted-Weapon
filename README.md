# RPG- crafting system
Object Oriented Programming
This project involves creating an RPG-like crafting system, allowing users to craft weapons and enchantments. We'll work with predefined material classes, design the Workshop, Forge, and Enchanter classes, and implement methods for crafting, disassembling, and displaying inventories.

## Materials:

Materials are provided in a hierarchy of classes, including Wood, Metal, and Gemstone. They have attributes used in crafting algorithms but don't require modification.

## Workshop:

The Workshop is the central hub for crafting, storing enchanters, forges, weapons, enchantments, and materials. We'll implement methods for managing these inventories.

## Crafter, Forge, and Enchanter:

The abstract Crafter class has craft and disassemble methods. Forge and Enchanter are specific implementations, focusing on weapons and enchantments.

## Weapon:

Weapons, crafted with two materials, may be enchanted. Implement getters, setters, calculateDamage, and attack methods.

## Enchantment:

Enchantments, crafted with primary and catalyst materials, have attributes like magicDamage and effect. Implement getters, setters, calculateMagicDamage, and useEffect methods.

## Testing & Outputs:

Test the implementation; ensure the output matches the specified format.
