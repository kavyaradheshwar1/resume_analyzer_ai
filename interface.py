import streamlit as st 

#refer analysis.py file
from analysis import analyze_resume

st.set_page_config(page_title='CV Analyzer')

st.title('RESUME ANALYZER USING AI 🤖🧠🇦🇮👾')

st.subheader('''This page helps you to compare your resume with the given Job Description''')

st.sidebar.subheader('Drop your resume here ⬇️')
pdf_doc = st.sidebar.file_uploader('Click here to browse', type = ['pdf'])

st.sidebar.markdown('Designed by Kavya Radheshwar')
st.sidebar.markdown('Github : https://github.com/kavyaradheshwar1')

job_des = st.text_area('Copy and paste JD here👉',max_chars=10000)
submit = st.button('Generate Score📊')

if submit:
    with st.spinner('Getting results....'):
        analyze_resume(pdf_doc,job_des)
    
    