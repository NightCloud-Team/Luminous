
document.getElementById("send-button").addEventListener("click", sendmessage);
document.getElementById("user-input").addEventListener("keypress", function (e) {
        if (e.key === "Enter") {
            sendmessage();
        }
    });
let websocket = null;
function connect() {
	const button = document.getElementById("send-button");
	button.disabled = true;
	document.getElementById("user-input").placeholder = "等待加载完成";
	const websocket = new WebSocket("ws://127.0.0.1:8888");
	websocket.onopen = function () {
		const button = document.getElementById("send-button");
		button.disabled = false;
		document.getElementById("user-input").placeholder = "输入你的需求";
		
	};
	websocket.onclose = function () {
		const button = document.getElementById("send-button");
		button.disabled = true;
		setTimeout(connect, 1000);
		console.log("WebSocket 连接未打开");
		document.getElementById("user-input").placeholder = "等待加载完成";

	};
	websocket.onerror = function () {
		const button = document.getElementById("send-button");
		button.disabled = true;
		setTimeout(connect, 1000);
		console.log("WebSocket 连接未打开");
		document.getElementById("user-input").placeholder = "等待加载完成";
	};
}
connect();
websocket.close();


function sendmessage() {
	const websocket = new WebSocket("ws://127.0.0.1:8888");
	websocket.onopen = function () {
		const inputField = document.getElementById("user-input");
		const messageText = inputField.value.trim();
		if (messageText === "") return;
		appendMessage("user", messageText);
		message = JSON.stringify({ "function": "chat", "message": messageText })
		websocket.send(message)
	}
	websocket.onmessage = function (event) {
		const data = JSON.parse(event.data);
		const message = data["message"]
		appendMessage("bot",message)
		
	}
	websocket.onclose = function () {
		connect()
	}
	websocket.onerror = function () {
		connect()
	}

}
function appendMessage(sender, text) {
        const chatWindow = document.getElementById("chat-window");
        const messageElement = document.createElement("div");
        messageElement.classList.add("message", sender);
        messageElement.innerText = text;
        chatWindow.appendChild(messageElement);

            // Scroll to the bottom of the chat window
        chatWindow.scrollTop = chatWindow.scrollHeight;
}