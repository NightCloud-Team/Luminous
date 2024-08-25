const button = document.getElementById("send-button");
button.disabled = true;
document.getElementById("user-input").placeholder = "等待加载完成";
let websocket = null;
function connect() {
	const websocket = new WebSocket("ws://127.0.0.1:8888");
	websocket.onopen = function () {
		const button = document.getElementById("send-button");
		button.disabled = false;
		document.getElementById("user-input").placeholder = "输入你的需求";
		websocket.close();
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
connect()


function sendmessage() {
	const websocket = new WebSocket("ws://127.0.0.1:8888");
	websocket.onopen = function () { }

}