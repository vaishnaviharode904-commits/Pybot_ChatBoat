import tkinter as tk
import random
import re
from datetime import datetime

def reply_time():
    now = datetime.now().strftime("%I:%M %p")
    return f"The current time is {now}.\nअभी समय {now} है।"

def reply_date():
    today = datetime.now().strftime("%d %B %Y")
    return f"Today's date is {today}.\nआज की तारीख {today} है।"

def reply_day():
    day = datetime.now().strftime("%A")
    hindi = {
        "Monday": "सोमवार", "Tuesday": "मंगलवार", "Wednesday": "बुधवार",
        "Thursday": "गुरुवार", "Friday": "शुक्रवार", "Saturday": "शनिवार",
        "Sunday": "रविवार",
    }
    return f"Today is {day}.\nआज {hindi[day]} है।"

responses = [
    (["time", "samay", "समय", "टाइम"], [reply_time]),
    (["date", "tarikh", "tarikh", "तारीख", "तारीख़"], [reply_date]),
    (["day", "din", "दिन", "weekday"], [reply_day]),

    (["good morning", "suprabhat", "सुप्रभात"], [
        "Good morning! Have a great day.\nसुप्रभात! आपका दिन शानदार हो।"]),
    (["good night", "shubh ratri", "शुभ रात्रि"], [
        "Good night! Sleep well.\nशुभ रात्रि! अच्छी नींद लें।"]),
    (["good afternoon"], [
        "Good afternoon! How can I help?\nनमस्कार! मैं कैसे मदद करूँ?"]),

    (["how are you", "kaise ho", "kya haal", "कैसे हो", "क्या हाल"], [
        "I'm doing great, thanks! How about you?\nमैं बहुत अच्छा हूँ, धन्यवाद! आप कैसे हैं?",
        "All good! What about you?\nसब बढ़िया! आप बताइए?"]),
    (["hello", "hi", "hey", "namaste", "नमस्ते", "हेलो"], [
        "Hello! How can I help you?\nनमस्ते! मैं आपकी कैसे मदद कर सकता हूँ?",
        "Hi there! Nice to meet you.\nहेलो! आपसे मिलकर अच्छा लगा।"]),

    (["your name", "who are you", "tumhara naam", "aapka naam", "तुम्हारा नाम", "आपका नाम"], [
        "I'm PyBot, a chatbot made with Python and Tkinter.\nमैं PyBot हूँ, Python और Tkinter से बना चैटबॉट।"]),
    (["who made you", "creator", "kisne banaya", "किसने बनाया"], [
        "A student developer built me using Python.\nमुझे एक स्टूडेंट डेवलपर ने Python से बनाया है।"]),
    (["what can you do", "kya kar sakte", "क्या कर सकते"], [
        "I can tell time, date, jokes, quotes and chat about coding.\nमैं समय, तारीख, जोक्स, कोट्स बता सकता हूँ और कोडिंग पर बात कर सकता हूँ।"]),

    (["python", "पायथन"], [
        "Python is easy, powerful and great for AI, web and automation.\nPython आसान और शक्तिशाली भाषा है, AI, वेब और ऑटोमेशन के लिए बढ़िया।"]),
    (["java", "जावा"], [
        "Java is popular for Android apps and backend systems.\nJava Android ऐप्स और बैकएंड सिस्टम के लिए बहुत लोकप्रिय है।"]),
    (["tkinter"], [
        "Tkinter is Python's built-in library for making GUI apps.\nTkinter Python की बिल्ट-इन लाइब्रेरी है जिससे GUI ऐप बनते हैं।"]),
    (["coding", "programming", "code"], [
        "Practice daily, build small projects and read other people's code.\nरोज़ अभ्यास करें, छोटे प्रोजेक्ट बनाएँ और दूसरों का कोड पढ़ें।"]),
    (["bug", "error"], [
        "Read the error message carefully, it usually tells you the line number.\nError मैसेज ध्यान से पढ़ें, उसमें अक्सर लाइन नंबर बताया होता है।"]),
    (["github"], [
        "GitHub is a great place to store projects and show your work to recruiters.\nGitHub प्रोजेक्ट रखने और रिक्रूटर्स को अपना काम दिखाने की बढ़िया जगह है।"]),

    (["internship", "इंटर्नशिप"], [
        "Build projects, keep your GitHub and LinkedIn updated, and apply regularly.\nप्रोजेक्ट बनाएँ, GitHub और LinkedIn अपडेट रखें और लगातार अप्लाई करें।"]),
    (["study", "padhai", "exam", "पढ़ाई", "परीक्षा"], [
        "Study in short focused sessions and revise regularly.\nछोटे-छोटे फोकस्ड सेशन में पढ़ें और नियमित रिवीज़न करें।"]),
    (["motivate", "motivation", "quote", "prerna", "प्रेरणा"], [
        "Small steps every day lead to big results.\nहर दिन के छोटे कदम बड़े नतीजे लाते हैं।",
        "Don't stop until you're proud.\nजब तक गर्व न हो, तब तक रुकें नहीं।",
        "Consistency beats talent.\nलगातार मेहनत प्रतिभा से आगे निकल जाती है।"]),

    (["joke", "funny", "mazak", "chutkula", "चुटकुला", "जोक"], [
        "Why do programmers prefer dark mode? Because light attracts bugs!\nप्रोग्रामर्स डार्क मोड क्यों पसंद करते हैं? क्योंकि रोशनी से बग आते हैं!",
        "Why did the developer go broke? He used up all his cache.\nडेवलपर कंगाल क्यों हो गया? उसका सारा कैश खत्म हो गया।"]),

    (["thank", "thanks", "shukriya", "dhanyavad", "धन्यवाद", "शुक्रिया"], [
        "You're welcome!\nआपका स्वागत है!",
        "Happy to help!\nमदद करके खुशी हुई!"]),
    (["sorry", "maaf", "माफ़", "माफी"], [
        "No problem at all.\nकोई बात नहीं।"]),
    (["love you", "i like you"], [
        "That's sweet! I'm just a bot, but I'm glad to chat.\nबहुत प्यारी बात! मैं बस एक बॉट हूँ, पर बात करके अच्छा लगा।"]),
    (["help", "madad", "मदद"], [
        "Try: hello, time, date, day, joke, quote, python, java, study, internship, bye.\n"
        "ये आज़माएँ: hello, time, date, day, joke, quote, python, java, study, internship, bye।"]),
    (["bye", "goodbye", "alvida", "अलविदा"], [
        "Goodbye! See you soon.\nअलविदा! फिर मिलेंगे।"]),
]

