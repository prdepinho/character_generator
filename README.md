
A set of programs to help dungeon masters generate random characters, encounters
and treasure for their D&amp;D 5E campaign.

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

# Encounter generator

## How to use:

The encounter generator generates encounters based on the level of the player
characters, the desired number of monsters and the difficulty of the encounter.
It has the following options:

-d --difficulty: Select the difficulty of the encounter. The options are: easy,
medium, hard and deadly.

-l --pc-levels: As list separated by comma of the level for each player
character. If you enclose the list in double quotes, you may separate the
levels with space.

-m --monsters: The number of monsters in the encounter. It may be either in
dice notation or as a number.  If not specified, the size of the encounter will
vary.

-e --environment: The environment from which to choose the monsters. If this is
not specified, monsters may be taken from all environments.  The options are:
arctic, coastal, desert, forest, grassland, hill, mountain, swamp, underdark,
underwater, urban.

-n --name: A comma separated list of partial names for any monster you want in
the encounter. Use this option instead of environment.

-t --treasure: The type of treasure the monsters carry. Options are personal
and hoard. The personal treasure is rolled for each monster. The hoard is
rolled for the highest level monster, twice if it is legendary. If this option
is not set, no treasure is generated.

It is possible that the program won't be able to generate an encounter
sufficiently challanging for the number of monsters specified. In this case,
re-execute the program with more enemies until the encounter's xp threshold
matches the party's.

Some times the program may also generate an encounter with a monster that has
challange level greater than the avarage level of the party. Use the encounter
with discression.

## Examples:

- Genarate a deadly encounter for a party of levels 5, 5, 4 and 3.
```
py dnd_encounter.py --pc-levels 5,5,4,3 --difficulty deadly
```

- Generate a medium encounter with 1d4 forest monsters for a party of levels 1, 1, 2 and 3.
```
py dnd_encounter.py --pc-levels 1,1,2,3 --environment forest --monsters 1d4 --difficulty medium
```

```
- Generate a hard encounter of gnolls and worgs for a party of levels 4, 4, 4 and 5:
py dnd_encounter.py --pc-levels 4,4,4,5 --difficulty hard --name gnoll,worg
```
