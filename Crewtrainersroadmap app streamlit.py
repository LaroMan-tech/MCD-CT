import streamlit as st

st.set_page_config(page_title="Crewtrainer Roadmap", layout="wide")

# McDonald's lichte kleuren
MCD_YELLOW = "#f7c948"
MCD_GREEN = "#1b5e20"

# Thema-fixes: licht, duidelijke borders en zachte achtergronden
st.markdown(
    f"""
    <style>
        :root {{ color-scheme: light; }}
        body, .stApp, div[data-testid="stAppViewContainer"], div[data-testid="stDecoration"] {{
            background: #ffffff !important;
            color: #0f0f0f !important;
        }}
        h1, h2, h3, h4, p, label, span, div, .stMarkdown {{
            color: #0f0f0f !important;
        }}
        .mcd-header {{
            background: linear-gradient(90deg, {MCD_YELLOW} 0%, {MCD_GREEN} 100%);
            color: #0f0f0f;
            padding: 16px 20px;
            border-radius: 10px;
            font-weight: 700;
            margin-bottom: 12px;
        }}
        /* Inputs en buttons licht */
        .stTextInput input[type="text"],
        .stDateInput input[type="text"],
        div[data-baseweb="input"] input {{
            border: 1.4px solid #cfcfcf !important;
            background: #f8f8fb !important;
            color: #0f0f0f !important;
            border-radius: 8px !important;
            box-shadow: none !important;
        }}
        /* Progress bars groen */
        .stProgress > div > div {{
            background: {MCD_GREEN} !important;
        }}
        /* Checkbox borders donker, achtergrond wit */
        div[data-testid="stCheckbox"] > label {{
            color: #0f0f0f !important;
        }}
        div[role="checkbox"] {{
            border: 1.3px solid #777 !important;
            background: #ffffff !important;
        }}
        button[kind="secondary"] {{
            background: #f7f7fa !important;
            color: #0f0f0f !important;
            border: 1.4px solid #d6d6d6 !important;
            box-shadow: none !important;
        }}
        /* Fase cards */
        .phase-card {{
            border: 1px solid #dcdcdc;
            border-radius: 10px;
            padding: 10px 12px;
            background: #fafafa;
            box-shadow: 0 1px 2px rgba(0,0,0,0.04);
        }}
        /* Step grid */
        .code-box {{
            border: 1px solid #e0c85b;
            background: #fff6d6;
            padding: 10px 12px;
            border-radius: 10px;
            font-weight: 700;
            text-align: center;
        }}
        .desc-box {{
            border: 1px solid #e6e6e6;
            background: #ffffff;
            padding: 10px 12px;
            border-radius: 12px;
        }}
        .desc-praktijk {{ background: #edf8ed; border-color: #8ccf8c; }}
        .desc-theorie {{ background: #eaf2ff; border-color: #8db8ff; }}
        .desc-checkin {{ background: #fff7df; border-color: #ffd86e; }}
        .side-box {{
            border: 1px solid #e6e6e6;
            background: #ffffff;
            padding: 10px 12px;
            border-radius: 10px;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)


# Data: fases en stappen
ROADMAP = [
    {
        "phase": "Fase 1 - Service Expert",
        "steps": [
            {"code": "1.0", "title": "Startgesprek met begeleider", "category": "Check-in"},
            {
                "code": "1.1",
                "title": "Behaal alle service Allround SOC's onaangekondigd 100%",
                "category": "Praktijk",
                "details": [
                    "Expediteur",
                    "Runner presenter",
                    "Beverage & desserts",
                    "McDelivery",
                    "Ordertaker",
                    "Friet",
                    "Raam 2 (Drive zaak)",
                    "Raam 1 (Drive zaak)",
                ],
            },
            {
                "code": "1.2",
                "title": "Behaal de extra SOC's onaangekondigd",
                "category": "Praktijk",
                "details": [
                    "Voorbereiding MPS zone",
                    "Hospitality",
                    "Table Service",
                    "Kiosk coach",
                    "Lobby",
                ],
            },
            {"code": "1.3", "title": "Voortgangsgesprek met begeleider", "category": "Check-in"},
            {
                "code": "1.4",
                "title": "Neem deze learnings door",
                "category": "Theorie",
                "details": [
                    "Een training plannen en invullen in RTS",
                    "Een training niet uitgevoerd in RTS",
                    "De indeling van RTS",
                ],
            },
            {"code": "1.5", "title": "1e aangekondigd SOC's meekijken met CT", "category": "Praktijk"},
            {"code": "1.6", "title": "2e aangekondigd SOC's meekijken met CT", "category": "Praktijk"},
            {"code": "1.7", "title": "1e aangekondigd SOC's zelfstandig met CT", "category": "Praktijk"},
            {"code": "1.8", "title": "Plan de theorie toets in en leer de service expert info", "category": "Theorie"},
            {"code": "1.9", "title": "Maak de service expert toets", "category": "Praktijk"},
            {"code": "1.10", "title": "Service Expert behaald", "category": "Check-in"},
        ],
    },
    {
        "phase": "Fase 1 - Productie Expert",
        "steps": [
            {"code": "1.0", "title": "Startgesprek met begeleider", "category": "Check-in"},
            {
                "code": "1.1",
                "title": "Behaal alle productie Allround SOC's onaangekondigd 100%",
                "category": "Praktijk",
                "details": [
                    "Assembler",
                    "Initiator",
                    "Grill",
                    "Friteuse",
                    "Friet",
                ],
            },
            {
                "code": "1.2",
                "title": "Behaal de extra SOC's onaangekondigd",
                "category": "Praktijk",
                "details": [
                    "Voorbereiding MFY zone",
                    "Dress",
                    "Gluten vrij",
                    "Tempering",
                    "Ontbijt",
                ],
            },
            {"code": "1.3", "title": "Voortgangsgesprek met begeleider", "category": "Check-in"},
            {
                "code": "1.4",
                "title": "Neem deze learnings door",
                "category": "Theorie",
                "details": [
                    "Een training plannen en invullen in RTS",
                    "Een training niet uitgevoerd in RTS",
                    "De indeling van RTS",
                ],
            },
            {"code": "1.5", "title": "1e aangekondigd SOC's meekijken met CT", "category": "Praktijk"},
            {"code": "1.6", "title": "2e aangekondigd SOC's meekijken met CT", "category": "Praktijk"},
            {"code": "1.7", "title": "1e aangekondigd SOC's zelfstandig met CT", "category": "Praktijk"},
            {"code": "1.8", "title": "Plan de theorie toets in en leer de productie expert info", "category": "Theorie"},
            {"code": "1.9", "title": "Maak de productie expert toets", "category": "Praktijk"},
            {"code": "1.10", "title": "Productie Expert behaald", "category": "Check-in"},
        ],
    },
    {
        "phase": "Fase 2 - Learnings en trainen",
        "steps": [
            {"code": "2.1", "title": "Startgesprek met begeleider", "category": "Check-in"},
            {"code": "2.2", "title": "Maak het crewtrainerswerkboek in campus", "category": "Theorie"},
            {"code": "2.3", "title": "Neem de module 'RTS' door", "category": "Theorie"},
            {"code": "2.4", "title": "1e COC SOC met training afname met crewtrainer", "category": "Praktijk"},
            {"code": "2.5", "title": "2e COC SOC met training afname met crewtrainer", "category": "Praktijk"},
            {"code": "2.6", "title": "1e COC SOC zonder training afname met crewtrainer", "category": "Praktijk"},
            {"code": "2.7", "title": "2e COC SOC zonder training afname met crewtrainer", "category": "Praktijk"},
            {"code": "2.8", "title": "Voortgangsgesprek met begeleider", "category": "Check-in"},
            {"code": "2.9", "title": "Neem de module 'Onboarding' door", "category": "Theorie"},
            {"code": "2.10", "title": "1e orientatie training meekijken met CT", "category": "Praktijk"},
            {"code": "2.11", "title": "2e orientatie training meekijken met CT", "category": "Praktijk"},
            {"code": "2.12", "title": "3e orientatie training meekijken met CT", "category": "Praktijk"},
            {"code": "2.13", "title": "1e orientatie training zelfstandig met CT + crewtrainers SOC", "category": "Praktijk"},
            {"code": "2.14", "title": "2e orientatie training zelfstandig met CT + crewtrainers SOC", "category": "Praktijk"},
            {"code": "2.15", "title": "3e orientatie training zelfstandig met CT + crewtrainers SOC", "category": "Praktijk"},
            {"code": "2.16", "title": "Voortgangsgesprek met begeleider", "category": "Check-in"},
            {"code": "2.17", "title": "Neem de module 'Evaluatie' door", "category": "Theorie"},
            {"code": "2.18", "title": "Kijk mee met een evaluatie met CT", "category": "Praktijk"},
            {"code": "2.19", "title": "Neem zelf evaluatie af samen met CT", "category": "Praktijk"},
            {"code": "2.20", "title": "Neem zelf evaluatie af samen met CT (herhaling)", "category": "Praktijk"},
        ],
    },
    {
        "phase": "Fase 3 - Zones en toetsing",
        "steps": [
            {"code": "3.1", "title": "Startgesprek met begeleider", "category": "Check-in"},
            {"code": "3.2", "title": "Neem het MOC 'Productie' door", "category": "Theorie"},
            {"code": "3.3", "title": "Orientatie Productie MOC met een Manager", "category": "Praktijk"},
            {"code": "3.4", "title": "Productie MOC met een Manager", "category": "Praktijk"},
            {"code": "3.5", "title": "Neem het MOC 'MPS' door", "category": "Theorie"},
            {"code": "3.6", "title": "Orientatie MPS MOC met een Manager", "category": "Praktijk"},
            {"code": "3.7", "title": "MPS MOC met een Manager", "category": "Praktijk"},
            {"code": "3.8", "title": "Neem het MOC 'Drive' door", "category": "Theorie"},
            {"code": "3.9", "title": "Orientatie Drive MOC met een Manager", "category": "Praktijk"},
            {"code": "3.10", "title": "Drive MOC met een Manager", "category": "Praktijk"},
            {"code": "3.11", "title": "Neem het HOC", "category": "Theorie"},
            {"code": "3.12", "title": "Orientatie HOC met een Manager", "category": "Praktijk"},
            {"code": "3.13", "title": "HOC met een Manager", "category": "Praktijk"},
            {"code": "3.14", "title": "Voortgangsgesprek met begeleider", "category": "Check-in"},
            {"code": "3.15", "title": "Plannen en leren voor Crewtrainertoets", "category": "Theorie"},
            {"code": "3.16", "title": "Maken crewtrainerstoets", "category": "Theorie"},
            {"code": "3.17", "title": "1e keer oefenen praktijkdag met CT", "category": "Praktijk"},
            {"code": "3.18", "title": "2e keer oefenen praktijkdag met CT", "category": "Praktijk"},
            {"code": "3.19", "title": "3e keer oefenen praktijkdag met begeleider", "category": "Praktijk"},
            {"code": "3.20", "title": "Maken Praktijk met begeleider", "category": "Praktijk"},
            {"code": "3.21", "title": "Officieel Crewtrainer", "category": "Check-in"},
        ],
    },
]


CATEGORY_COLORS = {
    "Praktijk": "#4CAF50",
    "Theorie": "#2196F3",
    "Check-in": "#FFC107",
    "Overig": "#9E9E9E",
}


def badge(text: str, color: str) -> str:
    return f"<span style='background:{color}; color:white; padding:3px 8px; border-radius:6px; font-size:12px;'>{text}</span>"


def init_state():
    if "step_state" not in st.session_state:
        st.session_state.step_state = {}
        for phase in ROADMAP:
            for step in phase["steps"]:
                st.session_state.step_state[f"{phase['phase']}|{step['code']}"] = False
    st.session_state.setdefault("crewtrainer_name", "")
    st.session_state.setdefault("crewtrainer_coach", "")
    st.session_state.setdefault("start_date", None)
    st.session_state.setdefault("end_date", None)


def reset_progress():
    for key in st.session_state.step_state:
        st.session_state.step_state[key] = False


def draw_phase(phase_data):
    phase = phase_data["phase"]
    steps = phase_data["steps"]

    done = sum(
        1 for step in steps if st.session_state.step_state[f"{phase}|{step['code']}"]
    )
    total = len(steps)
    pct = int(round(100 * done / total)) if total else 0

    st.subheader(f"{phase} - {pct}%")
    st.progress(pct / 100)

    for step in steps:
        key = f"{phase}|{step['code']}"
        cat = step.get("category", "Overig")
        color = CATEGORY_COLORS.get(cat, "#9E9E9E")
        desc_class = "desc-box"
        if cat == "Praktijk":
            desc_class += " desc-praktijk"
        elif cat == "Theorie":
            desc_class += " desc-theorie"
        elif cat == "Check-in":
            desc_class += " desc-checkin"

        cols = st.columns([1, 7, 2, 2])
        with cols[0]:
            st.markdown(f"<div class='code-box'>{step['code']}</div>", unsafe_allow_html=True)
        with cols[1]:
            st.markdown(f"<div class='{desc_class}'>", unsafe_allow_html=True)
            st.session_state.step_state[key] = st.checkbox(
                step["title"],
                value=st.session_state.step_state[key],
                key=key,
            )
            st.markdown(badge(cat, color), unsafe_allow_html=True)
            if step.get("details"):
                st.caption("\n".join(f"- {item}" for item in step["details"]))
            st.markdown("</div>", unsafe_allow_html=True)
        with cols[2]:
            st.markdown("<div class='side-box'>", unsafe_allow_html=True)
            st.text_input("Deadline", key=f"deadline-{key}", label_visibility="collapsed", placeholder="Deadline")
            st.markdown("</div>", unsafe_allow_html=True)
        with cols[3]:
            st.markdown("<div class='side-box'>", unsafe_allow_html=True)
            st.text_input("Notitie", key=f"note-{key}", label_visibility="collapsed", placeholder="Notitie")
            st.markdown("</div>", unsafe_allow_html=True)


def main():
    init_state()

    st.title("Crewtrainer Roadmap")
    st.caption("Vink per stap (1.0, 1.1, ...) af om de voortgang te volgen.")

    st.markdown("<div class='mcd-header'>🍔 Crewtrainersroadmap</div>", unsafe_allow_html=True)

    info_cols = st.columns([1, 1, 1, 1])
    with info_cols[0]:
        st.text_input("Naam", key="crewtrainer_name", placeholder="Vul naam in")
    with info_cols[1]:
        st.text_input("Begeleider", key="crewtrainer_coach", placeholder="Vul begeleider in")
    with info_cols[2]:
        st.date_input("Startdatum", key="start_date")
    with info_cols[3]:
        st.date_input("Einddatum", key="end_date")

    top_cols = st.columns([1, 1, 1])
    with top_cols[0]:
        if st.button("Reset alle vinkjes"):
            reset_progress()
            st.success("Alle stappen zijn gereset.")
    with top_cols[1]:
        st.markdown("🍟 McProgress")
    with top_cols[2]:
        total_steps = sum(len(phase["steps"]) for phase in ROADMAP)
        total_done = sum(st.session_state.step_state.values())
        overall_pct = int(round(100 * total_done / total_steps)) if total_steps else 0
        st.metric("Totale voortgang", f"{overall_pct}%", f"{total_done}/{total_steps}")
        st.progress(overall_pct / 100)

    st.markdown("### Voortgang per fase")
    phase_cols = st.columns(len(ROADMAP))
    for col, phase_data in zip(phase_cols, ROADMAP):
        phase = phase_data["phase"]
        steps = phase_data["steps"]
        done = sum(
            1 for step in steps if st.session_state.step_state[f"{phase}|{step['code']}"]
        )
        total = len(steps)
        pct = int(round(100 * done / total)) if total else 0
        with col:
            st.markdown(
                f"""
                <div class="phase-card">
                    <div style="font-weight:600; margin-bottom:4px;">{phase}</div>
                    <div style="font-size:24px; font-weight:800;">{pct}%</div>
                    <div style="font-size:13px; color:{MCD_GREEN};">↑ {done}/{total}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    for phase_data in ROADMAP:
        st.divider()
        draw_phase(phase_data)


if __name__ == "__main__":
    main()
