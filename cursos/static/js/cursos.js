
function toggleVideos(capituloId) {
    var videoContainer = document.getElementById('videos-' + capituloId);
    if (videoContainer.style.display === "none" || videoContainer.style.display === "") {
        videoContainer.style.display = "block";
    } else {
        videoContainer.style.display = "none";
    }
}
