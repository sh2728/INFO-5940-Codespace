
import streamlit as st
from logic import parse_symptom, triage_followups, assess_case, build_packet

st.set_page_config(page_title="Triage Assistant", layout="centered")

def nav(page): st.session_state.page = page

if "page" not in st.session_state: st.session_state.page="home"
if "profile" not in st.session_state: st.session_state.profile={}
if "assessment" not in st.session_state: st.session_state.assessment=None

# ---- Pages ----
def home():
    st.title("💊 Lightweight AI Triage Assistant")
    st.write("Enter symptoms → answer questions → get OTC & red-flag guidance.")
    if st.button("Start"): nav("intake")

def intake():
    st.header("Symptom Intake")
    desc = st.text_area("Describe your symptom:")
    age = st.selectbox("Age group", ["18-30","31-50","51-65","66+"])
    sex = st.selectbox("Sex assigned at birth", ["Male","Female","Other"])
    if st.button("Continue"):
        if not desc: st.warning("Enter symptom."); return
        st.session_state.profile={
            "desc":desc, "age":age, "sex":sex,
            "parsed": parse_symptom(desc, age, sex)
        }
        nav("triage")
    if st.button("Back"): nav("home")

def triage():
    st.header("Triage Questions")
    p = st.session_state.profile
    qs = triage_followups(p["desc"], p["parsed"])
    answers={}
    for i,q in enumerate(qs):
        answers[str(i)] = st.text_input(q, key=f"q{i}")
    if st.button("Assess"):
        p["answers"]=answers
        st.session_state.assessment = assess_case(p)
        nav("assessment")
    if st.button("Back"): nav("intake")

def assessment():
    a = st.session_state.assessment
    st.header("Assessment")
    st.subheader("Possible Conditions")
    for c in a["conditions"]:
        st.write(f"- **{c['name']}** ({c['likelihood']}): {c['reason']}")
    if a["red_flags"]:
        st.subheader("🚨 Red Flags")
        for r in a["red_flags"]: st.write(f"- {r}")
    st.subheader("OTC Options")
    for m in a["otc"]:
        st.write(f"**{m['name']}** - {m['info']}")
    st.write("Next steps:", a["next"])
    if a["rx"]:
        if st.button("Generate Clinician Packet"): nav("packet")
    if st.button("Back"): nav("triage")

def packet():
    st.header("Clinician Packet")
    p = st.session_state.profile
    a = st.session_state.assessment
    st.markdown(build_packet(p,a))
    if st.button("Back"): nav("assessment")

# ---- Router ----
page = st.session_state.page
{"home":home,"intake":intake,"triage":triage,"assessment":assessment,"packet":packet}[page]()
