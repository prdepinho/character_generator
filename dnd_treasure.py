# Generate random loot in form of personal belongings or hoards.
# Input:
# - the type of treasure: personal or hoard;
# - the level of the party or of the monster.
# Output:
# - a series of threasure items,
# - with the rolled results.

from range_dict import RangeDict
from dnd_dice import Dice, roll_from_list, roll
import getopt
import sys

chosen = {
        'hoard': False,
        'personal': False,
        'level': 0,
        'quantity': 1
        }

try:
    optlist, args = getopt.getopt(
            sys.argv[1:],
            'hpl:q:',
            ['hoard', 'personal', 'level=', 'quantity=', 'help']
            )
except getopt.GetooptError as e:
    print(e)
    exit()

for o, a in optlist:
    if o in ['-h', '--hoard']:
        chosen['hoard'] = True
    elif o in ['-p', '--personal']:
        chosen['personal'] = True
    elif o in ['-l', '--level']:
        chosen['level'] = int(a)
        chosen['level'] = 20 if chosen['level'] > 20 else chosen['level']
    elif o in ['-q', '--quantity']:
        chosen['quantity'] = int(a)
    elif o == '--help':
        print('Help')
        print('Exetute the program to generate a random personal or hoard treasure. The following options are available.')
        print('%-40s %s' % ('-h, --hoard:', 'Roll a trasure hoard. This is the default.'))
        print('%-40s %s' % ('-p, --personal:', 'Roll personal treasure. Use the --quantity with this option.'))
        print('%-40s %s' % ('-l, --level [level]', 'Choose the challange level of the party or of the monster associated with the treasure. The default is 0.'))
        print('%-40s %s' % ('-q, --quantity [quantity]', 'Choose the number of enemies to roll personal treasure. The default is 1.'))
        exit()
    else:
        print('unhandled option: %s' % o)

gemstones = {
    10: [
        "Azurite",
        "Banded agate",
        "Blue quartz",
        "Eye agate",
        "Hematite",
        "Lapis lazuli",
        "Malachite",
        "Moss agate",
        "Obsidian",
        "Rhodochrosite",
        "Tiger eye",
        "Turquoise"
    ],
    50: [
        "Bloodstone",
        "Carnelian",
        "Chalcedony",
        "Chrysoprase",
        "Citrine",
        "Jasper",
        "Moonstone",
        "Onyx",
        "Quarz",
        "Sardonyx",
        "Star rose quartz",
        "Zircon"
    ],
    100: [
        "Amber",
        "Amethyst",
        "Chysoberyl",
        "Coral",
        "Garnet",
        "Jade",
        "Jet",
        "Pearl",
        "Spinel",
        "Tourmaline"
    ],
    500: [
        "Alexandrite",
        "Aquamarine",
        "Black pearl",
        "Blue spinel",
        "Peridot",
        "Topaz"
    ],
    1000: [
        "Black opal",
        "Blue sapphire",
        "Emerald",
        "Fire opal",
        "Opal",
        "Star ruby",
        "Star sapphire",
        "Yellow sapphire"
    ],
    5000: [
        "Black sapphire",
        "Diamond",
        "Jacinth",
        "Ruby"
    ]
}

artobjects = {
    25: [
        "Silver ewer",
        "Carved bone statuette",
        "Small gold bracelet",
        "Cloth-of-gold vestments",
        "Black velvet mask stiched with silver thread",
        "Copper chalice with silver filigree",
        "Pair of engraved bone dice",
        "Small mirror set in a painted wooden frame",
        "Embroidered silk handkerchief",
        "Gold locket with a painted portrait inside"
    ],
    250: [
        "Gold ring set with bloodstones",
        "Carved ivory statuette",
        "Large gold bracelet",
        "Silver necklace with a gemstone pendant",
        "Bronze crown",
        "Silk robe with gold embroidery",
        "Large well-made tapestry",
        "Brass mug with jade inlay",
        "Box of turquise animal figurines",
        "Gold bird cage with electrum filigree"
    ],
    750: [
        "Silver chalice set with moonstones",
        "Silver-plated steel longsword with jet set in hilt",
        "Carved harp of exotic wood with ivory inlay and zicon gems",
        "Small gold idol",
        "Gold dragon comb set with red garnets as eyes",
        "Bottle stopper cork embossed with gold leaf and set with amethysts",
        "Ceremonial electrum dagger with black pearl in the pommel",
        "Silver and gold brooch",
        "Obsidian statuette with gold fittings and inlay",
        "Painted gold war mask"
    ],
    2500: [
        "Fine gold chain set with fire opal",
        "Old masterpiece painting",
        "Embroidered silk and velvet mantle set with numerous moonstones",
        "Platinum bracelet set with a sapphire",
        "Embroidered glove set with jewel chips",
        "Jeweled anklet",
        "Gold music box",
        "Gold circlet set with four aquamarines",
        "Eye patch with a mock eye set in blue sapphire and moonstone",
        "A necklace string of small pink pearls"
    ],
    7500: [
        "Jeweled gold crown",
        "Jeweled platinum ring",
        "Small gold statuette set with rubies",
        "Gold cup set with emeralds",
        "Gold jewelry box with platinum filigree",
        "Painted gold child's sarcophagus",
        "jade game board with solid gold playing pieces",
        "Bejeweled ivory drinking horn with gold filigree"
    ]
}

spellscroll = {
    0: [
        'Acid Splash',
        'Blade Ward',
        'Chill Touch',
        'Dancing Lights',
        'Firebolt'
        'Friends',
        'Light',
        'Mage Hand',
        'Mending',
        'Message',
        'Minor Illusion',
        'Poison Spray',
        'Prestidigitation',
        'Ray of Frost',
        'Shocking Grasp',
        'True Strike'
        ],
    1: [
        'Alarm',
        'Burning Hands',
        'Charm Person',
        "Chromatic Orb",
        'Color Spray',
        'Comprehend Languages',
        'Detect Magic',
        'Disguise Self',
        'Expeditious Retreat',
        'False Life',
        'Feather Fall',
        'Find Familiar',
        'Fog Cloud',
        'Grease',
        'Identify',
        'Illusory Script',
        'Jump',
        'Longstrider',
        'Mage Armor',
        'Magic Missle',
        'Protection from Evil and Good',
        'Ray of Sickness',
        'Shield',
        'Silent Image',
        'Sleep',
        "Tasha's Hideous Laughter",
        "Tense's Floating Disk",
        'Thunderwave',
        'Unseen Servant',
        'Witch Bolt'
        ],
    2: [
        "Alter Self",
        "Arcane Lock",
        "Blindness/Deafnedd",
        "Blur",
        "Cloud of Daggers",
        "Continual Flame",
        "Crown of Madness",
        "Darkness",
        "Darkvision",
        "Detect Thoughts",
        "Enlarge/Reduce",
        "Flaming Sphere",
        "Gentle Repose",
        "Gust of Wind",
        "Hold Person",
        "Invisibility",
        "Knock",
        "Levitate",
        "Locate Object",
        "Magic Mouth",
        "Magic Weapon",
        "Melf's Acid Arrow",
        "Mirror Image",
        "Misty Step",
        "Mystul's magic Aura",
        "Phantasmal Force",
        "Ray of Enfeeblement",
        "Rope Truck",
        "Scorching Ray",
        "See Invisibility",
        "Shatter",
        "Spider Climb",
        "Suggestion",
        "Web"
        ],
    3: [
        "Animate Dead",
        "Bestow Curse",
        "Blink",
        "Clairvoyance",
        "Counterspell",
        "Dispell Magic",
        "Fear",
        "Feign Death",
        "Fireball",
        "Fly",
        "Gaseous Form",
        "Glyph of Warding",
        "Haste",
        "Hypnotic Pattern",
        "Lomund's Tiny Hut",
        "Lightning Bolt",
        "Magic Circle",
        "Major Image",
        "Nondetection",
        "Phantom Steed",
        "Protection from Energy",
        "Remove Curse",
        "Sending",
        "Sleet Storm",
        "Slow",
        "Stinking Cloud",
        "Tongues",
        "Vampiric Touch",
        "Water Breathing"
        ],
    4: [
        "Arcane Eye",
        "Banishment",
        "Blight",
        "Confusion",
        "Conjure Minor Elementals",
        "Control Water",
        "Dimension Door",
        "Evard's Black Tentacles",
        "Fabricate",
        "Fire Shield",
        "Greater Invisibility",
        "Hallucinatory Terrain",
        "Ice Storm",
        "Leomund's Secret Chest",
        "Locate Creature",
        "Mordenkainen's Faithful Hound",
        "Mordenkainen's Private Sanctum",
        "Otiluke's Resilient Sphere",
        "Phantasmal Killer",
        "Polymorph",
        "Stone Shape",
        "Stoneskin",
        "Wall of Fire"
        ],
    5: [
        "Animate Objects",
        "Bigby's Hand",
        "Cloudkill",
        "Cone of Cold",
        "Conjure Elemental",
        "Contact Other Plane",
        "Creation",
        "Dominate Person",
        "Dream",
        "Geas",
        "Hold Monster",
        "Legend Lore",
        "Mislead",
        "Modify Memory",
        "Passwall",
        "Planar Binding",
        "Rary's Telepathic Bond",
        "Scrying",
        "Seeming",
        "Telekisesis",
        "TeleportationCircle",
        "Wall of Force",
        "Wall of Stone"
        ],
    6: [
        "Arcane Gate",
        "Chain Lightning",
        "Circle of Death",
        "Contingency",
        "Create Undead",
        "Disintegrate",
        "Drawmij's Instant Summons",
        "Eyebite",
        "Flesh to Stone",
        "Globe of Invulnerability",
        "Guards and Wards",
        "Magic Jar",
        "Mass Suggestion",
        "Move Earth",
        "Otiluke's Freezing Sphere",
        "Otto's Irresistible Dance",
        "Programmed Illusion",
        "Sunbeam",
        "True Seeing",
        "Wall of Ice"
        ],
    7: [
        "Delayed Blast Fireball",
        "Etherealness",
        "Finger of Death",
        "Forcecage",
        "Mirage Arcane",
        "Mordenkainen's Magnificent Mansion",
        "Mordenkainen's Sword",
        "Plane Shift",
        "Prismatic Spray",
        "Project Image",
        "Reverse Gravity",
        "Sequester",
        "Simulacrusm",
        "Symbol",
        "Teleport"
        ],
    8: [
        "Antimagic Field",
        "Antipathy/Sympathy",
        "Clone",
        "Control Weather",
        "Demiplane",
        "Dominate Monster",
        "Feeblemind",
        "Incendiary Cloud",
        "Maze",
        "Mind Blank",
        "Power Word Stun",
        "Sunburst",
        "Telepathy"
        ],
    9: [
        "Astral Projection",
        "Foresight",
        "Gate",
        "Imprisonment",
        "Meteor Swarm",
        "Power Word Kill",
        "Prismatic Wall",
        "Shapechange",
        "Time Stop",
        "True Polymorph",
        "Weird",
        "Wish"
        ]

}

