import streamlit as st
from agent import app

st.set_page_config(page_title="НВТП AI Assistant")

st.title("AI Помощник преподавателя НВТП")

user_task = st.text_area(
    "Введите задачу",
    placeholder="Например: Создай тест по военной топографии"
)

if st.button("Сгенерировать"):

    result = app.invoke({
        "task": user_task
    })

    st.subheader("Ответ AI")
    st.write(result["result"])