
from parsimonious.grammar import Grammar, NodeVisitor
import random

_grammar = Grammar(
        """
        expr            = dice (operator number)?
        operator        = "+" / "-" / "*"
        dice            = number? "d" number
        number          = ~"[0-9]+"
        """
        )


class Dice(NodeVisitor):
    """
    Dice class receives a dice expression in the traditional form, like 3d4+1,
    for example.  Only one set of dice and only one modifier, either positive
    or negative are allowed, no space between them.

    For example, 2d20+10, d4, d6-1 and 3d6 are permitted, but 2d4+2d6 and
    2d6+3+4 are not.

    After instantializing the Dice class, get the result by calling the roll
    method, which will return the result.  After that you can get a list of the
    values rolled for each die in the attribute rolls.

    Usage example:
    dice = Dice("3d6+1")
    result = dice.roll()    # can return 11
    rolls = dice.rolls      # can return [3, 4, 3]
    """
    def __init__(self, dice=''):
        if dice == '':
            dice = "d1-1"
        self._tree = _grammar.parse(dice)
        self.rolls = []

    def roll(self):
        result = self.visit(self._tree)
        return result

    def visit_expr(self, node, children):
        result = children[0]
        if type(children[1]) is list:
            operation = children[1][0]
            operator = operation[0][0].text
            rval = operation[1]

            if operator == "+":
                result = result + rval
            elif operator == "-":
                result = result - rval
            elif operator == "*":
                result = result * rval

        return result

    def visit_dice(self, node, children):
        quantity = 1
        if type(children[0]) is list:
            quantity = int(children[0][0])
        sides = children[2]
        self.rolls = [random.randint(1, sides) for x in range(quantity)]
        result = sum(self.rolls)
        return result

    def visit_number(self, node, children):
        return int(node.text)

    def generic_visit(self, node, children):
        return children or node


def roll(die):
    """ Row a die sided die. """
    return random.randint(1, die)


def roll_from_list(lst):
    """ Chose randomly an element of a given list. """
    if lst == []:
        return None
    return lst[roll(len(lst)) - 1]
