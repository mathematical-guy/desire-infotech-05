console.log("JavaScript is loaded 😂");


setTimeout((() => {
    fetch("https://api.dictionaryapi.dev/api/v2/entries/en/pen")
    .then(response => response.json())
    .then(data => console.log(data));
}), 3000)