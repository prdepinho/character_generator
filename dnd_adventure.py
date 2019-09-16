from range_dict import RangeDict
from dnd_dice import Dice, roll_from_list, roll

dungeon_goals = {
        1:  "Stop the dungeon's monstrous inhabitants from raiding the surface world.",
        2:  "Foil a villain's evil scheme.",
        3:  "Destroy a magical threat inside the dungeon.",
        4:  "Acquire treasure.",
        5:  "Find a particular item for a specific purpose.",
        6:  "Retrieve a stolen item hidden in the dungeon.",
        7:  "Find information needed for a special purpose.",
        8:  "Rescue a captive.",
        9:  "Discover the fate of a previous adventuring party.",
        10: "Find an NPC who disappeared in the area.",
        11: "Slay a dragon or some other challenging monster.",
        12: "Discover the nature and origin of a strange location or phenomenon.",
        13: "Pursue fleeing foes taking refuge in the dungeon.",
        14: "Escape from captivity in the dungeon.",
        15: "Clear a ruin so it can be rebuilt and reoccupied.",
        16: "Discover why a villain is interested in the dungeon.",
        17: "Win a bet or complete a rite of passage by surviving in the dungeon.",
        18: "Parley with a villain in the dungeon.",
        19: "Hide from a threaat outside the dungeon.",
        20: "Roll twice, ignoring results of 20.",
        }

wilderness_goals = {
        1:  "Locate a dungeon or other site of interest.",
        2:  "Assess the scope of a natural or unnatural disaster.",
        3:  "Escort an NPC to a destination.",
        4:  "Arrive at a destination without being seen by the billain's forces.",
        5:  "Stop monsters from raiding caravans and farms.",
        6:  "Establish trade with a distant town.",
        7:  "Protect a caravan traveling to a distant town.",
        8:  "Map a new land.",
        9:  "Find a place to establish a colony.",
        10: "Find a natural resource.",
        11: "Hunt a specific monster.",
        12: "Return home from a distant place.",
        13: "Obtain information from a reclusive hermit.",
        14: "Find an object that was lost in the wilds.",
        15: "Discover the fate of a missing group of explorers.",
        16: "Pursue fleeing foes.",
        17: "Assess the size of an approaching army.",
        18: "Escape the reign of a tyrant.",
        19: "Protect a wilderness site from attackers.",
        20: "Roll twice, ignoring results of 20.",
        }

other_goals = {
        1:  "Sieze control of a fortified location such as a fortress, town or ship.",
        2:  "Defend a location from attackers.",
        3:  "Retrieve an object from inside a secure location in a settlement.",
        4:  "Retrieve an object from a caravan.",
        5:  "Salvage an object or goods feom a lost vessel or caravan.",
        6:  "Break a prisoner out of jail or prison camp.",
        7:  "Escape from a jail or prison camp.",
        8:  "Successfully travel through an obstacle course to gain recognition or reward.",
        9:  "Infiltrate a fortified location.",
        10: "Find the source of strange occurrences in a haounted house or other location.",
        11: "Interfere with the operation of a business.",
        12: "Rescue a character, monster, or object from a natural or unnatural disaster.",
        }

villains = RangeDict()
villains.set(1, 1, "Beast or monstrosity with no particular agenda.")
villains.set(2, 3, "Aberration bent on corruption or domination.")
villains.set(3, 3, "Fiend bent on corruption or destruction.")
villains.set(4, 4, "Dragon best on domination and plunder.")
villains.set(5, 5, "Giant bent on plunder.")
villains.set(6, 7, "Undead with any agenda.")
villains.set(8, 8, "Fey with a mysterious goal.")
villains.set(9, 10, "Humanoid cultist.")
villains.set(11, 12, "Humanoid conqueror.")
villains.set(13, 13, "Humanoid seeking revenge.")
villains.set(14, 15, "Humanoid schemer seeking to rule.")
villains.set(16, 16, "Humanoid criminal mastermind.")
villains.set(17, 18, "Humanoid raider or ravager.")
villains.set(19, 19, "Humanoid under a curse.")
villains.set(20, 20, "Misguided humanoid zealot.")

allies = {
        1:  "Skilled adventurer.",
        2:  "Inexperienced adventurer.",
        3:  "Enthusiastic commoner.",
        4:  "Soldier.",
        5:  "Priest.",
        6:  "Sage.",
        7:  "Revenge seeker.",
        8:  "Raving lunatic.",
        9:  "Celestial ally.",
        10: "Fey ally.",
        11: "Disguised monster.",
        12: "Villain posing as an ally."
        }

