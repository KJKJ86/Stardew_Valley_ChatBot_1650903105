function askQuestion() {
    let question = document.getElementById("question").value;
    let chatBox = document.getElementById("chat-box");

    if (!question) return;

    // แสดงคำถาม
    chatBox.innerHTML += `<div><b>คุณ:</b> ${question}</div>`;

    // แสดงข้อความกำลังคิด
    let loadingMsg = document.createElement("div");
    loadingMsg.innerHTML = "<b>บอท:</b> กำลังคิด... กรุณารอสักครู่ ⏳";
    chatBox.appendChild(loadingMsg);

    fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: question })
    })
    .then(response => response.json())
    .then(data => {
        loadingMsg.innerHTML = `<b>บอท:</b> ${data.answer}`;
    })
    .catch(error => {
        loadingMsg.innerHTML = "<b>บอท:</b> มีข้อผิดพลาด โปรดลองอีกครั้ง!";
        console.error("Error:", error);
    });

    document.getElementById("question").value = "";
}
