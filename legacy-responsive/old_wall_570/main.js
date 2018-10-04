const showLinks = (id, id2) => {
    if (document.getElementById(id).style.display == "none") {
        document.getElementById(id).style.display = "block";
        document.getElementById(id2).style.display = "none";
    } else {
        document.getElementById(id).style.display = "none";
    }
}