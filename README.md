
A random character generation program for D&amp;D 5E.

D&D is property of Wizard of the Coast. https://company.wizards.com/

# Character generator

## How to use:

Executing py dnd.char.py will generate a random character.
Optionally, you can input these arguments to control how the character should
be generated:

-c --class \<class\>: specify the class of the character.

-r --race \<race\>: specify the race.

-s --statistics \<population\>: this generates a population of characters and exhibit statistics about them. This option works with the others. This is also useful to know the exact string to use to specify race and class.

-b --background \<bg\>: specify background.

--max-abilities: roll 20 for all abilities.

--roll-four: roll four dice for abilities and take out the lowest. This is the default.

--roll-three: roll three dice for abilities.

--random-class: choose a trully random class.

--help: print help.

Note: The algorithm chooses a class that makes sense for the abilities rolled,
in order not to have a wizard with low intelligence, for example.  If you want
trully random class, though, then use the --random-class option.


## Example:

- Generate a Forest Gnome Fighter with the outlander background:
```
py dnd_char.py -c Fighter -r "Forest Gnome" -b Outlander
```

# Treasure generator

## How to use:

Treasure generator generates treasure according to the party or a monster
challange level. The following options are available:

-h --hoard: Generate a treasure hoard.

-p --personal: Generate personal treasure.

-l --level \<level\>: Set the challenge level of the party or of the monster associated with the treasure.

-q --quantity \<quantity\>: Set the number of monsters to calculate personal treasure.

## Examples:

- Generate a hoard for a party of challange level 11:
```
py dnd_treasure.py --hoard --level 11
```

- Generate the personal treasure for a party of 5 monsters of challange level 15:
```
py dnd_treasure.py --personal --level 15 --quantity 5
```
