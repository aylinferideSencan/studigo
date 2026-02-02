import streamlit as st

st.set_page_config(page_title="Studigo", layout="centered")

st.title("📚 Studigo")
st.subheader("Sen çalış, planı biz yapalım")
st.write("Hoş geldin Aylin 💙")
motivation = [
    "Harika gidiyorsun Aylin 💙",
    "Birazdan çok daha iyi hissedeceksin ✨",
    "Devam et, bu disiplin seni çok ileri götürecek 🚀",
    "Kendinle gurur duy 👏"
]

# SESSION STATE
if "step" not in st.session_state:
    st.session_state.step = 1

# 1️⃣ ADIM – BİLGİ TOPLAMA
if st.session_state.step == 1:
    exam = st.selectbox(
        "🎯 Hangi sınava hazırlanıyorsun?",
        ["KPSS", "ALES", "IELTS", "YDS"]
    )

    hours = st.slider(
        "⏰ Günlük kaç saat çalışabilirsin?",
        1, 24, 6
    )

    if hours > 10:
        st.warning("⚠️ 10 saat üzeri çalışmalarda mutlaka mola planla 💙")

    if st.button("📅 Çalışma Planı Oluştur"):
        st.session_state.exam = exam
        st.session_state.hours = hours
        st.session_state.step = 2
        st.rerun()

# 2️⃣ ADIM – PLAN GÖSTERİMİ
if st.session_state.step == 2:
    exam = st.session_state.exam
    hours = st.session_state.hours

    st.success(f"📌 Sınav: {exam}")
    st.write(f"⏱️ Günlük toplam süre: **{hours} saat**")
    st.write("### 🧠 Akıllı Ders Dağılımı")

    if exam == "ALES":
        st.write(f"- Sayısal: **{hours * 0.5:.1f} saat**")
        st.write(f"- Sözel: **{hours * 0.3:.1f} saat**")
        st.write(f"- Mantık & Hız: **{hours * 0.2:.1f} saat**")

    if st.button("🔄 Planı Değiştir"):
        st.session_state.step = 1
        st.rerun()

import time
import random

st.divider()
st.subheader("⏳ Pomodoro Modu")

pomodoro_minutes = 25
break_minutes = 5

if st.button("▶️ Pomodoro Başlat"):
    st.info("🎯 Odaklan! Çalışma başladı")

    for i in range(pomodoro_minutes * 60):
        time.sleep(1)

    st.success("✅ Pomodoro bitti! Mola zamanı ☕")

    motivation = [
        "Harika gidiyorsun Aylin 💙",
        "Birazdan çok daha iyi hissedeceksin ✨",
        "Devam et, bu disiplin seni çok ileri götürecek 🚀",
        "Kendinle gurur duy 👏"
    ]

    st.info(random.choice(motivation))

st.divider()
st.subheader("📌 Bugün Buna Çalış")

if exam == "IELTS":
    today_focus = random.choice([
        "📖 Reading – True/False/Not Given",
        "✍️ Writing Task 1",
        "🎧 Listening – Section 2",
        "🗣️ Speaking – Part 2"
    ])

elif exam == "ALES":
    today_focus = random.choice([
        "➗ Sayısal – Problemler",
        "📐 Mantık Soruları",
        "📘 Sözel – Paragraf"
    ])

elif exam == "KPSS":
    today_focus = random.choice([
        "🌍 Tarih – İnkılap",
        "📊 Matematik – Temel Problemler",
        "📚 Türkçe – Anlam Bilgisi"
    ])
elif exam == "YDS":
    today_focus = random.choice([
        "📘 Kelime – Phrasal Verbs",
        "📗 Dil Bilgisi – Tense & Passive",
        "📖 Reading – Uzun Paragraf",
        "🧠 Çıkmış YDS Soruları",
        "📝 Çeviri – TR → EN"
    ])

elif exam == "YDS":
    st.write(f"- Kelime & Dil Bilgisi: **{hours * 0.4:.1f} saat**")
    st.write(f"- Reading: **{hours * 0.4:.1f} saat**")
    st.write(f"- Çıkmış Sorular & Çeviri: **{hours * 0.2:.1f} saat**")

st.success(f"👉 **{today_focus}**")
motivation.extend([
    "Bu kelimeler sınavda karşına çıkacak 👀",
    "Reading zor ama sen daha zorsun 💪",
    "Bir paragraf daha = bir net daha 📈"
])
