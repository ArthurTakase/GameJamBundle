import random

# List of ingredients as "constants"
BREAD_TOP=0
BREAD_BOTTOM=1
CHEESE=2
SALAD=3
STEAK=4
TOMATO=5
UNKNOW_INGREDIENT=-1
INGREDIENTS_AVAILABLE=6

def getNew():
    """
        Return a random ingredient
    """
    return random.randrange(2, INGREDIENTS_AVAILABLE)

def getName(ingredient):
    """
        Return the name of the ingredient
    """
    if ingredient == BREAD_TOP:
        return "Le pain au dessus"
    elif ingredient == BREAD_BOTTOM:
        return "Le pain au dessous"
    elif ingredient == CHEESE:
        return "Du fromage"
    elif ingredient == SALAD:
        return "De la salade"
    elif ingredient == STEAK:
        return "De la viande"
    elif ingredient == TOMATO:
        return "De la tomate"
    else:
        return "Ingrédient inconnu"

def getImage(ingredient, fish):
    """
        Return the image of the ingredient
    """
    folder="image/"
    if ingredient == BREAD_TOP:
        file="top.png"
    elif ingredient == BREAD_BOTTOM:
        file="bottom.png"
    elif ingredient == CHEESE:
        file="fromage.png"
    elif ingredient == SALAD:
        file="salade.png"
    elif ingredient == STEAK:
        if fish == "1" :
            file="saumon.png"
        else :
            file="viande.png"
    elif ingredient == TOMATO:
        file="tomate.png"
    else:
        file="jeizofjreiojfk.png"
    return folder + file
