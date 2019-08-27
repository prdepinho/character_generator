# character_generator
A random character generation program for D&amp;D 5E.

D&D is property of Wizard of the Coast. https://company.wizards.com/

# How to use:

Executing py dnd.char_py will generate a random character.
Optionally, you can input these arguments to control how the character should
be generated:

-c --class <class>: specify the class of the character.

-r --race <race>: specify the race.

-s --statistics <population>: this generates a population of characters and exhibit statistics about them. This option works with the others. This is also useful to know the exact string to use to specify race and class.

-b --background <bg>: specify background.

--max-abilities: roll 20 for all abilities.

--roll-four: roll four dice for abilities and take out the lowest. This is the default.

--roll-three: roll three dice for abilities.

--random-class: choose a trully random class.

--help: print help.

Note: The algorithm chooses a class that makes sense for the abilities rolled,
in order not to have a wizard with low intelligence, for example.  If you want
trully random class, though, then use the --random-class option.


# Example:

- Generate a Forest Gnome Fighter with the outlander background:
```
py dnd_char.py -c Fighter -r "Forest Gnome" -b Outlander
```
