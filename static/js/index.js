$(document).ready(function () {
    let serial = document.getElementsByClassName("badge");
    for (let i = 0; i < serial.length; i++)
        serial[i].innerHTML = (i + 1).toString();
});

function getValues() {
    let inputs = document.getElementsByTagName("input");
    let values = {};
    for (let i = 0; i < inputs.length; i++) {
        let input = inputs[i];
        values[i] = input.value === "" ? input.placeholder : input.value;
    }
    return JSON.stringify(values);
}

function make() {
    let httpRequest = new XMLHttpRequest();
    httpRequest.onreadystatechange = function () {
        if (this.readyState === 4)
            if (this.status === 521 || this.status === 404)
                alert("制作GIF动图失败.");
            else
                open(this.responseText);
    };
    let target = $("title").text().split(":")[1].replace(/\s+/g, "");
    httpRequest.open("POST", target + "/make", true);
    httpRequest.send(getValues());
}
