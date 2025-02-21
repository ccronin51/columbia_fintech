# Imports
import streamlit as st
from dataclasses import dataclass
from datetime import datetime
from typing import Any

@dataclass

@dataclass
class Block:
    data: Any
    creator_id: int
    timestamp: str = datetime.utcnow().strftime("%H:%M:%S")

input_data = st.text_input("Block Data")

if st.button("Add Block"):
    new_block = Block(data=input_data, creator_id=42)
    st.write(new_block)
