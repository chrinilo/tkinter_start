import tkinter as tk
import random
from deep_translator import GoogleTranslator
import pyttsx3

# --- Initialize TTS engine ---
tts_engine = pyttsx3.init()

# --- Lists ---
adjektiver = []
substantiver = []


# --- TTS helper ---
def les_historie():
    """Reads aloud whatever text is currently displayed in tekstboks."""
    current_text = tekstboks.get("1.0", tk.END).strip()
    if not current_text:
        return
    tts_engine.say(current_text)
    tts_engine.runAndWait()


# --- Functions ---


def legg_til_adjektiv():
    if len(adjektiver) >= 3:
        tekstboks.delete("1.0", tk.END)
        tekstboks.insert(tk.END, "⚠️ Maks 3 adjektiv tillatt!")
        return
    adj = adj_input.get().strip()
    if not adj:
        return
    adjektiver.append(adj)
    adj_input.delete(0, tk.END)
    oppdater_adjektiv_liste()
    tekstboks.delete("1.0", tk.END)


def legg_til_substantiv():
    if len(substantiver) >= 3:
        tekstboks.delete("1.0", tk.END)
        tekstboks.insert(tk.END, "⚠️ Maks 3 substantiv tillatt!")
        return
    sub = sub_input.get().strip()
    if not sub:
        return
    substantiver.append(sub)
    sub_input.delete(0, tk.END)
    oppdater_substantiv_liste()
    tekstboks.delete("1.0", tk.END)


def oppdater_adjektiv_liste():
    adj_listeboks.delete(0, tk.END)
    for i, a in enumerate(adjektiver, start=1):
        adj_listeboks.insert(tk.END, f"{i}. {a}")


def oppdater_substantiv_liste():
    sub_listeboks.delete(0, tk.END)
    for i, s in enumerate(substantiver, start=1):
        sub_listeboks.insert(tk.END, f"{i}. {s}")


def generer_historie():
    if len(adjektiver) < 3 or len(substantiver) < 3:
        tekstboks.delete("1.0", tk.END)
        tekstboks.insert(
            tk.END, "⚠️ Du må ha minst 3 adjektiv og 3 substantiv i listene!"
        )
        return

    global historie, oversatt, er_engelsk # type:ignore
    adj = adjektiver.copy()
    sub = substantiver.copy()

    historier = [
        f"Det var en {adj[0]} dag i byen. En {adj[1]} {sub[0]} løp forbi mens en {adj[2]} {sub[1]
        }blåste gjennom gatene. Folk stoppet opp og lurte på hva som egentlig foregikk.",
        f"I et {adj[0]} {sub[0]} langt borte bodde en {adj[1]} {sub[1]} med et {adj[2]
        } {sub[2]}. Ingen turte å nærme seg portene.",
        f"På en {adj[0]} {sub[0]} fant en {adj[1]} {sub[1]} en {adj[2]} {sub[2]
        }. Ryktene spredte seg raskt gjennom landsbyen.",
    ]

    historie = random.choice(historier)
    oversatt = ""
    er_engelsk = False

    tekstboks.delete("1.0", tk.END)
    tekstboks.insert(tk.END, historie)
    oversett_knapp.config(text="Oversett til engelsk")


def bytt_oversettelse():
    global er_engelsk, oversatt
    if not historie:
        tekstboks.delete("1.0", tk.END)
        tekstboks.insert(tk.END, "⚠️ Du må generere en historie først!")
        return

    try:
        if not er_engelsk:
            oversatt = GoogleTranslator(source="no", target="en").translate(historie)
            tekstboks.delete("1.0", tk.END)
            tekstboks.insert(tk.END, oversatt)
            oversett_knapp.config(text="Oversett til norsk")
            er_engelsk = True
        else:
            norsk = GoogleTranslator(source="en", target="no").translate(oversatt)
            tekstboks.delete("1.0", tk.END)
            tekstboks.insert(tk.END, norsk)
            oversett_knapp.config(text="Oversett til engelsk")
            er_engelsk = False
    except Exception as e:
        tekstboks.delete("1.0", tk.END)
        tekstboks.insert(tk.END, f"⚠️ Oversettelsen feilet: {e}")


def randomiser_historie():
    if len(adjektiver) < 3 or len(substantiver) < 3:
        tekstboks.delete("1.0", tk.END)
        tekstboks.insert(
            tk.END, "⚠️ Du må ha minst 3 adjektiv og 3 substantiv i listene!"
        )
        return
    random.shuffle(adjektiver)
    random.shuffle(substantiver)
    oppdater_adjektiv_liste()
    oppdater_substantiv_liste()
    generer_historie()


# --- GUI ---
root = tk.Tk()
root.title("Adjektiv- og Substantivfortelling med TTS")

historie = ""
oversatt = ""
er_engelsk = False

# Inputfelt for adjektiv
adj_frame = tk.Frame(root)
adj_frame.pack(pady=5)
adj_input = tk.Entry(adj_frame, width=20)
adj_input.grid(row=0, column=0, padx=5)
legg_til_adj_btn = tk.Button(
    adj_frame, text="Legg til adjektiv", command=legg_til_adjektiv
)
legg_til_adj_btn.grid(row=0, column=1, padx=5)

# Listeboks for adjektiv
adj_listeboks = tk.Listbox(root, width=50, height=3)
adj_listeboks.pack(pady=5)

# Inputfelt for substantiv
sub_frame = tk.Frame(root)
sub_frame.pack(pady=5)
sub_input = tk.Entry(sub_frame, width=20)
sub_input.grid(row=0, column=0, padx=5)
legg_til_sub_btn = tk.Button(
    sub_frame, text="Legg til substantiv", command=legg_til_substantiv
)
legg_til_sub_btn.grid(row=0, column=1, padx=5)

# Listeboks for substantiv
sub_listeboks = tk.Listbox(root, width=50, height=3)
sub_listeboks.pack(pady=5)

# Knappene for generering og oversettelse
knapp_frame = tk.Frame(root)
knapp_frame.pack(pady=10)

generer_knapp = tk.Button(
    knapp_frame, text="Generer historie", command=generer_historie, bg="lightblue"
)
generer_knapp.grid(row=0, column=0, padx=5)

oversett_knapp = tk.Button(
    knapp_frame, text="Oversett til engelsk", command=bytt_oversettelse, bg="lightgreen"
)
oversett_knapp.grid(row=0, column=1, padx=5)

random_knapp = tk.Button(
    knapp_frame, text="🎲 Randomiser", command=randomiser_historie, bg="orange"
)
random_knapp.grid(row=0, column=2, padx=5)

les_btn = tk.Button(
    knapp_frame, text="🔊 Les historien", command=les_historie, bg="lightyellow"
)
les_btn.grid(row=0, column=3, padx=5)

# Tekstboks for historie
tekstboks = tk.Text(root, width=60, height=8, wrap="word")
tekstboks.pack(padx=10, pady=10)

root.mainloop()
