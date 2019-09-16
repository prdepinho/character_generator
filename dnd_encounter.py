
from range_dict import RangeDict
from dnd_treasure import generate_personal_treasure, print_personal, generate_treasure_hoard, print_items
from dnd_dice import Dice, roll_from_list, roll
import statistics
import getopt
import sys


environments = [
        'arctic',
        'coastal',
        'desert',
        'forest',
        'grassland',
        'hill',
        'mountain',
        'swamp',
        'underdark',
        'underwater',
        'urban'
        ]

groups = [
        'bandits',
        'undead',
        'yuan-ti',
        'fire-elemental',
        'water-elemental',
        'air-elemental',
        'water-elementl',
        'golens',
        'sahuagin',
        'orcs',
        'myconids',
        'modrons',
        'kuo-toa',
        'draconic',
        'goblins',
        'gnolls',
        'gith',
        'giants',
        'spiders',
        'drow',
        'dinossaurs',
        'abysals',
        'celestials'
        ]

chosen = {
        'difficulty': 'medium',
        'pc-levels': [],
        'environment': '',
        'monsters': -1,
        'name': '',
        'treasure': ''
        }

if __name__ == "__main__":
    try:
        optlist, args = getopt.getopt(
                sys.argv[1:],
                'd:l:m:n:e:t:',
                ['difficulty=', 'pc-levels=', 'monsters=', 'name=', 'environment=', 'treasure=', 'help']
                )
    except getopt.GetooptError as e:
        print(e)
        exit()

    for o, a in optlist:
        if o in ['-d', '--difficulty']:
            chosen['difficulty'] = a.lower()
            if chosen['difficulty'] not in ['easy', 'medium', 'hard', 'deadly']:
                print('Difficulty options: easy, medium, hard, deadly.')
                exit()
        elif o in ['-l', '--pc-levels']:
            if a.isdigit():
                chosen['pc-levels'] = [int(a)]
            elif ',' in a:
                chosen['pc-levels'] = [int(n) for n in a.split(',')]
            elif ' ' in a:
                chosen['pc-levels'] = [int(n) for n in a.split(' ')]
            else:
                print('Please, either separate PC levels with commas, or, if inside double quotes, with spaces.')
                exit()
        elif o in ['-m', '--monsters']:
            if a.isdigit():
                chosen['monsters'] = int(a)
            else:
                chosen['monsters'] = Dice(a).roll()
            if chosen['monsters'] > 20:
                print('At most 20 monsters are permitted')
                exit()
        elif o in ['-n', '--name']:
            chosen['name'] = a.lower().split(',')
        elif o in ['-e', '--environment']:
            chosen['environment'] = a.lower()
            if chosen['environment'] not in environments:
                print('Environment options are: %s.' % str(environments))
                exit()
        elif o in ['-t', '--treasure']:
            chosen['treasure'] = a
            if chosen['treasure'] not in ['hoard', 'personal']:
                print('Options are hoard and personal')
                exit()
        elif o == '--help':
            print('Help')
            print('Exetute the program to generate a random encounter. The following options are available.')
            print('%-40s %s' % ('-d, --difficulty: [difficulty]', 'The difficulty of the encounter. The options are easy, medium, hard and deadly. The default is medium.'))
            print('%-40s %s' % ('-l, --pc-levels level1,level2,...', 'A comma separated list of player character levels. If you enclose the levels with double quotes, they may be separeted with spaces.'))
            print('%-40s %s' % ('-m, --monsters [number]', 'The number of monsters in the encounter. This may be represented in the dice notation, like 2d4+1, or as a number. If no value is specified, the size of the encounter is going to vary.'))
            print('%-40s %s' % ('-e, --environment [env]', 'The kind of environment in which the encounter takes place. If none is specified, monsters are taken from all environments. Options are: %s.' % str(environments)))
            print('%-40s %s' % ('-n, --name [name1,name2...]', 'Specify part of the name of the monster you want to use. Separate two or more names with a comma. Use this options instead of environment.'))
            print('%-40s %s' % ('-t, --treasure [type]', 'The kind of treasure that the monsters possess. Two types are available: personal and hoard. If none is set, then no treasure is rolled.'))
            exit()
        else:
            print('unhandled option: %s' % o)

threshold = {
        "easy": {
            1: 25,
            2: 50,
            3: 75,
            4: 125,
            5: 250,
            6: 300,
            7: 350,
            8: 450,
            9: 550,
            10: 600,
            11: 800,
            12: 1000,
            13: 1100,
            14: 1250,
            15: 1400,
            16: 1600,
            17: 2000,
            18: 2100,
            19: 2400,
            20: 2800
            },
        "medium": {
            1: 50,
            2: 100,
            3: 250,
            4: 250,
            5: 500,
            6: 600,
            7: 750,
            8: 900,
            9: 1100,
            10: 1200,
            11: 1600,
            12: 2000,
            13: 2200,
            14: 2500,
            15: 2800,
            16: 3200,
            17: 3900,
            18: 4200,
            19: 4900,
            20: 5700
            },
        "hard": {
            1: 75,
            2: 150,
            3: 225,
            4: 375,
            5: 750,
            6: 900,
            7: 1100,
            8: 1400,
            9: 1600,
            10: 1900,
            11: 2400,
            12: 3000,
            13: 3400,
            14: 3800,
            15: 4300,
            16: 4800,
            17: 5900,
            18: 6300,
            19: 7300,
            20: 8500
            },
        "deadly": {
            1: 100,
            2: 200,
            3: 400,
            4: 500,
            5: 1100,
            6: 1400,
            7: 1700,
            8: 2100,
            9: 2400,
            10: 2800,
            11: 3600,
            12: 4500,
            13: 5100,
            14: 5700,
            15: 6400,
            16: 7200,
            17: 8800,
            18: 9500,
            19: 10900,
            20: 12700
            }
        }

challange_xp_map = {
        0: 10,
        1/8: 25,
        1/4: 50,
        1/2: 100,
        1: 200,
        2: 450,
        3: 700,
        4: 1100,
        5: 1800,
        6: 2300,
        7: 2900,
        8: 3900,
        9: 5000,
        10: 5900,
        11: 7200,
        12: 8400,
        13: 10000,
        14: 11500,
        15: 13000,
        16: 15000,
        17: 18000,
        18: 20000,
        19: 22000,
        20: 25000,
        21: 33000,
        22: 41000,
        23: 50000,
        24: 62000,
        30: 155000
        }


short_party_multiplier = RangeDict()
short_party_multiplier.set(1,  1,   1.5)
short_party_multiplier.set(2,  2,   2)
short_party_multiplier.set(3,  6,   2.5)
short_party_multiplier.set(7,  10,  3)
short_party_multiplier.set(11, 100,  4)

encounter_multiplier = RangeDict()
encounter_multiplier.set(1,  1,   1)
encounter_multiplier.set(2,  2,   1.5)
encounter_multiplier.set(3,  6,   2)
encounter_multiplier.set(7,  10,  2.5)
encounter_multiplier.set(11, 14,  3)
encounter_multiplier.set(15, 100, 4)

large_party_multiplier = RangeDict()
large_party_multiplier.set(1,  2,   1)
large_party_multiplier.set(3,  6,   1.5)
large_party_multiplier.set(7,  10,  2)
large_party_multiplier.set(11, 14,  2.5)
large_party_multiplier.set(15, 100, 3)


def get_encounter_multiplier(party_size, monsters_size):
    if party_size <= 2:
        return short_party_multiplier.get(monsters_size)
    elif party_size in [3, 4, 5]:
        return encounter_multiplier.get(monsters_size)
    elif party_size >= 6:
        return large_party_multiplier.get(monsters_size)


class Monster:
    def __init__(self, name, cl, legendary=False):
        self.name = name
        self.xp = challange_xp_map[cl]
        self.cl = cl
        self.legendary = legendary


