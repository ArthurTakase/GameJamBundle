import ingredients

def getNew(size = 5):
    """
        Generate a new request
    """
    request = [ingredients.BREAD_TOP, ingredients.BREAD_BOTTOM]
    for i in range(size - 2):
        request.insert(1, ingredients.getNew());
    return request

def isFinished(sandwich):
    """
        Checks if a sandwich is finished
    """
    longeur = len(sandwich)
    return longeur != 0 and sandwich[len(sandwich) - 1] == ingredients.BREAD_BOTTOM

def isCorrect(request, sandwich):
    """
        Check if the sandwich has been correctly hade
    """
    if len(sandwich) != len(request):
        return False
    i = 0
    while i < len(request):
        if request[i] != sandwich[i]:
            return False
        i += 1
    return True
