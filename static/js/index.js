document.getElementById("btn_refresh_page").onclick = async () =>
{
    window.location.reload()
}

//document.getElementById("btn_cam_page").onclick = async () =>{window.location.href = "/cam"}

document.addEventListener("DOMContentLoaded", () => {
    const playButton = document.getElementById("btn_music_play")
    const turntable = document.querySelector(".vinyl div:nth-of-type(2)") // 회전 요소
    const turntableArm = document.querySelector(".turntable div:nth-of-type(1)") // 암 요소

    let isPlaying = false; // 재생 상태를 추적

    playButton.addEventListener("click", () => {
        isPlaying = !isPlaying // 상태 토글

        if (isPlaying) {
            turntable.style.animationPlayState = "running" // 회전 애니메이션 재생
            turntableArm.style.transform = "translate(-15px, -4px) rotate(30deg)" // 재생 위치로 이동
        } else {
            turntable.style.animationPlayState = "paused" // 회전 애니메이션 정지
            turntableArm.style.transform = "translate(0, 0) rotate(0)" // 원래 위치로 복귀
        }
    })
})