import streamlit as st
import requests
import pandas as pd
import io

API_URL = "https://flaskapi-1-04g0.onrender.com"

st.set_page_config(page_title="🧠 AI Smart Question Generator", page_icon="🧠", layout="wide")
st.title("🧠 AI Smart Question Generator")
st.write("Upload a PDF or paste text to generate intelligent questions, difficulty levels, and short answers.")

uploaded_file = st.file_uploader("📄 Upload a PDF", type=["pdf"])
text_input = st.text_area("✏️ Or paste your text here:")
num_questions = st.slider("Number of questions", 3, 10, 5)

if st.button("🚀 Generate Questions"):
    if not uploaded_file and not text_input.strip():
        st.warning("Please upload a PDF or enter text.")
    else:
        with st.spinner("Generating questions..."):
            # ✅ Convert Streamlit file to bytes manually
            files = None
            data = {"text": text_input, "num_questions": num_questions}

            if uploaded_file is not None:
                pdf_bytes = uploaded_file.read()
                files = {"file": ("uploaded.pdf", io.BytesIO(pdf_bytes), "application/pdf")}

            try:
                response = requests.post(API_URL, files=files, data=data)
            except Exception as e:
                st.error(f"Connection failed: {e}")
                st.stop()

            if response.status_code == 200:
                data = response.json().get("questions", [])
                if data:
                    st.success(f"✅ Generated {len(data)} Questions")

                    for i, q in enumerate(data, 1):
                        st.markdown(f"**{i}. {q['question']} ({q['difficulty']})**")
                        st.write(f"🧩 *Answer:* {q['answer']}")
                        st.markdown("---")

                    # Allow CSV export
                    df = pd.DataFrame(data)
                    csv = df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="📥 Download CSV",
                        data=csv,
                        file_name="questions.csv",
                        mime="text/csv",
                    )
                else:
                    st.warning("No questions generated.")
            else:
                st.error(f"Error: {response.text}")

