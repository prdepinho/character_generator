import random
import math
import sys
import getopt
import statistics


chosen = {
        'class': '',
        'race': '',
        'background': '',
        'statistics': 0,
        'roll_four': True,
        'roll_three': False,
        'max_abilities': False,
        'random_class': False
        }

try:
    optlist, args = getopt.getopt(
            sys.argv[1:],
            'c:r:b:s:',
            ['class=', 'race=', 'background=', 'statistics=', 'max-abilities', 'roll-four', 
             'roll-three', 'random-class', 'help'])

except getopt.GetoptError as e:
    print(e)
    exit()

for o, a in optlist:
    if o in ['-c', '--class']:
        chosen['class'] = a
    elif o in ['-r', '--race']:
        chosen['race'] = a
    elif o in ['-s', '--statistics']:
        chosen['statistics'] = int(a)
    elif o in ['-b', '--background']:
        chosen['background'] = a
    elif o == '--max-abilities':
        chosen['max_abilities'] = True
    elif o == '--roll-four':
        chosen['roll_four'] = True
    elif o == '--roll-three':
        chosen['roll_three'] = True
    elif o == '--random-class':
        chosen['random_class'] = True
    elif o == '--help':
        print('Execute the program to generate a character. The following options are available.')
        print('The program will try to choose the best class and skills according to rolled abilities.')
        print('%-40s %s' % ('-c, --class [class]:', 'Choose a class.'))
        print('%-40s %s' % ('-r, --race [race]:', 'Choose a race.'))
        print('%-40s %s' % ('-b, --background [background]:', 'Choose a background'))
        print('%-40s %s' % ('-s, --statistics [population]:', 'Create a population of random characters and show some statistics.'))
        print('%-40s %s' % ('--max-abilities:', 'Roll only 20s for abilities.'))
        print('%-40s %s' % ('--roll-four:', 'Roll four dice for abilitise and drop the lowest. This is the default.'))
        print('%-40s %s' % ('--roll-three:', 'Roll three dice for abilities.'))
        print('%-40s %s' % ('--random-class:', 'Choose a random class disregarding ability scores.'))
        exit()
    else:
        print('unhandled option: %s' % o)


def roll(die):
    """ Row a die sided die. """
    return random.randint(1, die)


def roll_attribute():
    """ Roll an attribute with four dice, dropping the lowest.
    Return the result followed by an ordered list of the rolls. """
    if chosen['max_abilities']:
        return 20, [6, 6, 8]
    else:
        if chosen['roll_three']:
            rolls = [0, 0, 0]
            for i in range(3):
                rolls[i] = roll(6)
            rolls = sorted(rolls)
            return sum(rolls), rolls
        elif chosen['roll_four']:
            rolls = [0, 0, 0, 0]
            for i in range(4):
                rolls[i] = roll(6)
            rolls = sorted(rolls)
            return sum(rolls[1:]), rolls


def roll_from_list(lst):
    """ Chose randomly an element of a given list. """
    if lst == []:
        return None
    return lst[roll(len(lst)) - 1]


def modifier(ability):
    """ Get the modifier for an ability score. """
    return math.floor((ability - 10) / 2)


skill_ability_map = {
        "Athletics": "str",
        'Acrobatics': 'dex',
        'Sleight of Hand': 'dex',
        'Stealth': 'dex',
        'Arcana': 'int',
        'History': 'int',
        'Investigation': 'int',
        'Nature': 'int',
        'Religion': 'int',
        'Animal Handling': 'wis',
        'Insight': 'wis',
        'Medicine': 'wis',
        'Perception': 'wis',
        'Survival': 'wis',
        'Deception': 'cha',
        'Intimidation': 'cha',
        'Performance': 'cha',
        'Persuasion': 'cha'
        }


class Background:
    def __init__(self, name, features, speciality_name, specialities, skill_proficiencies, traits, ideals, bonds, flaws):
        self.name = name
        self.traits = traits
        self.ideals = ideals
        self.bonds = bonds
        self.flaws = flaws
        self.skill_proficiencies = skill_proficiencies
        self.features = features
        self.speciality_name = speciality_name
        self.specialities = specialities


