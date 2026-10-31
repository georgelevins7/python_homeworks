"""Streamlit frontend for the existing Multi-Agent Travel Planner API."""

import os

import requests
import streamlit as st

API_URL = os.getenv("TRAVEL_API_URL", "http://127.0.0.1:8000/travel")

st.set_page_config(
    page_title="Atlas · AI Travel Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(ellipse at 80% 0%, #172a40 0%, #0d1726 38%, #0a1220 85%);
        color: #edf3fa;
    }
    .block-container { max-width: 1100px; padding-top: 3rem; padding-bottom: 5rem; }
    .eyebrow { color: #79c9c0; font-size: .77rem; font-weight: 700; letter-spacing: .19em; text-transform: uppercase; }
    .hero { font-size: clamp(2.6rem, 5vw, 4.6rem); font-weight: 800; line-height: 1.08; letter-spacing: -.045em; margin: .6rem 0 1rem; }
    .hero span { color: #80d7c7; }
    .sub { color: #a9bacb; font-size: 1.07rem; max-width: 680px; line-height: 1.7; margin-bottom: 1.8rem; }
    .feature { border: 1px solid #2a3d50; background: #142338; padding: 16px 18px; border-radius: 14px; min-height: 100px; }
    .feature strong { color: #eaf4fc; font-size: 1rem; }
    .feature p { color: #9db1c6; margin: .5rem 0 0; font-size: .86rem; }
    .result-head { color: #80d7c7; letter-spacing: .12em; font-size: .78rem; font-weight: 700; text-transform: uppercase; margin-top: 1rem; }
    div[data-testid="stForm"] { border: 1px solid #30475d; background: rgba(19, 35, 54, .94); border-radius: 20px; padding: 1.4rem 1.5rem; }
    div[data-testid="stTextArea"] textarea { background: #0d1b2b; color: #edf3fa; border: 1px solid #355066; border-radius: 12px; }
    div[data-testid="stFormSubmitButton"] button { background: #80d7c7; color: #0c2331; border: 0; border-radius: 10px; font-weight: 750; min-height: 48px; }
    div[data-testid="stFormSubmitButton"] button:hover { background: #a5e8dc; color: #0c2331; }
    div[data-testid="stMarkdownContainer"] h2 { color: #edf3fa; }
    #MainMenu, footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="eyebrow">ATLAS / MULTI-AGENT TRAVEL PLANNER</div>', unsafe_allow_html=True)
st.markdown('<div class="hero">Your next journey,<br><span>beautifully planned.</span></div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub">Tell us where you want to go, your budget, and what you love. '
    'Our AI agents will combine destination ideas, food recommendations, and cost estimates into one travel itinerary.</div>',
    unsafe_allow_html=True,
)

cols = st.columns(3, gap="medium")
features = [
    ("🌍  Destination", "Places and experiences tailored to your trip"),
    ("🍽️  Food", "Local dining ideas for your preferences"),
    ("💳  Budget", "Estimated costs for your journey"),
]
for col, (title, description) in zip(cols, features):
    with col:
        st.markdown(
            f'<div class="feature"><strong>{title}</strong><p>{description}</p></div>',
            unsafe_allow_html=True,
        )

st.write("")
st.subheader("Plan your trip")

with st.form("travel_form", clear_on_submit=False):
    travel_request = st.text_area(
        "Describe your ideal trip",
        placeholder=(
            "Example: Plan a 5-day trip to Rome for two people with a $2,000 budget. "
            "We love history, Italian food, and walking tours."
        ),
        height=145,
        help="Include your destination, trip duration, budget, number of travelers, and preferences.",
    )
    submitted = st.form_submit_button("✦ Generate my itinerary", use_container_width=True)

if "final_plan" not in st.session_state:
    st.session_state.final_plan = ""
if "last_request" not in st.session_state:
    st.session_state.last_request = ""

if submitted:
    if not travel_request.strip():
        st.warning("Please describe your trip before generating an itinerary.")
    else:
        with st.spinner("Your travel agents are preparing the itinerary. This may take a little while…"):
            try:
                response = requests.post(
                    API_URL,
                    json={"request": travel_request.strip()},
                    timeout=240,
                )
                response.raise_for_status()
                payload = response.json()
                final_plan = payload.get("final_plan")
                if not isinstance(final_plan, str) or not final_plan.strip():
                    st.error("The API returned no travel plan. Please try again.")
                else:
                    st.session_state.final_plan = final_plan
                    st.session_state.last_request = travel_request.strip()
            except requests.exceptions.ConnectionError:
                st.error("Cannot connect to FastAPI. Start the API server first: python -m uvicorn main:app --reload")
            except requests.exceptions.Timeout:
                st.error("The request timed out. Please try again.")
            except requests.exceptions.HTTPError as exc:
                st.error(f"The API returned an error: {exc}")
            except (requests.exceptions.RequestException, ValueError) as exc:
                st.error(f"Unable to generate the itinerary: {exc}")

if st.session_state.final_plan:
    st.divider()
    st.markdown('<div class="result-head">YOUR PERSONALIZED ITINERARY</div>', unsafe_allow_html=True)
    st.subheader("Your travel plan is ready ✨")
    with st.container(border=True):
        st.markdown(st.session_state.final_plan)
    st.download_button(
        "↓ Download itinerary (.txt)",
        data=st.session_state.final_plan,
        file_name="atlas_travel_plan.txt",
        mime="text/plain",
        use_container_width=True,
    )

st.write("")
st.caption("Powered by your LangGraph travel agents · Streamlit frontend · FastAPI backend")
