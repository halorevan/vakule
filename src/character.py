"""Character's classes and functions.

Characters are all that really exist within vakule that do things.  No special
treatment is necessarily given to the player or non-players.
"""

class Character:
    """A character which does things, usually by manipulation.
    """
    health = -1


class CharacterIntelligent(Character):
    """A character which is intelligent.

    An intelligent character can have a language and use skills.
    """
    pass


def overworldTravel(overworld, character, where):
    """Requests to selected overworld where a character may travel.

    Parameters:

        overworld: overworld.Overworld to travel on.

        character: Character to travel.

        where: overworld.Destination to travel to.
    """
    pass


