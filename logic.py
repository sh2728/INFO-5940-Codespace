
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
import glob, json

_llm=None; _store=None

def llm():
    global _llm
    if not _llm:
        _llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
    return _llm

def store():
    global _store
    if not _store:
        docs=[]
        for f in glob.glob("rag_data/*.txt"):
            with open(f) as x: docs.append(Document(page_content=x.read()))
        _store = Chroma.from_documents(docs, OpenAIEmbeddings(model="text-embedding-3-small"))
    return _store

def rag(q): return "
".join([d.page_content for d in store().similarity_search(q, k=3)])

def parse_symptom(desc, age, sex):
    p=f"""Extract JSON with: primary, duration, severity, notes.
Symptom: {desc}, Age:{age}, Sex:{sex}"""
    r=llm().invoke([{"role":"user","content":p}]).content
    try:
        js=r[r.find("{"):r.rfind("}")+1]
        return json.loads(js)
    except: return {"primary":"unknown","notes":[]}

def triage_followups(desc, parsed):
    ctx=rag(parsed.get("primary","symptom"))
    prompt=f"""Give 3 short follow-up questions:
Symptom:{desc}
Parsed:{parsed}
Context:{ctx}"""
    r=llm().invoke([{"role":"user","content":prompt}]).content.split("\n")
    return [x.strip("-• ") for x in r if x.strip()][:3]

def assess_case(p):
    ctx=rag(p["parsed"].get("primary","symptom"))
    prompt=f"""Return JSON with:
conditions:[{name,likelihood,reason}],
otc:[{name,info}],
red_flags:[...],
next:"string",
rx:true/false
Profile:{p}
Context:{ctx}"""
    r=llm().invoke([{"role":"user","content":prompt}]).content
    try:
        js=r[r.find("{"):r.rfind("}")+1]
        return json.loads(js)
    except:
        return {"conditions":[],"otc":[],"red_flags":[],"next":"Consult clinician.","rx":False}

def build_packet(p,a):
    return f"""### Prescription Request Packet (Mock)
**Symptom:** {p['desc']}
**Age/Sex:** {p['age']}/{p['sex']}
**Parsed:** {p['parsed']}
**Triage Answers:** {p.get('answers',{})}
**Assessment:** {a}
_Not a diagnosis. For clinician review only._"""
