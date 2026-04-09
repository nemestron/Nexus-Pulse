import streamlit as st
import sys
import os
import json
import uuid

# Ensure the src directory is in the system path for module resolution
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src.graph_engine import app

# UI Configuration
st.set_page_config(page_title="Nexus-Pulse Command Center", layout="wide")
st.title("Nexus-Pulse Autonomous Command Center")
st.markdown("---")

# Session State Initialization (Autonomous Thread Locking)
if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())
if "pending_approval" not in st.session_state:
    st.session_state.pending_approval = False
if "graph_state" not in st.session_state:
    st.session_state.graph_state = None

# Interface Layout
col1, col2 = st.columns([1, 2])

with col1:
    st.header("Mission Parameters")
    target_topic = st.text_input("Intelligence Target Topic", value="Quantum Computing Breakthroughs")
    
    config = {"configurable": {"thread_id": st.session_state.thread_id}}

    if st.button("Initialize Pipeline"):
        # Generate a fresh UUID for every single run to guarantee data isolation
        st.session_state.thread_id = str(uuid.uuid4())
        config = {"configurable": {"thread_id": st.session_state.thread_id}}
        
        st.session_state.pending_approval = False
        st.session_state.graph_state = None
        
        with st.spinner("Executing Autonomous Traversal..."):
            initial_state = {"topic": target_topic, "draft": "", "verified": False}
            
            try:
                for output in app.stream(initial_state, config=config):
                    pass 
                
                current_state = app.get_state(config)
                if current_state.next:
                    st.session_state.pending_approval = True
                    st.session_state.graph_state = current_state.values
                    st.rerun()
                    
            except Exception as e:
                st.error(f"Pipeline Execution Error: {str(e)}")
                
    # --- UI Branding and External Routing Integration ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("### Broadcast Network")
    st.markdown("<a href='https://t.me/NexusPulseNews' target='_blank' style='text-decoration: none; font-weight: bold; color: #0088cc;'>Join the Telegram Channel</a>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("**Created by - Dhiraj Malwade**")
    
    # HTML injection for hyperlinked external SVG logos
    logo_html = """
    <div style="display: flex; gap: 15px; margin-top: 10px;">
        <a href="https://www.linkedin.com/in/dhiraj-malwade-6a8385399/" target="_blank">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linkedin/linkedin-original.svg" width="35" height="35" alt="LinkedIn">
        </a>
        <a href="https://github.com/nemestron/Nexus-Pulse" target="_blank">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original.svg" width="35" height="35" alt="GitHub" style="filter: invert(1);">
        </a>
    </div>
    """
    st.markdown(logo_html, unsafe_allow_html=True)

with col2:
    st.header("Telemetry & Output")
    
    if st.session_state.pending_approval:
        st.info("HUMAN-IN-THE-LOOP AUTHORIZATION REQUIRED")
        
        state_dict = st.session_state.graph_state
        draft_content = "Unable to parse state."
        
        if state_dict:
            if "finalized_draft" in state_dict and state_dict["finalized_draft"]:
                draft_content = state_dict["finalized_draft"]
            elif "draft" in state_dict and state_dict["draft"]:
                draft_content = state_dict["draft"]
            else:
                draft_content = json.dumps(state_dict, indent=2, default=str)
                
        st.markdown("### Pending Intelligence Draft")
        st.markdown(draft_content)
        
        if st.button("Authorize Dissemination", type="primary"):
            with st.spinner("Transmitting Payload to Target Network..."):
                try:
                    for output in app.stream(None, config=config):
                        pass
                    st.success("[OPERATION SUCCESS] Payload Authorized and Delivered.")
                    st.session_state.pending_approval = False
                except Exception as e:
                    st.error(f"Transmission Error: {str(e)}")
    else:
        st.write("System Idle. Awaiting mission parameters.")