import random
import time
import streamlit as st

st.set_page_config(page_title="เกมทายศัพท์ภาษาอังกฤษ", page_icon="🐾")
st.title("🐾 เกมทายศัพท์ภาษาอังกฤษ (หมวดสัตว์)")

# 1. รายการคำศัพท์ คีย์คือคำถาม วาลิวคือคำตอบและคำใบ้
WORD_LIST = [
    {"word": "elephant", "hint": "ตัวใหญ่ มีงวง มีงา 🐘"},
    {"word": "giraffe", "hint": "คอยาว ชอบกินใบไม้สูงๆ 🦒"},
    {"word": "penguin", "hint": "นกที่บินไม่ได้ แต่อยู่ในที่เย็นจัด 🐧"},
    {"word": "dolphin", "hint": "สัตว์เลี้ยงลูกด้วยนมในทะเล ฉลาดมาก 🐬"},
    {"word": "rabbit", "hint": "ชอบกินแครอท หูยาว กระโดดไว 🐰"},
]

# 2. ตั้งค่าเริ่มต้นใน Session State
if "quiz" not in st.session_state:
    st.session_state.quiz = random.choice(WORD_LIST)
if "user_ans" not in st.session_state:
    st.session_state.user_ans = ""
if "is_ended" not in st.session_state:
    st.session_state.is_ended = False


# 📌 ฟังก์ชันสุ่มข้อใหม่/เริ่มเกมใหม่
def reset_game():
    st.session_state.quiz = random.choice(WORD_LIST)
    st.session_state.user_ans = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False


# ----------------------------------------------------
# 📌 ฟังก์ชัน Dialog แสดงผลลัพธ์
# ----------------------------------------------------
@st.dialog("📊 ผลการตอบคำถาม")
def show_result_dialog(user_answer, correct_word):
    u_ans = user_answer.strip().lower()

    if u_ans == correct_word:
        st.balloons()
        st.success("🎉 ถูกต้องแล้วครับ! คุณเก่งมาก!")
    else:
        st.error(f"❌ ยังไม่ถูกต้องนะ! คำตอบที่ถูกต้องคือ '**{correct_word}**'")

    if st.button("🔄 เล่นข้อถัดไป"):
        reset_game()
        st.rerun()


# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่น / สุ่มข้อใหม่
# ----------------------------------------------------
st.button("🎮 สุ่มคำศัพท์ใหม่", on_click=reset_game)

# 2. แถบแสดงเวลานับถอยหลัง (ให้เวลา 20 วินาที)
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(20 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.warning(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# 3. แสดงคำใบ้และช่องกรอกคำตอบ
quiz = st.session_state.quiz
st.subheader(f"💡 คำใบ้: {quiz['hint']}")

ans = st.text_input(
    "พิมพ์คำศัพท์ภาษาอังกฤษที่ถูกต้อง:",
    value=st.session_state.user_ans,
    placeholder="เช่น cat, dog...",
)
st.session_state.user_ans = ans

# 4. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()

# 5. แสดง Dialog ผลลัพธ์เมื่อกดส่งหรือหมดเวลา
if st.session_state.get("is_ended", False):
    show_result_dialog(ans, quiz["word"])

st.divider()
st.write("กลุ่ม1 นาย ภูริช เอกสุธรรม ม.4/9 เลขที่ 5
                น.ส.ศตกมลฉัฏ ศรีสามยอด ม.4/9 เลขที่ 28
                น.ส.ภิรัญญา เจียเจริญตระกูล ม.4/9 เลขที่ 41
                น.ส.ปปิยะ สุริยันต์ ม.4/9 เลขที่ 43 ")
