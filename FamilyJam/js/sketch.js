let camera;
let cameraIsShow = true;
let pictures = [];
let nextFrameIsShow = true;
let canvas;
let id = 0;
let filters;
let filterID = 3;
let isFlip = true;

function setup() {
    canvas = createCanvas(640, 480);
    background(0, 0, 0, 0);
    camera = createCapture(VIDEO);
    camera.size(640, 480);

    filters = [
        loadImage("img/rugby.png"),
        loadImage("img/simpson.png"),
        loadImage("img/blood.png"),
        loadImage("img/epitech.png"),
        loadImage("img/smoke.png"),
        loadImage("img/money.png"),
        loadImage("img/ranma.png"),
        loadImage("img/ungarsunefille.png"),
        loadImage("img/aerer.png"),
        loadImage("img/onepiece.png"),
        loadImage("img/clovers.png"),
        loadImage("img/flakes.png"),
        loadImage("img/hearts.png"),
        loadImage("img/bears.png"),
    ]
}

function draw() {
    let len = pictures.length - 1;

    clear();
    background(0, 0, 0, 0);

    try {
        for (let i = 0; i < pictures.length; i++) {
            let crop = pictures[i].get(frames[id][i]["x"], frames[id][i]["y"], frames[id][i]["w"], frames[id][i]["h"]);
            image(crop, frames[id][i]["x"], frames[id][i]["y"], frames[id][i]["w"], frames[id][i]["h"]);
        }
    } catch (e) {}

    try {
        if (nextFrameIsShow) {
            fill(255, 255, 255, 50);
            stroke(255, 255, 255);
            rect(frames[id][len + 1]["x"], frames[id][len + 1]["y"], frames[id][len + 1]["w"], frames[id][len + 1]["h"]);
        }
    } catch (e) {}

    try { image(filters[filterID], 0, 0); } catch (e) {}
}

function keyPressed() {
    if (keyCode === 32) pictures.push(camera.get());
    if (key == 't') filterID = (filterID + 1) % (filters.length + 1);
    if (key == 'g') nextFrame();
    if (key == 's') saveCanvas(canvas, 'family.jpg');
    if (key == 'r') pictures = [];
    if (key == 'f') nextFrameIsShow = !nextFrameIsShow;
    if (key == 'v') flipCamera();
}

// ------------------------------------

function nextFrame() {
    pictures = [];
    id = (id + 1) % frames.length;
}

function flipCamera() {
    const video = document.getElementsByTagName('video')[0];
    const canva = document.getElementsByTagName('canvas')[0];

    if (isFlip) {
        video.style.transform = 'scale(1.5, 1.5)';
        canva.style.transform = 'scale(1.5, 1.5)';
    } else {
        video.style.transform = 'scale(-1.5, 1.5)';
        canva.style.transform = 'scale(-1.5, 1.5)';
    }
    isFlip = !isFlip;
}