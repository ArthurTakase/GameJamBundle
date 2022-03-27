let game = new Wordle()
game.init()

document.addEventListener('keydown', function(event) {
    var key = event.key

    if (97 <= key.charCodeAt() && key.charCodeAt() <= 122 && game.currentCase < 5 && !game.win) {
        game.setCase(key)
        game.currentWord.push(key)
        game.currentCase += 1
        game.display()
    }
    if (key == "Enter" && game.currentCase == 5 && game.currentLine < 6) {
        if (dictionnaire.indexOf(game.currentWord.join("")) < 0) { return }
        game.check()
        game.currentLine += 1
        game.currentCase = 0
        game.currentWord = []
        game.display()
    }
    if (key == "Backspace" && game.currentCase > 0) {
        game.currentCase -= 1
        game.setCase(" ")
        game.currentWord.pop()
        game.display()
    }
    if (key == " ") { game.init() }
});