weapons = [
    "Club",
    "Dagger",
    "Greatclub",
    "Handaxe",
    "javelin",
    "Light hammer",
    "Mace",
    "Quarterstaff",
    "Sickle",
    "Spear",
    "Crossbow, light",
    "Dart",
    "Shortbow",
    "Sling",
    "Battleaxe",
    "Flail",
    "Glaive",
    "Greataxe",
    "Greatsword",
    "Halberd",
    "Lance",
    "Lingsword",
    "Maul",
    "Morningstar",
    "Pike",
    "Rapier",
    "Scimitar",
    "Shorsword",
    "Trident",
    "War pick",
    "Warhammer",
    "Whip",
    "Blowgun",
    "Crossbow, hand",
    "Crossbow, heavy",
    "Longbow",
    "Net"
]

magicitems = {
    'a': RangeDict(),
    'b': RangeDict(),
    'c': RangeDict(),
    'd': RangeDict(),
    'e': RangeDict(),
    'f': RangeDict(),
    'g': RangeDict(),
    'h': RangeDict(),
    'i': RangeDict()
}


class Item:
    def __init__(self, name, complement_roll=lambda: ''):
        self.name = name
        self.complement_roll = complement_roll


magicitems['a'].set(1, 50, Item(name="Potion of healing"))
magicitems['a'].set(51, 60, Item(name="Spell scroll (cantrip])", complement_roll=lambda: roll_from_list(spellscroll[0])))
magicitems['a'].set(61, 70, Item(name="Potion of climbing"))
magicitems['a'].set(71, 90, Item(name="Spell scroll (1st level)", complement_roll=lambda: roll_from_list(spellscroll[1])))
magicitems['a'].set(91, 94, Item(name="Spell scroll (2nd level)", complement_roll=lambda: roll_from_list(spellscroll[2])))
magicitems['a'].set(95, 98, Item(name="Potion of greater healing"))
magicitems['a'].set(99, 99, Item(name="Bag of holding"))
magicitems['a'].set(100, 100, Item(name="Driftglobe"))

magicitems['b'].set(1, 15, Item(name="Potion of greater healing"))
magicitems['b'].set(16, 22, Item(name="Potion of fire breath"))
magicitems['b'].set(23, 29, Item(name="Potion of resistance"))
magicitems['b'].set(30, 34, Item(name="Ammunition +1"))
magicitems['b'].set(35, 39, Item(name="Potion of animal friendship"))
magicitems['b'].set(40, 44, Item(name="Potion of hill giant strength"))
magicitems['b'].set(45, 49, Item(name="Potion of growth"))
magicitems['b'].set(50, 54, Item(name="Potion of water breathing"))
magicitems['b'].set(55, 59, Item(name="Spell scroll (2nd level)", complement_roll=lambda: roll_from_list(spellscroll[2])))
magicitems['b'].set(60, 64, Item(name="Spell scroll (3rd level)", complement_roll=lambda: roll_from_list(spellscroll[3])))
magicitems['b'].set(65, 67, Item(name="Bag of holding"))
magicitems['b'].set(68, 70, Item(name="Keoghtom's ointment"))
magicitems['b'].set(71, 73, Item(name="Oil of slipperiness"))
magicitems['b'].set(74, 75, Item(name="Dust of disappearance"))
magicitems['b'].set(76, 77, Item(name="Dust of dryness"))
magicitems['b'].set(78, 79, Item(name="Dust of sneezing and choking"))
magicitems['b'].set(80, 81, Item(name="Elemental gem"))
magicitems['b'].set(82, 83, Item(name="Philter of love"))
magicitems['b'].set(84, 84, Item(name="Alchemy jug"))
magicitems['b'].set(85, 85, Item(name="Cap of water breathing"))
magicitems['b'].set(86, 86, Item(name="Cloak of the manta ray"))
magicitems['b'].set(87, 87, Item(name="Driftglobe"))
magicitems['b'].set(88, 88, Item(name="Goggle of night"))
magicitems['b'].set(89, 89, Item(name="Helm of comprehending languages"))
magicitems['b'].set(90, 92, Item(name="Immovable rod"))
magicitems['b'].set(91, 92, Item(name="Lantern of revealing"))
magicitems['b'].set(92, 92, Item(name="Mariner's armor"))
magicitems['b'].set(93, 93, Item(name="Mithral armor"))
magicitems['b'].set(94, 94, Item(name="Potion of poison"))
magicitems['b'].set(95, 95, Item(name="Ring of swimming"))
magicitems['b'].set(96, 96, Item(name="Robe of usebul items"))
magicitems['b'].set(97, 97, Item(name="Rope of climbing"))
magicitems['b'].set(98, 98, Item(name="Saddle of the cavalier"))
magicitems['b'].set(99, 99, Item(name="Wand of magic detection"))
magicitems['b'].set(100, 100, Item(name="Wand of secrets"))