DEFAULT_REPLY = ("Sorry, I didn't understand that. Type 'help' for ideas.\n"
                 "माफ़ कीजिए, मैं समझ नहीं पाया। सुझाव के लिए 'help' लिखें।")

def keyword_match(keyword, text):
    if keyword.isascii():
        return re.search(r"\b" + re.escape(keyword) + r"\b", text) is not None
    return keyword in text

def get_reply(text):
    text = text.lower()
    for keywords, replies in responses:
        if any(keyword_match(k, text) for k in keywords):
            choice = random.choice(replies)
            return choice() if callable(choice) else choice
    return DEFAULT_REPLY

FONT = "Nirmala UI"          # Mac/Linux: "Noto Sans Devanagari" or "Arial Unicode MS"
EMOJI_FONT = "Segoe UI Emoji"

themes = {
    "light": {"bg": "#e5ddd5", "header": "#075e54", "header_fg": "#ffffff",
              "user_bg": "#dcf8c6", "user_fg": "#111111",
              "bot_bg": "#ffffff", "bot_fg": "#111111",
              "meta": "#667781", "bar": "#f0f0f0", "entry_bg": "#ffffff",
              "entry_fg": "#111111", "btn": "#25d366", "btn_fg": "#ffffff",
              "chip": "#d9eee3", "chip_fg": "#075e54"},
    "dark":  {"bg": "#0b141a", "header": "#202c33", "header_fg": "#e9edef",
              "user_bg": "#005c4b", "user_fg": "#e9edef",
              "bot_bg": "#202c33", "bot_fg": "#e9edef",
              "meta": "#8696a0", "bar": "#202c33", "entry_bg": "#2a3942",
              "entry_fg": "#e9edef", "btn": "#00a884", "btn_fg": "#ffffff",
              "chip": "#2a3942", "chip_fg": "#7fd6c2"},
}
current_theme = "light"

