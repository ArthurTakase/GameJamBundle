function update_nb() {
    console.log(nb_blanc, nb_rouge)
    var history = document.getElementsByClassName('dot-group')
    var last_history = history[history.length - 1]
    var label_white = last_history.getElementsByClassName('nb-white')
    var label_red = last_history.getElementsByClassName('nb-red')

    label_red[0].innerHTML = nb_rouge
    label_white[0].innerHTML = nb_blanc
}

function random_from_list(liste) {
    return liste[Math.floor(Math.random()*liste.length)]
}

function edit_subtitle(text, color) {
    var subtitle = document.getElementById('subtitle')

    subtitle.innerHTML = text
    subtitle.style.color = color
}

function reset() {
    nb_try = 0
    player_tab = []
    nb_dot = 0
    nb_blanc = 0
    nb_rouge = 0
    new_result()
    var history = document.getElementById('history-zone')

    history.innerHTML = '<div class="dot-group">\
                            <div class="nb nb-white">0</div>\
                            <div class="dot"></div>\
                            <div class="dot"></div>\
                            <div class="dot"></div>\
                            <div class="dot"></div>\
                            <div class="nb nb-red">0</div>\
                        </div>'
}

function add_new_history() {
    var history = document.getElementById('history-zone')

    history.innerHTML +=    '<div class="dot-group">\
                                <div class="nb nb-white">0</div>\
                                <div class="dot"></div>\
                                <div class="dot"></div>\
                                <div class="dot"></div>\
                                <div class="dot"></div>\
                                <div class="nb nb-red">0</div>\
                            </div>'
}

function add(color) {
    edit_subtitle(12 - nb_try, "white")
    var history = document.getElementsByClassName('dot-group')
    var dots = history[history.length - 1].getElementsByClassName('dot')
    player_tab.push(color)

    dots[nb_dot].classList.add('dot-full')
    dots[nb_dot].classList.add(color)
    nb_dot += 1

    if (nb_dot > 3) {
        mastermind()
    }
}

function defeat() {
    edit_subtitle("Défaite", "red")
    reset()
}

function victory() {
    edit_subtitle("Victoire", "green")
    reset()
}