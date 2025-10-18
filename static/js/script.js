document.addEventListener("DOMContentLoaded", () => {
    console.log("DOM fully loaded and parsed");
    setTimeout(() => {
        document.querySelector('#DA').style.display = 'none';
    }, 5000);
});