messages = []        # list of (sender, text, time)
typing_row = None
pending = 0

def stamp():
    return datetime.now().strftime("%I:%M %p")

def render_message(sender, text, when):
    t = themes[current_theme]
    is_user = sender == "user"
    bubble_bg = t["user_bg"] if is_user else t["bot_bg"]
    bubble_fg = t["user_fg"] if is_user else t["bot_fg"]

    row = tk.Frame(msg_frame, bg=t["bg"])
    row.pack(fill="x", padx=10, pady=4)

    holder = tk.Frame(row, bg=t["bg"])
    holder.pack(side="right" if is_user else "left")

    avatar = tk.Label(holder, text="🧑" if is_user else "🤖",
                      font=(EMOJI_FONT, 16), bg=t["bg"], fg=t["meta"])
    bubble = tk.Frame(holder, bg=bubble_bg, padx=10, pady=6)

    name = "You / आप" if is_user else "PyBot"
    tk.Label(bubble, text=name, font=(FONT, 8, "bold"), bg=bubble_bg,
             fg=t["meta"], anchor="w").pack(fill="x")
    tk.Label(bubble, text=text, font=(FONT, 11), bg=bubble_bg, fg=bubble_fg,
             wraplength=270, justify="left", anchor="w").pack(fill="x")
    tk.Label(bubble, text=when, font=(FONT, 7), bg=bubble_bg,
             fg=t["meta"], anchor="e").pack(fill="x")

    if is_user:
        bubble.pack(side="left")
        avatar.pack(side="left", padx=(6, 0), anchor="s")
    else:
        avatar.pack(side="left", padx=(0, 6), anchor="s")
        bubble.pack(side="left")

def keep_typing_last():
    if typing_row is not None:
        typing_row.pack_forget()
        typing_row.pack(fill="x", padx=10, pady=4)

def scroll_bottom():
    root.update_idletasks()
    canvas.yview_moveto(1.0)

def add_message(sender, text):
    when = stamp()
    messages.append((sender, text, when))
    render_message(sender, text, when)
    keep_typing_last()
    scroll_bottom()

def make_typing_row():
    global typing_row
    t = themes[current_theme]
    typing_row = tk.Frame(msg_frame, bg=t["bg"])
    typing_row.pack(fill="x", padx=10, pady=4)
    tk.Label(typing_row, text="🤖", font=(EMOJI_FONT, 16),
             bg=t["bg"], fg=t["meta"]).pack(side="left", padx=(0, 6))
    tk.Label(typing_row, text=" PyBot typing... / टाइप कर रहा है... ",
             font=(FONT, 9, "italic"), bg=t["bot_bg"], fg=t["meta"],
             pady=6).pack(side="left")

def show_typing():
    global pending
    pending += 1
    if typing_row is None:
        make_typing_row()
    scroll_bottom()

def hide_typing():
    global typing_row
    if typing_row is not None:
        typing_row.destroy()
        typing_row = None

def send(event=None, text=None):
    user = (text if text is not None else entry.get()).strip()
    if not user:
        return
    entry.delete(0, tk.END)
    add_message("user", user)
    show_typing()
    root.after(random.randint(600, 1100), lambda: bot_respond(user))

def bot_respond(user):
    global pending
    pending -= 1
    if pending <= 0:
        pending = 0
        hide_typing()
    add_message("bot", get_reply(user))

def rebuild():
    global typing_row
    for w in msg_frame.winfo_children():
        w.destroy()
    typing_row = None
    for sender, text, when in messages:
        render_message(sender, text, when)
    if pending > 0:
        make_typing_row()
    scroll_bottom()

def clear_chat():
    global pending
    messages.clear()
    pending = 0
    hide_typing()
    rebuild()
    add_message("bot", "Chat cleared. Say hello!\nचैट साफ़ हो गई। हेलो बोलिए!")

