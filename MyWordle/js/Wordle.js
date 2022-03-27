class Wordle {
    constructor() {
        this.canvas = document.getElementById("canvas")
        this.result
        this.currentLine
        this.currentCase
        this.cases
        this.currentWord
        this.win

        this.init()
    }

    reset() {
        this.result = dictionnaire[Math.floor(Math.random() * dictionnaire.length)]
        this.currentLine = 0
        this.currentCase = 0
        this.cases = []
        this.currentWord = []
        this.win = false
    }

    display() {
        var result = ""

        for (var y = 0; parseInt(y) != 6; y++) {
            result += "<div class=\"line\">"
            for (var x = 0; parseInt(x) != 5; x++)
                result += this.cases[y][x].display()
            result += "</div>"
        }

        canvas.innerHTML = result
    }

    init() {
        this.reset()

        var lineCase = []

        for (var y = 0; parseInt(y) != 6; y++) {
            lineCase = []
            for (var x = 0; parseInt(x) != 5; x++)
                lineCase.push(new Case(x, y))
            this.cases.push(lineCase)
        }
        this.display()
    }

    check() {
        var count = 0
        var temp_result = this.result.split("")
        var index

        for (var i = 0; i != 5; i++) {
            index = temp_result.indexOf(this.currentWord[i])
            if (this.currentWord[i] == temp_result[i]) {
                this.cases[this.currentLine][i].type = "good"
                temp_result[index] = "_"
                count++
            }
        }

        for (var i = 0; i != 5; i++) {
            index = temp_result.indexOf(this.currentWord[i])
            if (this.cases[this.currentLine][i].type == "good")
                continue // pour gérer les lettres en double
            if (temp_result.indexOf(this.currentWord[i]) >= 0) {
                this.cases[this.currentLine][i].type = "maybe"
                temp_result[index] = "_"
            } else
                this.cases[this.currentLine][i].type = "not"
        }

        if (count == 5)
            this.win = true
    }

    setCase(key) {
        this.cases[this.currentLine][this.currentCase].content = key
    }
}