patrons = RangeDict()
patrons.set(1, 2, "Retired adventurer.")
patrons.set(3, 4, "Local ruler.")
patrons.set(5, 6, "Military officer.")
patrons.set(7, 8, "Temple official.")
patrons.set(9, 10, "Sage.")
patrons.set(11, 12, "Respected elder.")
patrons.set(13, 13, "Deity or celestial.")
patrons.set(14, 14, "Mysterious fey.")
patrons.set(15, 15, "Old friend.")
patrons.set(16, 16, "Former teacher.")
patrons.set(17, 17, "Parent or other family member.")
patrons.set(18, 18, "Desperate commoner.")
patrons.set(19, 19, "Embattled merchant.")
patrons.set(20, 20, "Villain posing as a patron.")

introductions = {
    1: "While traveling in the wilderness, the characters fall into a sinkhole that opens beneath their feet, dropping them into the adventure location.",
    2: "While traveling in the wilderness, the characters notice the entrance to the adventure location.",
    3: "While traveling on a road, the characters are attacked by monsters that flee into the nearby adventure location.",
    4: "The adventurers find a map on a dead body. In addition to the map setting up the adventure, the adventure's villain wants the map.",
    5: "A mysterious magic item or a cruel villain teleports the character to the adventure location.",
    6: "A stranger approaches the characters in a tavern and urges them toward the adventure location.",
    7: "A town or village needs volunteers to go to the adventure location.",
    8: "An NPC the characters care about needs them to go to the adventure location.",
    9: "An NPC the characters must obey orders them to go to the adventure location.",
    10: "An NPC the characters respect asks them to go to the adventure location.",
    11: "One night, the characters all dream about entering the adventure location.",
    12: "A ghost appears and terrorizes a village. Research reveals that it can be put to rest only by entering the adventure location.",
    }

climaxes = {
    1: "The adventurers confront the main villain and a group of minions in a bloody battle to the finish.",
    2: "The adventurers chase the villain while dodging obstacles designed to thwart them, leading to a final controntation in or outside the villain's refuge.",
    3: "The actions of the adventurers or the villain result in a cataclysmic event that the adventurers must espace from.",
    4: "The adventurers race to the site where the villain is bringing a master plan to its conclusion, arriving just as the plan is about to be completed.",
    5: "The villain and two or three loeutenants perform separate rites in a large room. The adventurers must disrupt all the rites at the same time.",
    6: "An ally betrays the adventurers as they're about to achieve their goal. (Don't over use it.)",
    7: "A portal opens to another plane of existence. Creatures on the other side spill out, forcing the adventurers to close the portal and deal with the villain at the same time.",
    8: "Traps, hazards, or animated objects turn against the adventurers while the main villain attacks.",
    9: "The dungeon begins to collapse while the adventureres face the main villain, who attemps to escape in the chaos.",
    10: "A threat more powerful than the adventurers appears, destroys the main villain, and then turns its attention on the characters.",
    11: "The adventurers must choose whether to pursue the fleeing main villain or save an NPC theuy care about or a group of innocents.",
    12: "The adventurers must discover the main villain's secret weakness before they can hope to defeat that villain.",
    }

event_based_villain_actions = {
        1: {'name': "Big event",            'desc': "The villain's plans come to fruition during a festival, an astrological event, a holy (or unholy) rite, a royal wedding, the birth of a child, or some similar fixed time. The villain's activities up to that point are geared toward preparation for this event."},
        2: {'name': "Crime spree",          'desc': "The villain commits acts that become bolder and more heinous over time. A killer might start out by targeting the destitute in the city slums before moving up to a massacre in the marketplace, increasing the horror and the body count each time."},
        3: {'name': "Growing corruption",   'desc': "As time passes, the billain's power and influence grow, affecting more victims across a larger area. This might take the form of armies conquering new territory, an evil cult recruiting new members, or a spreading plague. A pretender to the throne might attempt to secure the support of the kingdom's nobility in the days or weeks leading up to a coup, or a guild leader could corrupt the members of a town council or bribe officers of the watch."},
        4: {'name': "One and done",         'desc': "The villain commits a single crime and then tries to avoid the consequences. Instead of an ongoing plan to commit more crimes, the villain's goal is to lie low or flee the scene."},
        5: {'name': "Serial crimes",        'desc': "The villain commits crimes one after the other, but these acts are repetitive in nature, rather than escalating to grater heights of deptravity. The trick to catching such a villain lies in determining the patters underlying the crimes. Though serial killers are a common example of this type of villain, your villain could be a serial arsonist favoring a certain type of building, a magical sickness that affects spellcasters who cast a specific spell, a thief that targets a certain kind of merchant, or a doppelganger kidnapping and impersonating one noble after another."},
        6: {'name': "Step by step",         'desc': "In pursuit of its goal, the villain carries out a specific set of actions in a particular sequence. A wizard might steal the items needed to create a phulactery and become a lich, or a cultist might ikdnap the priests of seven good-aligned gods as a sacrifice. Alternatively, the villain could be following a trail to find the object of its revenge, killing one victim fafter anoter while moving ever closer to the real target."},
        }

