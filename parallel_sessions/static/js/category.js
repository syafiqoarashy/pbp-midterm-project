const a = document.querySelectorAll(".title")
console.log(a)

const buttonPressed = e => {
    console.log(e.target.id);
    var sym = e.target.id
    sessionStorage.setItem("sym", sym)
    var globalVariable = {
        x: sym
    };
}

a.forEach(button => {
    button.addEventListener('click', buttonPressed)
})

    // for (let button of a) {
    //     var symp = button.addEventListener("click", buttonPressed);
    //     console.log(symp)
    // }