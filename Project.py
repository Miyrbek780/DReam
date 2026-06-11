import streamlit as st

# Ishtirokchilar ro'yxatini sessiyada saqlaymiz (Streamlit har safar yangilanganida o'chib ketmasligi uchun)
if "participants" not in st.session_state:
    st.session_state.participants = []

st.title("🏆 Ishtirokchilar Reyting Tizimi")

# 1. Ishtirokchi qo'shish qismi
st.header("👤 Yangi ishtirokchi qo'shish")
name = st.text_input("Ishtirokchi ismini kiriting:")
score_input = st.text_input("Ball kiriting:")

if st.button("Qo'shish"):
    if name and score_input:
        try:
            score = float(score_input)
            st.session_state.participants.append({"name": name, "score": score})
            st.success(f"{name} muvaffaqiyatli qo'shildi!")
        except ValueError:
            st.error("Xato! Ball faqat son bo'lishi kerak.")
    else:
        st.warning("Iltimos, barcha maydonlarni to'ldiring.")

st.markdown("---")

# 2. Reytingni ko'rsatish qismi
st.header("📊 Ishtirokchilar reytingi")
if len(st.session_state.participants) == 0:
    st.info("Hech qanday ishtirokchi yo'q.")
else:
    ranking = sorted(st.session_state.participants, key=lambda x: x["score"], reverse=True)
    for rank, p in enumerate(ranking, start=1):
        st.write(f"**{rank}. {p['name']}** - {p['score']} ball")

st.markdown("---")

# 3. G'olibni ko'rsatish qismi
st.header("🥇 Musobaqa G'olibi")
if len(st.session_state.participants) == 0:
    st.info("G'olibni aniqlash uchun ishtirokchilar yetarli emas.")
else:
    champion = max(st.session_state.participants, key=lambda x: x["score"])
    st.latex(r"\text{G'olib: } " + champion['name'] + r" \rightarrow " + str(champion['score']) + r"\text{ ball}")
