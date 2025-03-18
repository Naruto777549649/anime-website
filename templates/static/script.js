// Dark Mode Toggle
document.querySelector("header").addEventListener("click", function() {
    document.body.classList.toggle("dark-mode");
});

// Anime API Se Data Fetch
fetch('https://api.jikan.moe/v4/anime?q=naruto')
  .then(response => response.json())
  .then(data => console.log(data));