import streamlit as st

st.set_page_config(page_title="Arwa Salah's Portfolio", layout="wide")

st.title("Power BI Projects 📊")
st.write("Open Projects from URL:")

# ارفعي ملف .pbix على Google Drive أو OneDrive وخدي الرابط
report_url = "https://drive.google.com/uc?export=download&id=1Latfw53WfSD0e8fuGJf_e8XgKQp4hE2O"

st.markdown(f"[اضغط هنا لعرض التقرير التفاعلي]({report_url})", unsafe_allow_html=True)
st.info("يُفضل فتح التقرير باستخدام Power BI Desktop لعرض كامل التفاعل.")