event_based_goals = {
        1:  "Bring the villain to justice.",
        2:  "Clear the name of an innocent NPC.",
        3:  "Protect or hide an NPC.",
        4:  "Protect an object.",
        5:  "Discover the nature and origin of a strange phenomenon that might be the villain's doing.",
        6:  "Find a wanted fugitive.",
        7:  "Overthrow a tyrant.",
        8:  "Uncover a conspiracy to overthrow a ruler.",
        9:  "Negotiate peace between enemy nations or feuding families.",
        10: "Secure aid from a ruler or council.",
        11: "Help a villain find redemption.",
        12: "Parley with a villain.",
        13: "Smuggle weapons to rebel forces.",
        14: "Stop a band of smugglers.",
        15: "Gather intelligence on an anemy force.",
        16: "Win a tournament.",
        17: "Determine the villain's identity.",
        18: "Locate a stolen item.",
        19: "Make sure a wedding goes off without a hitch.",
        20: "Roll twice, ignoring results of 20.",
        }

framing_events = RangeDict()
framing_events.set(1, 2, "Anniversary of a monarch's reign.")
framing_events.set(3, 4, "Anniversary of an important event.")
framing_events.set(5, 6, "Arena event.")
framing_events.set(7, 8, "Arrival of a caravan or ship.")
framing_events.set(9, 10, "Arrival of a circus.")
framing_events.set(11, 12, "Arrivbal of an important NPC.")
framing_events.set(13, 14, "Arrival of marching modrons.")
framing_events.set(15, 16, "Artistic performance.")
framing_events.set(17, 18, "Athletic event.")
framing_events.set(19, 20, "Birth of a child.")
framing_events.set(21, 22, "Birthday of an important NPC.")
framing_events.set(23, 24, "Civic festival.")
framing_events.set(25, 26, "Comet appearance.")
framing_events.set(27, 28, "Commemoration of a past tragedy.")
framing_events.set(29, 30, "Consecration of a new temple.")
framing_events.set(31, 32, "Coronation.")
framing_events.set(33, 34, "Council meeting.")
framing_events.set(35, 36, "Equinox or solstice.")
framing_events.set(37, 38, "Execution.")
framing_events.set(39, 40, "Fertility festival.")
framing_events.set(41, 42, "Full moon.")
framing_events.set(43, 44, "Funeral.")
framing_events.set(45, 46, "Graduation of cadets or wizards.")
framing_events.set(47, 48, "Harvest festival.")
framing_events.set(49, 50, "Holy day.")
framing_events.set(51, 52, "Investiture of a knight or other noble.")
framing_events.set(53, 54, "Lunar eclipse.")
framing_events.set(55, 58, "Midsummer festival.")
framing_events.set(59, 60, "Midwinter festival.")
framing_events.set(61, 62, "Migration of monsters.")
framing_events.set(63, 64, "Monarch's ball.")
framing_events.set(65, 66, "New moon.")
framing_events.set(67, 68, "New year.")
framing_events.set(69, 70, "Pardoning of a prisoner.")
framing_events.set(71, 72, "Planar conjunction.")
framing_events.set(73, 74, "Planetary alignment.")
framing_events.set(75, 76, "Priestly investiture.")
framing_events.set(77, 78, "Procession of ghosts.")
framing_events.set(79, 80, "Remembrance for soldiers lost in war.")
framing_events.set(81, 82, "Royal address or proclamation.")
framing_events.set(83, 84, "Royal audience day.")
framing_events.set(85, 86, "Signing of a treaty.")
framing_events.set(87, 88, "Solar eclipse.")
framing_events.set(89, 91, "Tournament.")
framing_events.set(92, 94, "Trial.")
framing_events.set(95, 96, "Violent uprising.")
framing_events.set(97, 98, "Wedding or wedding anniversary.")
framing_events.set(99, 100, "Concurrence of two events (roll twice, ignoring reults of 99 or 100).")

moral_quandaries = RangeDict()
moral_quandaries.set(1, 3, "Ally quandary.")
moral_quandaries.set(4, 6, "Friend quandary.")
moral_quandaries.set(7, 12, "Honor quandary.")
moral_quandaries.set(13, 16, "Rescue quandary.")
moral_quandaries.set(17, 20, "Respect quandary.")