monsters = {
        "arctic": [
            Monster(name="Commoner", cl=0),
            Monster(name="Owl", cl=0),
            Monster(name="Bandit", cl=1/8),
            Monster(name="Blood hawk", cl=1/8),
            Monster(name="Kobold", cl=1/8),
            Monster(name="Tribal warrior", cl=1/8),
            Monster(name="Giant owl", cl=1/4),
            Monster(name="Winged kobold", cl=1/4),
            Monster(name="Ice mephit", cl=1/2),
            Monster(name="Orc", cl=1/2),
            Monster(name="Scout", cl=1/2),
            Monster(name="Brown bear", cl=1),
            Monster(name="Half-ogre", cl=1),
            Monster(name="Bandit captain", cl=2),
            Monster(name="Berserker", cl=2),
            Monster(name="Druid", cl=2),
            Monster(name="Griffon", cl=2),
            Monster(name="Ogre", cl=2),
            Monster(name="Orc Eye of Gruumsh", cl=2),
            Monster(name="Orog", cl=2),
            Monster(name="Polar bear", cl=2),
            Monster(name="Saber-toothed tiger", cl=2),
            Monster(name="Manticore", cl=3),
            Monster(name="Veteran", cl=3),
            Monster(name="Winter wolf", cl=3),
            Monster(name="Yeti", cl=3),
            Monster(name="Revenant", cl=5),
            Monster(name="Troll", cl=5),
            Monster(name="Werebear", cl=5),
            Monster(name="Young remorhaz", cl=5),
            Monster(name="Mammoth", cl=6),
            Monster(name="Young white dragon", cl=6),
            Monster(name="Frost giant", cl=8),
            Monster(name="Abominable yeti", cl=9),
            Monster(name="Remorhaz", cl=11),
            Monster(name="Roc", cl=11),
            Monster(name="Adult white dragon", cl=13),
            Monster(name="Ancient white dragon", cl=20)
            ],
        "coastal": [
            Monster(name="Commoner", cl=0),
            Monster(name="Crab", cl=1/8),
            Monster(name="Eagle", cl=1/8),
            Monster(name="Bandit", cl=1/8),
            Monster(name="Blood hawk", cl=1/8),
            Monster(name="Giant crab", cl=1/8),
            Monster(name="Guard", cl=1/8),
            Monster(name="Kobold", cl=1/8),
            Monster(name="Merfolk", cl=1/8),
            Monster(name="Poisonous snake", cl=1/8),
            Monster(name="Stirge", cl=1/8),
            Monster(name="Tribal warrior", cl=1/8),
            Monster(name="Giant lizzard", cl=1/4),
            Monster(name="Giant wolf spider", cl=1/4),
            Monster(name="Pseudodragon", cl=1/4),
            Monster(name="Pteranodon", cl=1/4),
            Monster(name="Winged kobold", cl=1/4),
            Monster(name="Sahuagin", cl=1/2),
            Monster(name="Scout", cl=1/2),
            Monster(name="Giant eagle", cl=1),
            Monster(name="Giant toad", cl=1),
            Monster(name="Harpy", cl=1),
            Monster(name="Bandit captain", cl=2),
            Monster(name="Berserker", cl=2),
            Monster(name="Druid", cl=2),
            Monster(name="Griffon", cl=2),
            Monster(name="Ogre", cl=2),
            Monster(name="Merrow", cl=2),
            Monster(name="Plesiosaurus", cl=2),
            Monster(name="Sahuagin priestess", cl=2),
            Monster(name="Sea hag", cl=2),
            Monster(name="Manticore", cl=3),
            Monster(name="Veteran", cl=3),
            Monster(name="Banshee", cl=4),
            Monster(name="Sahuagin baron", cl=5),
            Monster(name="Water elemental", cl=5),
            Monster(name="Cyclops", cl=6),
            Monster(name="Young bronze dragon", cl=8),
            Monster(name="Young blue dragon", cl=9),
            Monster(name="Djinni", cl=11),
            Monster(name="Marid", cl=11),
            Monster(name="Roc", cl=11),
            Monster(name="Storm giant", cl=13),
            Monster(name="Adult bronze dragon", cl=15),
            Monster(name="Adult blue dragon", cl=16),
            Monster(name="Dragon turtle", cl=17),
            Monster(name="Ancient bronze dragon", cl=22),
            Monster(name="Ancient blue dragon", cl=23)
            ],
        'desert': [
            Monster(name="Cat", cl=0),
            Monster(name="Commoner", cl=0),
            Monster(name="Hyena", cl=0),
            Monster(name="Jackal", cl=0),
            Monster(name="Scorpion", cl=0),
            Monster(name="Vulture", cl=0),
            Monster(name="Bantit", cl=1/8),
            Monster(name="Camel", cl=1/8),
            Monster(name="Flying snake", cl=1/8),
            Monster(name="Guard", cl=1/8),
            Monster(name="Kobolt", cl=1/8),
            Monster(name="Mule", cl=1/8),
            Monster(name="Poisonous snake", cl=1/8),
            Monster(name="Stirge", cl=1/8),
            Monster(name="Tribal warrior", cl=1/8),
            Monster(name="Constrictor snake", cl=1/4),
            Monster(name="Giant lizard", cl=1/4),
            Monster(name="Giant poisonous snake", cl=1/4),
            Monster(name="Giant wolf spider", cl=1/4),
            Monster(name="Pseudodragon", cl=1/4),
            Monster(name="Winged kobold", cl=1/4),
            Monster(name="Dust mephit", cl=1/2),
            Monster(name="Gnoll", cl=1/2),
            Monster(name="Hobgolin", cl=1/2),
            Monster(name="Jackalwere", cl=1/2),
            Monster(name="Scout", cl=1/2),
            Monster(name="Swarm of insects", cl=1/2),
            Monster(name="Death dog", cl=1),
            Monster(name="Giant hyena", cl=1),
            Monster(name="Giant spider", cl=1),
            Monster(name="Giant toad", cl=1),
            Monster(name="Giant vulture", cl=1),
            Monster(name="Half-ogre", cl=1),
            Monster(name="Lion", cl=1),
            Monster(name="Thri-kreen", cl=1),
            Monster(name="Yuan-ti pureblood", cl=1),
            Monster(name="Bandit captain", cl=2),
            Monster(name="Berserker", cl=2),
            Monster(name="Druid", cl=2),
            Monster(name="Giant constrictor snake", cl=2),
            Monster(name="Gnoll pack lord", cl=2),
            Monster(name="Ogre", cl=2),
            Monster(name="Giant scorpion", cl=3),
            Monster(name="Hobgoblin captain", cl=3),
            Monster(name="Mummy", cl=3),
            Monster(name="Phase spider", cl=3),
            Monster(name="Wight", cl=3),
            Monster(name="Yuan-ti malison", cl=3),
            Monster(name="Couatl", cl=4),
            Monster(name="Gnoll gant of Yeenoghu", cl=4),
            Monster(name="Lamia", cl=4),
            Monster(name="Weretiger", cl=4),
            Monster(name="Air elemental", cl=5),
            Monster(name="Fire elemental", cl=5),
            Monster(name="Revenant", cl=5),
            Monster(name="Cyclops", cl=6),
            Monster(name="Medusa", cl=6),
            Monster(name="Young brass dragon", cl=6),
            Monster(name="Yuan-ti abomination", cl=7),
            Monster(name="Young blue dragon", cl=9),
            Monster(name="Guardian naga", cl=10),
            Monster(name="Efreeti", cl=11),
            Monster(name="Gynosphinx", cl=11),
            Monster(name="Roc", cl=11),
            Monster(name="Adult brass dragon", cl=13),
            Monster(name="Mummy lord", cl=15),
            Monster(name="Purple worm", cl=15),
            Monster(name="Adult blue dragon", cl=16),
            Monster(name="Adult blue dracolich", cl=17, legendary=True),
            Monster(name="Androsphinx", cl=17),
            Monster(name="Ancient brass dragon", cl=20),
            Monster(name="Ancient blue dragon", cl=23),
            ],
        "forest": [
            Monster(name="Awakened shrub", cl=0),
            Monster(name="Baboon", cl=0),
            Monster(name="Badger", cl=0),
            Monster(name="Cat", cl=0),
            Monster(name="Commoner", cl=0),
            Monster(name="Deer", cl=0),
            Monster(name="Hyena", cl=0),
            Monster(name="Owl", cl=0),
            Monster(name="Bandit", cl=1/8),
            Monster(name="Blood hawk", cl=1/8),
            Monster(name="Flying snake", cl=1/8),
            Monster(name="Giant rat", cl=1/8),
            Monster(name="Giant weasel", cl=1/8),
            Monster(name="Guard", cl=1/8),
            Monster(name="Kobold", cl=1/8),
            Monster(name="Mastiff", cl=1/8),
            Monster(name="Poisonous snake", cl=1/8),
            Monster(name="Stirge", cl=1/8),
            Monster(name="Tribal warrior", cl=1/8),
            Monster(name="Twig blight", cl=1/8),
            Monster(name="Blink dog", cl=1/4),
            Monster(name="Boar", cl=1/4),
            Monster(name="Constrictor snake", cl=1/4),
            Monster(name="Elk", cl=1/4),
            Monster(name="Giant badger", cl=1/4),
            Monster(name="Giant bat", cl=1/4),
            Monster(name="Giant frog", cl=1/4),
            Monster(name="Giant lizard", cl=1/4),
            Monster(name="Giant owl", cl=1/4),
            Monster(name="Giant poisonous snake", cl=1/4),
            Monster(name="Giant wolf spider", cl=1/4),
            Monster(name="Goblin", cl=1/4),
            Monster(name="Kenku", cl=1/4),
            Monster(name="Needle blight", cl=1/4),
            Monster(name="Panther", cl=1/4),
            Monster(name="Pixie", cl=1/4),
            Monster(name="Pseudodragon", cl=1/4),
            Monster(name="Sprite", cl=1/4),
            Monster(name="Swarm of ravens", cl=1/4),
            Monster(name="Winged kobold", cl=1/4),
            Monster(name="Wolf", cl=1/4),
            Monster(name="Ape", cl=1/2),
            Monster(name="Black bear", cl=1/2),
            Monster(name="Giant wasp", cl=1/2),
            Monster(name="Gnoll", cl=1/2),
            Monster(name="Hobglobin", cl=1/2),
            Monster(name="Lizardfolk", cl=1/2),
            Monster(name="Orc", cl=1/2),
            Monster(name="Satyr", cl=1/2),
            Monster(name="Scout", cl=1/2),
            Monster(name="Swarm of insects", cl=1/2),
            Monster(name="Vine blight", cl=1/2),
            Monster(name="Worg", cl=1/2),
            Monster(name="Brown bear", cl=1),
            Monster(name="Bugbear", cl=1),
            Monster(name="Dire wolf", cl=1),
            Monster(name="Dryad", cl=1),
            Monster(name="Faerie dragon, yellow or younger", cl=1),
            Monster(name="Giant hyena", cl=1),
            Monster(name="Giant spider", cl=1),
            Monster(name="Giant toad", cl=1),
            Monster(name="Goblin boss", cl=1),
            Monster(name="Half-ogre", cl=1),
            Monster(name="Harpy", cl=1),
            Monster(name="Tiger", cl=1),
            Monster(name="Yuan-ti pureblood", cl=1),
            Monster(name="Ankheg", cl=2),
            Monster(name="Awakened tree", cl=2),
            Monster(name="Bandit captain", cl=2),
            Monster(name="Berserker", cl=2),
            Monster(name="Centaur", cl=2),
            Monster(name="Druid", cl=2),
            Monster(name="Ettercap", cl=2),
            Monster(name="Faerie dragon, green or older", cl=2),
            Monster(name="Giant boar", cl=2),
            Monster(name="Giant constrictor snake", cl=2),
            Monster(name="Giant elk", cl=2),
            Monster(name="Gnoll pack lord", cl=2),
            Monster(name="Grick", cl=2),
            Monster(name="Lizardfolk", cl=2),
            Monster(name="Shaman", cl=2),
            Monster(name="Ogre", cl=2),
            Monster(name="Orc Eye of Gruumsh", cl=2),
            Monster(name="Orog", cl=2),
            Monster(name="Pegasus", cl=2),
            Monster(name="Swarm of poisonous snakes", cl=2),
            Monster(name="Wererat", cl=2),
            Monster(name="Will-o'-wisp", cl=2),
            Monster(name="Displacer beast", cl=3),
            Monster(name="Green hag", cl=3),
            Monster(name="Hobgoblin captain", cl=3),
            Monster(name="Owlbear", cl=3),
            Monster(name="Phase spider", cl=3),
            Monster(name="Veteran", cl=3),
            Monster(name="Werewolf", cl=3),
            Monster(name="Yuan-ti malison", cl=3),
            Monster(name="Banshee", cl=4),
            Monster(name="Couatl", cl=4),
            Monster(name="Gnoll fang of Yeenoghu", cl=4),
            Monster(name="Wereboar", cl=4),
            Monster(name="Weretiger", cl=4),
            Monster(name="Gorgon", cl=5),
            Monster(name="Revenant", cl=5),
            Monster(name="Shambling mound", cl=5),
            Monster(name="Troll", cl=5),
            Monster(name="Unicorn", cl=5),
            Monster(name="Werebear", cl=5),
            Monster(name="Giant ape", cl=7),
            Monster(name="Grick alpha", cl=7),
            Monster(name="Oni", cl=7),
            Monster(name="Yuan-ti abomination", cl=7),
            Monster(name="Young green dragon", cl=8),
            Monster(name="Treant", cl=9),
            Monster(name="Guardian naga", cl=10),
            Monster(name="young gold dragon", cl=10),
            Monster(name="Adult green dragon", cl=15),
            Monster(name="Adult gold dragon", cl=17),
            Monster(name="Ancient green dragon", cl=22),
            Monster(name="Ancient gold dragon", cl=24)
            ],
        "grassland": [
            Monster(name="Cat", cl=0),
            Monster(name="Commoner", cl=0),
            Monster(name="Deer", cl=0),
            Monster(name="Eagle", cl=0),
            Monster(name="Goat", cl=0),
            Monster(name="Hyena", cl=0),
            Monster(name="Jackal", cl=0),
            Monster(name="Vulture", cl=0),
            Monster(name="Blood hawk", cl=1/8),
            Monster(name="Flying snake", cl=1/8),
            Monster(name="Giant weasel", cl=1/8),
            Monster(name="Guard", cl=1/8),
            Monster(name="Poisonous snake", cl=1/8),
            Monster(name="Stirge", cl=1/8),
            Monster(name="Tribal warrior", cl=1/8),
            Monster(name="Axe beak", cl=1/4),
            Monster(name="Boar", cl=1/4),
            Monster(name="Elk", cl=1/4),
            Monster(name="Giant poisonous", cl=1/4),
            Monster(name="Snake", cl=1/4),
            Monster(name="Giant wolf spider", cl=1/4),
            Monster(name="Goblin", cl=1/4),
            Monster(name="Panther (leopard)", cl=1/4),
            Monster(name="Pteranodon", cl=1/4),
            Monster(name="Riding horse", cl=1/4),
            Monster(name="Wolf", cl=1/4),
            Monster(name="Cockatrice", cl=1/2),
            Monster(name="Giant goat", cl=1/2),
            Monster(name="Giant wasp", cl=1/2),
            Monster(name="Gnoll", cl=1/2),
            Monster(name="Hobgoblin", cl=1/2),
            Monster(name="Jackalwere", cl=1/2),
            Monster(name="Orc", cl=1/2),
            Monster(name="Scout", cl=1/2),
            Monster(name="Swarm of insects", cl=1/2),
            Monster(name="Worg", cl=1/2),
            Monster(name="Bugbear", cl=1),
            Monster(name="Giant eagle", cl=1),
            Monster(name="Giant hyena", cl=1),
            Monster(name="Giant bulture", cl=1),
            Monster(name="Goblin boss", cl=1),
            Monster(name="Hippogriff", cl=1),
            Monster(name="Lion", cl=1),
            Monster(name="Scarecrow", cl=1),
            Monster(name="Thri-kreen", cl=1),
            Monster(name="Tiger", cl=1),
            Monster(name="Allosaurus", cl=2),
            Monster(name="Ankheg", cl=2),
            Monster(name="Centaur", cl=2),
            Monster(name="Druid", cl=2),
            Monster(name="Giant boar", cl=2),
            Monster(name="Giant elk", cl=2),
            Monster(name="Gnoll pack lord", cl=2),
            Monster(name="Griffon", cl=2),
            Monster(name="Ogre", cl=2),
            Monster(name="Orc Eye of Gruumsh", cl=2),
            Monster(name="Orog", cl=2),
            Monster(name="Pegasus", cl=2),
            Monster(name="Rhinoceros", cl=2),
            Monster(name="Ankylosaurus", cl=3),
            Monster(name="Hobgoblin captain", cl=3),
            Monster(name="Manticore", cl=3),
            Monster(name="Phase spider", cl=3),
            Monster(name="Veteran", cl=3),
            Monster(name="Couatl", cl=4),
            Monster(name="Elephant", cl=4),
            Monster(name="Gnoll fang of Yeenoghu", cl=4),
            Monster(name="Wereboar", cl=4),
            Monster(name="Weretiger", cl=4),
            Monster(name="Bulette", cl=5),
            Monster(name="Gorgon", cl=5),
            Monster(name="Triceratops", cl=5),
            Monster(name="Chimera", cl=6),
            Monster(name="Cyclops", cl=6),
            Monster(name="Tyrannosaururs Rex", cl=8),
            Monster(name="Young gold dragon", cl=10),
            Monster(name="Adult gold dragon", cl=17),
            Monster(name="Ancient gold dragon", cl=24)
            ],
        "hill": [
            Monster(name="Baboon", cl=0),
            Monster(name="Commoner", cl=0),
            Monster(name="Eagle", cl=0),
            Monster(name="Goat", cl=0),
            Monster(name="Hyena", cl=0),
            Monster(name="Raven", cl=0),
            Monster(name="Vulture", cl=0),
            Monster(name="Bandit", cl=1/8),
            Monster(name="Blood hawk", cl=1/8),
            Monster(name="Giant weasel", cl=1/8),
            Monster(name="Guard", cl=1/8),
            Monster(name="Kobold", cl=1/8),
            Monster(name="Mastiff", cl=1/8),
            Monster(name="Mule", cl=1/8),
            Monster(name="Poisonous snake", cl=1/8),
            Monster(name="Stirge", cl=1/8),
            Monster(name="Tribal warrior", cl=1/8),
            Monster(name="Axe beak", cl=1/4),
            Monster(name="Boar", cl=1/4),
            Monster(name="Elk", cl=1/4),
            Monster(name="Giant owl", cl=1/4),
            Monster(name="Giant wolf spider", cl=1/4),
            Monster(name="Goblin", cl=1/4),
            Monster(name="Panther (cougar)", cl=1/4),
            Monster(name="Pseudodragon", cl=1/4),
            Monster(name="Swarm of bats", cl=1/4),
            Monster(name="Swarm of ravens", cl=1/4),
            Monster(name="Winged kobol", cl=1/4),
            Monster(name="Wolf", cl=1/4),
            Monster(name="Giant goat", cl=1/2),
            Monster(name="Gnoll", cl=1/2),
            Monster(name="Hobgoblin", cl=1/2),
            Monster(name="Orc", cl=1/2),
            Monster(name="Scout", cl=1/2),
            Monster(name="Swarm of insects", cl=1/2),
            Monster(name="Worg", cl=1/2),
            Monster(name="Brown bear", cl=1),
            Monster(name="Dire wolf", cl=1),
            Monster(name="Giant eagle", cl=1),
            Monster(name="Giant hyena", cl=1),
            Monster(name="Goblin boss", cl=1),
            Monster(name="Half-ogre", cl=1),
            Monster(name="Harpy", cl=1),
            Monster(name="Hippogriff", cl=1),
            Monster(name="Lion", cl=1),
            Monster(name="Bandit captain", cl=2),
            Monster(name="Berserker", cl=2),
            Monster(name="Druid", cl=2),
            Monster(name="Giant boar", cl=2),
            Monster(name="Giant elk", cl=2),
            Monster(name="Gnoll pack lord", cl=2),
            Monster(name="Griffon", cl=2),
            Monster(name="Ogre", cl=2),
            Monster(name="Orc Eye of Gruumsh", cl=2),
            Monster(name="Orog", cl=2),
            Monster(name="Pegasus", cl=2),
            Monster(name="Peryton", cl=2),
            Monster(name="Green hag", cl=3),
            Monster(name="Hobgoblin captain", cl=3),
            Monster(name="Manticore", cl=3),
            Monster(name="Phase spider", cl=3),
            Monster(name="Veteran", cl=3),
            Monster(name="Werewolf", cl=3),
            Monster(name="Ettin", cl=4),
            Monster(name="Gnoll fang of Yeenoghu", cl=4),
            Monster(name="Wereboar", cl=4),
            Monster(name="Bulette", cl=5),
            Monster(name="Gorgon", cl=5),
            Monster(name="Hill giant", cl=5),
            Monster(name="Revenant", cl=5),
            Monster(name="Troll", cl=5),
            Monster(name="Werebear", cl=5),
            Monster(name="Chimera", cl=6),
            Monster(name="Cyclops", cl=6),
            Monster(name="Galeb duhr", cl=6),
            Monster(name="Wyvern", cl=6),
            Monster(name="Stone giant", cl=7),
            Monster(name="young copper dragon", cl=7),
            Monster(name="Young red dragon", cl=10),
            Monster(name="Roc", cl=11),
            Monster(name="Adult copper dragon", cl=14),
            Monster(name="Adult red dragon", cl=17),
            Monster(name="Anccient copper dragon", cl=21),
            Monster(name="Ancient red dragon", cl=24)
            ],
        "mountain": [
            Monster(name="Eagle", cl=0),
            Monster(name="Goat", cl=0),
            Monster(name="Blood hawk", cl=1/8),
            Monster(name="Guard", cl=1/8),
            Monster(name="Kobold", cl=1/8),
            Monster(name="Stirge", cl=1/8),
            Monster(name="Tribal warrior", cl=1/8),
            Monster(name="Aarakocra", cl=1/4),
            Monster(name="Psaudodragon", cl=1/4),
            Monster(name="Pteranodon", cl=1/4),
            Monster(name="Swarm of bats", cl=1/4),
            Monster(name="Winged kobold", cl=1/4),
            Monster(name="Giant goat", cl=1/2),
            Monster(name="Orc", cl=1/2),
            Monster(name="Scout", cl=1/2),
            Monster(name="Giant eagle", cl=1),
            Monster(name="Half-ogre", cl=1),
            Monster(name="harpy", cl=1),
            Monster(name="Hippogriff", cl=1),
            Monster(name="Lion", cl=1),
            Monster(name="Berserker", cl=2),
            Monster(name="Druid", cl=2),
            Monster(name="Giant elk", cl=2),
            Monster(name="Griffon", cl=2),
            Monster(name="Ogre", cl=2),
            Monster(name="Orc Eye of Gruumsh", cl=2),
            Monster(name="Orog", cl=2),
            Monster(name="Peryton", cl=2),
            Monster(name="Saber-toothed tiger", cl=2),
            Monster(name="Basilisk", cl=3),
            Monster(name="Hell hound", cl=3),
            Monster(name="Manticore", cl=3),
            Monster(name="Veteran", cl=3),
            Monster(name="Ettin", cl=4),
            Monster(name="Air elemental", cl=5),
            Monster(name="Bulette", cl=5),
            Monster(name="Troll", cl=5),
            Monster(name="Chimera", cl=6),
            Monster(name="Cyclops", cl=6),
            Monster(name="Galeb duhr", cl=6),
            Monster(name="Wyvern", cl=6),
            Monster(name="Stone giant", cl=7),
            Monster(name="Frost giant", cl=8),
            Monster(name="Cloud giant", cl=9),
            Monster(name="Fire giant", cl=9),
            Monster(name="Young silver dragon", cl=9),
            Monster(name="Young red dragon", cl=10),
            Monster(name="Roc", cl=11),
            Monster(name="Adult silver dragon", cl=16),
            Monster(name="Adult red dragon", cl=17),
            Monster(name="Ancient silver dragon", cl=23),
            Monster(name="Ancient red dragon", cl=24)
            ],
        "swamp": [
            Monster(name="Rat", cl=0),
            Monster(name="Raven", cl=0),
            Monster(name="Giant rat", cl=1/8),
            Monster(name="Kobold", cl=1/8),
            Monster(name="Poisonous snake", cl=1/8),
            Monster(name="Stirge", cl=1/8),
            Monster(name="Tribal warrior", cl=1/8),
            Monster(name="Bullywug", cl=1/4),
            Monster(name="Constrictor snake", cl=1/4),
            Monster(name="Giant frog", cl=1/4),
            Monster(name="Giant lizard", cl=1/4),
            Monster(name="Giant poisonous snake", cl=1/4),
            Monster(name="Mud mephit", cl=1/4),
            Monster(name="Swarm of rats", cl=1/4),
            Monster(name="Swarm of ravens", cl=1/4),
            Monster(name="Winged kobold", cl=1/4),
            Monster(name="Crocodile", cl=1/2),
            Monster(name="Lizardfold", cl=1/2),
            Monster(name="Orc", cl=1/2),
            Monster(name="Scout", cl=1/2),
            Monster(name="Swarm of insects", cl=1/2),
            Monster(name="Ghoul", cl=1),
            Monster(name="Giant spider", cl=1),
            Monster(name="Giant toad", cl=1),
            Monster(name="Yuan-ti pureblood", cl=1),
            Monster(name="Druid", cl=2),
            Monster(name="Ghast", cl=2),
            Monster(name="Giant constrictor snake", cl=2),
            Monster(name="Lizardfold shaman", cl=2),
            Monster(name="Ogre", cl=2),
            Monster(name="Orc Eye of Gruumsh", cl=2),
            Monster(name="Swarm of poisonous snakes", cl=2),
            Monster(name="Will-o'-wisp", cl=2),
            Monster(name="Green hag", cl=3),
            Monster(name="Wight", cl=3),
            Monster(name="Yuan-ti malison", cl=3),
            Monster(name="Giant crocodile", cl=5),
            Monster(name="Revenant", cl=5),
            Monster(name="Shambling mound", cl=5),
            Monster(name="Troll", cl=5),
            Monster(name="Water elemental", cl=5),
            Monster(name="Young black dragon", cl=7),
            Monster(name="Yuan-ti abomination", cl=7),
            Monster(name="Hydra", cl=8),
            Monster(name="Adult black dragon", cl=14),
            Monster(name="Ancient black dragon", cl=21)
            ],
        "underdark": [
            Monster(name="Giant fire beetle", cl=0),
            Monster(name="Shrieker", cl=0),
            Monster(name="Myconid sprout", cl=0),
            Monster(name="Flumph", cl=1/8),
            Monster(name="Giant rat", cl=1/8),
            Monster(name="Kobold", cl=1/8),
            Monster(name="Stirge", cl=1/8),
            Monster(name="Tribal warrior", cl=1/8),
            Monster(name="Drow", cl=1/4),
            Monster(name="Giant bat", cl=1/4),
            Monster(name="Giant centipede", cl=1/4),
            Monster(name="Giant lizard", cl=1/4),
            Monster(name="Giant poisonous snake", cl=1/4),
            Monster(name="Goblin", cl=1/4),
            Monster(name="Grimlock", cl=1/4),
            Monster(name="Kuo-toa", cl=1/4),
            Monster(name="Swarm of bats", cl=1/4),
            Monster(name="Trogodyte", cl=1/4),
            Monster(name="Violet fungus", cl=1/4),
            Monster(name="Winged kobold", cl=1/4),
            Monster(name="Darkmantle", cl=1/2),
            Monster(name="Deep gnome", cl=1/2),
            Monster(name="Gas spore", cl=1/2),
            Monster(name="Gray ooze", cl=1/2),
            Monster(name="Hobgoblin", cl=1/2),
            Monster(name="Magma mephit", cl=1/2),
            Monster(name="Myconid adult", cl=1/2),
            Monster(name="Orc", cl=1/2),
            Monster(name="Piercer", cl=1/2),
            Monster(name="Rust monster", cl=1/2),
            Monster(name="Scout", cl=1/2),
            Monster(name="Shadow", cl=1/2),
            Monster(name="Swarm of insects", cl=1/2),
            Monster(name="Bugbear", cl=1),
            Monster(name="Duergar", cl=1),
            Monster(name="Fire snake", cl=1),
            Monster(name="Ghoul", cl=1),
            Monster(name="Giant spider", cl=1),
            Monster(name="Giant toad", cl=1),
            Monster(name="Goblin boss", cl=1),
            Monster(name="Half-ogre", cl=1),
            Monster(name="Kuo-toa whip", cl=1),
            Monster(name="Quaggoth", cl=1),
            Monster(name="Spore servant", cl=1),
            Monster(name="Specter", cl=1),
            Monster(name="Carrion crawler", cl=2),
            Monster(name="Druid", cl=2),
            Monster(name="Gargoyle", cl=2),
            Monster(name="Gelatinous cube", cl=2),
            Monster(name="Ghast", cl=2),
            Monster(name="Giant constrictor snake", cl=2),
            Monster(name="Gibbering mouther", cl=2),
            Monster(name="Grick", cl=2),
            Monster(name="Intellect devourer", cl=2),
            Monster(name="Mimic", cl=2),
            Monster(name="Minotaur skeleton", cl=2),
            Monster(name="Nothic", cl=2),
            Monster(name="Ochre jelly", cl=2),
            Monster(name="Ogre", cl=2),
            Monster(name="Orc Eye of Gruumsh", cl=2),
            Monster(name="Orog", cl=2),
            Monster(name="Polar bear (cave bear)", cl=2),
            Monster(name="Quaggoth", cl=2),
            Monster(name="Doppelganger", cl=3),
            Monster(name="Grell", cl=3),
            Monster(name="Hobgoblin captain", cl=3),
            Monster(name="Hell hound", cl=3),
            Monster(name="Hook horror", cl=3),
            Monster(name="Kuo-toa monitor", cl=3),
            Monster(name="Minotaur", cl=3),
            Monster(name="Quaggoth thonot", cl=3),
            Monster(name="Phase spider", cl=3),
            Monster(name="Spectator", cl=3),
            Monster(name="Veteran", cl=3),
            Monster(name="Water weird", cl=3),
            Monster(name="Wight", cl=3),
            Monster(name="Black pudding", cl=4),
            Monster(name="Bone naga", cl=4),
            Monster(name="Chuul", cl=4),
            Monster(name="Ettin", cl=4),
            Monster(name="Flameskull", cl=4),
            Monster(name="Ghost", cl=4),
            Monster(name="Beholder zombie", cl=5),
            Monster(name="Drow elite warrior", cl=5),
            Monster(name="Earth elemental", cl=5),
            Monster(name="Otyugh", cl=5),
            Monster(name="Roper", cl=5),
            Monster(name="Salamander", cl=5),
            Monster(name="Troll", cl=5),
            Monster(name="Umber hulk", cl=5),
            Monster(name="Vampire spawn", cl=5),
            Monster(name="Wraith", cl=5),
            Monster(name="Xorn", cl=5),
            Monster(name="Chimera", cl=6),
            Monster(name="Cyclops", cl=6),
            Monster(name="Drider", cl=6),
            Monster(name="Drow mage", cl=7),
            Monster(name="Grick alpha", cl=7),
            Monster(name="Mind flayer", cl=7),
            Monster(name="Stone giant", cl=7),
            Monster(name="Cloaker", cl=8),
            Monster(name="Fomorian", cl=8),
            Monster(name="Mind flayer arcanist", cl=8),
            Monster(name="Spirit naga", cl=8),
            Monster(name="Fire giant", cl=9),
            Monster(name="Aboleth", cl=10),
            Monster(name="Behir", cl=11),
            Monster(name="Dao", cl=11),
            Monster(name="Beholder", cl=13),
            Monster(name="Young red shadow dragon", cl=13),
            Monster(name="Death tyrant", cl=14),
            Monster(name="Purple worm", cl=15)
            ],
        "underwater": [
            Monster(name="Quipper", cl=0),
            Monster(name="Merfolk", cl=1/8),
            Monster(name="Constrictor snake", cl=1/4),
            Monster(name="Steam mephit", cl=1/4),
            Monster(name="Giant sea horse", cl=1/2),
            Monster(name="Reef shark", cl=1/2),
            Monster(name="Sahuagin", cl=1/2),
            Monster(name="Giant octopus", cl=1),
            Monster(name="Swarm of quippers", cl=1),
            Monster(name="Giant constrictor snake", cl=2),
            Monster(name="Hunter shark", cl=2),
            Monster(name="Merrow", cl=2),
            Monster(name="Plesiosaurus", cl=2),
            Monster(name="Sahuagin priestess", cl=2),
            Monster(name="Sea hag", cl=2),
            Monster(name="Killer whale", cl=3),
            Monster(name="Giant shark", cl=5),
            Monster(name="Sahuagin baron", cl=5),
            Monster(name="Water elemental", cl=5),
            Monster(name="Marid", cl=11),
            Monster(name="Storm giant", cl=13),
            Monster(name="Dragon turtle", cl=17),
            Monster(name="Kraken", cl=23),
            ],
        "urban": [
            Monster(name="Cat", cl=0),
            Monster(name="Commoner", cl=0),
            Monster(name="Goat", cl=0),
            Monster(name="Rat", cl=0),
            Monster(name="Raven", cl=0),
            Monster(name="Bandit", cl=1/8),
            Monster(name="Cultist", cl=1/8),
            Monster(name="Flying snake", cl=1/8),
            Monster(name="Giant rat", cl=1/8),
            Monster(name="Guard", cl=1/8),
            Monster(name="Kobold", cl=1/8),
            Monster(name="Mastiff", cl=1/8),
            Monster(name="Mule", cl=1/8),
            Monster(name="Noble", cl=1/8),
            Monster(name="Pony", cl=1/8),
            Monster(name="Stirge", cl=1/8),
            Monster(name="Acolyte", cl=1/4),
            Monster(name="draft horse", cl=1/4),
            Monster(name="Giant centipede", cl=1/4),
            Monster(name="Giant poisonous snake", cl=1/4),
            Monster(name="Kenku", cl=1/4),
            Monster(name="Pseudodragon", cl=1/4),
            Monster(name="Riding horse", cl=1/4),
            Monster(name="Skeleton", cl=1/4),
            Monster(name="Smoke mephit", cl=1/4),
            Monster(name="Swarm of bats", cl=1/4),
            Monster(name="Swarm of rats", cl=1/4),
            Monster(name="Swarm of ravens", cl=1/4),
            Monster(name="Winged kobold", cl=1/4),
            Monster(name="Zombie", cl=1/4),
            Monster(name="Crocodile", cl=1/2),
            Monster(name="Giant wasp", cl=1/2),
            Monster(name="Shadow", cl=1/2),
            Monster(name="Swarm of insects", cl=1/2),
            Monster(name="Thug", cl=1/2),
            Monster(name="Warhorse", cl=1/2),
            Monster(name="Ghoul", cl=1),
            Monster(name="Giant spider", cl=1),
            Monster(name="Half-ogre", cl=1),
            Monster(name="Specter", cl=1),
            Monster(name="Spy", cl=1),
            Monster(name="Yuan-ti pureblood", cl=1),
            Monster(name="Bandit captain", cl=2),
            Monster(name="Cult fanatic", cl=2),
            Monster(name="Gargoyle", cl=2),
            Monster(name="Ghast", cl=2),
            Monster(name="Mimic", cl=2),
            Monster(name="Priest", cl=2),
            Monster(name="Wererat", cl=2),
            Monster(name="Will-o'-wisp", cl=2),
            Monster(name="Doppelganger", cl=3),
            Monster(name="Knight", cl=3),
            Monster(name="Phase spider", cl=3),
            Monster(name="Veteran", cl=3),
            Monster(name="Water weird", cl=3),
            Monster(name="Wight", cl=3),
            Monster(name="Couatl", cl=4),
            Monster(name="Ghost", cl=4),
            Monster(name="Succubus or incubus", cl=4),
            Monster(name="Cambion", cl=5),
            Monster(name="Gladiator", cl=5),
            Monster(name="Revenant", cl=5),
            Monster(name="Vampire spawn", cl=5),
            Monster(name="Invisible stalker", cl=6),
            Monster(name="Mage", cl=6),
            Monster(name="Oni", cl=7),
            Monster(name="Shield guardian", cl=7),
            Monster(name="Assassin", cl=8),
            Monster(name="Gray slaad", cl=9),
            Monster(name="Young silver dragon", cl=9),
            Monster(name="Archmage", cl=12),
            Monster(name="Rakshasa", cl=13),
            Monster(name="Vampire", cl=13),
            Monster(name="Spellcaster or warrior vampire", cl=15),
            Monster(name="Adult silver dragon", cl=16),
            Monster(name="Ancient silver dragon", cl=23),
            Monster(name="Tarrasque", cl=30)
            ]
        }

