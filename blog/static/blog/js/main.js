document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('#select-pitching-stats').addEventListener('click', () => showPitchingStats());
    document.querySelector('#select-batting-stats').addEventListener('click', () => showBattingStats());
})

function showPitchingStats() {
    document.querySelector('#batting-stats').style.display = "none";
    document.querySelector('#pitching-stats').style.display = "block";
}

function showBattingStats() {
    document.querySelector('#batting-stats').style.display = "block";
    document.querySelector('#pitching-stats').style.display = "none";
}

