# Q‑A Chatbot

A versatile chatbot supporting **OpenAI**, **Groq**, and **Ollama** as backend LLMs. Users can choose their preferred model, set generation parameters like `temperature` and `max_tokens`, and get intelligent answers from either cloud-based or local models.

---

## ✨ Features

- 🔁 **Model Selection**: Choose between OpenAI, Groq, or Ollama
- 🎛️ **Control Parameters**: Adjust `temperature` and `max_tokens` dynamically
- 🔐 **Secure Access**: Use `.env` for managing OpenAI and Groq API keys
- 🧠 **Local Inference**: Use Ollama to run LLMs like LLaMA3 or Mistral locally
- 🧰 Modular, extensible codebase

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/shishiradk/Q-Achatbot.git
cd Q-Achatbot
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 API Keys

Create a `.env` file in the project root with the following content:

```env
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
```

- **OpenAI** and **Groq** require API keys.
- **Ollama** does not require any API key and runs models locally.

---

## 🚀 Running the Chatbot

To launch the chatbot:

```bash
python app.py
```

You will be prompted or able to configure:
- Selected model (`OpenAI`, `Groq`, `Ollama`)
- `temperature` (e.g., 0.7)
- `max_tokens` (e.g., 256)
- Your input prompt

The chatbot will return a response from the chosen LLM based on your input.

---

## 🧠 Supported Models

| Provider | Models (Examples)            | Requirements             |
|----------|------------------------------|--------------------------|
| OpenAI   | `gpt-3.5-turbo`, `gpt-4`     | Requires API key         |
| Groq     | `llama3-8b`, `mixtral-8x7b`  | Requires API key         |
| Ollama   | `llama2`, `llama3`, `mistral`| Runs locally, no API key |

> Ollama must be installed and running on your system to use its models.

---

## 🧩 Project Structure

```
Q-Achatbot/
├── app.py                # Main chatbot interface
├── .env                  # API keys (not committed)
├── requirements.txt      # Dependencies list
├── models/
│   └── llm_handler.py    # LLM routing logic
├── utils/
│   └── config.py         # Environment and config utilities
└── README.md             # Project documentation
```

---

## 🛠 Example Workflow

1. Set your `.env` with valid API keys
2. Run `python app.py`
3. Choose:
   - Model: OpenAI, Groq, Ollama
   - Temperature: e.g., 0.7
   - Max Tokens: e.g., 200
4. Enter your prompt
5. View the LLM’s response

---

## 📸 Optional Enhancements

- Add a Streamlit UI or web interface
- Include logging and history saving
- Support multiple API versions or tools (e.g., Claude, Gemini)

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repo
2. Create a new branch
3. Make your changes
4. Submit a pull request

---

## 📜 License

This project is open-sourced under the **MIT License**. See [`LICENSE`](./LICENSE) for details.

---

## 🙏 Credits

- [OpenAI](https://openai.com/)
- [Groq](https://groq.com/)
- [Ollama](https://ollama.com/)
- Project inspired by modular AI chatbot design patterns and multimodal toolkits

---

> Build locally. Scale globally. Choose your AI brain — one prompt at a time.
# Q-Achatbot

<img width="952" alt="image" src="https://github.com/user-attachments/assets/8fadc68a-68d6-43f6-a6bc-46be63aa55e1" />

---





