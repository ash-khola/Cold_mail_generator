import os
os.environ["USER_AGENT"] = "ColdMailBot/1.0"
import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
import re
from chains import Chain
from portfolio import Portfolio
from utils import clean_text

def create_streamlit_app(llm, portfolio, clean_text):
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h1 style='text-align: center;'>📧 Cold Mail Generator</h1>", unsafe_allow_html=True)
        url_input = st.text_input("🔗 Enter Job URL", value="https://jobs.nike.com/job/R-33460")
        submit_button = st.button("🚀 Generate Email")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            if jobs:
                job = jobs[0]  # Only take the first job
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                # st.json(job)  # This will show extracted job dict
                email = llm.write_mail(job, links)
                st.markdown(f"""
                    <div style="
                        border: 1px solid #ccc;
                        padding: 20px;
                        border-radius: 8px;
                        text-align: left;
                        white-space: pre-wrap;
                        position: relative;
                        background-color: #1e1e1e;
                        color: white;
                    ">
                        <button onclick="navigator.clipboard.writeText(document.getElementById('email-content').innerText); this.innerText='✅ Copied!'; setTimeout(() => this.innerText='📋 Copy', 1500);"
                            style="
                                width: 60px;
                                position: absolute;
                                top: 10px;
                                right: 10px;
                                background-color: #2a2a2a;
                                color: #ccc;
                                border: 1px solid #555;
                                padding: 4px 10px;
                                font-size: 12px;
                                border-radius: 4px;
                                cursor: pointer;
                                transition: all 0.2s ease-in-out;
                            "
                            onmouseover="this.style.backgroundColor='#444'; this.style.color='white';"
                            onmouseout="this.style.backgroundColor='#2a2a2a'; this.style.color='#ccc';"
                        >
                            📋 Copy
                        </button>
                        <div id="email-content">{email}</div>
                    </div>
                """, unsafe_allow_html=True)

                # Hidden native st.code() for fallback copy support
                # To remove the repetition just comment out below 3 lines
                st.markdown('<div style="height: 0; overflow: hidden;">', unsafe_allow_html=True)
                st.code(email, language='text')
                st.markdown('</div>', unsafe_allow_html=True)

            else:
                st.warning("No jobs found on the provided URL.")

        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    st.markdown("""
        <style>
            .block-container {
                background-color: #f5f5f5;;
            }
            <div class = block-container st-emotion-cache-1jicfl2 ea3mdgi5>
            
        </style>
        """, unsafe_allow_html=True)
    create_streamlit_app(chain, portfolio, clean_text)


