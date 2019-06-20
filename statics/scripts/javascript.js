function show_newWork_menu() {
    let newWork_menu = document.getElementById("newWork_menu");
    if (newWork_menu.classList.contains("hidden"))
        newWork_menu.classList.remove("hidden");
    else
        newWork_menu.classList.add("hidden");
}