magicitems['c'].set(1, 15, Item(name="Potion of superior healing"))
magicitems['c'].set(16, 22, Item(name="Spell scroll (4th level)", complement_roll=lambda: roll_from_list(spellscroll[4])))
magicitems['c'].set(23, 27, Item(name="Ammunition +2"))
magicitems['c'].set(28, 32, Item(name="Potion of clairvoiance"))
magicitems['c'].set(33, 37, Item(name="Potion of diminution"))
magicitems['c'].set(38, 42, Item(name="Potion of gaseous form"))
magicitems['c'].set(43, 47, Item(name="Potion of frost giant strength"))
magicitems['c'].set(48, 52, Item(name="Potion of stone giant strength"))
magicitems['c'].set(53, 57, Item(name="Potion of heroism"))
magicitems['c'].set(58, 62, Item(name="Potion of inbulnerability"))
magicitems['c'].set(63, 67, Item(name="Potion of mind reading"))
magicitems['c'].set(68, 72, Item(name="Spell scroll (5th level)", complement_roll=lambda: roll_from_list(spellscroll[5])))
magicitems['c'].set(73, 75, Item(name="Elixir of health"))
magicitems['c'].set(76, 78, Item(name="Oil of etherealness"))
magicitems['c'].set(79, 81, Item(name="Potion of fire giant strength"))
magicitems['c'].set(82, 84, Item(name="Quaal's feather token"))
magicitems['c'].set(85, 87, Item(name="Scroll of protection"))
magicitems['c'].set(88, 89, Item(name="Bag of beans"))
magicitems['c'].set(90, 91, Item(name="Bead of force"))
magicitems['c'].set(92, 92, Item(name="Chime of opening"))
magicitems['c'].set(93, 93, Item(name="Decanteer of endless water"))
magicitems['c'].set(94, 94, Item(name="Eyes of minute seeing"))
magicitems['c'].set(95, 95, Item(name="Folding boat"))
magicitems['c'].set(96, 96, Item(name="Heward's handy haversack"))
magicitems['c'].set(97, 97, Item(name="Horseshoes of speed"))
magicitems['c'].set(98, 98, Item(name="Necklace of fireballs"))
magicitems['c'].set(99, 99, Item(name="Periapt of health"))
magicitems['c'].set(100, 100, Item(name="Sending stones"))

magicitems['d'].set(1, 20, Item(name="Potion of supreme healing"))
magicitems['d'].set(21, 30, Item(name="Potion of invisibility"))
magicitems['d'].set(31, 40, Item(name="Potion of speed"))
magicitems['d'].set(41, 50, Item(name="Spell scroll (6th level)", complement_roll=lambda: roll_from_list(spellscroll[6])))
magicitems['d'].set(51, 57, Item(name="Spell scroll (7th level)", complement_roll=lambda: roll_from_list(spellscroll[7])))
magicitems['d'].set(58, 62, Item(name="Ammunition + 3"))
magicitems['d'].set(63, 67, Item(name="Oil of sharpness"))
magicitems['d'].set(68, 72, Item(name="Potion of flying"))
magicitems['d'].set(73, 77, Item(name="Potion of cloud giant strength"))
magicitems['d'].set(78, 82, Item(name="Potion of longevity"))
magicitems['d'].set(83, 87, Item(name="Potion of vitality"))
magicitems['d'].set(88, 92, Item(name="Spell scroll (8th level)", complement_roll=lambda: roll_from_list(spellscroll[8])))
magicitems['d'].set(93, 95, Item(name="Horseshoes of a zephyr"))
magicitems['d'].set(96, 98, Item(name="Nolzur's marvelous pigments"))
magicitems['d'].set(99, 99, Item(name="Bag of devouring"))
magicitems['d'].set(100, 100, Item(name="Portable hole"))

magicitems['e'].set(1, 30, Item(name="Spell scroll (8th level)", complement_roll=lambda: roll_from_list(spellscroll[8])))
magicitems['e'].set(31, 55, Item(name="Potion of storm giant strength"))
magicitems['e'].set(56, 70, Item(name="Potion of supreme healing"))
magicitems['e'].set(71, 85, Item(name="Spell scroll (9th level)", complement_roll=lambda: roll_from_list(spellscroll[9])))
magicitems['e'].set(86, 93, Item(name="Universal solvent"))
magicitems['e'].set(94, 98, Item(name="Arrow of slaying"))
magicitems['e'].set(99, 100, Item(name="Sovereign glue"))

magicitems['f'].set(1, 15, Item(name="Weapon +1", complement_roll=lambda: roll_from_list(weapons)))
magicitems['f'].set(16, 18, Item(name="Shield +1"))
magicitems['f'].set(19, 21, Item(name="Sentinel shield"))
magicitems['f'].set(22, 23, Item(name="Amulet of proof against detection and location"))
magicitems['f'].set(24, 25, Item(name="Boot of elvenkind"))
magicitems['f'].set(26, 27, Item(name="Boots of striding and springing"))
magicitems['f'].set(28, 29, Item(name="Bracers of archery"))
magicitems['f'].set(30, 31, Item(name="Brooch of shielding"))
magicitems['f'].set(32, 33, Item(name="Broom of flying"))
magicitems['f'].set(34, 35, Item(name="Cloak of elvenkind"))
magicitems['f'].set(36, 37, Item(name="Cloak of protection"))
magicitems['f'].set(38, 39, Item(name="Gauntlets of ogre power"))
magicitems['f'].set(40, 41, Item(name="Hat of disguise"))
magicitems['f'].set(42, 43, Item(name="Javelin of lightning"))
magicitems['f'].set(44, 45, Item(name="Pearl of power"))
magicitems['f'].set(46, 47, Item(name="Rod of the pact keeper +1"))
magicitems['f'].set(48, 49, Item(name="Slippers of spider climbing"))
magicitems['f'].set(50, 51, Item(name="Staff of the adder"))
magicitems['f'].set(52, 53, Item(name="Staff of the python"))
magicitems['f'].set(54, 55, Item(name="Sword of vengeance"))
magicitems['f'].set(56, 57, Item(name="Trident of fish command"))
magicitems['f'].set(58, 59, Item(name="Wand of magic missiles"))
magicitems['f'].set(60, 61, Item(name="Wand of the war mage +1"))
magicitems['f'].set(62, 63, Item(name="Wand of web"))
magicitems['f'].set(64, 65, Item(name="Weapon of warning", complement_roll=lambda: roll_from_list(weapons)))
magicitems['f'].set(66, 66, Item(name="Adamantine armor (chain mail)"))
magicitems['f'].set(67, 67, Item(name="Adamantine armor (chain shirt)"))
magicitems['f'].set(68, 68, Item(name="Adamantine armor (scale mail)"))
magicitems['f'].set(69, 69, Item(name="Bag of tricks (gray)"))
magicitems['f'].set(70, 70, Item(name="Bag of tricks (rust)"))
magicitems['f'].set(71, 71, Item(name="Bag of tricks(tan)"))
magicitems['f'].set(72, 72, Item(name="Boots of the winterlands"))
magicitems['f'].set(73, 73, Item(name="Circlet of blasting"))
magicitems['f'].set(74, 74, Item(name="Deck of illusions"))
magicitems['f'].set(75, 75, Item(name="Eversmoking bottle"))
magicitems['f'].set(76, 76, Item(name="Eyes of charming"))
magicitems['f'].set(77, 77, Item(name="Eyes of the eagle"))
magicitems['f'].set(78, 78, Item(name="Figurine of wondrous power (silver raven)"))
magicitems['f'].set(79, 79, Item(name="Gem of brightness"))
magicitems['f'].set(80, 80, Item(name="Gloves of missile snaring"))
magicitems['f'].set(81, 81, Item(name="Gloves of swimming and climbing"))
magicitems['f'].set(82, 82, Item(name="Gloves of thievery"))
magicitems['f'].set(83, 83, Item(name="Headband of intellect"))
magicitems['f'].set(84, 84, Item(name="Helm of telepathy"))
magicitems['f'].set(85, 85, Item(name="Instrument of the bards (Doss lute)"))
magicitems['f'].set(86, 86, Item(name="Instrument of the bards (Fochlucan bandore)"))
magicitems['f'].set(87, 87, Item(name="Instrument of the bards (Mac-Fuimidh cittern)"))
magicitems['f'].set(88, 88, Item(name="Medallion of thoughts"))
magicitems['f'].set(89, 89, Item(name="Necklace of adaptation"))
magicitems['f'].set(90, 90, Item(name="Periapt of wound closure"))
magicitems['f'].set(91, 91, Item(name="Pipes of haunting"))
magicitems['f'].set(92, 92, Item(name="Pipes of the sewers"))
magicitems['f'].set(93, 93, Item(name="Ring of jumping"))
magicitems['f'].set(94, 94, Item(name="Ring of mind shielding"))
magicitems['f'].set(95, 95, Item(name="Ring of warmth"))
magicitems['f'].set(96, 96, Item(name="Ring of water walking"))
magicitems['f'].set(97, 97, Item(name="Quiver of Ehlonna"))
magicitems['f'].set(98, 98, Item(name="Stone of good luck"))
magicitems['f'].set(99, 99, Item(name="Wind fant"))
magicitems['f'].set(100, 100, Item(name="Winged boots"))