backgrounds = [
        Background(name="Acolyte",
                   features=["Shelter of the Faithful"],
                   speciality_name="",
                   specialities=[],
                   skill_proficiencies=['Insight', 'Religion'],
                   traits=[
                       "I adolize a particular hero of my faith, and constantly refer to that person's deeds and example",
                       "I can find common ground between the fiercest enemies, empathizing with them and always working towar peace.",
                       "I see omens in every event and action. The gods try to speak to us, we just need to listen.",
                       "Nothing can shake my optimistic attitude.",
                       "I quote (or misquote) sacred texts and proverbs in almost every situation.",
                       "I am tolerant (or intolerant) of other faiths and respect (or condenm) the worship of other gods.",
                       "I've enjoyed fine food, drink, and high society among my temple's elite. Rough living grates on me.",
                       "I've spent so long in the temple that I have little practical experience dealing with people in the outside world."
                       ],
                   ideals=[
                       ("Tradition", "The ancient traditions of worship and sacrifice must be preserved and upheld.", 'lawful'),
                       ("Charity", "I always try to help those in need, no matter what the personal cost.", 'good'),
                       ("Change", "We must help bring about the changes the gods are constantly woking in the world.", 'chaotic'),
                       ("Power", "I hope to one day rise to the top of my faith's religious hierarchy.", "lawful"),
                       ("Faith", "I trust that my deity will guide my actions. I have faith that if I work hard, things will go well.", 'lawful'),
                       ('Aspiration', "I seek to prove myself worthy of my god's favormy matching my actions against his or her teachins.", 'any')
                       ],
                   bonds=[
                       "I would die to recover an ancient relic of my faith that was lost long ago.",
                       "I will someday get revenge on the corrupt temple hierarchy who branded me a heretic.",
                       "I owe my life to the priest who took me in when my parents died.",
                       "Everything I do is for the common people.",
                       "I will do anything to protect the temple where I served.",
                       "I seek to preserve a sacred text that my enemies consider heretical and seek to destroy."
                       ],
                   flaws=[
                       "I judge others harshly, and myself even more seveerly.",
                       "I put too much trust in those who wield power within my temple's hierarchy.",
                       "My piety sometimes leads me to blindly trust those that profess faith in my god.",
                       "I am inflexible in my thinking.",
                       "I am suspicious of strangers and expect the worst of them.",
                       "Once I pick a goal, I become obsessed with it to the detriment of everything else."
                       ]),
        Background(name="Charlatan",
                   features=["False Identity"],
                   speciality_name="Scam",
                   specialities=[
                       "I cheat at games of change.",
                       "I shave coins or forge documents.",
                       "I insinuate myself into people's lives to prey on their weakness and secure their fortunes.",
                       "I put on new identities like clothes.",
                       "I run sleight-of-hand cons on street corners.",
                       "I convince people that worthless junk is worth their hard-earned money."
                       ],
                   skill_proficiencies=['Deception', 'Sleight of Hand'],
                   traits=[
                       "I fall in and out of love easily, and am always pursuing someone.",
                       "I have a joke for every occasion, especially occasions where humor is inppropriate.",
                       "Flattery is my preferred trick for getting what I want.",
                       "I'm a born gambler who can't resiste taking a risk for a potential payoff.",
                       "I lie about almost everything, even when there's no good reason to.",
                       "Sarcarm and insults are my weapons of choice.",
                       "I keep multiple holy symbols on me and invoke whatever deity might come in useful at ny given moment.",
                       "I pocket anything I see that might have some value."
                       ],
                   ideals=[
                       ('Independence', "I am free spirit - no one tells me what to do", 'chaotic'),
                       ('Fairness', "I never target people who can't afford to lose a few coins", 'lawful'),
                       ('Charity', "I distribute the money I acquire to the people who really need it.", 'good'),
                       ('Creativity', "I never run the same con twice.", 'chaotic'),
                       ('Friendship', "Materail goods come and go. Bonds of friendship last forever.", 'good'),
                       ('Aspiration', "I'm determined to make something of myself.", 'any')
                       ],
                   bonds=[
                       "I fleeced the wrong person and must work to ensure that this individual nevercrsses paths with meor those I care about.",
                       "I owe everything to my mentor - a horrible person who's probably rotting in a jail somewhere.",
                       "Somewhere out there, I have a cild who desn't know me. I'm making the world better for mid or her.",
                       "I come from a noble family, and one day I'll reclaim my lands and title from those who stole them from me.",
                       "A powerful person killed someone I love. Some day soon, I'll have my revenge.",
                       "I swindled and ruined aperson who didn't deserved it. I seek to atone for my misdeeds but might neverbe able to forgive myself."
                       ],
                   flaws=[
                       "I can't resist a pretty face."
                       "I'm always in debt. I spend my ill-gotten gains on decadent luxuries faster than I bring them in.",
                       "I'm convinced that no one could ever fool me the way I fool others.",
                       "I'm too greedy for my own good. I can't resist takin a rist if there's money involved.",
                       "I can't resist swindling people who are more powerful than me.",
                       "I hate to admint it and will hate myself for it, but I'll run and preserve my own hide if the going gets tough."
                       ]),
        Background(name="Criminal",
                   features=["Criminal Contact"],
                   speciality_name="Speciality",
                   specialities=[
                       "Blackmailer",
                       "Burglar",
                       "Enforcer",
                       "Fence",
                       "Highway robber",
                       "Hired killer",
                       "Pickpocket",
                       "Smuggler",
                       ],
                   skill_proficiencies=['Deception', 'Stealth'],
                   traits=[
                       "I always have a plan for what to do when things go wrong.",
                       "I am always calm, no matter hat the situation. I never raise my voice or let my emotions control me.",
                       "The first thing I do in a new place is not the locations of everything valuable - or where such things could be hidden.",
                       "I would rather make a new friend than a new enemy.",
                       "I am incredibly slow to trust. Thosewho seem the fairest often have the most to hide.",
                       "I don't payattention to he risks in a situation. Never tell me the odds.",
                       "The best way to get me to do something is to tell me I can't do it.",
                       "I blow up at the slightest insult."
                       ],
                   ideals=[
                       ('Honor', "I don't steal from others in the trade.", 'lawful'),
                       ('Freedom', "Chains are meant to be broken, as are those who would forge them.", 'chaotic'),
                       ('Charity', "I steal from the wealthy so that I can help people in need.", 'good'),
                       ('Greed', "I will do whatever it takes to become wealthy.", 'evil'),
                       ('People', "I'm loyal to my friends, not to any ideals, and everyone else can take a trip down the Styx for all I care.", 'neutral'),
                       ('Redemption', "There is a spark of good in everyone.", 'good')
                       ],
                   bonds=[
                       "I'm trying to pay off an old debt I owe to a generous benefactor.",
                       "My ill-gotten gains go to support my family.",
                       "Something important was taken from me, and I aim to steal it back.",
                       "I will become the greatest thief that ever lived.",
                       "I'm guilty of a terrible crime. I hope I can redeem myself for it.",
                       "Someone I loved died because of a mistake I made. That will never happen again."
                       ],
                   flaws=[
                       "When I see something valuable, I can't think about anything but how to steal it.",
                       "When faced with a choice between money and my friends, I usually choose the money.",
                       "If there's aplan, I'll forget it. If I don't forget it, I'll ignore it.",
                       "I have a 'tell' that reveals when I'm lying.",
                       "I turn tail and run when things look bad.",
                       "An innocent person is in prison for a crime that I committed. I'm okay with that."
                       ]),
        Background(name="Entertainer",
                   features=["By Popular Demand"],
                   speciality_name="Entertainer Routines",
                   specialities=["Actor", 'Dancer', 'Fire-eater', 'Jester', 'Juggler', 'Instrumentalist', 'Poet', 'Singer', 'Storyteller', 'Tumbler'],
                   skill_proficiencies=['Acrobatics', 'Performance'],
                   traits=[
                       "I know a story relevant to almost every situation.",
                       "Whenever I come to a new place, I collect local rmors and spread gossip.",
                       "I'm a hopeless romantic, always searching for that 'special someone.'",
                       "Nobody stays angry at me or around me for long, since I can defuse any amount of tension.",
                       "I love a good insult, even one directed at me.",
                       "I get bitter if I'm no the center of attention.",
                       "I'll settle for nothing less than perfection.",
                       "I change my mood or my mind as quickly as I change key in a song."
                       ],
                   ideals=[
                       ('Beauty', "When I perform, I make the world better than it was.", 'Good'),
                       ('Tradition', "The stories, legends, and songs of the past must never be forgotten, for they teach us who we are.", 'lawful'),
                       ('Creativity', "The world is in need of new ideas and bold action.", 'chaotic'),
                       ('Greed', "I'm only in it for the money and fame.", 'evil'),
                       ('People', "I like seeing the smiles on people's faces when I perform. That's all that matters.", 'neutral'),
                       ('Honesty', "Art should refect the soul; it should come from within and reveal who we really are.", 'any')
                       ],
                   bonds=[
                       "My instrument is my most treasured possession, and it reminds me of someone I love.",
                       "Someone stole my precious instrument, and someday I'll get it back.",
                       "I want to be famous, whatever it takes.",
                       "I idolize a hero of the old tales and measure my deeds against that person's.",
                       "I will do anything to prove myself superior to my hated rival.",
                       "I would do anything for the other members of my old troupe."
                       ],
                   flaws=[
                       "I'll do anything to win fame and renown.",
                       "I'm a sucker for a pretty face.",
                       "A scandal prevents me from ever going home again.That kind of trouble seems to follow me around.",
                       "I once satirized a noble who still wants my had. It was a mistake that I will likely repeat.",
                       "I have trouble keeping my true feelings hiddden. My sharp tongue lands me in trouble.",
                       "Despite my best efforts, I am unreliable to my friends."
                       ]),
        Background(name="Folk Hero",
                   features=["Rustic Hospitality"],
                   speciality_name="Defining Event",
                   specialities=[
                       "I stood up to a tyrant's agents.",
                       "I saved people during a natural disaster",
                       "I stood alone against a terrible monster.",
                       "I stole from acorrumpt merchant to help the poor.",
                       "I led a militia to fight off a ninvading army.",
                       "I broke into a trant's castle and stole weapons to arm the people.",
                       "I trained the peasantry to use farm implements as weapons against a tyrant's soldiers.",
                       "A lord rescinded an unpopular decree after I led a symbolic act of protest against it.",
                       "A celestial, fey, or similar creature gave me a blessing or revealed my secret origin.",
                       "Recreited into a lord's army, I rose to leadership and was commended for my heroism."
                       ],
                   skill_proficiencies=['Animal Handling', 'Survival'],
                   traits=[
                       "I judge people by their actions, not their words.",
                       "If someone is in trouble, I'm always ready to lend help.",
                       "When I set my mind to something, I follow through no matter what gets in my way.",
                       "I have a strong sense offair play and always try to find the most equitable solution to arguments.",
                       "I'm confident ni my own abilities and do what I can to instill confidence in others.",
                       "Thinking is for other people. I prefer action.",
                       "I misuse long words in an attempt to sound smarter.",
                       "I get bored easily. When am I going to get on with my destiny?"
                       ],
                   ideals=[
                       ('Respect', "People deserve to be treated with dignity and respect.", 'good'),
                       ('Fairness', "No one should get preferential treatment before the aw, and no one is above the law.", 'lawful'),
                       ('Freedom', "Tyrants myst not be allowed to oppress the people.", 'chaotic'),
                       ('Might', "If I become strong, I can take what I want - what I deserve.", 'evil'),
                       ('Sincerity', "There's no good in pretending to be something I'm not.", 'neutral'),
                       ('Destiny', "Nothing and no one can steer me away from my higher calling.", 'any')
                       ],
                   bonds=[
                       "I have a family, but I have no idea where they are. One day, I hope to see them gain.",
                       "I worded the land, I love the land, and I will protect the land.",
                       "A proud noble once gave me a horrible beating, and I will take my revenge on any bully I encounter.",
                       "My tools are symbols of my past life, and I carry them so that I will never forget my roots.",
                       "I protect those who cannot protect themselves.",
                       "I wish my childhood sweetheart had come with me to pursue my destiny."
                       ],
                   flaws=[
                       "The tyrant who rules my land will stop at nothing to see me killed.",
                       "I'm convinced of the significance of my destiny, and blind to my shortcomings and the risk of failure.",
                       "The people who knew me when I was young know my shameful secret, so I can never go home again.",
                       "I have a weakness for the vices of the city, especially hard drink.",
                       "Secretly, I believe that things would be better if I were a tyrant lording over the land.",
                       "I have trouble trusting in my allies."
                       ]),
        Background(name="Guild Artisan",
                   features=["Guild Membership"],
                   speciality_name="Guild Business",
                   specialities=[
                       'Alchemists and apothecaries', 'Armorers, locksmiths, and finesmiths',
                       'Brewers, distillers, andvintners', 'Calligraphers, scribes, and scriveners',
                       'Calligraphers, scribes, and scriveners', 'Carpenters, roofers, and plasterers',
                       'Cartographers, surveyors, and chart-makers', 'Cobblers and shoemakers',
                       'Cooks and bakers', 'Glassblowers and glaziers', 'Jewlers and gemcutters',
                       'Leatherworkers, skinners, and tanners', 'Masons and stonecutters', 'Painters, limners, and sign-makers',
                       'Potters and tile-makers', 'Shipwrights and sailmakers', 'Smiths and metal-forgers',
                       'Tinkers, pewterers, and casters', 'Wagon-makers and wheelwrights',
                       'Weavers and dyers', 'Woodcarvers, coopers, and bowyers'
                       ],
                   skill_proficiencies=['Insight', 'Persuasion'],
                   traits=[
                       "I believe that anything worth doing is worth doing right. I can't help it - I'm a perfectionist.",
                       "I'm a snob who looks down on those who can't appreciate fine art.",
                       "I always want to knowhow things work and what makes people tick.",
                       "I'm full of witty aphorisms and have a proverb for every occasion.",
                       "I'm rude to people who lack my commitment to hard work and fair play.",
                       "I like to talk at length about my profession.",
                       "I don't part with my money easily and will haggle tirelessly to get the best deal possible.",
                       "I'm well known for my work, and I want to make sure everyone appreciates it. I'm always take naack when people haven't heard of me."
                       ],
                   ideals=[
                       ('Community', "It is duty of all civilized people to strengthen the bonds of community and the security of civilization.", 'lawful'),
                       ('Generosity', "My talentswere given to me so that I could use them to benefit the world.", 'good'),
                       ('Freedom', "Everyone should be free to pursue his or her own livelihood.", 'chaotic'),
                       ('Greed', "I'm only in it for he money.", 'evil'),
                       ('People', "I'm committed to the people I care about, not to ideals.", 'neutral'),
                       ('aspiation', "I work hard to be the best there is at my craft.", 'any')
                       ],
                   bonds=[
                       "The workshop where I learned my trade is the most imnportant place in the world to me.",
                       "I created a great wrk for someone, and then found them unworthy to receive it. I'm still looking for someone worthy.",
                       "I owe my guild a great debt for forging me into the person that I am today.",
                       "I pursue wealth to secure someone's love.",
                       "One day I will retun o my guild and prove that I am the greatest artisan of them all.",
                       "I will get revenge on the evil forces that destroyed my place of business and ruined my livelihood."
                       ],
                   flaws=[
                       "I'll do anything to get my hands on something rare or priceless.",
                       "I'm quick to assume that someone is trying to cheat me.",
                       "Non one must ever learn that I once stle money from guild coffers.",
                       "I'm never satisfied with what I have - I always want more.",
                       "I would kill to acquire a noble title.",
                       "I'm horribly jealous of anyone who can outshine my hadiwork. Everywhere I go, I'm surrounded by rivals."
                       ]),
        Background(name="Hermit",
                   features=["Discovery"],
                   speciality_name="Life of Seclusion",
                   specialities=[
                       "I was searching for spiritual enlightenment",
                       "I was partaking of communal living in accordance with the dictates of a religious order.",
                       "I was exile for a crime I didn't commit.",
                       "I retreated from society after a life-altering event.",
                       "I needed a quiet place to work on my art, literature, music, or manifesto.",
                       "I needed to commune with nature, far from civilization.",
                       "I was the caretaker of an ancient ruin or relic.",
                       "I was a pilgrim in search of a person, place, or relic of spiritual signifiacnce."
                       ],
                   skill_proficiencies=['Medicine', 'Religion'],
                   traits=[
                       "I've been isolated for so long that I rarely speak, preferring gestures and the occasional grunt.",
                       "I am utterly serene, even in the face of disaster.",
                       "The leader of my community had something wise to say on every topic, and I am eager to share that wisdom.",
                       "I feel tremendous empathy for all who suffer.",
                       "I'm oblivious to etiquette and social expectations.",
                       "I connect everything that happens to me to a gran, cosmic plan.",
                       "I often get lost in my own thoughts and contemplation, becoming oblivious to my surroundings.",
                       "I am working on a grand philosophical theory and love sharing my ideals."
                       ],
                   ideals=[
                       ('Greateer Good', "My gifts are meant to be shared with all, not used for my own benefit.", 'good'),
                       ('Logic', "Emotions must not cloud our sense of what is rightand true, orour logical thinking.", 'lawful'),
                       ('Free Thinking', "Inquiry and curiosity are the pillars of progress.", 'chaotic'),
                       ('Power', "Solitude and contemplation are paths toward mystical or magical power.", 'evil'),
                       ('Live and Let Live', "Meddling in the affairs of others only causes troube.", 'neutral'),
                       ('Self-Knoweledge', "If you know yourself, there's nothing left to know.", 'any')
                       ],
                   bonds=[
                       "Nothing is more important than the other members of my hermitage, order or association.",
                       "I entered seclusion to hide from the ones who might still be hunting me. I myst someday confront them.",
                       "I'm still seeking enlightenment I pursued in my seclusion, and it still eludes me.",
                       "I entered seclusion because I loved someone I could not have.",
                       "Should my discovery come to light, it could brin ruin to the world.",
                       "My isolation gave me great insight into a great evil that only I can destroy."
                       ],
                   flaws=[
                       "Now that I've returned to the world, I enjoy its delights a little too mych.",
                       "I harbor dark, bloodthirsty thoughts that my isolation and meditation failedto quell.",
                       "I am dogmatic in my thoughts and philosophy.",
                       "I letmy need to win arguments overshadow friendships and harmony.",
                       "I'd risk too mych to uncover a lost bit of knowledge.",
                       "I like keeping secrets and won't share them with anyone."
                       ]),
        Background(name="Noble",
                   features=["Position of Privilege"],
                   speciality_name="",
                   specialities=[],
                   skill_proficiencies=['History', 'Persuasion'],
                   traits=[
                       "My eloquent flattery makes everyone I talk to feel like the most wonderful and important person in the world.",
                       "The common folk love mefor my kindness and generosity.",
                       "No one coulddoubt by looking at my regal bearing that I am a cut above the unwashd masses.",
                       "I take great pains to always look my best and follow the latest fashins.",
                       "I don't like to get my hands dirty, and I won't be caught dead in unsuitable accommodations.",
                       "Despite my noble birth, I do not place myself above other folk. We all have the same blood.",
                       "My favor, once lost, is lost forever.",
                       "If you do me an injury, I will crush you, ruin your name, and salt your fields."
                       ],
                   ideals=[
                       ('Respect', "Respect is due to me because of my position, but all people regardless of station deserve to be treated with dignity.", 'good'),
                       ('Responsibility', "It is my duty to respect the authority o those aove me, just as those below me must respect mine.", 'lawful'),
                       ('Independence', "I must prove that I can handle myself without the coddling of my family.", 'chaotic'),
                       ('Power', "If I can attain more power, no one will tell me what to do.", 'evil'),
                       ('Family', "Blood runs thicker than water.", 'any'),
                       ('Noble Obligation', "It is my duty to protect and care for the people beneath me.", 'good')
                       ],
                   bonds=[
                       "I will face any challenge to win the approval of my family.",
                       "My house's alliance with another noble family must be sustained at all costs.",
                       "Nothing is more important than the ther members of my family.",
                       "I am in love with the heir of a family that my family despises.",
                       "My loyalty to my sovereign is unwavering.",
                       "The common folk must see me as a hero of the people."
                       ],
                   flaws=[
                       "I secretly believethat everyone is beneath me.",
                       "I hide a truly scandalous secret that could ruin my family forever.",
                       "I too often hear veied insults and threats in every word addressed to me, and I'm quick to anger.",
                       "I have an insatiable desire for carnal pleasures.",
                       "In fact, the world does revolve around me.",
                       "By my words and actions, I often bring shame to my family."
                       ]),
        Background(name="Outlander",
                   features=["Wanderer"],
                   speciality_name="Origin",
                   specialities=['Forester', 'Trapper', 'Homesteader', 'Guide', 'Exile or outcast', 'Bounty hunter', 'Pilgrim', 'Tribal nomad', 'Hunter-gatherer', 'Tribal marauder'],
                   skill_proficiencies=['Athletics', 'Survival'],
                   traits=[
                       "I'm driven by a wanderlust tat led me away from home.",
                       "I watch over my friends as if they were a litter of nweborn cups.",
                       "I once ra ntwenty-five miles without stopping to warn to my clan of an approaching orc horde. I'd do it again if I had to.",
                       "I have a lesson for every situation, drawn from observing nature.",
                       "I place no stock in wealthy or well-mannered folk. Money and manners won't save you from a hungry owlbear.",
                       "I'm always picking things up, absently fiddling with them, ad sometimes accidentally breaking them.",
                       "I feel far more comfortable around animals than people.",
                       "I was, in fact, raised by wolves."
                       ],
                   ideals=[
                       ('Change', "Life is like the seasons, in constant change, and we must change with it.", 'chaotic'),
                       ('Greater Good', "It is each person's responsibility to make the most hppiness for the whole tribe.", 'good'),
                       ('Honor', "If I dishonor myself, I dishonor my whole clan.", 'lawful'),
                       ('Might', "The strongest aremeant to rule.", 'evil'),
                       ('Nature', "The natural world i more important than all the constructs of civilization.", 'neutral'),
                       ('Glory', "I must earn glory in battle, for myself and my clan", 'any')
                       ],
                   bonds=[
                       "My family, clan, or tribe is the most important thing in my life, even when they are far from me.",
                       "An injury to the unspoiled wilderness of my home is an injury to me.",
                       "I will bring terrible wrath down on te evildoers who destroyed my homeland.",
                       "I am the last of my tribe, and it is up to me to ensure their names enter legend.",
                       "I suffer awful visions of a comingdisaster and will do anything to prevent it.",
                       "It is my duty to provide children to sustain my tribe."
                       ],
                   flaws=[
                       "I am too enamored of ale, wine, andother intoxicants.",
                       "There's no room for caution in a life lived to the fullest.",
                       "I remember every insult I've received and nurse a silent resentment toward anyone who's ever wronged me.",
                       "I am slow to trust members of other races, tribes, and societies.",
                       "Violence is my answer to almost any challange.",
                       "Don't expect me to save those who can't save themselves. It is nature's way that the strong thrive and the weak perish."
                       ]),
        Background(name="Sage",
                   features=["Researcher"],
                   speciality_name="Speciality",
                   specialities=['Alchemist', 'Astronomer', 'Discredited academic', 'Librarian', 'Professor', 'Researcher', "Wizard's appendice", 'Scribe'],
                   skill_proficiencies=['Arcana', 'History'],
                   traits=[
                       "I use plysyllabic words that convey theimpression of great erudition.",
                       "I've read every book in the world's greatest librarise - or I like to boast that I have.",
                       "I'm used to helping out those who aren't as smart as I am, and I patiently explain anything and everything to others.",
                       "There's nothing I like more than agood mystery",
                       "I'm willing to listen to every side of an argument before I make my own judgment.",
                       "I...speak...slowly...wen talking...to idiots,...which...almost...everyone...is...compared...to me.",
                       "I am horribly, horribly awkward in social situations.",
                       "I'm convinced that people are always trying to steal my secrets."
                       ],
                   ideals=[
                       ('Knowledge', "The path to power and self-improvement is through knowledge.", 'neutral'),
                       ('Beauty', "What is beautiful points us beyong itself toward what is true.", 'good'),
                       ('Logic', "Emotions must not cloud our logical thinking.", 'lawful'),
                       ('No Limits', "Nothing should fetter the infinite possibility inherent in all existence.", 'chaotic'),
                       ('Power', "Knowledge is the path to power and domination.", 'evil'),
                       ('Self-Improvement', "The goal of a life of study is the betterment of oneself.", 'any')
                       ],
                   bonds=[
                       "It is my duty to protect my students.",
                       "I have an ancient text that holds terrible secrets that must not fall into the wrong hands.",
                       "I work to preserve a library, university, scriptorium, or monastery.",
                       "My life's work is a series of tomes related to a specific field of lore.",
                       "I've been searching my whole life for the answer to a certain question.",
                       "I sold my sould for knowledge. I hope to do great deeds and win it back."
                       ],
                   flaws=[
                       "I am easily distracted by the promise of information.",
                       "Most people scream and run when they see a demon. I stop and take notes on its anatomy.",
                       "Unlocking an ancient mystery is worth the price of a civilization.",
                       "I overlook obvious solutionsin favor of complicated ones.",
                       "I speak without really thinking through my words, invariably insultingothers.",
                       "I can't keep a secret to save my life, or anyone else's."
                       ]),
        Background(name="Sailor",
                   features=["Ship's Passage", "Bad Reputation"],
                   speciality_name="",
                   specialities=[],
                   skill_proficiencies=['Athletics', 'Perception'],
                   traits=[
                       "My friends know they can rely on me, no matter what.",
                       "I work hard so that I can play hard when the work is done.",
                       "I ejoy sailing into new pos and making new friends over a flagon of ale.",
                       "I stretch the truth for the sake of a good story.",
                       "To me, a tavern brawl is a nice way to get to know a new city.",
                       "I never pass up a friendly wager.",
                       "My language is as foul as an otyugh nest.",
                       "I like a job wel done, especially if I can convince someone else to do it."
                       ],
                   ideals=[
                       ('Respect', "The thing that keeps a ship together is mutual respect between captain and crew.", 'good'),
                       ('Fairness', "We all do the work, so we all share in the rewards.", 'lawful'),
                       ('Freedom', "The sea is freedom - the freedom to go anywhere and do anything.", 'chaotic'),
                       ('Mastery', "I'm a predator, ad the other ships on the sea are my prey.", 'evil'),
                       ('People', "I'm committed to my crewmates, not to ideals.", 'neutral'),
                       ('Aspiration', "Someday I'll own my own ship nd chart my own destiny.", 'any')
                       ],
                   bonds=[
                       "I'm loyal to my captain first, everything else second.",
                       "The ship is most important - crewmates and captains come and go.",
                       "I'll always remember my first ship.",
                       "In a harbor town, I have a paramour whose eyes nearly stole me from the sea.",
                       "I was cheated out of my fair share of profits, and I want to get my due.",
                       "Ruthless pirates murdered my captain and crewmates, plundered our ship, and left me to die. Vengeance will be mine."
                       ],
                   flaws=[
                       "I follow orders, even if I think they're wrong.",
                       "I'll say anything to avoid having to do extra work.",
                       "Onecesomeone questions my courage, I never back down no mattter how dangerous the situation.",
                       "Once I start drinking, it's hard for me to stop.",
                       "I can't help but pocket loose coins and other trinkets I come accross.",
                       "My pride will probably lead to mt destruction."
                       ]),
        Background(name="Soldier",
                   features=["Military Rank"],
                   speciality_name="Speciality",
                   specialities=['Officer', 'Scout', 'Infantry', 'Cavalry', 'Healer', 'Quartermaster', 'Standard bearer', 'Support staff (cook, blacksmith, or the like)'],
                   skill_proficiencies=['Athletics', 'Intimidation'],
                   traits=[
                       "I'm always polite and respectful.",
                       "I'm haunted by memories of war. I can't get the images of violence out of my mind.",
                       "I've lost too many friends, and I'm slow to make new ones.",
                       "I'm full of inspiring and cautionary tales from my military experience relevant to almost every combat situation.",
                       "I can stare down a hell hound without flinching.",
                       "I enjoy being strong and like breaking things.",
                       "I have a crude sense of humor.",
                       "I face problems head-on. A simple, direct solution is the best path to success."
                       ],
                   ideals=[
                       ('Greater Good', "Our lot is to lay down our lives in defense o others.", 'good'),
                       ('Responsibility', "I do what I must and obey just authority.", 'lawful'),
                       ('Independence', "When people follow orders blindly, they embrace a kind of tyranny.", 'chaotic'),
                       ('Might', "In life as in war, the stronger force wins.", 'evil'),
                       ('Live and Let Live', "Ideals aren't worth killing over or going to war for.", 'neutral'),
                       ('Nation', "My city, nation, or people are all that matter.", 'any')
                       ],
                   bonds=[
                       "I would still lay down my lifefor the peopleI serve with.",
                       "Someone saved my life on the battlefield. To thisday, I will never leave a friend behind.",
                       "My honor is my life.",
                       "I'll never forget the crushing defeat my company suffered or the enemis who dealt it.",
                       "Those who fight beside me are those worth dying for.",
                       "I fight for those who cannot fight for themselves."
                       ],
                   flaws=[
                       "The monstrous enemy we faced in battle till leaves me quivering with fear.",
                       "I have little respect for anyone who is not a proven warrior.",
                       "I made a terrible mistake in battle that cost many lives, and I would do anything to keep that mistake secret.",
                       "My hatred of my enemies is blind and unreasoning.",
                       "I obry the law, even if the law causes misery.",
                       "I'd rather eat my armor than admit wen I'm wrong."
                       ]),
        Background(name="Urchin",
                   features=["City Secrets"],
                   speciality_name="",
                   specialities=[],
                   skill_proficiencies=['Sleight of Hand', 'Stealth'],
                   traits=[
                       "I hide scraps of food and trinkets away in my pockets.",
                       "I ask a lot of questions.",
                       "I like to squeeze into small places where no one else can get to me.",
                       "I sleep with my back to a wall or tree, with everything I own wrappe in a bundle in my arms.",
                       "I eat like a pig and have bad manners.",
                       "I think anyone who's nice to me is hiding evil intent.",
                       "I don't like to bathe.",
                       "I bluntly say what other people are hinting at or hiding."
                       ],
                   ideals=[
                       ('Respect', "All people, rich or poor, deserve respect.", 'good'),
                       ('Community', "We have to take care of each other, because no one else is going to do it.", 'lawful'),
                       ('Change', "The low are lifted up, and the high and mighty are brought down. Change isthe nature of things.", 'chaotic'),
                       ('Retributions', "The ich need to be shown what life and death are like in the gutters.", 'evil'),
                       ('People', "I help the people who help me - that's what keeps us alive.", 'neutral'),
                       ('Aspiration', "I'm going to pove that I'm worthy of abtter ilfe.", 'any')
                       ],
                   bonds=[
                       "My town or city is my home, and I'll fight to defend it.",
                       "I sponsor an orphanage to keep others from enduring what I was forced to endure.",
                       "I owe my survival to another urchin who taught me to live on the streets.",
                       "I owe a debt I can never repay to the person who took pity on me.",
                       "I escaped my life of poverty by robbing an important person, and I'm wanted for it.",
                       "No one else should have to endure the hardships I've been through."
                       ],
                   flaws=[
                       "Ifi I'm outnumbered, I will run away from a fight.",
                       "Gold seems like a lot of money to me, and I'll dojust about anything for more of it.",
                       "I will never fully trust anyone other than myself.",
                       "I'd rather kill someone in their sleep than fight fair.",
                       "It's not stealing if I need it more than someone else.",
                       "People who can't take care of themselves get what they deserve."
                       ]),
        ]


