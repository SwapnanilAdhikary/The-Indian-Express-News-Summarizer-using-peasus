from extractor import get_news
from summarizer import generate_summary
import streamlit as st
st.image("img.png")
st.title("news summarizer")
st.info("for now its only available on the indian express")

URL = st.text_input("Enter URL to fetch news:")
if st.button("summarize news"):
    if URL:
        news = get_news(URL)
        if news:
            st.subheader("heres the news summary")
            st.write(generate_summary(news))
    else:
        st.warning("please enter url")