figurine = RangeDict()
figurine.set(1, 1, "Bronze griffon")
figurine.set(2, 2, "Ebony fly")
figurine.set(3, 3, "Golden lions")
figurine.set(4, 4, "Ivory goats")
figurine.set(5, 5, "Marble elephant")
figurine.set(6, 7, "Onyx dog")
figurine.set(8, 8, "Serpentine owl")

magicitems['g'].set(1, 11, Item(name="Weapon +2", complement_roll=lambda: roll_from_list(weapons)))
magicitems['g'].set(12, 14, Item(name="Figurine of wondrous power", complement_roll=lambda: figurine.get(Dice('d8'))))
magicitems['g'].set(15, 15, Item(name="Adamantine armor (breastplate)"))
magicitems['g'].set(16, 16, Item(name="Adamantine armor (splint)"))
magicitems['g'].set(17, 17, Item(name="Amulet of health"))
magicitems['g'].set(18, 18, Item(name="Armor of vulnerability"))
magicitems['g'].set(19, 19, Item(name="Arrow-catching sield"))
magicitems['g'].set(20, 20, Item(name="Belt of dwarvenkind"))
magicitems['g'].set(21, 21, Item(name="Belt of hill giant strength"))
magicitems['g'].set(22, 22, Item(name="Berserker axe"))
magicitems['g'].set(23, 23, Item(name="Boots of levitation"))
magicitems['g'].set(24, 24, Item(name="Boots of speed"))
magicitems['g'].set(25, 25, Item(name="Bowl of commanding water elementals"))
magicitems['g'].set(26, 26, Item(name="Bracers of defense"))
magicitems['g'].set(27, 27, Item(name="Brazier of commanding fire elementals"))
magicitems['g'].set(28, 28, Item(name="Cape of the mountebank"))
magicitems['g'].set(29, 29, Item(name="Censer of controlling air elementals"))
magicitems['g'].set(30, 30, Item(name="Armor +1 (Chain mail)"))
magicitems['g'].set(31, 31, Item(name="Armor of resistance (chain mail)"))
magicitems['g'].set(32, 32, Item(name="Armor + 1 (chain shirt)"))
magicitems['g'].set(33, 33, Item(name="Armor of resistance (chain shirt)"))
magicitems['g'].set(34, 34, Item(name="Cloak of displacement"))
magicitems['g'].set(35, 35, Item(name="Cloak of the bat"))
magicitems['g'].set(36, 36, Item(name="Cube of force"))
magicitems['g'].set(37, 37, Item(name="Daern's instant fortress"))
magicitems['g'].set(38, 38, Item(name="Dagger of venom"))
magicitems['g'].set(39, 39, Item(name="Dimensional shackles"))
magicitems['g'].set(40, 40, Item(name="Dragon slayer"))
magicitems['g'].set(41, 41, Item(name="Elven chain"))
magicitems['g'].set(42, 42, Item(name="Flame tongue"))
magicitems['g'].set(43, 43, Item(name="Gem of seeing"))
magicitems['g'].set(44, 44, Item(name="Giant slayer"))
magicitems['g'].set(45, 45, Item(name="Glamoured studded leather"))
magicitems['g'].set(46, 46, Item(name="Helm of teleportation"))
magicitems['g'].set(47, 47, Item(name="Horn of blasting"))
magicitems['g'].set(48, 48, Item(name="Horn of Valhalla", complement_roll=lambda: roll_from_list(['silver', 'brass'])))
magicitems['g'].set(49, 49, Item(name="Instrument of the bards (Canaith mandolin)"))
magicitems['g'].set(50, 50, Item(name="Instrument of the bards (Cli lyre)"))
magicitems['g'].set(51, 51, Item(name="Ioun stone (awareness)"))
magicitems['g'].set(52, 52, Item(name="Ioun stone (protection)"))
magicitems['g'].set(53, 53, Item(name="Ioun stone (reserve)"))
magicitems['g'].set(54, 54, Item(name="Ioun stone (sustenance)"))
magicitems['g'].set(55, 55, Item(name="Iron bands of Bilarro"))
magicitems['g'].set(56, 56, Item(name="Armor +1 (leather)"))
magicitems['g'].set(57, 57, Item(name="Armor of resistance (leather)"))
magicitems['g'].set(58, 58, Item(name="Mace of disruption"))
magicitems['g'].set(59, 59, Item(name="Mace of smiting"))
magicitems['g'].set(60, 60, Item(name="Mace of terror"))
magicitems['g'].set(61, 61, Item(name="Mantle of spell resistance"))
magicitems['g'].set(62, 62, Item(name="Necklace of prayer beads"))
magicitems['g'].set(63, 63, Item(name="Periapt of proof against poison"))
magicitems['g'].set(64, 64, Item(name="Ring of animal influence"))
magicitems['g'].set(65, 65, Item(name="Ring of evasion"))
magicitems['g'].set(66, 66, Item(name="Ring of feather falling"))
magicitems['g'].set(67, 67, Item(name="Ring of free action"))
magicitems['g'].set(68, 68, Item(name="Ring of protection"))
magicitems['g'].set(69, 69, Item(name="Ring of resistance"))
magicitems['g'].set(70, 70, Item(name="Ring of spell storing"))
magicitems['g'].set(71, 71, Item(name="Ring of the ram"))
magicitems['g'].set(72, 72, Item(name="Ring of X-ray vision"))
magicitems['g'].set(73, 73, Item(name="Robe of eyes"))
magicitems['g'].set(74, 74, Item(name="Rod of rulership"))
magicitems['g'].set(75, 75, Item(name="Rod of the pact keeper +2"))
magicitems['g'].set(76, 76, Item(name="Rope of entanglement"))
magicitems['g'].set(77, 77, Item(name="Armor +1 (scale mail)"))
magicitems['g'].set(78, 78, Item(name="Armor or resistance (scale mail)"))
magicitems['g'].set(79, 79, Item(name="Shield +2"))
magicitems['g'].set(80, 80, Item(name="Shield of missile attraction"))
magicitems['g'].set(81, 81, Item(name="Staff of charming"))
magicitems['g'].set(82, 82, Item(name="Staff of healing"))
magicitems['g'].set(83, 83, Item(name="Staff of swarming insects"))
magicitems['g'].set(84, 84, Item(name="Staff of the woodlands"))
magicitems['g'].set(85, 85, Item(name="Staff of withering"))
magicitems['g'].set(86, 86, Item(name="Stone of controlling earth elementals"))
magicitems['g'].set(87, 87, Item(name="Sun blade"))
magicitems['g'].set(88, 88, Item(name="Sword of life stealing"))
magicitems['g'].set(89, 89, Item(name="Sword of wounding"))
magicitems['g'].set(90, 90, Item(name="Tentacle rod"))
magicitems['g'].set(91, 91, Item(name="Vicious weapon", complement_roll=lambda: roll_from_list(weapons)))
magicitems['g'].set(92, 92, Item(name="Wand of binding"))
magicitems['g'].set(93, 93, Item(name="Wand of enemy detection"))
magicitems['g'].set(94, 94, Item(name="Wand of fear"))
magicitems['g'].set(95, 95, Item(name="Wand of fireballs"))
magicitems['g'].set(96, 96, Item(name="Wand of lightning bolts"))
magicitems['g'].set(97, 97, Item(name="Wand of paralysis"))
magicitems['g'].set(98, 98, Item(name="Wand of the war mage +2"))
magicitems['g'].set(99, 99, Item(name="Wand of wonder"))
magicitems['g'].set(100, 100, Item(name="Wings of flying"))

