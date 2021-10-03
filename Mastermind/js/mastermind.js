var all_color = ["yellow", "blue", "red", "green", "white", "black"]
var result = []
var player_tab = []
var nb_dot = 0
var nb_try = 0
var nb_blanc = 0 // dans la soluce
var nb_rouge = 0 // bonne place

function new_result() {
    result = []
    for (var i = 0; i != 4; i++) {
        result.push(random_from_list(all_color))
    }
}

function mastermind() {
    for (color in player_tab) {
        if (player_tab[color] == result[color]) {
            nb_rouge += 1
        } else if (result.includes(player_tab[color])) {
            nb_blanc += 1
        }
    }
    
    update_nb()
    if (nb_rouge == 4) {
        victory()
    } else {
        nb_rouge = 0
        nb_blanc = 0
        nb_try += 1
        nb_dot = 0
        player_tab = []
        edit_subtitle(12 - nb_try, "white")
        add_new_history()
        if (nb_try > 11)
            defeat()
    }
}

new_result()