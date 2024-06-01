import streamlit as st
import os
from streamlit_pdf_viewer import pdf_viewer
import time

main_folder_path = os.listdir("certificates")
st.subheader("Collection of links to :green[DataCamp] certificates that I(:blue[Thu Ta]) has achieved")
for i, f in enumerate(main_folder_path):
    st.write(f"{i+1}. {f.rstrip('.pdf')}")
    time.sleep(0.5)
    pdf_viewer(f"certificates/{f}")