magicitems['h'].set(1, 10, Item(name="Weapon +3", complement_roll=lambda: roll_from_list(weapons)))
magicitems['h'].set(11, 12, Item(name="Amulet of the planes"))
magicitems['h'].set(13, 14, Item(name="Carpet of lying"))
magicitems['h'].set(15, 16, Item(name="Crystal ball (very rare version)"))
magicitems['h'].set(17, 18, Item(name="Ring of regeneration"))
magicitems['h'].set(19, 20, Item(name="Ring of shooting stars"))
magicitems['h'].set(21, 22, Item(name="Ring of telekinesis"))
magicitems['h'].set(23, 24, Item(name="Robe of scintillating colors"))
magicitems['h'].set(25, 26, Item(name="Robe of stars"))
magicitems['h'].set(27, 28, Item(name="Rod of absorption"))
magicitems['h'].set(29, 30, Item(name="Rod of alertness"))
magicitems['h'].set(31, 32, Item(name="Rod of security"))
magicitems['h'].set(33, 34, Item(name="Rod of the pact keeper +3"))
magicitems['h'].set(35, 36, Item(name="Scimitar of speed"))
magicitems['h'].set(37, 38, Item(name="Shield +3"))
magicitems['h'].set(39, 40, Item(name="Staff of fire"))
magicitems['h'].set(41, 42, Item(name="Staff of frost"))
magicitems['h'].set(43, 44, Item(name="Staff of power"))
magicitems['h'].set(45, 46, Item(name="Staff of striking"))
magicitems['h'].set(47, 48, Item(name="Staff of thunder and lightning"))
magicitems['h'].set(49, 50, Item(name="Sword of sharpness"))
magicitems['h'].set(51, 52, Item(name="Wand of polymorph"))
magicitems['h'].set(53, 54, Item(name="Wand of the warmage +3"))
magicitems['h'].set(55, 55, Item(name="Adamantine armor (half plate)"))
magicitems['h'].set(56, 56, Item(name="Adamantine armor (plate)"))
magicitems['h'].set(57, 57, Item(name="Animated shield"))
magicitems['h'].set(58, 58, Item(name="Belt of fire giant strength"))
magicitems['h'].set(59, 59, Item(name="Belt of giant strength", complement_roll=lambda: roll_from_list(['frost', 'stone'])))
magicitems['h'].set(60, 60, Item(name="Armor +1 (breastplate)"))
magicitems['h'].set(61, 61, Item(name="Armor of resistance (breastplate)"))
magicitems['h'].set(62, 62, Item(name="Candle of invocation"))
magicitems['h'].set(63, 63, Item(name="Armor +2 (chain mail)"))
magicitems['h'].set(64, 64, Item(name="Armor +2 (chain shirt)"))
magicitems['h'].set(65, 65, Item(name="Cloak of arachnida"))
magicitems['h'].set(66, 66, Item(name="Dancing sword"))
magicitems['h'].set(67, 67, Item(name="Demon armor"))
magicitems['h'].set(68, 68, Item(name="Dragon scale mail"))
magicitems['h'].set(69, 69, Item(name="Dwarven plate"))
magicitems['h'].set(70, 70, Item(name="Dwarven thrower"))
magicitems['h'].set(71, 71, Item(name="Efreeti bottle"))
magicitems['h'].set(72, 72, Item(name="Figurine of wondrous power (obsidian steed)"))
magicitems['h'].set(73, 73, Item(name="Frost brand"))
magicitems['h'].set(74, 74, Item(name="Helm of brilliance"))
magicitems['h'].set(75, 75, Item(name="Horn of Valhalla (bronze)"))
magicitems['h'].set(76, 76, Item(name="Instrument of the bards (Antruth harp)"))
magicitems['h'].set(77, 77, Item(name="Ioun stone (absorption)"))
magicitems['h'].set(78, 78, Item(name="Ioun stone (agility)"))
magicitems['h'].set(79, 79, Item(name="Ioun stone (fortitude)"))
magicitems['h'].set(80, 80, Item(name="Ioun stone (insight)"))
magicitems['h'].set(81, 81, Item(name="Ioun stone (intellect)"))
magicitems['h'].set(82, 82, Item(name="Ioun stone (leadership)"))
magicitems['h'].set(83, 83, Item(name="Ioun stone (strength)"))
magicitems['h'].set(84, 84, Item(name="Armor +2 (leather)"))
magicitems['h'].set(85, 85, Item(name="Manal of bodily health"))
magicitems['h'].set(86, 86, Item(name="Manual of gainful exercise"))
magicitems['h'].set(87, 87, Item(name="Manual of golems"))
magicitems['h'].set(88, 88, Item(name="Manual of quickness of action"))
magicitems['h'].set(89, 89, Item(name="Mirror of life trapping"))
magicitems['h'].set(90, 90, Item(name="Nine lives stealer"))
magicitems['h'].set(91, 91, Item(name="Oathbow"))
magicitems['h'].set(92, 92, Item(name="Armor +2 (scale mail)"))
magicitems['h'].set(93, 93, Item(name="Spellguard shield"))
magicitems['h'].set(94, 94, Item(name="Armor +1 (splint)"))
magicitems['h'].set(95, 95, Item(name="Armor if resistance (split)"))
magicitems['h'].set(96, 96, Item(name="Armor +1 (studded leather)"))
magicitems['h'].set(97, 97, Item(name="Armor of resistance (studded leather)"))
magicitems['h'].set(98, 98, Item(name="Tome of clear thought"))
magicitems['h'].set(99, 99, Item(name="Tome of leadership and influence"))
magicitems['h'].set(100, 100, Item(name="Tome of understanding"))

magicarmor = RangeDict()
magicarmor.set(1, 2, "Armor +2 (half plate)")
magicarmor.set(3, 4, "Armor +2 (plate)")
magicarmor.set(5, 6, "Armor +3 (studded leather)")
magicarmor.set(7, 8, "Armor +3 (breastplate)")
magicarmor.set(9, 10, "Armor +3 (splint)")
magicarmor.set(11, 11, "Armor +3 (half plate)")
magicarmor.set(12, 12, "Armor +3 (plate)")

magicitems['i'].set(1, 5, Item(name="Defender"))
magicitems['i'].set(6, 10, Item(name="Hammer of thunderbolts"))
magicitems['i'].set(11, 15, Item(name="Luck blade"))
magicitems['i'].set(16, 20, Item(name="Sword of answering"))
magicitems['i'].set(21, 23, Item(name="Holy avenger"))
magicitems['i'].set(24, 26, Item(name="Ring of djinni summoning"))
magicitems['i'].set(27, 29, Item(name="Ring of invisibility"))
magicitems['i'].set(30, 32, Item(name="Ring of spell turning"))
magicitems['i'].set(33, 35, Item(name="Rod of lordly might"))
magicitems['i'].set(36, 38, Item(name="Staff of the magi"))
magicitems['i'].set(39, 41, Item(name="Vorpal sword"))
magicitems['i'].set(42, 43, Item(name="Belt of cloud giant strength"))
magicitems['i'].set(44, 45, Item(name="Armor +2 (breastplate)"))
magicitems['i'].set(46, 47, Item(name="Armor +3 (chain mail)"))
magicitems['i'].set(48, 49, Item(name="Armor +3 (chain shirt)"))
magicitems['i'].set(50, 51, Item(name="Cloak of invisibility"))
magicitems['i'].set(52, 53, Item(name="Crystal ball (legendary version)"))
magicitems['i'].set(54, 55, Item(name="Armor +1 (half plate)"))
magicitems['i'].set(56, 57, Item(name="Iron flask"))
magicitems['i'].set(58, 59, Item(name="Armor +3 (leather)"))
magicitems['i'].set(60, 61, Item(name="Armor +1 (plate)"))
magicitems['i'].set(62, 63, Item(name="Robe of the archmagi"))
magicitems['i'].set(64, 65, Item(name="Rod of resurrection"))
magicitems['i'].set(66, 67, Item(name="Armor +1 (scale mail)"))
magicitems['i'].set(68, 69, Item(name="Scarab of protection"))
magicitems['i'].set(70, 71, Item(name="Armor +2 (splint)"))
magicitems['i'].set(72, 73, Item(name="Armor +2 (studded leather)"))
magicitems['i'].set(74, 75, Item(name="Well of many worlds"))
magicitems['i'].set(76, 76, Item(name="Magic Armor", complement_roll=lambda: magicarmor.get(Dice('d12'))))
magicitems['i'].set(77, 77, Item(name="Apparatus of Kwalish"))
magicitems['i'].set(78, 78, Item(name="Armor of inbulnerability"))
magicitems['i'].set(79, 79, Item(name="Belt of storm giant strength"))
magicitems['i'].set(80, 80, Item(name="Cubic gate"))
magicitems['i'].set(81, 81, Item(name="Deck of many things"))
magicitems['i'].set(82, 82, Item(name="Efreeti chain"))
magicitems['i'].set(83, 83, Item(name="Armor of resistance (half plate)"))
magicitems['i'].set(84, 84, Item(name="Horn of Valhalla (iron)"))
magicitems['i'].set(85, 85, Item(name="Instrument of the bards (Ollamh harp)"))
magicitems['i'].set(86, 86, Item(name="Ioun stone (greater absorption)"))
magicitems['i'].set(87, 87, Item(name="Ioun stone (mastery)"))
magicitems['i'].set(88, 88, Item(name="Ioun stone (regeneration)"))
magicitems['i'].set(89, 89, Item(name="Plte armor of etherealness"))
magicitems['i'].set(90, 90, Item(name="Plate armor of resistance"))
magicitems['i'].set(91, 91, Item(name="Ring of air elemental command"))
magicitems['i'].set(92, 92, Item(name="Ring of earth elemental command"))
magicitems['i'].set(93, 93, Item(name="Ring of fire elemental command"))
magicitems['i'].set(94, 94, Item(name="Ring of three wishes"))
magicitems['i'].set(95, 95, Item(name="Ring of water elemental command"))
magicitems['i'].set(96, 96, Item(name="Sphere of annihilation"))
magicitems['i'].set(97, 97, Item(name="Talisman of pure good"))
magicitems['i'].set(98, 98, Item(name="Talisman of the sphere"))
magicitems['i'].set(99, 99, Item(name="Talisman of ultimate evil"))
magicitems['i'].set(100, 100, Item(name="Tome of the stilled tongue"))


