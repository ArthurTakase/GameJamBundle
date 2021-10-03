import ingredients
from pygame.locals import *

def translateToIngredient(key):
    """
        Translate a key to a int
    """
    try:
        res=int(key.unicode)
        if res < ingredients.INGREDIENTS_AVAILABLE:
            return res
        else:
            return ingredients.UNKNOW_INGREDIENT
    except:
        return ingredients.UNKNOW_INGREDIENT