twists = {
        1: "The adventurers are racing against other creatures with the same or opposite goal.",
        2: "The adventurers become responsible for the safety of a noncombatant NPC.",
        3: "The adventurers are prohibited from killing the villain, but the villain has no compunctions about killing them.",
        4: "The adventurers have a time limit.",
        5: "The adventurers have a received false or extraneous information.",
        6: "Completing an adventure goal fulfills a prophecy or prevents the fulfillment of a prophecy.",
        7: "The adventurers have two different goals, but they can complete only one.",
        8: "Completing the goal secretly helps the villain.",
        9: "The adventurers must cooperate with a known enemy to achieve the goal.",
        10: "The adventurers are under magical compulsion (such as a geas spell) to complete their goal.",
        }

site_quests = {
        1: "Find a specific item rumored to be in the area.",
        2: "Retrieve a stolen item in the villain's possession.",
        3: "Receive information from an NPC in the area.",
        4: "Rescue a captive.",
        5: "Discover the fate of a missing NPC.",
        6: "Slay a specific monster.",
        7: "Discover the nature and origin of a strange phenomenon in the area.",
        8: "Secure the aid of a character or creature in the area.",
        }


def roll_dungeon_goal():
    result = roll(20)
    if result < 20:
        dungeon_goal = [dungeon_goals[result]]
    else:
        dungeon_goal = [
                dungeon_goals[roll(19)],
                dungeon_goals[roll(19)]
                ]
    return dungeon_goal


def roll_wilderness_goal():
    result = roll(20)
    result1 = roll(19)
    result2 = roll(19)
    wilderness_dungeon_goal = []
    if result < 20:
        wilderness_goal = [wilderness_goals[roll(result)]]
    else:
        wilderness_goal = [
                wilderness_goals[result1],
                wilderness_goals[result2]
                ]
    if 1 in [result, result1, result2]:
        wilderness_dungeon_goal = roll_dungeon_goal()

    return wilderness_goal, wilderness_dungeon_goal

def roll_other_goal():
    other_goal = [other_goals[roll(12)]]
    return other_goal

def roll_event_based_goals():
    result = roll(20)
    if result < 20:
        return [
                event_based_goals[result]
                ]
    else:
        return [
                event_based_goals[roll(19)],
                event_based_goals[roll(19)]
                ]


def roll_framing_events():
    result = roll(100)
    if result < 99:
        return [
                framing_events.get(result)
                ]
    else:
        return [
                framing_events.get(roll(98)),
                framing_events.get(roll(98))
                ]


if __name__ == "__main__":
    dungeon = roll(2) == 1
    location = roll_from_list(['dungeon', 'wilderness', 'other'])
    if location == 'dungeon':
        dungeon_goal = roll_dungeon_goal()
    elif location == 'wilderness':
        wilderness_goal, wilderness_dungeon_goal = roll_wilderness_goal()
    else:
        other_goal = roll_other_goal()
    villain = villains.get(roll(20))
    ally = allies[roll(12)]
    patron = patrons.get(roll(20))
    introduction = introductions[roll(12)]
    climax = climaxes[roll(12)]

    event_based_villain_action = event_based_villain_actions[roll(6)]
    event_based_goal = roll_event_based_goals()
    framing_event = roll_framing_events()
    moral_quandary = moral_quandaries.get(roll(20))
    twist = twists[roll(10)]
    side_quest = site_quests[roll(8)]


    # print
    if location == 'dungeon':
        print('Adventure location: Dungeon:')
        for goal in dungeon_goal:
            print('- Goal: %s' % goal)

    elif location == 'wilderness':
        print('Adventure location: Wilderness:')
        for goal in wilderness_goal:
            print('- Goal: %s' % goal)
        for goal in wilderness_dungeon_goal:
            print('Dungeon Goal: %s' % goal)

    else:
        print('Adventure location: Other:')
        for goal in other_goal:
            print("- Goal: %s" % goal)

    print("- Villain: %s" % villain)
    print("- Ally: %s" % ally)
    print("- Patron: %s" % patron)
    print("- Introduction: %s" % introduction)
    print("- Climax: %s" % climax)

    print("- Event based billain actions: %s: %s" % (event_based_villain_action['name'], event_based_villain_action['desc']))
    print("- Event based goal: %s" % event_based_goal)
    print("- Framing event: %s" % framing_event)
    print("- Moral quandary: %s" % moral_quandary)
    print("- Side quest: %s" % side_quest)