class HoardItem:
    def __init__(self, gems_dice, gems, magic_dice, magic, magic2_dice=Dice(), magic2=None):
        self.gems_dice = gems_dice
        self.gems = gems
        self.magic_dice = magic_dice
        self.magic = magic
        self.magic2_dice = magic2_dice
        self.magic2 = magic2


class HoardTable:
    def __init__(self, cp, sp, ep, gp, pp, items):
        self.cp = cp
        self.sp = sp
        self.ep = ep
        self.gp = gp
        self.pp = pp
        self.items = items


hoard_tiers = {
    1: HoardTable(cp=Dice("6d6*100"), sp=Dice("3d6*100"), ep=Dice(), gp=Dice(), pp=Dice(), items=RangeDict()),
    2: HoardTable(cp=Dice("2d6*100"), sp=Dice("2d6*1000"), ep=Dice(), gp=Dice("6d6*100"), pp=Dice("3d6*10"), items=RangeDict()),
    3: HoardTable(cp=Dice(), sp=Dice(), ep=Dice(), gp=Dice("4d6*1000"), pp=Dice("5d6*100"), items=RangeDict()),
    4: HoardTable(cp=Dice(), sp=Dice(), ep=Dice(), gp=Dice("12d6*1000"), pp=Dice("8d6*1000"), items=RangeDict())
}

hoard_tiers[1].items.set(1, 6, HoardItem(Dice(), None, Dice(), None))
hoard_tiers[1].items.set(7, 16, HoardItem(Dice("2d6"), gemstones[10], Dice(), None))
hoard_tiers[1].items.set(17, 26, HoardItem(Dice("2d4"), artobjects[25], Dice(), None))
hoard_tiers[1].items.set(27, 36, HoardItem(Dice("2d6"), gemstones[50], Dice(), None))
hoard_tiers[1].items.set(37, 44, HoardItem(Dice("2d6"), gemstones[10], Dice("1d6"), magicitems['a']))
hoard_tiers[1].items.set(45, 52, HoardItem(Dice("2d4"), artobjects[25], Dice("1d6"), magicitems['a']))
hoard_tiers[1].items.set(53, 60, HoardItem(Dice("2d6"), gemstones[50], Dice("1d6"), magicitems['a']))
hoard_tiers[1].items.set(61, 65, HoardItem(Dice("2d6"), gemstones[10], Dice("1d4"), magicitems['b']))
hoard_tiers[1].items.set(66, 70, HoardItem(Dice("2d4"), artobjects[25], Dice("1d4"), magicitems['b']))
hoard_tiers[1].items.set(71, 75, HoardItem(Dice("2d6"), gemstones[50], Dice("1d4"), magicitems['b']))
hoard_tiers[1].items.set(76, 78, HoardItem(Dice("2d6"), gemstones[10], Dice("1d4"), magicitems['c']))
hoard_tiers[1].items.set(79, 80, HoardItem(Dice("2d4"), artobjects[25], Dice("1d4"), magicitems['c']))
hoard_tiers[1].items.set(81, 85, HoardItem(Dice("2d6"), gemstones[50], Dice("1d4"), magicitems['c']))
hoard_tiers[1].items.set(86, 92, HoardItem(Dice("2d4"), artobjects[25], Dice("1d4"), magicitems['f']))
hoard_tiers[1].items.set(93, 97, HoardItem(Dice("2d6"), gemstones[50], Dice("1d4"), magicitems['f']))
hoard_tiers[1].items.set(98, 99, HoardItem(Dice("2d4"), artobjects[25], Dice("1d1"), magicitems['g']))
hoard_tiers[1].items.set(100, 100, HoardItem(Dice("2d6"), gemstones[50], Dice("1d1"), magicitems['g']))

hoard_tiers[2].items.set(1, 4, HoardItem(Dice(""), None, Dice(""), None))
hoard_tiers[2].items.set(5, 10, HoardItem(Dice("2d4"), artobjects[25], Dice(""), None))
hoard_tiers[2].items.set(11, 16, HoardItem(Dice("3d6"), gemstones[50], Dice(""), None))
hoard_tiers[2].items.set(17, 22, HoardItem(Dice("3d6"), gemstones[10], Dice(""), None))
hoard_tiers[2].items.set(23, 28, HoardItem(Dice("2d4"), artobjects[250], Dice(""), None))
hoard_tiers[2].items.set(29, 32, HoardItem(Dice("2d4"), artobjects[25], Dice("1d6"), magicitems['a']))
hoard_tiers[2].items.set(33, 36, HoardItem(Dice("3d6"), gemstones[50], Dice("1d6"), magicitems['a']))
hoard_tiers[2].items.set(37, 40, HoardItem(Dice("3d6"), gemstones[100], Dice("1d6"), magicitems['a']))
hoard_tiers[2].items.set(41, 44, HoardItem(Dice("2d4"), artobjects[250], Dice("1d6"), magicitems['a']))
hoard_tiers[2].items.set(45, 49, HoardItem(Dice("2d4"), artobjects[25], Dice("1d4"), magicitems['b']))
hoard_tiers[2].items.set(50, 54, HoardItem(Dice("3d6"), gemstones[50], Dice("1d4"), magicitems['b']))
hoard_tiers[2].items.set(55, 59, HoardItem(Dice("3d6"), gemstones[100], Dice("1d4"), magicitems['b']))
hoard_tiers[2].items.set(60, 63, HoardItem(Dice("2d4"), artobjects[250], Dice("1d4"), magicitems['b']))
hoard_tiers[2].items.set(64, 66, HoardItem(Dice("2d4"), artobjects[25], Dice("1d4"), magicitems['c']))
hoard_tiers[2].items.set(67, 69, HoardItem(Dice("3d6"), gemstones[50], Dice("1d4"), magicitems['c']))
hoard_tiers[2].items.set(70, 72, HoardItem(Dice("3d6"), gemstones[100], Dice("1d4"), magicitems['c']))
hoard_tiers[2].items.set(73, 74, HoardItem(Dice("2d4"), artobjects[250], Dice("1d4"), magicitems['c']))
hoard_tiers[2].items.set(75, 76, HoardItem(Dice("2d4"), artobjects[25], Dice("1d1"), magicitems['d']))
hoard_tiers[2].items.set(77, 78, HoardItem(Dice("3d6"), gemstones[50], Dice("1d1"), magicitems['d']))
hoard_tiers[2].items.set(79, 79, HoardItem(Dice("3d6"), gemstones[100], Dice("1d1"), magicitems['d']))
hoard_tiers[2].items.set(80, 80, HoardItem(Dice("2d4"), artobjects[250], Dice("1d1"), magicitems['d']))
hoard_tiers[2].items.set(81, 84, HoardItem(Dice("2d4"), artobjects[25], Dice("1d4"), magicitems['f']))
hoard_tiers[2].items.set(85, 88, HoardItem(Dice("3d6"), gemstones[50], Dice("1d4"), magicitems['f']))
hoard_tiers[2].items.set(89, 91, HoardItem(Dice("3d6"), gemstones[100], Dice("1d4"), magicitems['f']))
hoard_tiers[2].items.set(92, 94, HoardItem(Dice("2d4"), artobjects[250], Dice("1d4"), magicitems['f']))
hoard_tiers[2].items.set(95, 96, HoardItem(Dice("3d6"), gemstones[100], Dice("1d4"), magicitems['g']))
hoard_tiers[2].items.set(97, 98, HoardItem(Dice("2d4"), artobjects[250], Dice("1d4"), magicitems['g']))
hoard_tiers[2].items.set(99, 99, HoardItem(Dice("3d6"), gemstones[100], Dice("1d1"), magicitems['h']))
hoard_tiers[2].items.set(100, 100, HoardItem(Dice("2d4"), artobjects[250], Dice("1d1"), magicitems['h']))

