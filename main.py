import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()   # ✅ MUST be here before imports

from agents.researcher import impact_researcher
from agents.extractor import data_extractor
from agents.writer import brief_writer
import streamlit as st
import os
from dotenv import load_dotenv

# Load .env ONCE here
load_dotenv()

# Debug check
st.write("Groq Key Loaded:", os.getenv("GROQ_API_KEY") is not None)

from agents.researcher import impact_researcher
from agents.extractor import data_extractor
from agents.writer import brief_writer
import streamlit as st
import streamlit as st
from agents.researcher import impact_researcher
from agents.extractor import data_extractor
from agents.writer import brief_writer

st.set_page_config(page_title="Environmental Impact Briefer", layout="wide")

st.title("🌍 Environmental Impact Briefer (Agentic AI)")
st.write("Generate environmental impact reports using multi-agent AI system")

# Input
topic = st.text_input("Enter Topic", placeholder="e.g. Plastic pollution in India")

if st.button("Generate Report"):
    if topic.strip() == "":
        st.warning("Please enter a topic")
    else:
        with st.spinner("🔍 Researching..."):
            research = impact_researcher(topic)

        with st.spinner("📊 Extracting data..."):
            extracted = data_extractor(research)

        with st.spinner("📝 Writing report..."):
            report = brief_writer(extracted, topic)

        st.success("✅ Report Generated!")

        # Show sections
        st.subheader("📄 Final Report")
        st.write(report)

        # Expandable debug sections (very useful for viva)
        with st.expander("🔍 Research Data"):
            st.write(research)

        with st.expander("📊 Extracted Data"):
            st.write(extracted)
            st.write("Tavily Key Loaded:", os.getenv("TAVILY_API_KEY") is not None)