def apply_theme():
    t = themes[current_theme]
    root.config(bg=t["bg"])
    header.config(bg=t["header"])
    title_lbl.config(bg=t["header"], fg=t["header_fg"])
    status_lbl.config(bg=t["header"], fg="#9ee6c4")
    head_avatar.config(bg=t["header"])
    for b in (theme_btn, clear_btn):
        b.config(bg=t["header"], fg=t["header_fg"],
                 activebackground=t["header"], activeforeground=t["header_fg"])
    theme_btn.config(text="☀ Light" if current_theme == "dark" else "🌙 Dark")
    canvas.config(bg=t["bg"])
    msg_frame.config(bg=t["bg"])
    chips_bar.config(bg=t["bar"])
    for c in chips:
        c.config(bg=t["chip"], fg=t["chip_fg"],
                 activebackground=t["chip"], activeforeground=t["chip_fg"])
    input_bar.config(bg=t["bar"])
    entry.config(bg=t["entry_bg"], fg=t["entry_fg"], insertbackground=t["entry_fg"])
    send_btn.config(bg=t["btn"], fg=t["btn_fg"],
                    activebackground=t["btn"], activeforeground=t["btn_fg"])
    rebuild()

def toggle_theme():
    global current_theme
    current_theme = "dark" if current_theme == "light" else "light"
    apply_theme()

root = tk.Tk()
root.title("PyBot - English/हिंदी")
root.geometry("460x640")
root.minsize(380, 480)

header = tk.Frame(root, pady=8)
header.pack(fill="x")
head_avatar = tk.Label(header, text="🤖", font=(EMOJI_FONT, 20))
head_avatar.pack(side="left", padx=(10, 6))
name_box = tk.Frame(header)
name_box.pack(side="left")
title_lbl = tk.Label(name_box, text="PyBot", font=(FONT, 13, "bold"))
title_lbl.pack(anchor="w")
status_lbl = tk.Label(name_box, text="● Online / ऑनलाइन", font=(FONT, 8))
status_lbl.pack(anchor="w")
name_box.config(bg=themes["light"]["header"])
clear_btn = tk.Button(header, text="🗑 Clear", command=clear_chat, relief="flat", bd=0)
clear_btn.pack(side="right", padx=6)
theme_btn = tk.Button(header, command=toggle_theme, relief="flat", bd=0)
theme_btn.pack(side="right")

chat_area = tk.Frame(root)
chat_area.pack(fill="both", expand=True)
canvas = tk.Canvas(chat_area, highlightthickness=0)
scrollbar = tk.Scrollbar(chat_area, command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

msg_frame = tk.Frame(canvas)
win = canvas.create_window((0, 0), window=msg_frame, anchor="nw")
msg_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.bind("<Configure>", lambda e: canvas.itemconfig(win, width=e.width))

def on_wheel(event):
    if event.num == 4:
        canvas.yview_scroll(-2, "units")
    elif event.num == 5:
        canvas.yview_scroll(2, "units")
    else:
        canvas.yview_scroll(int(-event.delta / 60) or (-1 if event.delta > 0 else 1), "units")

canvas.bind_all("<MouseWheel>", on_wheel)
canvas.bind_all("<Button-4>", on_wheel)
canvas.bind_all("<Button-5>", on_wheel)

chips_bar = tk.Frame(root, pady=4)
chips_bar.pack(fill="x")
chips = []
for label, msg in [("👋 Hello", "hello"), ("🕒 Time", "time"), ("📅 Date", "date"),
                   ("😂 Joke", "joke"), ("💡 Quote", "quote"), ("❓ Help", "help")]:
    b = tk.Button(chips_bar, text=label, font=(FONT, 9), relief="flat", bd=0,
                  padx=8, pady=2, command=lambda m=msg: send(text=m))
    b.pack(side="left", padx=4)
    chips.append(b)

input_bar = tk.Frame(root, pady=8)
input_bar.pack(fill="x")
entry = tk.Entry(input_bar, font=(FONT, 11), relief="flat")
entry.pack(side="left", fill="x", expand=True, padx=(10, 6), ipady=8)
entry.bind("<Return>", send)
entry.focus()
send_btn = tk.Button(input_bar, text="Send / भेजें ➤", font=(FONT, 10, "bold"),
                     relief="flat", bd=0, padx=10, pady=6, command=send)
send_btn.pack(side="right", padx=(0, 10))

apply_theme()
add_message("bot", "Hello! I'm PyBot. Tap a button below or type 'help'.\n"
                   "नमस्ते! मैं PyBot हूँ। नीचे बटन दबाएँ या 'help' लिखें।")
root.mainloop()