hoard_tiers[3].items.set(1, 3, HoardItem(Dice(""), None, Dice(""), None))
hoard_tiers[3].items.set(4, 6, HoardItem(Dice("2d4"), artobjects[250], Dice(""), None))
hoard_tiers[3].items.set(7, 9, HoardItem(Dice("2d4"), artobjects[750], Dice(""), None))
hoard_tiers[3].items.set(10, 12, HoardItem(Dice("3d6"), gemstones[500], Dice(""), None))
hoard_tiers[3].items.set(13, 15, HoardItem(Dice("3d6"), gemstones[1000], Dice(""), None))
hoard_tiers[3].items.set(16, 19, HoardItem(Dice("2d4"), artobjects[250], Dice("1d4"), magicitems['a'], Dice('1d6'), magicitems['b']))
hoard_tiers[3].items.set(20, 23, HoardItem(Dice("2d4"), artobjects[750], Dice("1d4"), magicitems['a'], Dice('1d6'), magicitems['b']))
hoard_tiers[3].items.set(24, 26, HoardItem(Dice("3d6"), gemstones[500], Dice("1d4"), magicitems['a'], Dice('1d6'), magicitems['b']))
hoard_tiers[3].items.set(27, 29, HoardItem(Dice("3d6"), gemstones[1000], Dice("1d4"), magicitems['a'], Dice('1d6'), magicitems['b']))
hoard_tiers[3].items.set(30, 35, HoardItem(Dice("2d4"), artobjects[250], Dice("1d6"), magicitems['c']))
hoard_tiers[3].items.set(36, 40, HoardItem(Dice("2d4"), artobjects[750], Dice("1d6"), magicitems['c']))
hoard_tiers[3].items.set(41, 45, HoardItem(Dice("3d6"), gemstones[500], Dice("1d6"), magicitems['c']))
hoard_tiers[3].items.set(46, 50, HoardItem(Dice("3d6"), gemstones[1000], Dice("1d6"), magicitems['c']))
hoard_tiers[3].items.set(51, 54, HoardItem(Dice("2d4"), artobjects[250], Dice("1d4"), magicitems['d']))
hoard_tiers[3].items.set(55, 58, HoardItem(Dice("2d4"), artobjects[750], Dice("1d4"), magicitems['d']))
hoard_tiers[3].items.set(59, 62, HoardItem(Dice("3d6"), gemstones[500], Dice("1d4"), magicitems['d']))
hoard_tiers[3].items.set(63, 66, HoardItem(Dice("3d6"), gemstones[1000], Dice("1d4"), magicitems['d']))
hoard_tiers[3].items.set(67, 68, HoardItem(Dice("2d4"), artobjects[250], Dice("1d1"), magicitems['e']))
hoard_tiers[3].items.set(69, 70, HoardItem(Dice("2d4"), artobjects[750], Dice("1d1"), magicitems['e']))
hoard_tiers[3].items.set(71, 72, HoardItem(Dice("3d6"), gemstones[500], Dice("1d1"), magicitems['e']))
hoard_tiers[3].items.set(73, 74, HoardItem(Dice("3d6"), gemstones[1000], Dice("1d1"), magicitems['e']))
hoard_tiers[3].items.set(75, 76, HoardItem(Dice("2d4"), artobjects[250], Dice("1d1"), magicitems['f'], Dice('1d4'), magicitems['g']))
hoard_tiers[3].items.set(77, 78, HoardItem(Dice("2d4"), artobjects[750], Dice("1d1"), magicitems['f'], Dice('1d4'), magicitems['g']))
hoard_tiers[3].items.set(79, 80, HoardItem(Dice("3d6"), gemstones[500], Dice("1d1"), magicitems['f'], Dice('1d4'), magicitems['g']))
hoard_tiers[3].items.set(81, 82, HoardItem(Dice("3d6"), gemstones[1000], Dice("1d1"), magicitems['f'], Dice('1d4'), magicitems['g']))
hoard_tiers[3].items.set(83, 85, HoardItem(Dice("2d4"), artobjects[250], Dice("1d4"), magicitems['h']))
hoard_tiers[3].items.set(86, 88, HoardItem(Dice("2d4"), artobjects[750], Dice("1d4"), magicitems['h']))
hoard_tiers[3].items.set(89, 90, HoardItem(Dice("3d6"), gemstones[500], Dice("1d4"), magicitems['h']))
hoard_tiers[3].items.set(91, 92, HoardItem(Dice("3d6"), gemstones[1000], Dice("1d4"), magicitems['h']))
hoard_tiers[3].items.set(93, 94, HoardItem(Dice("2d4"), artobjects[250], Dice("1d1"), magicitems['i']))
hoard_tiers[3].items.set(95, 96, HoardItem(Dice("2d4"), artobjects[750], Dice("1d1"), magicitems['i']))
hoard_tiers[3].items.set(97, 98, HoardItem(Dice("3d6"), gemstones[500], Dice("1d1"), magicitems['i']))
hoard_tiers[3].items.set(99, 100, HoardItem(Dice("3d6"), gemstones[1000], Dice("1d1"), magicitems['i']))

hoard_tiers[4].items.set(1, 2,    HoardItem(Dice(""),   None, Dice(""), None))
hoard_tiers[4].items.set(3, 5,    HoardItem(Dice("3d6"), gemstones[1000],  Dice("1d8"), magicitems['c']))
hoard_tiers[4].items.set(6, 8,    HoardItem(Dice("1d10"), artobjects[2500], Dice("1d8"), magicitems['c']))
hoard_tiers[4].items.set(9, 11,   HoardItem(Dice("1d4"),  artobjects[7500], Dice("1d8"), magicitems['c']))
hoard_tiers[4].items.set(12, 14,  HoardItem(Dice("1d8"), gemstones[5000],  Dice("1d8"), magicitems['c']))
hoard_tiers[4].items.set(15, 22,  HoardItem(Dice("3d6"), gemstones[1000],  Dice("1d6"), magicitems['d']))
hoard_tiers[4].items.set(23, 30,  HoardItem(Dice("1d10"), artobjects[2500], Dice("1d6"), magicitems['d']))
hoard_tiers[4].items.set(31, 38,  HoardItem(Dice("1d4"), artobjects[7500], Dice("1d6"), magicitems['d']))
hoard_tiers[4].items.set(39, 46,  HoardItem(Dice("1d8"), gemstones[5000],  Dice("1d6"), magicitems['d']))
hoard_tiers[4].items.set(47, 52,  HoardItem(Dice("3d6"), gemstones[1000],  Dice("1d6"), magicitems['e']))
hoard_tiers[4].items.set(53, 58,  HoardItem(Dice("1d10"), artobjects[2500], Dice("1d6"), magicitems['e']))
hoard_tiers[4].items.set(59, 63,  HoardItem(Dice("1d4"), artobjects[7500], Dice("1d6"), magicitems['e']))
hoard_tiers[4].items.set(64, 68,  HoardItem(Dice("1d8"), gemstones[5000],  Dice("1d6"), magicitems['e']))
hoard_tiers[4].items.set(69, 69,  HoardItem(Dice("3d6"), gemstones[1000],  Dice("1d4"), magicitems['g']))
hoard_tiers[4].items.set(70, 70,  HoardItem(Dice("1d10"), artobjects[2500], Dice("1d4"), magicitems['g']))
hoard_tiers[4].items.set(71, 71,  HoardItem(Dice("1d4"), artobjects[7500], Dice("1d4"), magicitems['g']))
hoard_tiers[4].items.set(72, 72,  HoardItem(Dice("1d8"), gemstones[5000],  Dice("1d4"), magicitems['g']))
hoard_tiers[4].items.set(73, 74,  HoardItem(Dice("3d6"), gemstones[1000],  Dice("1d4"), magicitems['h']))
hoard_tiers[4].items.set(75, 76,  HoardItem(Dice("1d10"), artobjects[2500], Dice("1d4"), magicitems['h']))
hoard_tiers[4].items.set(77, 78,  HoardItem(Dice("1d4"), artobjects[7500], Dice("1d4"), magicitems['h']))
hoard_tiers[4].items.set(79, 80,  HoardItem(Dice("1d8"), gemstones[5000],  Dice("1d4"), magicitems['h']))
hoard_tiers[4].items.set(81, 85,  HoardItem(Dice("3d6"), gemstones[1000],  Dice("1d4"), magicitems['i']))
hoard_tiers[4].items.set(86, 90,  HoardItem(Dice("1d10"), artobjects[2500], Dice("1d4"), magicitems['i']))
hoard_tiers[4].items.set(91, 95,  HoardItem(Dice("1d4"), artobjects[7500], Dice("1d4"), magicitems['i']))
hoard_tiers[4].items.set(96, 100, HoardItem(Dice("1d8"), gemstones[5000], Dice("1d4"), magicitems['i']))