all_monsters = []
for m in monsters:
    all_monsters.extend(monsters[m])
all_monsters = list(set(all_monsters))


all_monsters = {
        Monster(name="Aarakocra", cl=1/4),
        Monster(name="Aboleth", cl=10, legendary=True),
        Monster(name="Deva", cl=10),
        Monster(name="Planetar", cl=16),
        Monster(name="Solar", cl=21, legendary=True),
        Monster(name="Animated Armor", cl=1),
        Monster(name="Flying Sword", cl=1/4),
        Monster(name="Ankheg", cl=2),
        Monster(name="Azer", cl=2),
        Monster(name="Banshee", cl=4),
        Monster(name="Basilisk", cl=3),
        Monster(name="Behir", cl=11),
        Monster(name="Beholder", cl=13, legendary=True),
        Monster(name="Death Tyrant", cl=14, legendary=True),
        Monster(name="Spectator", cl=3),
        Monster(name="Needle Blight", cl=1/4),
        Monster(name="Twig Blight", cl=1/8),
        Monster(name="Vine Blight", cl=1/2),
        Monster(name="Bugbear", cl=1),
        Monster(name="Bugbear Chief", cl=3),
        Monster(name="Bulette", cl=5),
        Monster(name="Bullywug", cl=1/4),
        Monster(name="Cambion", cl=5),
        Monster(name="Carrion Crawler", cl=2),
        Monster(name="Centaur", cl=2),
        Monster(name="Chimera", cl=6),
        Monster(name="Chuul", cl=4),
        Monster(name="Cloaker", cl=8),
        Monster(name="Cockatrice", cl=1/2),
        Monster(name="Couatl", cl=4),
        Monster(name="Crawling Claw", cl=0),
        Monster(name="Cyclops", cl=6),
        Monster(name="Darkmantle", cl=1/2),
        Monster(name="Death Knight", cl=17),
        Monster(name="Demilich", cl=18, legendary=True),
        Monster(name="Balor", cl=19),
        Monster(name="Barlgura", cl=5),
        Monster(name="Chasme", cl=6),
        Monster(name="Dretch", cl=1/4),
        Monster(name="Glabrezu", cl=9),
        Monster(name="Goristro", cl=17),
        Monster(name="Hezrou", cl=8),
        Monster(name="Marilith", cl=16),
        Monster(name="Nalfeshnee", cl=13),
        Monster(name="Quasit", cl=1),
        Monster(name="Shadow Demon", cl=4),
        Monster(name="Vrock", cl=6),
        Monster(name="Yochlol", cl=10),
        Monster(name="Barbed Devil", cl=5),
        Monster(name="Bearded Debil", cl=3),
        Monster(name="Bone Devil", cl=9),
        Monster(name="Chain Devil", cl=8),
        Monster(name="Erinyes", cl=12),
        Monster(name="Horned Devil", cl=11),
        Monster(name="Ice Devil", cl=14),
        Monster(name="Imp", cl=1),
        Monster(name="Lemure", cl=0),
        Monster(name="Pit Fiend", cl=20),
        Monster(name="Spined Devil", cl=2),
        Monster(name="Allossaururs", cl=2),
        Monster(name="Ankylosaurus", cl=3),
        Monster(name="Plesiosaurus", cl=2),
        Monster(name="Triceratops", cl=5),
        Monster(name="Pteranodon", cl=1/4),
        Monster(name="Tyrannosaurus Red", cl=8),
        Monster(name="Displacer Beast", cl=3),
        Monster(name="Doppelganger", cl=3),
        Monster(name="Adult Blue Dracolich", cl=17, legendary=True),
        Monster(name="Young Red Shadow Dragon", cl=13),
        Monster(name="Ancient Black Dragon", cl=21, legendary=True),
        Monster(name="Adult Black Dragon", cl=14, legendary=True),
        Monster(name="Young Black Dragon", cl=7),
        Monster(name="Black Dragon Wyrmling", cl=2),
        Monster(name="Ancient Blue Dragon", cl=23, legendary=True),
        Monster(name="Adult Blue Dragon", cl=16, legendary=True),
        Monster(name="Young Blue Dragon", cl=9),
        Monster(name="Blue Dragon Wyrmling", cl=3),
        Monster(name="Ancient Green Dragon", cl=22, legendary=True),
        Monster(name="Adult Green Dragon", cl=15, legendary=True),
        Monster(name="Young Green Dragon", cl=8),
        Monster(name="Green Dragon Wyrmling", cl=2),
        Monster(name="Ancient Red Dragon", cl=24, legendary=True),
        Monster(name="Adult Red Dragon", cl=17, legendary=True),
        Monster(name="Young Red Dragon", cl=10),
        Monster(name="Red Dragon Wyrmling", cl=4),
        Monster(name="Ancient White Dragon", cl=20, legendary=True),
        Monster(name="Adult White Dragon", cl=13, legendary=True),
        Monster(name="Young White Dragon", cl=6),
        Monster(name="Whiat Dragon Wyrmling", cl=2),
        Monster(name="Ancient Brass Dragon", cl=20, legendary=True),
        Monster(name="Adult Brass Dragon", cl=13, legendary=True),
        Monster(name="Young Brass Dragon", cl=6),
        Monster(name="Brass Dragon Wyrmling", cl=1),
        Monster(name="Ancient Bronze Dragon", cl=22, legendary=True),
        Monster(name="Adult Bronze Dragon", cl=15, legendary=True),
        Monster(name="Young Bronze Dragon", cl=8),
        Monster(name="Bronze Dragon Wyrmling", cl=2),
        Monster(name="Ancient Copper Dragon", cl=21, legendary=True),
        Monster(name="Adult Copper Dragon", cl=14, legendary=True),
        Monster(name="Young Copper Dragon", cl=7),
        Monster(name="Copper Dragon Wyrmling", cl=1),
        Monster(name="Ancient Gold Dragon", cl=24, legendary=True),
        Monster(name="Adult Gold Dragon", cl=17, legendary=True),
        Monster(name="Young Gold Dragon", cl=10),
        Monster(name="Gold Dragon Wyrmling", cl=3),
        Monster(name="Ancient Silver Dragon", cl=23, legendary=True),
        Monster(name="Adult Silver Dragon", cl=16, legendary=True),
        Monster(name="Young Silver Dragon", cl=9),
        Monster(name="Silver Dragon Wyrmling", cl=2),
        Monster(name="Dragon Turtle", cl=17),
        Monster(name="Drider", cl=6),
        Monster(name="Dryad", cl=1),
        Monster(name="Duergar", cl=1),
        Monster(name="Air Elemental", cl=5),
        Monster(name="Earth Elemental", cl=5),
        Monster(name="Fire Elemental", cl=5),
        Monster(name="Water Elemental", cl=5),
        Monster(name="Drow", cl=1/4),
        Monster(name="Drow Elite Warrior", cl=5),
        Monster(name="Drow Mage", cl=7),
        Monster(name="Drow Priestess of Lolth", cl=8),
        Monster(name="Empyrean", cl=23, legendary=True),
        Monster(name="Ettercap", cl=2),
        Monster(name="Ettin", cl=4),
        Monster(name="Faerie Dragon (Yellow or younger)", cl=1),
        Monster(name="Faerie Dragon (Green or older)", cl=2),
        Monster(name="Flameskull", cl=4),
        Monster(name="Flumph", cl=1/8),
        Monster(name="Fomorian", cl=8),
        Monster(name="Gas Spore", cl=1/2),
        Monster(name="Shrieker", cl=0),
        Monster(name="Violet Fungus", cl=1/4),
        Monster(name="Galeb Duhr", cl=6),
        Monster(name="Gargoyle", cl=2),
        Monster(name="Dao", cl=11),
        Monster(name="Djinni", cl=11),
        Monster(name="Efreeti", cl=11),
        Monster(name="Marid", cl=11),
        Monster(name="Ghost", cl=4),
        Monster(name="Ghast", cl=2),
        Monster(name="Ghoul", cl=1),
        Monster(name="Cloud Giant", cl=9),
        Monster(name="Fire Giant", cl=9),
        Monster(name="Frost Giant", cl=8),
        Monster(name="Hill Giant", cl=5),
        Monster(name="Stone Giant", cl=7),
        Monster(name="Storm Giant", cl=13),
        Monster(name="Gibbering Mouther", cl=2),
        Monster(name="Githyanki Warrior", cl=3),
        Monster(name="Githyanki Knight", cl=8),
        Monster(name="Githzerai Monk", cl=2),
        Monster(name="Githzerai Zerth", cl=6),
        Monster(name="Gnoll", cl=1/2),
        Monster(name="Gnoll Pack Lord", cl=2),
        Monster(name="Gnoll Fang of Yeenoghu", cl=4),
        Monster(name="Deep Gnome", cl=1/2),
        Monster(name="Goblin", cl=1/4),
        Monster(name="Goblin Boss", cl=1),
        Monster(name="Clay Golem", cl=9),
        Monster(name="Flesh Golem", cl=5),
        Monster(name="Iron Golem", cl=16),
        Monster(name="Stone Golem", cl=10),
        Monster(name="Gorgon", cl=5),
        Monster(name="Grell", cl=3),
        Monster(name="Grick", cl=2),
        Monster(name="Grick Alpha", cl=7),
        Monster(name="Griffon", cl=2),
        Monster(name="Grimlock", cl=1/4),
        Monster(name="Green Hag", cl=3),
        Monster(name="Night Hag", cl=5),
        Monster(name="Sea Hag", cl=2),
        Monster(name="Half-Red Dragon Veteran", cl=5),
        Monster(name="Harpy", cl=1),
        Monster(name="Hell Hound", cl=3),
        Monster(name="Helmed Horror", cl=4),
        Monster(name="Hippogriff", cl=1),
        Monster(name="Hobgoblin", cl=1/2),
        Monster(name="Hobgoblin Captain", cl=3),
        Monster(name="Hobgoblin Warlord", cl=6),
        Monster(name="Homunculus", cl=0),
        Monster(name="Hook Horror", cl=3),
        Monster(name="Hydra", cl=8),
        Monster(name="Intellect Devourer", cl=2),
        Monster(name="Invisible Stalker", cl=6),
        Monster(name="Jackalwere", cl=1/2),
        Monster(name="Kenku", cl=1/4),
        Monster(name="Winged Kobold", cl=1/4),
        Monster(name="Kobold", cl=1/8),
        Monster(name="Kraken", cl=23, legendary=True),
        Monster(name="Kuo-Toa", cl=1/4),
        Monster(name="Kuo-Toa Archpriest", cl=6),
        Monster(name="Kuo-Toa Whip", cl=1),
        Monster(name="Lamia", cl=4),
        Monster(name="Lich", cl=21, legendary=True),
        Monster(name="Lizardfolk", cl=1/2),
        Monster(name="Lizardfold Shaman", cl=2),
        Monster(name="Lizard King/Queen", cl=4),
        Monster(name="Werebear", cl=5),
        Monster(name="Wereboar", cl=4),
        Monster(name="Wererat", cl=2),
        Monster(name="Weretiger", cl=4),
        Monster(name="Werewolf", cl=3),
        Monster(name="Magmin", cl=1/2),
        Monster(name="Manticore", cl=3),
        Monster(name="Medusa", cl=6),
        Monster(name="Dust Mephit", cl=1/2),
        Monster(name="Ice Mephit", cl=1/2),
        Monster(name="Magma Mephit", cl=1/2),
        Monster(name="Mud Mephit", cl=1/4),
        Monster(name="Smoke Mephit", cl=1/4),
        Monster(name="Steam Mephit", cl=1/4),
        Monster(name="Ice Mephit", cl=1/4),
        Monster(name="Merfolk", cl=1/8),
        Monster(name="Merrow", cl=2),
        Monster(name="Mimic", cl=2),
        Monster(name="Mind Flayer", cl=7),
        Monster(name="Minotaur", cl=3),
        Monster(name="Monodrone", cl=1/8),
        Monster(name="Duodrone", cl=1/4),
        Monster(name="Tridrone", cl=1/2),
        Monster(name="Quadrone", cl=1),
        Monster(name="Pentadrone", cl=2),
        Monster(name="Mummy", cl=3),
        Monster(name="Mummy Lord", cl=15, legendary=True),
        Monster(name="Myconid Spout", cl=0),
        Monster(name="Quaggoth Spore Servant", cl=1),
        Monster(name="Myconid Adult", cl=1/2),
        Monster(name="Myconid Sovereign", cl=2),
        Monster(name="Bone Naga", cl=4),
        Monster(name="Spirit Naga", cl=8),
        Monster(name="Guardian naga", cl=10),
        Monster(name="Nightmare", cl=3),
        Monster(name="Nothic", cl=2),
        Monster(name="Ogre", cl=2),
        Monster(name="Half-Ogre", cl=1),
        Monster(name="Oni", cl=7),
        Monster(name="Black Pudding", cl=4),
        Monster(name="Gelatinous Cube", cl=2),
        Monster(name="Gray Ooze", cl=1/2),
        Monster(name="Ochre Jelly", cl=2),
        Monster(name="Orc", cl=1/2),
        Monster(name="Orc War Chief", cl=4),
        Monster(name="Orc Eye of Gruumsh", cl=2),
        Monster(name="Orog", cl=2),
        Monster(name="Otyugh", cl=5),
        Monster(name="Owlbear", cl=3),
        Monster(name="Pegasus", cl=2),
        Monster(name="Peryton", cl=2),
        Monster(name="Piercer", cl=1/2),
        Monster(name="Pixie", cl=1/4),
        Monster(name="Pseudodragon", cl=1/4),
        Monster(name="Purple Worm", cl=15),
        Monster(name="Quaggoth", cl=2),
        Monster(name="Rakshasa", cl=13),
        Monster(name="Young Remorhaz", cl=5),
        Monster(name="Revenant", cl=5),
        Monster(name="Roc", cl=11),
        Monster(name="Roper", cl=5),
        Monster(name="Rust Monster", cl=1/2),
        Monster(name="Sahuagin", cl=1/2),
        Monster(name="Sahuagin Priestess", cl=2),
        Monster(name="Sahuagin Baron", cl=5),
        Monster(name="Fire Snake", cl=1),
        Monster(name="Salamander", cl=5),
        Monster(name="Satyr", cl=1/2),
        Monster(name="Scarecrow", cl=1),
        Monster(name="Shadow", cl=1/2),
        Monster(name="Shambling Mound", cl=5),
        Monster(name="Shield Guardian", cl=7),
        Monster(name="Skeleton", cl=1/4),
        Monster(name="Minotaur Skeleton", cl=2),
        Monster(name="Warhorse Skeleton", cl=1/2),
        Monster(name="Red Slaad", cl=5),
        Monster(name="Slaad Tadpole", cl=1/8),
        Monster(name="Blue Slaad", cl=7),
        Monster(name="Green Slaad", cl=8),
        Monster(name="Gray Slaad", cl=9),
        Monster(name="Death Slaad", cl=10),
        Monster(name="Specter", cl=1),
        Monster(name="Androsphinx", cl=17, legendary=True),
        Monster(name="Gynosphinx", cl=11, legendary=True),
        Monster(name="Sprite", cl=1/4),
        Monster(name="Stirge", cl=1/8),
        Monster(name="Succubus/Incubus", cl=4),
        Monster(name="Tarrasque", cl=30, legendary=True),
        Monster(name="Thri-Kreen", cl=1),
        Monster(name="Treant", cl=9),
        Monster(name="Troglodyte", cl=1/4),
        Monster(name="Troll", cl=5),
        Monster(name="Umber Hulk", cl=5),
        Monster(name="Unicorn", cl=5, lengedary=True),
        Monster(name="Vampire", cl=13, legendary=True),
        Monster(name="Vampire Spawn", cl=5),
        Monster(name="Water Weird", cl=3),
        Monster(name="Wight", cl=3),
        Monster(name="Will-o'-Wisp", cl=2),
        Monster(name="Wraith", cl=5),
        Monster(name="Wyvern", cl=6),
        Monster(name="Xorn", cl=5),
        Monster(name="Yeti", cl=3),
        Monster(name="Abominable Yeti", cl=9),
        Monster(name="Yuan-ti Abomination", cl=7),
        Monster(name="Yuan-ti Malison", cl=3),
        Monster(name="Yuan-ti Pureblood", cl=1),
        Monster(name="Arcanoloth", cl=12),
        Monster(name="Mezzoloth", cl=5),
        Monster(name="Nycaloth", cl=9),
        Monster(name="Ultroloth", cl=13),
        Monster(name="Zombie", cl=1/4),
        Monster(name="Ogre Zombie", cl=2),
        Monster(name="Beholder Zombie", cl=5),
        Monster(name="Ape", cl=1/2),
        Monster(name="Awakened Shrub", cl=0),
        Monster(name="Awakened Tree", cl=2),
        Monster(name="Axe Beak", cl=1/4),
        Monster(name="Baboon", cl=0),
        Monster(name="Badger", cl=0),
        Monster(name="Bat", cl=0),
        Monster(name="Black Bear", cl=1/2),
        Monster(name="Blink Dog", cl=1/4),
        Monster(name="Blood Hawk", cl=1/8),
        Monster(name="Boar", cl=1/4),
        Monster(name="Brown Bear", cl=1),
        Monster(name="Camel", cl=1/8),
        Monster(name="Cat", cl=0),
        Monster(name="Constrictor Snake", cl=1/4),
        Monster(name="Crab", cl=0),
        Monster(name="Crocodile", cl=1/2),
        Monster(name="Death Dog", cl=1),
        Monster(name="Deer", cl=0),
        Monster(name="Dire Wolf", cl=1),
        Monster(name="Draft Horse", cl=1/4),
        Monster(name="Eagle", cl=0),
        Monster(name="Elephant", cl=4),
        Monster(name="Elk", cl=1/4),
        Monster(name="Flying Snake", cl=1/8),
        Monster(name="Frog", cl=0),
        Monster(name="Giant Ape", cl=7),
        Monster(name="Giant Badger", cl=1/4),
        Monster(name="Giant Bat", cl=1/4),
        Monster(name="Giant Boar", cl=2),
        Monster(name="Giant Centipede", cl=1/4),
        Monster(name="Giant Constrictor Snake", cl=2),
        Monster(name="Giant Crab", cl=1/8),
        Monster(name="Giant Crocodile", cl=5),
        Monster(name="Giant Eagle", cl=1),
        Monster(name="Giant Elk", cl=2),
        Monster(name="Giant Fire Beetle", cl=0),
        Monster(name="Giant Frog", cl=1/4),
        Monster(name="Giant Goat", cl=1/2),
        Monster(name="Giant Hyena", cl=1),
        Monster(name="Giant Lizard", cl=1/4),
        Monster(name="Giant Octopus", cl=1),
        Monster(name="Giant Owl", cl=1/4),
        Monster(name="Giant Poisonous Snake", cl=1/4),
        Monster(name="Giant Rat", cl=1/8),
        Monster(name="Giant Scorpion", cl=3),
        Monster(name="Giant Sea Horse", cl=1/2),
        Monster(name="Giant Shark", cl=5),
        Monster(name="Giant Spider", cl=1),
        Monster(name="Giant Toad", cl=1),
        Monster(name="Giant Vulture", cl=1),
        Monster(name="Giant Wasp", cl=1/2),
        Monster(name="Giant Weasel", cl=1/8),
        Monster(name="Giant Wolf Spider", cl=1/4),
        Monster(name="Goat", cl=0),
        Monster(name="Hawk", cl=0),
        Monster(name="Hunter Shark", cl=2),
        Monster(name="Hyena", cl=0),
        Monster(name="Jackal", cl=0),
        Monster(name="Killer Whale", cl=3),
        Monster(name="Lion", cl=1),
        Monster(name="Lizard", cl=0),
        Monster(name="Mammoth", cl=6),
        Monster(name="Mastiff", cl=1/8),
        Monster(name="Mule", cl=-1/8),
        Monster(name="Octopus", cl=0),
        Monster(name="Owl", cl=0),
        Monster(name="Panther", cl=1/4),
        Monster(name="Phase Spider", cl=3),
        Monster(name="Poisonous Snake", cl=1/8),
        Monster(name="Polar Bear", cl=2),
        Monster(name="Pony", cl=1/8),
        Monster(name="Quipper", cl=0),
        Monster(name="Rat", cl=0),
        Monster(name="Raven", cl=0),
        Monster(name="Reef Shark", cl=1/2),
        Monster(name="Rhinoceros", cl=2),
        Monster(name="Riding Horse", cl=1/4),
        Monster(name="Saber-Toothed Tiger", cl=2),
        Monster(name="Scorpion", cl=0),
        Monster(name="Sea Horse", cl=0),
        Monster(name="Spider", cl=0),
        Monster(name="Swarm of Bats", cl=1/4),
        Monster(name="Swarm of Insects", cl=1/2),
        Monster(name="Swarm of Poisonous Snakes", cl=2)
        Monster(name="Swarm of Quippers", cl=1),
        Monster(name="Swarm of Rats", cl=1/4),
        Monster(name="Swarm of Ravens", cl=1/4),
        Monster(name="Tiger", cl=1),
        Monster(name="Vulture", cl=0),
        Monster(name="Warhorse", cl=1/2),
        Monster(name="Weasel", cl=0),
        Monster(name="Winter Wolf", cl=3),
        Monster(name="Wolf", cl=1/4),
        Monster(name="Worg", cl=1/2),
        Monster(name="Acolyte", cl=1/4),
        Monster(name="Archmage", cl=12),
        Monster(name="Assassin", cl=8),
        Monster(name="Bandit", cl=1/8),
        Monster(name="Bandit Captain", cl=2),
        Monster(name="Berserker", cl=2),
        Monster(name="Commoner", cl=0),
        Monster(name="Cultist", cl=1/8),
        Monster(name="Cult Fanatic", cl=2),
        Monster(name="Druid", cl=2),
        Monster(name="Gladiator", cl=5),
        Monster(name="Guard", cl=1/8),
        Monster(name="Knight", cl=3),
        Monster(name="Mage", cl=6),
        Monster(name="Noble", cl=1/8),
        Monster(name="Priest", cl=2),
        Monster(name="Scout", cl=1/2),
        Monster(name="Spy", cl=1),
        Monster(name="Thug", cl=1/2),
        Monster(name="Tribal Warrior", cl=1/8),
        Monster(name="Veteran", cl=3),
        Monster(name="
        Monster(name="
        Monster(name="
        Monster(name="
        Monster(name="
        Monster(name="
        Monster(name="
        Monster(name="
        Monster(name="
        Monster(name="
        Monster(name="
        Monster(name="
        Monster(name="
        Monster(name="
        Monster(name="
        Monster(name="
        Monster(name="
        Monster(name="
        }


groups = {

        'bandits': [
            Monster(name="Cat", cl=0),
            ],
        'undead': [

            ],
        'yuan-ti': [

            ],
        'fire-elemental': [

            ],
        'water-elemental': [

            ],
        'air-elemental': [

            ],
        'water-elementl': [

            ],
        'golens': [

            ],
        'sahuagin': [

            ],
        'orcs': [

            ],
        'myconids': [

            ],
        'modrons': [

            ],
        'kuo-toa': [

            ],
        'draconic': [

            ],
        'goblins': [

            ],
        'gnolls': [

            ],
        'gith': [

            ],
        'giants': [

            ],
        'spiders': [

            ],
        'drow': [

            ],
        'dinossaurs': [

            ],
        'abysals': [

            ],
        'celestials': [

            ],
        }


def get_party_threshold(pc_levels, difficulty):
    return sum([threshold[difficulty][level] for level in pc_levels])


def choose_monsters(budget, party_size, monster_pool, number_monsters=-1):
    """ A simple genetic algorithm to choose monsters. """
    generations = 100
    total_population = 100
    best = 10

    # generate start population
    population = [{}] * total_population
    for p in range(total_population):
        population[p] = {'key': 0, 'monsters': []}
        encounter_size = number_monsters if number_monsters > 0 else roll(20)
        for _ in range(encounter_size):
            population[p]['monsters'].append(roll_from_list(monster_pool))
        population[p]['key'] = abs(budget - sum([monster.xp for monster in population[p]['monsters']]) * get_encounter_multiplier(party_size, encounter_size))

    # start generations
    for generation in range(generations):
        population.sort(key=lambda p: p['key'])

        # return if found the monsters.
        if population[0]['key'] == 0:
            return population[0]['monsters']

        # generate the next generation.
        for p in range(best, total_population):
            population[p] = {'key': 0, 'monsters': []}
            encounter_size = number_monsters if number_monsters > 0 else roll(20)
            for _ in range(encounter_size):
                population[p]['monsters'].append(roll_from_list(monster_pool))
            population[p]['key'] = abs(budget - sum([monster.xp for monster in population[p]['monsters']]) * get_encounter_multiplier(party_size, encounter_size))

    population.sort(key=lambda p: p['key'])
    return population[0]['monsters']


if __name__ == "__main__":
    print("----------")
    if len(chosen['pc-levels']) > 0:
        difficulty = chosen['difficulty']
        pc_levels = chosen['pc-levels']
        number_monsters = chosen['monsters']
        party_avarage_level = statistics.mean(pc_levels)
        party_threshold = get_party_threshold(pc_levels, difficulty)

        # info
        print("Difficulty: %s" % difficulty)
        print('Character levels: %s (avarage: %.2f) %s' % (
            str(pc_levels),
            party_avarage_level,
            ("(Small party)" if len(pc_levels) <= 2 else ("(Large party)" if len(pc_levels) >= 6 else ""))))
        print('Party xp threshold: %d' % (party_threshold))

        # define the monster pool and find the group
        if chosen['name'] != '':
            environment = 'any environment'
            monster_pool = [m for m in all_monsters if any(n for n in chosen['name'] if n in m.name.lower())]
            if len(monster_pool) == 0:
                print('No monster found with names that include: %s' % str(chosen['name']))
                exit()
            monsters = choose_monsters(party_threshold, len(pc_levels), monster_pool, number_monsters)
        else:
            environment = chosen['environment']
            if environment != '':
                monster_pool = monsters[environment]
            else:
                environment = 'any environment'
                monster_pool = all_monsters
            monsters = choose_monsters(party_threshold, len(pc_levels), monster_pool, number_monsters)

        number_monsters = len(monsters)
        multiplier = get_encounter_multiplier(len(pc_levels), number_monsters)

        # monsters
        print('')
        print('Monsters: %d (x%.1f xp) (%s)' % (number_monsters, multiplier, environment))
        total_monster_xp = 0
        monsters.sort(reverse=True, key=lambda m: m.cl)
        cl_warning = False
        for monster in monsters:
            warning = (monster.cl > party_avarage_level)
            cl_warning = cl_warning or warning
            print('  %-40s cl: %-5s xp: %d' % (
                "%s%s" % (("* " if warning else ""), monster.name),
                ("1/8" if monster.cl == 1/8 else ("1/4" if monster.cl == 1/4 else ("1/2" if monster.cl == 1/2 else str(monster.cl)))) + ",",
                monster.xp))
            total_monster_xp += monster.xp
        print('')
        print('Total encounter xp: %-10d (reward %d to each PC)' % (total_monster_xp, total_monster_xp / len(pc_levels)))

        threshold_warning = abs(total_monster_xp * multiplier - party_threshold) > (party_threshold / 25)
        print('Modified encounter xp%s: %d' % (
            ('**' if threshold_warning else ''), total_monster_xp * multiplier))

        # warnings
        if cl_warning:
            print("")
            print("* Warning: Monster is significantly stronger than party.")

        if threshold_warning:
            print("")
            print("** Warning. The enconter does not match the party's xp threshold.")

        # treasure
        if chosen['treasure'] == 'personal':
            print('')
            print('Personal treasure:')
            total_treasure = {"cp": 0, "sp": 0, "ep": 0, "gp": 0, "pp": 0}
            for monster in monsters:
                treasure = generate_personal_treasure(int(statistics.mean([m.cl for m in monsters])))
                total_treasure['cp'] += treasure['cp']
                total_treasure['sp'] += treasure['sp']
                total_treasure['ep'] += treasure['ep']
                total_treasure['gp'] += treasure['gp']
                total_treasure['pp'] += treasure['pp']
            print_personal(total_treasure)

        elif chosen['treasure'] == 'hoard':
            hoard = {
                    "cp": 0, "sp": 0, "ep": 0, "gp": 0, "pp": 0, "magic": [],
                    "gems_quantity": [], "gems_name": [], "gem_price": [], 'hoard_item_roll': []}
            for _ in range(2 if any([m.legendary for m in monsters]) else 1):
                treasure = generate_treasure_hoard(monsters[0].cl if monsters[0].cl >= 1 else 0)

                hoard['hoard_item_roll'].append(treasure['hoard_item_roll'])
                hoard['gems_quantity'].append(treasure['gems_quantity'])
                hoard['gems_name'].append(treasure['gems_name'])
                hoard['gem_price'].append(treasure['gem_price'])

                hoard['cp'] += treasure['cp']
                hoard['sp'] += treasure['sp']
                hoard['ep'] += treasure['ep']
                hoard['gp'] += treasure['gp']
                hoard['pp'] += treasure['pp']

                hoard['magic'].extend(treasure['magic'])

            print('')
            print('Treasure hoard: (level: %d) (rolled: %s)' % (monsters[0].cl, hoard['hoard_item_roll']))

            print_personal(hoard)
            print("Gems or Art objecs:")
            for i in range(len(hoard['hoard_item_roll'])):
                if hoard['gems_quantity'][i] > 0:
                    print("  %d %s (%d gp each)" % (hoard['gems_quantity'][i], hoard['gems_name'][i], hoard['gem_price'][i]))

            magic = hoard['magic']
            if len(magic) > 0:
                print("Magic Items:")
                print_items(magic)

    else:
        print('Please, specify the pc-levels option. See --help for details.')
    print("----------")
