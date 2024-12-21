const c_METHOD_GET = "GET"
const c_METHOD_POST = "POST"

const c_DEFAULT_METHOD = "GET"
const c_DEFAULT_HEADERS = {}
const c_DEFAULT_BODY = undefined

function goBack() {
    window.location.href = "/";
}

function playMusic(id) {
    fetch(`/music/control/play/${id}`, {
        method: c_METHOD_POST,
        headers: c_DEFAULT_HEADERS,
        body: c_DEFAULT_BODY
    })
}

function updateMusic(id) {
    alert('Updating music with ID: ' + id);
    // Add actual update functionality here
}

async function deleteMusic(id) {
    await fetch(`/musiclist/delete/${id}`, {
        method: c_METHOD_POST,
        headers: c_DEFAULT_HEADERS,
        body: c_DEFAULT_BODY
    })
}

function clearRecords()
{
    let musiclistHtml = document.getElementById("musiclist")

    musiclistHtml.querySelectorAll(".music_record").forEach((record) => {
        musiclistHtml.removeChild(record)
    })
}

function createRecord(id, music_name, artists, upload_date) {
    record = document.createElement("tr")
    col_id = document.createElement("td")
    col_music_name = document.createElement("td")
    col_artists = document.createElement("td")
    col_upload_date = document.createElement("td")
    col_buttons = document.createElement("td")

    record.classList.add("music_record")
    col_id.classList.add("txt-align-right")

    col_id.innerText = id
    span_music_name = document.createElement("span")
    span_music_name.innerText = music_name
    col_artists.innerText = artists
    col_upload_date.innerText = upload_date

    button_play = document.createElement("button")
    button_delete = document.createElement("button")

    button_play.innerText = "Play"
    button_delete.innerText = "Delete"

    button_play.onclick = () => {
        playMusic(id)
    }
    button_delete.onclick = async () => {
        await deleteMusic(id)
        reloadRecords()
    }

    record.appendChild(col_id)
    record.appendChild(col_music_name)
    col_music_name.appendChild(span_music_name)
    record.appendChild(col_artists)
    record.appendChild(col_upload_date)
    record.appendChild(col_buttons)

    if (id != "")
    {
        col_buttons.appendChild(button_play)
        col_buttons.appendChild(button_delete)
    }

    return record
}

async function reloadRecords()
{
    let response = await fetch("/musiclist/reload", {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }
    })

    let musiclistHtml = document.getElementById("musiclist")
    let musiclist = await response.json()
    let i = 0

    clearRecords()

    for (i = 0; i < musiclist.length; ++i)
    {
        let musicdata = musiclist[i]

        let id = musicdata[0]
        let music_name = musicdata[1]
        let artists = musicdata[2]
        let upload_date = musicdata[3]

        let record = createRecord(id, music_name, artists, upload_date)

        musiclistHtml.appendChild(record)
    }

    if (i == 0)
    {
        let dummyRecord = createRecord("", "Empty Music", "", "")
        musiclistHtml.appendChild(record)
    }
}

document.addEventListener("DOMContentLoaded", () => {
    reloadRecords()
})