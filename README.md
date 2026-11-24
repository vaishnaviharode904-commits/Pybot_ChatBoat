# 🤖 PyBot: Bilingual Chatbot (English + हिंदी)

A desktop chatbot built with **Python and Tkinter**. It replies in **both English and Hindi**, shows messages as **chat bubbles** like a real messaging app, and needs **no external libraries or API**.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

<!-- Replace this with your own screenshot: create an `assets` folder and add screenshot.png -->
![PyBot Screenshot](assets/screenshot.png)

## ✨ Features

- 💬 **Chat bubbles:** your messages on the right, bot replies on the left, with avatars and timestamps
- 🌐 **Bilingual replies:** every answer in English and Hindi (Devanagari)
- 🕒 **Live time, date and day** from your system clock
- ⌨️ **Typing indicator** before each reply
- 🌙 **Light and dark mode**
- ⚡ **Quick-reply buttons** (Hello, Time, Date, Joke, Quote, Help)
- 🗣️ **Understands Hindi, English and Hinglish keywords** (e.g. `kaise ho`, `namaste`, `धन्यवाद`)
- 🧹 **Clear chat** button and smooth scrolling

## 🚀 Getting Started

### Requirements
- Python 3.8 or higher
- Tkinter (already included with most Python installations)

### Run it

```bash
git clone https://github.com/vaishnaviharode904-commits/Pybot_ChatBoat
cd pybot-chatbot
python chatbot_gui_bubbles.py
```

> **Linux:** if Tkinter is missing, install it with `sudo apt install python3-tk`.

## 💡 Try These Messages

| You type | PyBot replies about |
|---|---|
| `hello` / `namaste` | Greeting |
| `what is the time` / `samay` | Current time |
| `date` / `tarikh` | Today's date |
| `tell me a joke` / `chutkula` | A programming joke |
| `quote` / `motivate me` | Motivational quote |
| `python`, `java`, `github` | Short coding tips |
| `help` | List of things to try |

## 🛠️ How It Works

1. The bot keeps a list of **keywords and replies** (`responses`).
2. When you send a message, it searches for a matching keyword using **regex word matching** (English) and substring matching (Hindi).
3. The first match is used, and a random reply is chosen from its list.
4. Messages are drawn as bubbles using Tkinter `Canvas`, `Frame` and `Label` widgets.

## ⚙️ Customize

**Add a new topic:** add a line to the `responses` list:

```python
(["keyword1", "keyword2"], ["English reply.\nहिंदी उत्तर।"]),
```

**Change colors:** edit the `themes` dictionary (`user_bg`, `bot_bg`, `header`, etc.).

**Fix Hindi font on Mac/Linux:** change `FONT` to `"Noto Sans Devanagari"` and `EMOJI_FONT` to `"Noto Color Emoji"`.

## 📁 Project Structure

```
pybot-chatbot/
├── chatbot_gui_bubbles.py   # main application
├── assets/
│   └── screenshot.png       # app screenshot
├── README.md
├── LICENSE
└── .gitignore
```

## 🔮 Future Improvements

- [ ] Voice input and output
- [ ] Save chat history to a file
- [ ] AI-powered mode using an LLM API
- [ ] More languages and topics
- [ ] Package as a `.exe` using PyInstaller

## 🤝 Contributing

Suggestions and improvements are welcome. Fork the repo, make your changes and open a pull request.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file.

## 👤 Author

**YOUR NAME**
Aspiring Software Developer| Python and Java
🔗 LinkedIn:https://www.linkedin.com/in/vaishnavi-harode 💻 GitHub:https://github.com/vaishnaviharode904-commits

⭐ If you like this project, give it a star!