class PersonalItem:
    def __init__(self, cp, sp, ep, gp, pp):
        self.cp = cp
        self.sp = sp
        self.ep = ep
        self.gp = gp
        self.pp = pp


personal_tiers = {
    1: RangeDict(),
    2: RangeDict(),
    3: RangeDict(),
    4: RangeDict()
}

personal_tiers[1].set(1, 30, PersonalItem(cp=Dice('5d6'), sp=Dice(''), ep=Dice(''), gp=Dice(''), pp=Dice('')))
personal_tiers[1].set(31, 60, PersonalItem(cp=Dice(''), sp=Dice('4d6'), ep=Dice(''), gp=Dice(''), pp=Dice('')))
personal_tiers[1].set(61, 70, PersonalItem(cp=Dice(''), sp=Dice(''), ep=Dice('3d6'), gp=Dice(''), pp=Dice('')))
personal_tiers[1].set(71, 95, PersonalItem(cp=Dice(''), sp=Dice(''), ep=Dice(''), gp=Dice('3d6'), pp=Dice('')))
personal_tiers[1].set(96, 100, PersonalItem(cp=Dice(''), sp=Dice(''), ep=Dice(''), gp=Dice(''), pp=Dice('1d6')))

personal_tiers[2].set(1, 30, PersonalItem(cp=Dice('4d6*100'), sp=Dice(''), ep=Dice('1d6*10'), gp=Dice(''), pp=Dice('')))
personal_tiers[2].set(31, 60, PersonalItem(cp=Dice(''), sp=Dice('6d6*10'), ep=Dice(''), gp=Dice('2d6*10'), pp=Dice('')))
personal_tiers[2].set(61, 70, PersonalItem(cp=Dice(''), sp=Dice(''), ep=Dice('3d6*10'), gp=Dice('2d6*10'), pp=Dice('')))
personal_tiers[2].set(71, 95, PersonalItem(cp=Dice(''), sp=Dice(''), ep=Dice(''), gp=Dice('4d6*10'), pp=Dice('')))
personal_tiers[2].set(96, 100, PersonalItem(cp=Dice(''), sp=Dice(''), ep=Dice(''), gp=Dice('2d6*10'), pp=Dice('3d6')))

personal_tiers[3].set(1, 20, PersonalItem(cp=Dice(''), sp=Dice('4d6*100'), ep=Dice(''), gp=Dice('1d6*100'), pp=Dice('')))
personal_tiers[3].set(21, 35, PersonalItem(cp=Dice(''), sp=Dice(''), ep=Dice('1d6*100'), gp=Dice('1d6*100'), pp=Dice('')))
personal_tiers[3].set(36, 75, PersonalItem(cp=Dice(''), sp=Dice(''), ep=Dice(''), gp=Dice('2d6*100'), pp=Dice('1d6*10')))
personal_tiers[3].set(76, 100, PersonalItem(cp=Dice(''), sp=Dice(''), ep=Dice(''), gp=Dice('2d6*100'), pp=Dice('2d6*10')))

personal_tiers[4].set(1, 15, PersonalItem(cp=Dice(''), sp=Dice(''), ep=Dice('2d6*1000'), gp=Dice('8d6*100'), pp=Dice('')))
personal_tiers[4].set(16, 55, PersonalItem(cp=Dice(''), sp=Dice(''), ep=Dice(''), gp=Dice('1d6*1000'), pp=Dice('1d6*100')))
personal_tiers[4].set(56, 100, PersonalItem(cp=Dice(''), sp=Dice(''), ep=Dice(''), gp=Dice('1d6*1000'), pp=Dice('2d6*100')))


hoard = RangeDict()
hoard.set(0, 4, hoard_tiers[1])
hoard.set(5, 10, hoard_tiers[2])
hoard.set(11, 16, hoard_tiers[3])
hoard.set(17, 20, hoard_tiers[4])

personal = RangeDict()
personal.set(0, 4, personal_tiers[1])
personal.set(5, 10, personal_tiers[2])
personal.set(11, 16, personal_tiers[3])
personal.set(17, 20, personal_tiers[4])


def get_gem_price(gem):
    for k in gemstones:
        if gem in gemstones[k]:
            return k
    for k in artobjects:
        if gem in artobjects[k]:
            return k
    return -1


def generate_trasure_hoard(level):
    # roll treasure
    cp = 0
    sp = 0
    ep = 0
    gp = 0
    pp = 0
    gems_quantity = 0
    gems_name = ""
    gem_price = 0
    magic = []

    chosen_hoard = hoard.get(level)

    cp = chosen_hoard.cp.roll()
    sp = chosen_hoard.sp.roll()
    ep = chosen_hoard.ep.roll()
    gp = chosen_hoard.gp.roll()
    pp = chosen_hoard.pp.roll()

    dice = Dice("d100")
    hoard_item = chosen_hoard.items.get(dice.roll())
    hoard_item_roll = dice.rolls

    gems_quantity = hoard_item.gems_dice.roll()
    if gems_quantity > 0:
        gems_name = roll_from_list(hoard_item.gems)
        gem_price = get_gem_price(gems_name)

    magic_quantity = hoard_item.magic_dice.roll()
    for i in range(magic_quantity):
        magic.append(hoard_item.magic.get(roll(100)))

    magic_quantity = hoard_item.magic2_dice.roll()
    for i in range(magic_quantity):
        magic.append(hoard_item.magic2.get(roll(100)))

    # print treasure

    print("Treasure Hoard level: %d (rolled: %s)" % (level, hoard_item_roll))
    print("Coins:")
    print("  cp: %d" % cp)
    print("  sp: %d" % sp)
    print("  ep: %d" % ep)
    print("  gp: %d" % gp)
    print("  pp: %d" % pp)

    if gems_quantity > 0:
        print("Gems or Art objecs:")
        print("  %d %s (%d gp each)" % (gems_quantity, gems_name, gem_price))

    if len(magic) > 0:
        print("Magic Items:")
        for item in magic:
            name = item.name
            complement = item.complement_roll()
            print("  %s%s" % (name, ": "+complement if complement != "" else ""))


def generate_personal_treasure(level, quantity):
    # roll treasure
    cp = 0
    sp = 0
    ep = 0
    gp = 0
    pp = 0

    chosen_personal = personal.get(level)

    for i in range(quantity):
        dice = Dice('d100')
        personal_item = chosen_personal.get(dice.roll())

        cp += personal_item.cp.roll()
        sp += personal_item.sp.roll()
        ep += personal_item.ep.roll()
        gp += personal_item.gp.roll()
        pp += personal_item.pp.roll()

    # print treasure
    print("Personal Treasure level: %d, quantity: %d" % (level, quantity))
    print("Coins:")
    print("  cp: %d" % cp)
    print("  sp: %d" % sp)
    print("  ep: %d" % ep)
    print("  gp: %d" % gp)
    print("  pp: %d" % pp)


if (chosen['hoard'] or chosen['personal']) is False:
    chosen['hoard'] = True

print("----------")
if chosen['hoard']:
    generate_trasure_hoard(chosen['level'])

elif chosen['personal']:
    generate_personal_treasure(chosen['level'], chosen['quantity'])
print("----------")
