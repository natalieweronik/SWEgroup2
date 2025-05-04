let player;

function onYouTubeIframeAPIReady() {
  player = new YT.Player('player', {
    height: '390',
    width: '640',
    videoId: '7MwgfkhcG7Q',
    playerVars: { 'playsinline': 1 },
    events: {
      'onReady': onPlayerReady
    }
  });
}

function onPlayerReady(event) {
  document.getElementById("playPauseBtn").addEventListener("click", () => {
    const state = player.getPlayerState();
    if (state === YT.PlayerState.PLAYING) {
      player.pauseVideo();
    } else {
      player.playVideo();
    }
  });

  document.getElementById("muteBtn").addEventListener("click", () => {
    if (player.isMuted()) {
      player.unMute();
    } else {
      player.mute();
    }
  });
}
