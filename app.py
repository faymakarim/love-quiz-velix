import streamlit as st
from datetime import datetime

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(page_title="Love Reflection Quiz", page_icon="❤️", layout="centered")

# ----------------------------
# STYLE
# ----------------------------
st.markdown("""
    <style>
    body {
        background-color: #800000;
        color: white;
        font-family: 'Montserrat', sans-serif;
    }
    .stButton>button {
        background-color: white;
        color: black;
        border-radius: 10px;
        padding: 8px 16px;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #f0f0f0;
        color: black;
    }
    .question {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# DATA QUIZ
# ----------------------------
questions = [
    ("Hal pertama yang kamu lakuin kalau kita sendirian berdua setelah LDR selesai?",
     ["Peluk kamu erat-erat sampe kamu susah lepas", "Minta makan dulu", "Tidur sendirian dulu ah"],
     "Peluk kamu erat-erat sampe kamu susah lepas"),
    ("Tempat paling pengen kamu… ehem… cuddle sama aku?",
     ["Your bed HAHAHA", "Mall favorit kita", "Kamar mandi umum (gila lu)"],
     "Your bed HAHAHA"),
    ("Hal paling bikin kamu kangen pas kita video call malem-malem?",
     ["Junior", "Kipas angin", "Lampu kamarmu"],
     "Junior"),
    ("Apa hal paling nakal yang pernah kepikiran kamu pas inget aku?",
     ["Sleep beside u and kiss u passionatly", "Nyolong charger kamu", "Ngeliatin kamu makan"],
     "Sleep beside u and kiss u passionatly"),
    ("Makanan yang kamu pengen kita makan berdua di kasur?",
     ["KAMUU HAHAHA", "Sashimi", "Burger pinggir jalan"],
     "KAMUU HAHAHA"),
    ("Kalau kita liburan bareng di hotel, hal pertama yang kamu lakuin?",
     ["Pelukan?", "Buka koper dulu", "Pesan room service dulu"],
     "Pelukan?"),
    ("Kalau aku bisik ke telinga kamu 'I miss you', respon kamu?",
     ["Bisik balik 'I miss you more' sambil peluk", "Diam aja", "Pura-pura nggak denger"],
     "Bisik balik 'I miss you more' sambil peluk"),
    ("Apa hal paling bikin kamu melt pas aku deketin muka kamu?",
     ["Cara kamu liatin aku sebelum cium", "Bau parfum kamar", "Laptop kamu di meja"],
     "Cara kamu liatin aku sebelum cium"),
    ("Kalau kita bisa pilih satu hari buat nggak keluar kamar, kamu mau ngapain?",
     ["Cuddle + binge nonton film sambil peluk", "Tidur masing-masing pojokan", "Bersih-bersih kamar doang"],
     "Cuddle + binge nonton film sambil peluk"),
    ("Hal random paling bikin kamu jatuh cinta sama aku lagi dan lagi?",
     ["Cara kamu bikin aku ketawa pas malem-malem call", "Cara kamu buka pintu", "Cara kamu geser kursi"],
     "Cara kamu bikin aku ketawa pas malem-malem call"),
]

# ----------------------------
# STATE
# ----------------------------
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
    st.session_state.score = 0

# ----------------------------
# OPENING
# ----------------------------
if st.session_state.current_q == 0:
    st.image("foto_opening.png", width=250)
    st.markdown("<h3 style='text-align:center;'>10 Questions for Pluppie ❤️</h3>", unsafe_allow_html=True)
    if st.button("Start Quiz"):
        st.session_state.current_q = 1
        st.rerun()

# ----------------------------
# QUIZ
# ----------------------------
elif 1 <= st.session_state.current_q <= len(questions):
    idx = st.session_state.current_q - 1
    q, options, answer = questions[idx]

    st.markdown(f"<div class='question'>{q}</div>", unsafe_allow_html=True)
    choice = st.radio("Pilih jawabanmu:", options)

    if st.button("Kirim Jawaban"):
        if choice == answer:
            st.success("Siap sayang bener 😘")
            st.session_state.score += 1
        else:
            st.error("GA DIKASIH JATAH YA WLEE 😜")

        st.session_state.current_q += 1
        st.rerun()

    st.markdown(f"**Skor:** {st.session_state.score}/{len(questions)}")

# ----------------------------
# HASIL AKHIR
# ----------------------------
else:
    st.balloons()  # animasi confetti
    st.markdown("## I LOVE U SAYANG 🤍")
    st.write("""
    Thank you for being a boyfriend yang sabar,
    yang selalu ada walau kita jauh.
    Aku bersyukur banget sama kamu — ga sabar buat ketemu lagi dan peluk kamu lama-lama.
    """)

    # Tambahkan galeri foto di akhir
    st.markdown("### Our Memories ❤️")
    st.image(["foto2.png", "foto3.png"], width=250, caption=["Memory 1", "Memory 2"])

    # Countdown
    target_date = datetime(2025, 8, 18)
    now = datetime.now()
    delta = target_date - now
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    st.markdown(f"**Countdown ke 18 Agustus 2025:** {days} hari, {hours} jam, {minutes} menit, {seconds} detik ❤️**")