class Race:
    def __init__(self, name, age, size, speed, languages, additional_languages, armor_proficiencies, weapon_proficiencies, tool_proficiencies, skill_proficiencies, additional_proficiencies, traits, ability_modifiers, additional_spells, spells):
        self.name = name
        self.age = age
        self.size = size
        self.speed = speed
        self.armor_proficiencies = armor_proficiencies
        self.weapon_proficiencies = weapon_proficiencies
        self.tool_proficiencies = tool_proficiencies
        self.skill_proficiencies = skill_proficiencies
        self.additional_proficiencies = additional_proficiencies
        self.traits = traits
        self.languages = languages
        self.additional_languages = additional_languages
        self.ability_modifiers = ability_modifiers
        self.additional_spells = additional_spells
        self.spells = spells


races = [
        Race(name="Hill Dwarf", age=50, size="Medium", speed=25,
             languages=['Common', 'Dwarvish'],
             additional_languages=0,
             armor_proficiencies=[],
             weapon_proficiencies=['Battle axe', 'Hand axe', 'Light hammer', 'Warhammer'],
             tool_proficiencies=["Smith's tool, brewer's supplies or manson's tools"],
             skill_proficiencies=[],
             additional_proficiencies=0,
             traits=['Darkvision', 'Dwarven Resilience', 'Dwarven Combat Training', 'Stonecutting', 'Dwarven Toughness'],
             additional_spells={0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
             spells={0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []},
             ability_modifiers={
                'str': 0, 'dex': 0, 'con': 2, 'int': 0, 'wis': 1, 'cha': 0}),
        Race(name="Mountain Dwarf", age=50, size="Medium", speed=25,
             languages=['Common', 'Dwarvish'],
             additional_languages=0,
             armor_proficiencies=['Light armor', 'Medium armor'],
             weapon_proficiencies=['Battle axe', 'Hand axe', 'Light hammer', 'Warhammer'],
             tool_proficiencies=["Smith's tool, brewer's supplies or manson's tools"],
             skill_proficiencies=['Perception'],
             additional_proficiencies=0,
             traits=['Darkvision', 'Dwarven Resilience', 'Dwarven Combat Training', 'Stonecutting', 'Dwarven Armor Training'],
             additional_spells={0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
             spells={0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []},
             ability_modifiers={
                'str': 2, 'dex': 0, 'con': 2, 'int': 0, 'wis': 0, 'cha': 0}),
        Race(name="High Elf", age=100, size="Medium", speed=30,
             languages=['Common', 'Elvish'],
             additional_languages=1,
             armor_proficiencies=[],
             weapon_proficiencies=['Long sword', 'Short sword', 'Shortbow', 'Longbow'],
             tool_proficiencies=[],
             skill_proficiencies=['Perception'],
             additional_proficiencies=0,
             traits=['Darkvision', 'Keen Senses', 'Fey Ancestry', 'Trance', 'Elf Weapon Training', 'Cantrip'],
             additional_spells={0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
             spells={0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []},
             ability_modifiers={
                'str': 0, 'dex': 2, 'con': 0, 'int': 1, 'wis': 0, 'cha': 0}),
        Race(name="Wood Elf", age=100, size="Medium", speed=35,
             languages=['Common', 'Elvish'],
             additional_languages=0,
             armor_proficiencies=[],
             weapon_proficiencies=['Long sword', 'Short sword', 'Shortbow', 'Longbow'],
             tool_proficiencies=[],
             skill_proficiencies=['Perception'],
             additional_proficiencies=0,
             traits=['Darkvision', 'Keen Senses', 'Fey Ancestry', 'Trance', 'Elf Weapon Training', 'Fleet of Foot', 'Mark of the Wild'],
             additional_spells={0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
             spells={0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []},
             ability_modifiers={
                'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 1, 'cha': 0}),
        Race(name="Drow", age=100, size="Medium", speed=30,
             languages=['Common', 'Elvish'],
             additional_languages=0,
             armor_proficiencies=[],
             weapon_proficiencies=['Rapiers', 'Shortswords', 'Hand crossbows'],
             tool_proficiencies=[],
             skill_proficiencies=['Perception'],
             additional_proficiencies=0,
             traits=['Superior Darkvision', 'Keen Senses', 'Fey Ancestry', 'Trance', 'Sunlight Sensitivity', 'Drow Magic', 'Drow Weapon Training'],
             additional_spells={0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
             spells={0: ['Dancing Light'], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []},
             ability_modifiers={
                'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'cha': 1}),
        Race(name="Lightfoot Halfling", age=20, size="Small", speed=25,
             languages=['Common', 'Halfling'],
             additional_languages=0,
             armor_proficiencies=[],
             weapon_proficiencies=[],
             tool_proficiencies=[],
             skill_proficiencies=[],
             additional_proficiencies=0,
             traits=['Lucky', 'Brave', 'Halfling Nimbleness', 'Naturally Stealthy'],
             additional_spells={0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
             spells={0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []},
             ability_modifiers={
                'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'cha': 1}),
        Race(name="Stout Halfling", age=20, size="Small", speed=25,
             languages=['Common', 'Halfling'],
             additional_languages=0,
             armor_proficiencies=[],
             weapon_proficiencies=[],
             tool_proficiencies=[],
             skill_proficiencies=[],
             additional_proficiencies=0,
             traits=['Lucky', 'Brave', 'Halfling Nimbleness', 'Stout Resilience'],
             additional_spells={0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
             spells={0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []},
             ability_modifiers={
                'str': 0, 'dex': 2, 'con': 1, 'int': 0, 'wis': 0, 'cha': 0}),
        Race(name="Human", age=18, size="Medium", speed=30,
             languages=['Common'],
             additional_languages=1,
             armor_proficiencies=[],
             weapon_proficiencies=[],
             tool_proficiencies=[],
             skill_proficiencies=[],
             additional_proficiencies=0,
             traits=[],
             additional_spells={0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
             spells={0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []},
             ability_modifiers={
                'str': 1, 'dex': 1, 'con': 1, 'int': 1, 'wis': 1, 'cha': 1}),
        Race(name="Dragonborn", age=15, size="Medium", speed=30,
             languages=['Common', 'Draconic'],
             additional_languages=0,
             armor_proficiencies=[],
             weapon_proficiencies=[],
             tool_proficiencies=[],
             skill_proficiencies=[],
             additional_proficiencies=0,
             traits=['Damage Resitance', 'Breath Weapon', 'Draconic Ancestry'],
             additional_spells={0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
             spells={0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []},
             ability_modifiers={
                'str': 2, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 1}),
        Race(name="Forest Gnome", age=40, size="Small", speed=25,
             languages=['Common', 'Gnomish'],
             additional_languages=0,
             armor_proficiencies=[],
             weapon_proficiencies=[],
             tool_proficiencies=[],
             skill_proficiencies=[],
             additional_proficiencies=0,
             traits=['Darkvision', 'Gnome Cunning', 'Natural Illusionist', 'Speak with Small Beasts'],
             additional_spells={0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
             spells={0: ['Minor Illusion'], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []},
             ability_modifiers={
                'str': 0, 'dex': 1, 'con': 0, 'int': 2, 'wis': 0, 'cha': 0}),
        Race(name="Rock Gnome", age=40, size="Small", speed=25,
             languages=['Common', 'Gnomish'],
             additional_languages=0,
             armor_proficiencies=[],
             weapon_proficiencies=[],
             tool_proficiencies=[],
             skill_proficiencies=[],
             additional_proficiencies=0,
             traits=['Darkvision', 'Gnome Cunning', "Artificer's Lore", "Tinker"],
             additional_spells={0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
             spells={0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []},
             ability_modifiers={
                'str': 0, 'dex': 0, 'con': 1, 'int': 2, 'wis': 0, 'cha': 0}),
        Race(name="Half-Elf", age=20, size="Medium", speed=30,
             languages=['Common', 'Elvish'],
             additional_languages=1,
             armor_proficiencies=[],
             weapon_proficiencies=[],
             tool_proficiencies=[],
             skill_proficiencies=[],
             additional_proficiencies=2,
             traits=['Dark Vision', 'Fey Ancestry', 'Skill Versatility'],
             additional_spells={0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
             spells={0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []},
             ability_modifiers={
                'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 2}),
        Race(name="Half-Orc", age=14, size="Medium", speed=30,
             languages=['Common', 'Orc'],
             additional_languages=0,
             armor_proficiencies=[],
             weapon_proficiencies=[],
             tool_proficiencies=[],
             skill_proficiencies=['Intimidation'],
             additional_proficiencies=0,
             traits=['Darkvision', 'Menacing', 'Relentless Endurance', 'Savage Attacks'],
             additional_spells={0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
             spells={0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []},
             ability_modifiers={
                'str': 2, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'cha': 0}),
        Race(name="Tiefling", age=18, size="Medium", speed=30,
             languages=['Common', 'Infernal'],
             additional_languages=0,
             armor_proficiencies=[],
             weapon_proficiencies=[],
             tool_proficiencies=[],
             skill_proficiencies=[],
             additional_proficiencies=0,
             traits=['Darkvision', 'Hellish Resistance', 'Infernal Legacy'],
             additional_spells={0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
             spells={0: ['Thaumaturgy'], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []},
             ability_modifiers={
                'str': 0, 'dex': 0, 'con': 0, 'int': 2, 'wis': 0, 'cha': 1})
        ]


class Class:
    def __init__(self, name, hit_die, save_proficiencies, armor_proficiencies,
                 weapon_proficiencies, tool_proficiencies, skill_proficiencies,
                 skill_options, primary_abilities):
        self.name = name
        self.hit_die = hit_die
        self.save_proficiencies = save_proficiencies
        self.armor_proficiencies = armor_proficiencies
        self.weapon_proficiencies = weapon_proficiencies
        self.tool_proficiencies = tool_proficiencies
        self.skill_proficiencies = skill_proficiencies
        self.skill_options = skill_options
        self.primary_abilities = primary_abilities


classes = [
        Class(name="Barbarian",
              hit_die=12, save_proficiencies=['str', 'con'],
              armor_proficiencies=['Light armor', 'Medium armor', 'Shields'],
              weapon_proficiencies=['Simple weapons', 'Martial weapons'],
              tool_proficiencies=[],
              skill_proficiencies=2,
              skill_options=['Animal Handling', 'Athletics', 'Intimidation', 'Nature', 'Perception', 'Survival'],
              primary_abilities=['str', 'con']),
        Class(name="Bard",
              hit_die=8, save_proficiencies=['dex', 'cha'],
              armor_proficiencies=['Light armor'],
              weapon_proficiencies=['Simple weapons', 'Hand crossbows', 'Longswords', 'Rapiers', 'Shortswords'],
              tool_proficiencies=['Three musical instruments'],
              skill_proficiencies=3,
              skill_options=list(skill_ability_map.keys()),
              primary_abilities=['cha', 'dex']),
        Class(name="Cleric",
              hit_die=8, save_proficiencies=['wis', 'cha'],
              armor_proficiencies=['Light armor', 'Medium armor', 'Shields'],
              weapon_proficiencies=['Simple weapons'],
              tool_proficiencies=[],
              skill_proficiencies=2,
              skill_options=['History', 'Insight', 'Medicine', 'Persuasion', 'Religion'],
              primary_abilities=['wis', ['str', 'con']]),
        Class(name="Druid",
              hit_die=8, save_proficiencies=[['int'], ['wis']],
              armor_proficiencies=['Light non metal armor', 'Medium non metal armor', 'Non metal shields'],
              weapon_proficiencies=['Clubs', 'Daggers', 'Darts', 'Maces', 'Quarterstaffs', 'Scimitars', 'Sickles', 'Slings', 'Spears'],
              tool_proficiencies=['Herbalism Kit'],
              skill_proficiencies=2,
              skill_options=['Arcana', 'Animal Handling', 'Insight', 'Medicine', 'Nature', 'Perception', 'Religion', 'Survival'],
              primary_abilities=['wis', 'con']),
        Class(name="Fighter",
              hit_die=10, save_proficiencies=['str', 'con'],
              armor_proficiencies=['All armor', 'Shields'],
              weapon_proficiencies=['Simple weapons', 'Martial weapons'],
              tool_proficiencies=[],
              skill_proficiencies=2,
              skill_options=['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight', 'Intimidation', 'Perception', 'Survival'],
              primary_abilities=[['str', 'dex'], ['con', 'int']]),
        Class(name="Monk",
              hit_die=8, save_proficiencies=['str', 'dex'],
              armor_proficiencies=[],
              weapon_proficiencies=['Simple weapons', 'Shortswords'],
              tool_proficiencies=['An artisan tool or a musical instrument'],
              skill_proficiencies=2,
              skill_options=['Acrobatics', 'Athletics', 'History', 'Insight', 'Religion', 'Stealth'],
              primary_abilities=['dex', 'wis']),
        Class(name="Paladin",
              hit_die=10, save_proficiencies=['wis', 'cha'],
              armor_proficiencies=['All armor', 'Shields'],
              weapon_proficiencies=['Simple weapons', 'Martial weapons'],
              tool_proficiencies=[],
              skill_proficiencies=2,
              skill_options=['Athletics', 'Insight', 'Intimidation', 'Medicine', 'Persuasion', 'Religion'],
              primary_abilities=['str', 'cha']),
        Class(name="Ranger",
              hit_die=10, save_proficiencies=['str', 'dex'],
              armor_proficiencies=['Light armor', 'Medium armor', 'Shields'],
              weapon_proficiencies=['Simple weapons', 'Martial weapons'],
              tool_proficiencies=[],
              skill_proficiencies=2,
              skill_options=['Animal Handling', 'Athletics', 'Insight', 'Investigation', 'Nature', 'Perception', 'Stealth', 'Survival'],
              primary_abilities=[['str', 'dex'], 'wis']),
        Class(name="Rogue",
              hit_die=8, save_proficiencies=['dex', 'int'],
              armor_proficiencies=['Light armor'],
              weapon_proficiencies=['Simple weapons', 'Hand crossbow', 'Longswords', 'Rapiers', 'Shortswords'],
              tool_proficiencies=["Thieve's tools"],
              skill_proficiencies=4,
              skill_options=['Acrobatics', 'Athletics', 'Deception', 'Insight', 'Intimidation', 'Investigation', 'Perception', 'Performance', 'Persuasion', 'Sleight of Hand', 'Stealth'],
              primary_abilities=['dex', ['int', 'cha']]),
        Class(name="Sorcerer",
              hit_die=6, save_proficiencies=['con', 'cha'],
              armor_proficiencies=[],
              weapon_proficiencies=['Daggers', 'Darts', 'Slings', 'Quarterstaffs', 'Light crossbows'],
              tool_proficiencies=[],
              skill_proficiencies=2,
              skill_options=['Arcana', 'Deception', 'Insight', 'Intimidation', 'Persuasion', 'Religion'],
              primary_abilities=['cha', 'con']),
        Class(name="Warlock",
              hit_die=8, save_proficiencies=['wis', 'cha'],
              armor_proficiencies=['Light armor'],
              weapon_proficiencies=['Simple weapons'],
              tool_proficiencies=[],
              skill_proficiencies=2,
              skill_options=['Arcana', 'Deception', 'History', 'Intimidation', 'Investigation', 'Nature', 'Religion'],
              primary_abilities=['cha', 'con']),
        Class(name="Wizard",
              hit_die=6, save_proficiencies=['int', 'wis'],
              armor_proficiencies=[],
              weapon_proficiencies=['Daggers', 'Darts', 'Slings', 'Quarterstaffs', 'Light crossbows'],
              tool_proficiencies=[],
              skill_proficiencies=2,
              skill_options=['Arcana', 'History', 'Insight', 'Investigation', 'Medicine', 'Religion'],
              primary_abilities=['int', ['con', 'dex']])
        ]


class Character:
    def __init__(self):
        pass

    def generate_random_character(self):
        self.ancestry = ''
        self.features = []

        self.skill_proficiencies = []
        self.armor_proficiencies = []
        self.weapon_proficiencies = []
        self.tool_proficiencies = []

        # roll ability scores.

        self.ability = {}
        self.ability_rolls = {}

        self.ability['str'], self.ability_rolls['str'] = roll_attribute()
        self.ability['dex'], self.ability_rolls['dex'] = roll_attribute()
        self.ability['con'], self.ability_rolls['con'] = roll_attribute()
        self.ability['int'], self.ability_rolls['int'] = roll_attribute()
        self.ability['wis'], self.ability_rolls['wis'] = roll_attribute()
        self.ability['cha'], self.ability_rolls['cha'] = roll_attribute()

        # choose a race.

        if chosen['race'] in [race.name for race in races]:
            self.race = [race for race in races if race.name == chosen['race']][0]
        else:
            self.race = roll_from_list(races)
        self.size = self.race.size
        self.speed = self.race.speed

        self.ability['str'] += self.race.ability_modifiers['str']
        self.ability['dex'] += self.race.ability_modifiers['dex']
        self.ability['con'] += self.race.ability_modifiers['con']
        self.ability['int'] += self.race.ability_modifiers['int']
        self.ability['wis'] += self.race.ability_modifiers['wis']
        self.ability['cha'] += self.race.ability_modifiers['cha']

        self.languages = self.race.languages.copy()
        self.race_traits = self.race.traits.copy()

        for ability in self.ability:
            if self.ability[ability] > 20:
                self.ability[ability] = 20

        if self.race.name == 'Half-Elf':
            chosen_abilities = random.sample(['str', 'dex', 'con', 'int', 'wis'], 2)
            self.ability[chosen_abilities[0]] += 1
            self.ability[chosen_abilities[1]] += 1

        elif self.race.name == "Dragonborn":
            self.ancestry = roll_from_list(['Black', 'Blue', 'Brass', 'Bronze', 'Copper',
                                            'Gold', 'Green', 'Red', 'Silver', 'White'])

        # choose a class based on primary abilities.

        def rate_class(cls, abilities):
            if chosen['random_class']:
                return 1
            else:
                rate = []
                for elm in cls.primary_abilities:
                    if type(elm) is str:
                        rate.append(abilities[elm])
                    elif type(elm) is list:
                        rate.append(max([abilities[abl] for abl in elm]))

                rval = rate[0] + modifier(rate[1])

                return rval

        rated_classes = {}
        for cls in classes:
            rated_classes[cls.name] = rate_class(cls, self.ability)

        candidate_classes = [classes[0]]
        highest_rate = rated_classes[classes[0].name]
        for cls in classes[1:]:
            if rated_classes[cls.name] > highest_rate:
                highest_rate = rated_classes[cls.name]
                candidate_classes = [cls]
            elif rated_classes[cls.name] == highest_rate:
                candidate_classes.append(cls)

        self.character_class = roll_from_list(candidate_classes)
        self.proficiency_bonus = 2

        # choose a background, traits, an ideal, a bond and a flaw.

        if chosen['background'] in [bg.name for bg in backgrounds]:
            self.background = [bg for bg in backgrounds if bg.name == chosen['background']][0]
        else:
            self.background = roll_from_list(backgrounds)
        self.traits = random.sample(self.background.traits, 2)
        self.ideal = roll_from_list(self.background.ideals)
        self.bond = roll_from_list(self.background.bonds)
        self.flaw = roll_from_list(self.background.flaws)

        self.features.append(roll_from_list(self.background.features))
        self.speciality_name = self.background.speciality_name
        self.speciality = roll_from_list(self.background.specialities)

        # choose an alignment based on the ideal.

        self.order = roll_from_list(['lawful', 'neutral', 'chaotic'])
        self.moral = roll_from_list(['good', 'neutral', 'evil'])

        if self.ideal[2] in ['lawful', 'chaotic']:
            self.order = self.ideal[2]
        elif self.ideal[2] in ['good', 'evil']:
            self.moral = self.ideal[2]
        elif self.ideal[2] == 'neutral':
            if roll(2) == 1:
                self.order = self.ideal[2]
            else:
                self.moral = self.ideal[2]

        # race proficiencies

        self.skill_proficiencies.extend(self.race.skill_proficiencies)
        self.weapon_proficiencies.extend(self.race.weapon_proficiencies)
        self.armor_proficiencies.extend(self.race.armor_proficiencies)
        self.tool_proficiencies.extend(self.race.tool_proficiencies)

        # choose proficiencies according to the best ability scores.

        self.skill_proficiencies.extend(self.background.skill_proficiencies)

        candidate_skills = list(set(self.character_class.skill_options) - set(self.skill_proficiencies))

        def pick_best_skills(candidate_skills, number):
            rate_skills_map = {}
            for skill in candidate_skills:
                rate = self.ability[skill_ability_map[skill]]
                if rate not in rate_skills_map:
                    rate_skills_map[rate] = []
                rate_skills_map[rate].append(skill)

            ordered_rate_skills_pairs = sorted(
                    rate_skills_map.items(), key=lambda kv: kv[0], reverse=True)

            taken_skills = []
            skills_remaining = number
            for pair in ordered_rate_skills_pairs:
                rate = pair[0]
                skills = pair[1]
                to_take = skills_remaining if skills_remaining <= len(skills) else len(skills)
                skills_remaining -= to_take
                taken_skills.extend(random.sample(skills, to_take))
            return taken_skills

        self.skill_proficiencies.extend(pick_best_skills(candidate_skills, self.character_class.skill_proficiencies))

        # aditional race skill proficiencies.
        candidate_skills = list(set(skill_ability_map.keys()) - set(self.skill_proficiencies))
        self.skill_proficiencies.extend(pick_best_skills(candidate_skills, self.race.additional_proficiencies))

        # other proficiencies.

        self.armor_proficiencies.extend(self.character_class.armor_proficiencies)
        self.weapon_proficiencies.extend(self.character_class.weapon_proficiencies)
        self.tool_proficiencies.extend(self.character_class.tool_proficiencies)

        # hit points
        self.hit_points = self.character_class.hit_die + modifier(self.ability['con'])
        if "Dwarven Toughness" in self.race_traits:
            self.hit_points += 1

    def print_sheet(self):
        # print everything.

        print('Character:')
        print('Race: ' + self.race.name)
        if self.ancestry != '':
            print('Ancestry: ' + self.ancestry + ' Dragon')
        print('Class: ' + self.character_class.name)
        print('Alignment: ' + ((self.order + ' ' + self.moral) if self.order != self.moral else self.order))
        print('Hit Points: %d' % (self.hit_points))
        print('Speed: %d' % self.speed)
        print('Size: ' + self.size)
        print('Saving Throw Proficiencies: %s' % self.character_class.save_proficiencies)
        print('')
        print('Abilities: ')
        print('STR: %d (%d) rolls: %s' % (
            self.ability['str'], modifier(self.ability['str']), str(self.ability_rolls['str'])))
        print('DEX: %d (%d) rolls: %s' % (
            self.ability['dex'], modifier(self.ability['dex']), str(self.ability_rolls['dex'])))
        print('CON: %d (%d) rolls: %s' % (
            self.ability['con'], modifier(self.ability['con']), str(self.ability_rolls['con'])))
        print('INT: %d (%d) rolls: %s' % (
            self.ability['int'], modifier(self.ability['int']), str(self.ability_rolls['int'])))
        print('WIS: %d (%d) rolls: %s' % (
            self.ability['wis'], modifier(self.ability['wis']), str(self.ability_rolls['wis'])))
        print('CHA: %d (%d) rolls: %s' % (
            self.ability['cha'], modifier(self.ability['cha']), str(self.ability_rolls['cha'])))
        print('')
        print('Background: ' + self.background.name)
        if self.speciality is not None:
            print('%s: %s' % (self.speciality_name, self.speciality))
        print('Traits:')
        print('- ' + self.traits[0])
        print('- ' + self.traits[1])
        print('Ideal:')
        print('- %s. %s (%s)' % (self.ideal[0], self.ideal[1], self.ideal[2]))
        print('Bond:')
        print('- ' + self.bond)
        print('Flaw:')
        print('- ' + self.flaw)
        print('')
        print('Proficiency bonus: %d' % self.proficiency_bonus)
        print('')
        print('Languages:')
        for language in self.languages:
            print('- ' + language)
        print('')
        print('Features:')
        for feature in self.features:
            print('- ' + feature)
        print('')
        print('Skill Proficiencies:')
        for proficiency in self.skill_proficiencies:
            print('- %s (%s) (%d)' % (
                proficiency, skill_ability_map[proficiency],
                (self.proficiency_bonus + modifier(self.ability[skill_ability_map[proficiency]]))))
        print('')
        print('Armor Proficiencies: ' + str(self.armor_proficiencies))
        print('Weapon Proficiencies: ' + str(self.weapon_proficiencies))
        print('Tool Proficiencies: ' + str(self.tool_proficiencies))
        print('')
        print('Race Traits:')
        for trait in self.race_traits:
            print('- ' + trait)


if chosen['statistics'] > 0:
    class_count_map = {cls.name: 0 for cls in classes}
    race_count_map = {race.name: 0 for race in races}
    ability_data_map = {abl: [] for abl in ['str', 'dex', 'con', 'int', 'wis', 'cha']}

    total = chosen['statistics']
    for i in range(total):
        if chosen['class'] in [cls.name for cls in classes]:
            while True:
                c = Character()
                c.generate_random_character()
                if c.character_class.name == chosen['class']:
                    break
        else:
            c = Character()
            c.generate_random_character()

        class_count_map[c.character_class.name] += 1
        race_count_map[c.race.name] += 1
        for abl in c.ability:
            ability_data_map[abl].append(c.ability[abl])

    print('')
    print('Classes:')
    for cls in class_count_map:
        print('- %-20s %-6d (%f)' % (cls + ':', class_count_map[cls], (class_count_map[cls] / total)))
    print('')
    print(' %-20s %f' % ('Mean:', statistics.mean(class_count_map.values())))
    print(' %-20s %f' % ('Median:', statistics.median(class_count_map.values())))
    print(' %-20s %f' % ('Standard Deviation:', statistics.stdev(class_count_map.values())))

    print('')
    print('Races:')
    for race in race_count_map:
        print('- %-20s %-6d (%f)' % (race + ':', race_count_map[race], (race_count_map[race] / total)))
    print('')
    print(' %-20s %f' % ('Mean:', statistics.mean(race_count_map.values())))
    print(' %-20s %f' % ('Median:', statistics.median(race_count_map.values())))
    print(' %-20s %f' % ('Standard Deviation:', statistics.stdev(race_count_map.values())))
    print('')
    print('Abilities:')
    for abl in ability_data_map:
        print('%s:' % abl)
        print('  %-20s %f' % ('Mean:', statistics.mean(ability_data_map[abl])))
        print('  %-20s %f' % ('Median:', statistics.median(ability_data_map[abl])))
        print('  %-20s %f' % ('Standard Deviation:', statistics.stdev(ability_data_map[abl])))

else:
    if chosen['class'] in [cls.name for cls in classes]:
        while True:
            c = Character()
            c.generate_random_character()
            if c.character_class.name == chosen['class']:
                c.print_sheet()
                break

    else:
        c = Character()
        c.generate_random_character()
        c.print_sheet()
