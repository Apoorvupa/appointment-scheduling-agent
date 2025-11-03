import React, { useState } from "react";
import axios from "axios";

export default function ChatInterface() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    const userMessage = { sender: "user", text: input };
    setMessages([...messages, userMessage]);

    const response = await axios.post("http://localhost:8000/api/chat", { message: input, user_id: "user1" });
    setMessages([...messages, userMessage, { sender: "agent", text: response.data.reply }]);
    setInput("");
  };

  return (
    <div>
      <div style={{ border: "1px solid gray", padding: "10px", height: "400px", overflowY: "scroll" }}>
        {messages.map((m, i) => (
          <div key={i} style={{ textAlign: m.sender === "user" ? "right" : "left" }}>{m.text}</div>
        ))}
      </div>
      <input
  value={input}
  onChange={(e) => setInput(e.target.value)}
  onKeyDown={(e) => {
    if (e.key === "Enter") {
      sendMessage();
    }
  }}
/>

      <button onClick={sendMessage}>Send</button>
    </div>
  );
}
