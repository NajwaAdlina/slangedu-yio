// Definisi fungsi generateResponse
function generateResponse(userInput) {
    // Lakukan sesuatu dengan input pengguna dan kembalikan respons
}

// Fungsi untuk mengirim pesan pengguna
function sendMessage() {
    const userInput = document.getElementById("user-input").value.trim().toLowerCase();
    const chatDisplay = document.getElementById("chat-display");

    // Membuat elemen untuk pesan pengguna
    const userMessageElement = document.createElement("div");
    userMessageElement.classList.add("user-bubble"); 
    userMessageElement.textContent = userInput;
    chatDisplay.appendChild(userMessageElement);

    // Menampilkan jawaban dari chatbot
    const chatbotResponse = generateResponse(userInput); // Panggil fungsi generateResponse
    const chatbotMessageElement = document.createElement("div");
    chatbotMessageElement.classList.add("bot-bubble");
    chatbotMessageElement.textContent = chatbotResponse;
    chatDisplay.appendChild(chatbotMessageElement);

    // Membersihkan input pengguna
    document.getElementById("user-input").value = "";

    // Menggulir ke bawah untuk melihat pesan terbaru
    chatDisplay.scrollTop = chatDisplay.scrollHeight;
}

// Fungsi untuk menangani tombol enter
function handleKeyPress(event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        sendMessage();
    }
}
