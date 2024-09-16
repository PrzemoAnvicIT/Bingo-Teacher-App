import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
import random
from ttkthemes import ThemedTk  # You may need to install ttkthemes
# Your verbs data
verbs = [
    {'base': 'be', 'past_simple': 'was/were', 'past_participle': 'been'},
    {'base': 'beat', 'past_simple': 'beat', 'past_participle': 'beaten'},
    {'base': 'become', 'past_simple': 'became', 'past_participle': 'become'},
    {'base': 'begin', 'past_simple': 'began', 'past_participle': 'begun'},
    {'base': 'break', 'past_simple': 'broke', 'past_participle': 'broken'},
    {'base': 'bring', 'past_simple': 'brought', 'past_participle': 'brought'},
    {'base': 'build', 'past_simple': 'built', 'past_participle': 'built'},
    {'base': 'buy', 'past_simple': 'bought', 'past_participle': 'bought'},
    {'base': 'catch', 'past_simple': 'caught', 'past_participle': 'caught'},
    {'base': 'choose', 'past_simple': 'chose', 'past_participle': 'chosen'},
    {'base': 'come', 'past_simple': 'came', 'past_participle': 'come'},
    {'base': 'cost', 'past_simple': 'cost', 'past_participle': 'cost'},
    {'base': 'cut', 'past_simple': 'cut', 'past_participle': 'cut'},
    {'base': 'do', 'past_simple': 'did', 'past_participle': 'done'},
    {'base': 'draw', 'past_simple': 'drew', 'past_participle': 'drawn'},
    {'base': 'drink', 'past_simple': 'drank', 'past_participle': 'drunk'},
    {'base': 'drive', 'past_simple': 'drove', 'past_participle': 'driven'},
    {'base': 'eat', 'past_simple': 'ate', 'past_participle': 'eaten'},
    {'base': 'fall', 'past_simple': 'fell', 'past_participle': 'fallen'},
    {'base': 'feel', 'past_simple': 'felt', 'past_participle': 'felt'},
    {'base': 'fight', 'past_simple': 'fought', 'past_participle': 'fought'},
    {'base': 'find', 'past_simple': 'found', 'past_participle': 'found'},
    {'base': 'fly', 'past_simple': 'flew', 'past_participle': 'flown'},
    {'base': 'forget', 'past_simple': 'forgot', 'past_participle': 'forgotten'},
    {'base': 'get', 'past_simple': 'got', 'past_participle': 'got/gotten'},
    {'base': 'give', 'past_simple': 'gave', 'past_participle': 'given'},
    {'base': 'go', 'past_simple': 'went', 'past_participle': 'gone'},
    {'base': 'have', 'past_simple': 'had', 'past_participle': 'had'},
    {'base': 'hear', 'past_simple': 'heard', 'past_participle': 'heard'},
    {'base': 'hit', 'past_simple': 'hit', 'past_participle': 'hit'},
    {'base': 'hold', 'past_simple': 'held', 'past_participle': 'held'},
    {'base': 'hurt', 'past_simple': 'hurt', 'past_participle': 'hurt'},
    {'base': 'keep', 'past_simple': 'kept', 'past_participle': 'kept'},
    {'base': 'know', 'past_simple': 'knew', 'past_participle': 'known'},
    {'base': 'learn', 'past_simple': 'learned/learnt', 'past_participle': 'learned/learnt'},
    {'base': 'leave', 'past_simple': 'left', 'past_participle': 'left'},
    {'base': 'lend', 'past_simple': 'lent', 'past_participle': 'lent'},
    {'base': 'let', 'past_simple': 'let', 'past_participle': 'let'},
    {'base': 'lose', 'past_simple': 'lost', 'past_participle': 'lost'},
    {'base': 'make', 'past_simple': 'made', 'past_participle': 'made'},
    {'base': 'mean', 'past_simple': 'meant', 'past_participle': 'meant'},
    {'base': 'meet', 'past_simple': 'met', 'past_participle': 'met'},
    {'base': 'pay', 'past_simple': 'paid', 'past_participle': 'paid'},
    {'base': 'put', 'past_simple': 'put', 'past_participle': 'put'},
    {'base': 'read', 'past_simple': 'read', 'past_participle': 'read'},
    {'base': 'ride', 'past_simple': 'rode', 'past_participle': 'ridden'},
    {'base': 'run', 'past_simple': 'ran', 'past_participle': 'run'},
    {'base': 'say', 'past_simple': 'said', 'past_participle': 'said'},
    {'base': 'see', 'past_simple': 'saw', 'past_participle': 'seen'},
    {'base': 'sell', 'past_simple': 'sold', 'past_participle': 'sold'},
    {'base': 'show', 'past_simple': 'showed', 'past_participle': 'shown'},
    {'base': 'sing', 'past_simple': 'sang', 'past_participle': 'sung'},
    {'base': 'sit', 'past_simple': 'sat', 'past_participle': 'sat'},
    {'base': 'sleep', 'past_simple': 'slept', 'past_participle': 'slept'},
    {'base': 'speak', 'past_simple': 'spoke', 'past_participle': 'spoken'},
    {'base': 'spend', 'past_simple': 'spent', 'past_participle': 'spent'},
    {'base': 'stand', 'past_simple': 'stood', 'past_participle': 'stood'},
    {'base': 'steal', 'past_simple': 'stole', 'past_participle': 'stolen'},
    {'base': 'swim', 'past_simple': 'swam', 'past_participle': 'swum'},
    {'base': 'take', 'past_simple': 'took', 'past_participle': 'taken'},
    {'base': 'teach', 'past_simple': 'taught', 'past_participle': 'taught'},
    {'base': 'tell', 'past_simple': 'told', 'past_participle': 'told'},
    {'base': 'think', 'past_simple': 'thought', 'past_participle': 'thought'},
    {'base': 'throw', 'past_simple': 'threw', 'past_participle': 'thrown'},
    {'base': 'understand', 'past_simple': 'understood', 'past_participle': 'understood'},
    {'base': 'wear', 'past_simple': 'wore', 'past_participle': 'worn'},
    {'base': 'win', 'past_simple': 'won', 'past_participle': 'won'},
    {'base': 'write', 'past_simple': 'wrote', 'past_participle': 'written'}
]


class BingoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Irregular Verbs Bingo")

        # Adjust scaling for high DPI displays
        self.scaling_factor = self.root.winfo_fpixels('1i') / 96  # 96 DPI is standard
        self.root.tk.call('tk', 'scaling', self.scaling_factor)

        # Set minimum window size and allow resizing
        base_width = 800
        base_height = 700
        self.root.minsize(int(base_width * self.scaling_factor), int(base_height * self.scaling_factor))

        # Adjust default font sizes
        default_font = tkfont.nametofont("TkDefaultFont")
        default_font.configure(size=int(default_font.cget("size") * self.scaling_factor))

        # Apply theme
        self.style = ttk.Style()
        self.style.theme_use('clam')  # You can choose other themes like 'arc', 'radiance', etc.

        # Set fonts for different elements
        self.header_font = tkfont.Font(family="Helvetica", size=int(24 * self.scaling_factor), weight="bold")
        self.word_font = tkfont.Font(family="Helvetica", size=int(32 * self.scaling_factor), weight="bold")
        self.label_font = tkfont.Font(family="Helvetica", size=int(18 * self.scaling_factor))
        self.listbox_font = tkfont.Font(family="Helvetica", size=int(22 * self.scaling_factor))
        self.timer_font = tkfont.Font(family="DS-Digital", size=int(48 * self.scaling_factor))

        self.selected_form = tk.StringVar()
        self.timer_seconds = tk.IntVar(value=30)  # Default timer value

        # Initialize lists
        self.available_words = []
        self.used_words = []

        # Timer variables
        self.timer_running = False
        self.timer_countdown = 0

        self.create_widgets()

    def create_widgets(self):
        # Create styles
        self.style.configure('Header.TLabel', font=self.header_font)
        self.style.configure('Label.TLabel', font=self.label_font)
        self.style.configure('Timer.TLabel', font=self.timer_font)
        self.style.configure('TButton', font=self.label_font)
        self.style.configure('TEntry', font=self.label_font)
        self.style.configure('TRadiobutton', font=self.label_font)
        self.style.configure('TLabelFrame', font=self.label_font)

        # Header Frame
        header_frame = ttk.Frame(self.root)
        header_frame.pack(pady=int(10 * self.scaling_factor))
        header_label = ttk.Label(header_frame, text="Irregular Verbs Bingo", style='Header.TLabel')
        header_label.pack()

        # Form selection frame
        form_frame = ttk.LabelFrame(self.root, text="Select Verb Form")
        form_frame.pack(pady=int(10 * self.scaling_factor), padx=int(20 * self.scaling_factor), fill="x")
        forms = [("Base Form", "base"), ("Past Simple", "past_simple"), ("Past Participle", "past_participle")]
        for text, value in forms:
            rb = ttk.Radiobutton(form_frame, text=text, variable=self.selected_form, value=value)
            rb.pack(side=tk.LEFT, padx=int(10 * self.scaling_factor), pady=int(5 * self.scaling_factor))

        # Start button
        start_button = ttk.Button(self.root, text="Start Game", command=self.start_game)
        start_button.pack(pady=int(10 * self.scaling_factor))

        # Last drawn word display
        self.last_word_label = tk.Label(self.root, text="", font=self.word_font, fg="blue")
        self.last_word_label.pack(pady=int(10 * self.scaling_factor))

        # Main frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(pady=int(10 * self.scaling_factor), padx=int(20 * self.scaling_factor), fill="both", expand=True)

        # Left column - Available words
        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill="both", expand=True, padx=int(10 * self.scaling_factor))

        left_label = ttk.Label(left_frame, text="Available Words")
        left_label.pack(pady=int(5 * self.scaling_factor))

        self.available_listbox = tk.Listbox(left_frame, font=self.listbox_font)
        self.available_listbox.pack(fill="both", expand=True)

        # Middle frame for buttons
        middle_frame = ttk.Frame(main_frame)
        middle_frame.pack(side=tk.LEFT, fill="y", pady=int(20 * self.scaling_factor))

        # Draw word button
        self.draw_button = ttk.Button(middle_frame, text="Draw Word ▶", command=self.draw_word, state=tk.DISABLED)
        self.draw_button.pack(pady=int(5 * self.scaling_factor))

        # Right column - Used words
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side=tk.LEFT, fill="both", expand=True, padx=int(10 * self.scaling_factor))

        right_label = ttk.Label(right_frame, text="Used Words")
        right_label.pack(pady=int(5 * self.scaling_factor))

        self.used_listbox = tk.Listbox(right_frame, font=self.listbox_font)
        self.used_listbox.pack(fill="both", expand=True)

        # Control frame
        control_frame = ttk.LabelFrame(self.root, text="Timer Controls")
        control_frame.pack(pady=int(10 * self.scaling_factor), padx=int(20 * self.scaling_factor), fill="x")

        # Timer controls
        timer_subframe = ttk.Frame(control_frame)
        timer_subframe.pack(pady=int(5 * self.scaling_factor))

        ttk.Label(timer_subframe, text="Timer (seconds):").pack(side=tk.LEFT)
        self.timer_entry = ttk.Entry(timer_subframe, textvariable=self.timer_seconds, width=5)
        self.timer_entry.pack(side=tk.LEFT, padx=int(5 * self.scaling_factor))
        self.start_timer_button = ttk.Button(timer_subframe, text="Start Timer", command=self.start_timer)
        self.start_timer_button.pack(side=tk.LEFT, padx=int(5 * self.scaling_factor))
        self.stop_timer_button = ttk.Button(timer_subframe, text="Stop Timer", command=self.stop_timer)
        self.stop_timer_button.pack(side=tk.LEFT, padx=int(5 * self.scaling_factor))
        self.reset_timer_button = ttk.Button(timer_subframe, text="Reset Timer", command=self.reset_timer)
        self.reset_timer_button.pack(side=tk.LEFT, padx=int(5 * self.scaling_factor))

        # Stopwatch display
        self.timer_label = tk.Label(control_frame, text="00:00", font=self.timer_font, fg="green")
        self.timer_label.pack(pady=int(10 * self.scaling_factor))

    # Rest of the class methods remain the same
    def start_game(self):
        form = self.selected_form.get()
        if form not in ['base', 'past_simple', 'past_participle']:
            tk.messagebox.showerror("Error", "Please select a verb form.")
            return

        # Reset lists
        self.available_words.clear()
        self.used_words.clear()
        self.last_word_label.config(text="")
        self.update_timer_label(0)

        # Populate available words
        self.available_words = [verb[form] for verb in verbs]
        random.shuffle(self.available_words)

        # Update listboxes
        self.update_available_listbox()
        self.update_used_listbox()

        # Enable draw button
        self.draw_button.config(state=tk.NORMAL)

    def update_available_listbox(self):
        self.available_listbox.delete(0, tk.END)
        for word in self.available_words:
            self.available_listbox.insert(tk.END, word)

    def update_used_listbox(self):
        self.used_listbox.delete(0, tk.END)
        for index, word in enumerate(self.used_words, start=1):
            self.used_listbox.insert(tk.END, f"{index}. {word}")

    def draw_word(self):
        if not self.available_words:
            tk.messagebox.showinfo("Info", "No more words to draw.")
            return
        word = self.available_words.pop(0)
        self.used_words.append(word)
        self.update_available_listbox()
        self.update_used_listbox()

        # Update the last drawn word display
        self.last_word_label.config(text=word.capitalize())

    def start_timer(self):
        if self.timer_running:
            return
        try:
            self.timer_countdown = int(self.timer_entry.get())
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid number of seconds.")
            return
        self.timer_running = True
        self.countdown()

    def stop_timer(self):
        self.timer_running = False

    def reset_timer(self):
        self.stop_timer()
        self.update_timer_label(0)
        self.timer_label.config(fg="green")

    def countdown(self):
        if self.timer_running and self.timer_countdown > 0:
            self.update_timer_label(self.timer_countdown)
            self.timer_countdown -= 1
            self.root.after(1000, self.countdown)
        elif self.timer_running and self.timer_countdown == 0:
            self.update_timer_label(0)
            self.timer_running = False
            self.timer_label.config(fg="red")
            tk.messagebox.showinfo("Timer", "Time's up!")

    def update_timer_label(self, seconds):
        mins = seconds // 60
        secs = seconds % 60
        time_str = f"{mins:02d}:{secs:02d}"
        self.timer_label.config(text=time_str)

        # Change color based on time left
        if seconds > 10:
            self.timer_label.config(fg="green")
        elif 5 < seconds <= 10:
            self.timer_label.config(fg="orange")
        else:
            self.timer_label.config(fg="red")


if __name__ == "__main__":
    # Use ThemedTk for better appearance
    root = ThemedTk(theme="arc")  # You can choose different themes like 'breeze', 'elegance', etc.
    app = BingoApp(root)
    root.mainloop()
