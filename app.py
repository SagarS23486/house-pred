import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import hashlib

# =========================
# AUTH
# =========================
USERS = {
    "admin": hashlib.sha256("admin123".encode()).hexdigest(),
    "sagar": hashlib.sha256("sagar123".encode()).hexdigest(),
}

def hash_pw(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

# =========================
# LOGIN PAGE
# =========================
if not st.session_state.logged_in:
    st.set_page_config(page_title="Login | RE Platform", layout="centered")
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url('https://images.unsplash.com/photo-1583608205776-bfd35f0d9f83?w=1920&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
    }
    [data-testid="stAppViewContainer"]::before {
        content: '';
        position: fixed;
        inset: 0;
        background: rgba(8,8,20,0.82);
        z-index: 0;
        pointer-events: none;
    }
    [data-testid="stAppViewContainer"] > * { position: relative; z-index: 1; }
    [data-testid="stHeader"] { background: transparent; }
    [data-testid="stSidebar"] { display: none; }
    [data-testid="collapsedControl"] { display: none; }
    input, textarea {
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        caret-color: #000000 !important;
        background: #ffffff !important;
        border: 1px solid rgba(233,69,96,0.4) !important;
        border-radius: 8px !important;
        font-size: 15px !important;
    }
    input::placeholder { color: rgba(0,0,0,0.4) !important; -webkit-text-fill-color: rgba(0,0,0,0.4) !important; }
    input:focus { border-color: #e94560 !important; box-shadow: 0 0 0 2px rgba(233,69,96,0.2) !important; }
    .stTextInput > div > div > input {
        background: #ffffff !important;
        border: 1px solid rgba(233,69,96,0.4) !important;
        border-radius: 8px !important;
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        caret-color: #000000 !important;
        font-size: 15px !important;
        padding: 12px 16px !important;
    }
    .stTextInput > div > div > input:focus {
        border-color: #e94560 !important;
        box-shadow: 0 0 0 2px rgba(233,69,96,0.2) !important;
    }
    .stTextInput > div > div > input::placeholder {
        color: rgba(0,0,0,0.4) !important;
        -webkit-text-fill-color: rgba(0,0,0,0.4) !important;
    }
    .stTextInput label { color: #c9d1d9 !important; -webkit-text-fill-color: #c9d1d9 !important; font-size: 13px !important; font-weight: 600 !important; letter-spacing: 0.5px; }
    .stButton > button {
        background: #e94560 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 12px 0 !important;
        font-size: 15px !important;
        font-weight: 700 !important;
        width: 100%;
        letter-spacing: 0.5px;
        transition: background 0.2s !important;
    }
    .stButton > button:hover { background: #c0304a !important; }
    p, span, label, div { color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center;padding:48px 0 32px;">
        <div style="display:inline-flex;align-items:center;justify-content:center;
            width:70px;height:70px;background:linear-gradient(135deg,#e94560,#c0304a);
            border-radius:18px;font-size:2rem;margin-bottom:18px;
            box-shadow:0 8px 28px rgba(233,69,96,0.45);">🏠</div>
        <div style="font-size:2.4rem;font-weight:900;color:#ffffff;letter-spacing:1px;
            background:linear-gradient(90deg,#ffffff,#e94560,#ffffff);
            -webkit-background-clip:text;-webkit-text-fill-color:transparent;
            margin-bottom:6px;">Real Estate Intelligence</div>
        <div style="font-size:1rem;font-weight:600;color:#e94560;letter-spacing:4px;
            text-transform:uppercase;margin-bottom:6px;">AI Platform</div>
        <div style="font-size:13px;color:#8b949e;letter-spacing:1px;">Bengaluru Property Market · Powered by AI</div>
        <div style="width:50px;height:2px;background:linear-gradient(90deg,#e94560,#0f3460);
            margin:14px auto 0;border-radius:2px;"></div>
    </div>
    """, unsafe_allow_html=True)

    col = st.columns([1, 1.2, 1])[1]
    with col:
        st.markdown('<div style="background:rgba(0,0,0,0.7);border:1px solid rgba(233,69,96,0.3);border-radius:16px;padding:32px 28px;">', unsafe_allow_html=True)
        st.markdown('<div style="color:#e94560;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:20px;text-align:center;">SIGN IN TO CONTINUE</div>', unsafe_allow_html=True)
        username = st.text_input("Username", placeholder="Enter your username")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        if st.button("🔐  Sign In", use_container_width=True):
            if username in USERS and USERS[username] == hash_pw(password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
            else:
                st.markdown('<div style="background:rgba(233,69,96,0.15);border:1px solid rgba(233,69,96,0.5);border-radius:8px;padding:10px 14px;margin-top:12px;color:#ff6b6b;font-size:13px;text-align:center;">❌ Incorrect username or password</div>', unsafe_allow_html=True)
        st.markdown('<div style="margin-top:20px;padding-top:16px;border-top:1px solid rgba(255,255,255,0.06);display:flex;gap:10px;"><div style="flex:1;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);border-radius:8px;padding:10px;text-align:center;"><div style="color:#8b949e;font-size:11px;">Username</div><div style="color:#fff;font-size:13px;font-weight:600;">admin</div><div style="color:#8b949e;font-size:11px;margin-top:4px;">Password</div><div style="color:#fff;font-size:13px;font-weight:600;">admin123</div></div><div style="flex:1;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);border-radius:8px;padding:10px;text-align:center;"><div style="color:#8b949e;font-size:11px;">Username</div><div style="color:#fff;font-size:13px;font-weight:600;">sagar</div><div style="color:#8b949e;font-size:11px;margin-top:4px;">Password</div><div style="color:#fff;font-size:13px;font-weight:600;">sagar123</div></div></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# =========================
# LOAD DATA
# =========================
data = pd.read_csv("Bengaluru_House_Data.csv")
data.columns = data.columns.str.lower()

# =========================
# CLEAN DATA (BANGALORE DATASET)
# =========================

# convert size → bedrooms
if 'size' in data.columns:
    data['bedrooms'] = data['size'].str.extract('(\d+)').astype(float)
    data = data.drop('size', axis=1)

if 'bhk' in data.columns:
    data['bedrooms'] = data['bhk']
    data = data.drop('bhk', axis=1)

# rename columns
if 'total_sqft' in data.columns:
    data = data.rename(columns={'total_sqft': 'area'})
if 'bath' in data.columns:
    data = data.rename(columns={'bath': 'bathrooms'})

# clean area (handle ranges like 2100-2850)
def convert_sqft(x):
    try:
        x = str(x)
        if '-' in x:
            a, b = x.split('-')
            return (float(a) + float(b)) / 2
        return float(x)
    except:
        return None

data['area'] = data['area'].apply(convert_sqft)

# clean location
data['location'] = data['location'].astype(str).str.strip()

# remove rare locations
location_counts = data['location'].value_counts()
data = data[data['location'].isin(location_counts[location_counts > 50].index)]

# drop unnecessary columns
for col in ['area_type', 'availability', 'society', 'balcony']:
    if col in data.columns:
        data = data.drop(col, axis=1)

# remove missing values
data = data.dropna()

# =========================
# ADD MAP COORDINATES
# =========================
np.random.seed(42)
data['lat'] = np.random.uniform(12.8, 13.2, len(data))
data['lon'] = np.random.uniform(77.4, 77.8, len(data))

# =========================
# MODEL PREP
# =========================
locations = sorted(data['location'].unique())

data_model = pd.get_dummies(data, columns=['location'], drop_first=True)

feature_cols = ['area', 'bedrooms', 'bathrooms']
if 'stories' in data_model.columns:
    feature_cols.append('stories')
if 'parking' in data_model.columns:
    feature_cols.append('parking')

location_cols = [col for col in data_model.columns if col.startswith('location_')]

X = data_model[feature_cols + location_cols]
y = data_model['price']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

@st.cache_resource
def train_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    return model

model = train_model(X_train, y_train)

# =========================
# UI
# =========================
st.set_page_config(page_title="Real Estate AI Platform", layout="wide")

st.markdown("""
<style>
/* ── Global ── */
[data-testid="stAppViewContainer"] {
    background-image: url('https://images.unsplash.com/photo-1583608205776-bfd35f0d9f83?w=1920&auto=format&fit=crop');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: #c9d1d9;
}
[data-testid="stAppViewContainer"]::before {
    content: '';
    position: fixed;
    inset: 0;
    background: rgba(8, 8, 20, 0.78);
    z-index: 0;
    pointer-events: none;
}
[data-testid="stAppViewContainer"] > * {
    position: relative;
    z-index: 1;
}
[data-testid="stHeader"] { background: transparent; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #0d1117 !important;
    border-right: 2px solid #e94560 !important;
    min-width: 220px !important;
}
[data-testid="stSidebar"] > div { padding: 0 !important; }

/* ── Top Navbar ── */
.topnav {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    background: linear-gradient(90deg, #1a1a2e, #0f3460);
    padding: 12px 24px;
    border-radius: 14px;
    margin-bottom: 28px;
    box-shadow: 0 4px 20px rgba(233,69,96,0.15);
}
.topnav a {
    color: #c9d1d9;
    text-decoration: none;
    font-size: 14px;
    font-weight: 600;
    padding: 8px 18px;
    border-radius: 8px;
    letter-spacing: 0.4px;
    transition: all 0.2s;
}
.topnav a:hover {
    background: rgba(233,69,96,0.15);
    color: #e94560;
}
.topnav a.active {
    background: #e94560;
    color: white;
    box-shadow: 0 2px 10px rgba(233,69,96,0.4);
}

/* ── Title ── */
h1 {
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
    font-size: 2.6rem !important;
    font-weight: 800 !important;
    letter-spacing: 1px;
    text-shadow: 0 2px 10px rgba(0,0,0,0.9);
}
h2, h3 { color: #e94560 !important; text-shadow: 0 2px 8px rgba(0,0,0,0.9); }

/* ── Metric cards ── */
[data-testid="stMetric"] {
    background: rgba(0,0,0,0.75);
    border: 1px solid rgba(233,69,96,0.6);
    border-radius: 12px;
    padding: 18px 22px;
    backdrop-filter: blur(6px);
    transition: transform 0.2s, box-shadow 0.2s;
}
[data-testid="stMetric"]:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(233,69,96,0.4);
}
[data-testid="stMetricLabel"] { color: #ffffff !important; font-size: 13px; font-weight: 600; }
[data-testid="stMetricValue"] { color: #e94560 !important; font-size: 1.8rem !important; font-weight: 700; }

/* ── Nav Buttons ── */
.stButton > button {
    background: #16213e !important;
    color: #c9d1d9 !important;
    border: 1px solid #2a2a4a !important;
    border-radius: 8px !important;
    padding: 11px 16px !important;
    font-size: 14px !important;
    font-weight: 700 !important;
    font-family: 'Segoe UI', 'Inter', sans-serif !important;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    transition: background 0.2s, color 0.2s, border-color 0.2s !important;
    width: 100%;
    text-align: left !important;
}
.stButton > button:hover {
    background: #e94560 !important;
    border-color: #e94560 !important;
    color: #ffffff !important;
}
.stButton > button[data-testid="baseButton-primary"],
button[kind="primary"] {
    background: #e94560 !important;
    border: none !important;
    color: #ffffff !important;
    font-weight: 800 !important;
    font-size: 14px !important;
    font-family: 'Segoe UI', 'Inter', sans-serif !important;
    letter-spacing: 0.6px;
    text-transform: uppercase;
    border-radius: 8px !important;
    border-left: 4px solid #ffffff !important;
}
.stButton > button[data-testid="baseButton-primary"]:hover {
    background: #c0304a !important;
}

/* ── Sliders ── */
[data-testid="stSlider"] > div > div > div > div { background: #e94560 !important; }
[data-testid="stSlider"] label {
    color: #ffffff !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    letter-spacing: 0.5px;
}
[data-testid="stSlider"] p {
    color: #e94560 !important;
    font-weight: 700 !important;
}

/* ── Selectbox ── */
[data-testid="stSelectbox"] > div > div {
    background: linear-gradient(135deg, rgba(15,52,96,0.9), rgba(26,26,46,0.95)) !important;
    border: 1.5px solid #e94560 !important;
    border-radius: 12px !important;
    color: #ffffff !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    padding: 4px 8px !important;
    box-shadow: 0 4px 15px rgba(233,69,96,0.3) !important;
    transition: all 0.3s !important;
}
[data-testid="stSelectbox"] > div > div:hover {
    border-color: #ffffff !important;
    box-shadow: 0 6px 20px rgba(233,69,96,0.5) !important;
}
[data-testid="stSelectbox"] span,
[data-testid="stSelectbox"] div,
[data-testid="stSelectbox"] label {
    color: #ffffff !important;
    font-weight: 600 !important;
}
[data-testid="stSelectbox"] label {
    font-size: 15px !important;
    letter-spacing: 0.5px;
}
/* ── Dropdown popup list ── */
ul[data-testid="stSelectboxVirtualDropdown"],
[data-baseweb="popover"] ul,
[data-baseweb="menu"] {
    background: linear-gradient(135deg, #1a1a2e, #0f3460) !important;
    border: 1px solid rgba(233,69,96,0.6) !important;
    border-radius: 12px !important;
}
[data-baseweb="menu"] li,
[data-baseweb="option"] {
    background: transparent !important;
    color: #ffffff !important;
    font-weight: 500 !important;
    font-size: 14px !important;
}
[data-baseweb="option"]:hover,
[data-baseweb="menu"] li:hover {
    background: rgba(233,69,96,0.25) !important;
    color: #ffffff !important;
}
[aria-selected="true"][data-baseweb="option"] {
    background: rgba(233,69,96,0.4) !important;
    color: #ffffff !important;
}

/* ── Success / Info alerts ── */
[data-testid="stAlert"] {
    border-radius: 10px;
    font-size: 18px;
    font-weight: 700;
    background: rgba(0,0,0,0.75) !important;
    color: #ffffff !important;
    border: 1px solid #e94560 !important;
}
[data-testid="stAlert"] p {
    color: #ffffff !important;
    font-size: 18px !important;
    font-weight: 700 !important;
}

/* ── Dataframe ── */
[data-testid="stDataFrame"] {
    background: rgba(0,0,0,0.75) !important;
    border: 1px solid rgba(233,69,96,0.6);
    border-radius: 10px;
    overflow: hidden;
    color: #ffffff !important;
}

/* ── General text ── */
p, span, label, div, li {
    color: #ffffff !important;
}
h1 {
    background: linear-gradient(90deg, #e94560, #ffffff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 2.6rem !important;
    font-weight: 800 !important;
    letter-spacing: 1px;
}
h2, h3 { color: #e94560 !important; text-shadow: 0 2px 8px rgba(0,0,0,0.8); }

/* ── Sliders label ── */
[data-testid="stSlider"] label { color: #ffffff !important; font-weight: 600; }

/* ── Subheader ── */
[data-testid="stMarkdownContainer"] p { color: #ffffff !important; }

/* ── Footer ── */
footer, .css-1lsmgbg { visibility: hidden; }
.custom-footer {
    text-align: center;
    color: #ffffff;
    font-size: 13px;
    padding: 12px 0 4px;
    border-top: 1px solid rgba(233,69,96,0.5);
    margin-top: 20px;
    background: rgba(0,0,0,0.6);
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;padding:30px 20px 10px;">
    <div style="font-size:3.2rem;font-weight:900;letter-spacing:2px;
    background:linear-gradient(90deg,#e94560,#ffffff,#e94560);
    -webkit-background-clip:text;-webkit-text-fill-color:transparent;
    text-shadow:none;animation:none;">
        🏠 Real Estate Intelligence Platform
    </div>
    <div style="color:#c9d1d9;font-size:1.1rem;font-weight:400;margin-top:8px;
    letter-spacing:3px;text-transform:uppercase;text-shadow:0 2px 8px rgba(0,0,0,0.8);">
        ✦ AI-Powered Property Insights for Bengaluru ✦
    </div>
    <div style="width:80px;height:3px;background:linear-gradient(90deg,#e94560,#0f3460);
    margin:14px auto 0;border-radius:2px;"></div>
</div>
""", unsafe_allow_html=True)

pages = ["Dashboard", "Prediction", "Analytics", "Insights", "Recommendations", "Map", "EMI Calculator", "Compare", "Search", "Finance"]
icons = {"Dashboard": "📊", "Prediction": "🏠", "Analytics": "📈", "Insights": "💡", "Recommendations": "⭐", "Map": "🗺️", "EMI Calculator": "💳", "Compare": "⚖️", "Search": "🔍", "Finance": "💰"}

if "menu" not in st.session_state:
    st.session_state.menu = "Dashboard"

main_pages = ["Dashboard", "Prediction", "Analytics", "Insights", "Recommendations", "Map"]
tool_pages = ["EMI Calculator", "Compare", "Search", "Finance"]

# =========================
# SIDEBAR NAVIGATION
# =========================
with st.sidebar:
    st.markdown("""
    <div style="padding:24px 16px 16px;">
        <div style="font-size:1.3rem;font-weight:900;color:#e94560;letter-spacing:1px;margin-bottom:4px;">🏠 RE Platform</div>
        <div style="font-size:11px;color:#c9d1d9;letter-spacing:2px;text-transform:uppercase;margin-bottom:24px;">Bengaluru AI</div>
        <div style="font-size:10px;color:#e94560;font-weight:800;letter-spacing:3px;text-transform:uppercase;margin-bottom:10px;">🧭 MAIN</div>
    </div>
    """, unsafe_allow_html=True)

    for page in main_pages:
        active = st.session_state.menu == page
        if st.button(icons[page] + "  " + page, key=f"btn_{page}", use_container_width=True, type="primary" if active else "secondary"):
            st.session_state.menu = page
            st.rerun()

    st.markdown('<div style="padding:20px 20px 4px;font-size:10px;color:#484f58;font-weight:700;letter-spacing:2.5px;text-transform:uppercase;">TOOLS</div>', unsafe_allow_html=True)

    for page in tool_pages:
        active = st.session_state.menu == page
        if st.button(icons[page] + "  " + page, key=f"btn_{page}", use_container_width=True, type="primary" if active else "secondary"):
            st.session_state.menu = page
            st.rerun()

    st.markdown('<div style="margin-top:32px;border-top:1px solid rgba(255,255,255,0.06);padding:16px 20px 4px;">', unsafe_allow_html=True)
    st.markdown(f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;"><div style="width:32px;height:32px;border-radius:50%;background:#e94560;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:700;color:#fff;">{st.session_state.username[0].upper()}</div><div><div style="color:#ffffff;font-size:13px;font-weight:600;">{st.session_state.username}</div><div style="color:#484f58;font-size:11px;">Logged in</div></div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("⏻  Logout", key="logout_btn", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()
    st.markdown('<div style="padding:8px 20px 16px;text-align:center;color:#484f58;font-size:11px;">Built by Sagar 🚀</div>', unsafe_allow_html=True)

menu = st.session_state.menu

# =========================
# DASHBOARD
# =========================
if menu == "Dashboard":

    # ── KPI Cards ──
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Listings", f"{len(data):,}")
    col2.metric("Avg Price (L)", f"₹{data['price'].mean():,.1f}")
    col3.metric("Avg Area (sqft)", f"{data['area'].mean():,.0f}")
    col4.metric("Locations", f"{data['location'].nunique()}")

    st.markdown('<div style="margin-top:24px;"></div>', unsafe_allow_html=True)

    # ── Row 1: Top Locations Bar + Price Distribution ──
    r1c1, r1c2 = st.columns(2, gap="large")

    with r1c1:
        st.markdown('<div style="background:rgba(0,0,0,0.75);border:1px solid rgba(233,69,96,0.4);border-radius:14px;padding:20px;">', unsafe_allow_html=True)
        st.markdown('<div style="color:#e94560;font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:14px;">🏆 Top 10 Locations by Avg Price</div>', unsafe_allow_html=True)
        top_locs = data.groupby('location')['price'].mean().nlargest(10).sort_values()
        fig1, ax1 = plt.subplots(figsize=(6, 4), facecolor='none')
        bars = ax1.barh(top_locs.index, top_locs.values, color='#e94560', edgecolor='none', height=0.6)
        for bar, val in zip(bars, top_locs.values):
            ax1.text(val + 0.5, bar.get_y() + bar.get_height()/2, f'₹{val:.0f}L', va='center', color='white', fontsize=8)
        ax1.set_facecolor('none')
        ax1.tick_params(colors='white', labelsize=8)
        ax1.set_xlabel('Avg Price (Lakhs)', color='#c9d1d9', fontsize=9)
        for spine in ax1.spines.values(): spine.set_edgecolor((1,1,1,0.1))
        fig1.patch.set_alpha(0)
        st.pyplot(fig1)
        st.markdown('</div>', unsafe_allow_html=True)

    with r1c2:
        st.markdown('<div style="background:rgba(0,0,0,0.75);border:1px solid rgba(233,69,96,0.4);border-radius:14px;padding:20px;">', unsafe_allow_html=True)
        st.markdown('<div style="color:#e94560;font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:14px;">📊 Price Distribution</div>', unsafe_allow_html=True)
        fig2, ax2 = plt.subplots(figsize=(6, 4), facecolor='none')
        clipped = data['price'].clip(upper=data['price'].quantile(0.97))
        ax2.hist(clipped, bins=40, color='#0f3460', edgecolor='#e94560', linewidth=0.4, alpha=0.9)
        ax2.axvline(data['price'].mean(), color='#e94560', linewidth=1.5, linestyle='--', label=f"Mean: ₹{data['price'].mean():.0f}L")
        ax2.legend(fontsize=8, labelcolor='white', facecolor='none', edgecolor='none')
        ax2.set_facecolor('none')
        ax2.tick_params(colors='white', labelsize=8)
        ax2.set_xlabel('Price (Lakhs)', color='#c9d1d9', fontsize=9)
        ax2.set_ylabel('Count', color='#c9d1d9', fontsize=9)
        for spine in ax2.spines.values(): spine.set_edgecolor((1,1,1,0.1))
        fig2.patch.set_alpha(0)
        st.pyplot(fig2)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div style="margin-top:20px;"></div>', unsafe_allow_html=True)

    # ── Row 2: Bedrooms Pie + Price vs Area Scatter ──
    r2c1, r2c2 = st.columns(2, gap="large")

    with r2c1:
        st.markdown('<div style="background:rgba(0,0,0,0.75);border:1px solid rgba(233,69,96,0.4);border-radius:14px;padding:20px;">', unsafe_allow_html=True)
        st.markdown('<div style="color:#e94560;font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:14px;">🛏️ Listings by Bedrooms</div>', unsafe_allow_html=True)
        bed_counts = data['bedrooms'].value_counts().sort_index()
        bed_counts = bed_counts[bed_counts.index <= 6]
        colors_pie = ['#e94560','#0f3460','#0f9460','#f5a623','#7b2d8b','#1a7abf']
        fig3, ax3 = plt.subplots(figsize=(5, 4), facecolor='none')
        wedges, texts, autotexts = ax3.pie(
            bed_counts.values, labels=[f"{int(b)} BHK" for b in bed_counts.index],
            colors=colors_pie[:len(bed_counts)], autopct='%1.1f%%',
            textprops={'color': 'white', 'fontsize': 9},
            wedgeprops={'edgecolor': (0, 0, 0, 0.3), 'linewidth': 1}
        )
        for at in autotexts: at.set_fontsize(8)
        ax3.set_facecolor('none')
        fig3.patch.set_alpha(0)
        st.pyplot(fig3)
        st.markdown('</div>', unsafe_allow_html=True)

    with r2c2:
        st.markdown('<div style="background:rgba(0,0,0,0.75);border:1px solid rgba(233,69,96,0.4);border-radius:14px;padding:20px;">', unsafe_allow_html=True)
        st.markdown('<div style="color:#e94560;font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:14px;">📐 Price vs Area</div>', unsafe_allow_html=True)
        sample = data.sample(min(800, len(data)), random_state=42)
        fig4, ax4 = plt.subplots(figsize=(6, 4), facecolor='none')
        sc = ax4.scatter(sample['area'], sample['price'], c=sample['bedrooms'],
                         cmap='RdYlGn', alpha=0.6, s=18, edgecolors='none')
        cbar = fig4.colorbar(sc, ax=ax4)
        cbar.set_label('Bedrooms', color='white', fontsize=8)
        cbar.ax.yaxis.set_tick_params(color='white', labelsize=7)
        plt.setp(cbar.ax.yaxis.get_ticklabels(), color='white')
        ax4.set_facecolor('none')
        ax4.tick_params(colors='white', labelsize=8)
        ax4.set_xlabel('Area (sqft)', color='#c9d1d9', fontsize=9)
        ax4.set_ylabel('Price (Lakhs)', color='#c9d1d9', fontsize=9)
        ax4.set_xlim(0, sample['area'].quantile(0.97))
        ax4.set_ylim(0, sample['price'].quantile(0.97))
        for spine in ax4.spines.values(): spine.set_edgecolor((1,1,1,0.1))
        fig4.patch.set_alpha(0)
        st.pyplot(fig4)
        st.markdown('</div>', unsafe_allow_html=True)

# =========================
# PREDICTION (REAL LOCATION)
# =========================
elif menu == "Prediction":

    st.markdown("""
    <div style="text-align:center;margin-bottom:24px;">
        <div style="font-size:1.8rem;font-weight:800;color:#ffffff;text-shadow:0 2px 10px rgba(0,0,0,0.9);letter-spacing:1px;">🏠 House Price Predictor</div>
        <div style="color:#c9d1d9;font-size:0.95rem;letter-spacing:2px;text-transform:uppercase;margin-top:4px;">Fill in the details below to get an instant estimate</div>
        <div style="width:60px;height:3px;background:linear-gradient(90deg,#e94560,#0f3460);margin:10px auto 0;border-radius:2px;"></div>
    </div>
    """, unsafe_allow_html=True)

    col_left, col_right = st.columns([1, 1], gap="large")

    with col_left:
        st.markdown('<div style="background:rgba(0,0,0,0.75);border:1px solid rgba(233,69,96,0.5);border-radius:16px;padding:28px 28px 20px;">'
        '<div style="color:#e94560;font-size:13px;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:18px;">📐 Property Details</div>',
        unsafe_allow_html=True)
        area = st.slider("🏗️ Area (sq ft)", 500, 10000, 2000)
        bedrooms = st.slider("🛏️ Bedrooms", 1, 6, 2)
        bathrooms = st.slider("🛁 Bathrooms", 1, 5, 2)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_right:
        st.markdown('<div style="background:rgba(0,0,0,0.75);border:1px solid rgba(233,69,96,0.5);border-radius:16px;padding:28px 28px 20px;">'
        '<div style="color:#e94560;font-size:13px;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:18px;">📍 Location</div>',
        unsafe_allow_html=True)
        selected_location = st.selectbox("Select Neighbourhood", locations)
        st.markdown("""
        <div style="margin-top:20px;padding:14px 16px;background:rgba(233,69,96,0.1);
        border:1px dashed rgba(233,69,96,0.5);border-radius:10px;color:#c9d1d9;font-size:13px;">
            💡 Tip: Location is one of the strongest price factors in Bengaluru.
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div style="margin-top:24px;"></div>', unsafe_allow_html=True)

    if st.button("🔮 Predict Price", key="predict_btn", type="primary"):

        input_dict = {
            'area': area,
            'bedrooms': bedrooms,
            'bathrooms': bathrooms
        }

        # encode location
        for loc in locations:
            col_name = f"location_{loc}"
            if col_name in X.columns:
                input_dict[col_name] = 1 if loc == selected_location else 0

        input_df = pd.DataFrame([input_dict])
        input_df = input_df.reindex(columns=X.columns, fill_value=0)

        prediction = model.predict(input_df)[0]

        
        st.success(f"🏠 Estimated Price: ₹{prediction:,.0f} lakhs")
        st.info(f"📍 Location: {selected_location}")

# =========================
# ANALYTICS
# =========================
elif menu == "Analytics":

    st.markdown('<div style="text-align:center;margin-bottom:24px;"><div style="font-size:1.8rem;font-weight:800;color:#ffffff;">📈 Analytics</div><div style="color:#c9d1d9;font-size:0.9rem;letter-spacing:2px;text-transform:uppercase;">Deep dive into property data</div><div style="width:60px;height:3px;background:linear-gradient(90deg,#e94560,#0f3460);margin:10px auto 0;border-radius:2px;"></div></div>', unsafe_allow_html=True)

    def card(title):
        st.markdown(f'<div style="background:rgba(0,0,0,0.75);border:1px solid rgba(233,69,96,0.4);border-radius:14px;padding:20px;margin-bottom:20px;"><div style="color:#e94560;font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:14px;">{title}</div>', unsafe_allow_html=True)

    def card_end():
        st.markdown('</div>', unsafe_allow_html=True)

    def style_ax(ax, fig):
        ax.set_facecolor('none')
        ax.tick_params(colors='white', labelsize=8)
        for spine in ax.spines.values(): spine.set_edgecolor((1,1,1,0.1))
        fig.patch.set_alpha(0)

    # ── Row 1 ──
    c1, c2 = st.columns(2, gap="large")

    with c1:
        card("📊 Price vs Area Scatter")
        sample = data.sample(min(800, len(data)), random_state=42)
        fig, ax = plt.subplots(figsize=(6, 4), facecolor='none')
        sc = ax.scatter(sample['area'], sample['price'], c=sample['bedrooms'], cmap='plasma', alpha=0.65, s=20, edgecolors='none')
        cbar = fig.colorbar(sc, ax=ax)
        cbar.set_label('Bedrooms', color='white', fontsize=8)
        cbar.ax.yaxis.set_tick_params(color='white', labelsize=7)
        plt.setp(cbar.ax.yaxis.get_ticklabels(), color='white')
        ax.set_xlabel('Area (sqft)', color='#c9d1d9', fontsize=9)
        ax.set_ylabel('Price (Lakhs)', color='#c9d1d9', fontsize=9)
        ax.set_xlim(0, sample['area'].quantile(0.97))
        ax.set_ylim(0, sample['price'].quantile(0.97))
        style_ax(ax, fig)
        st.pyplot(fig)
        card_end()

    with c2:
        card("🏙️ Avg Price by Top 15 Locations")
        top15 = data.groupby('location')['price'].mean().nlargest(15).sort_values()
        fig, ax = plt.subplots(figsize=(6, 4), facecolor='none')
        colors_bar = plt.cm.RdYlGn(np.linspace(0.2, 0.9, len(top15)))
        bars = ax.barh(top15.index, top15.values, color=colors_bar, edgecolor='none', height=0.65)
        for bar, val in zip(bars, top15.values):
            ax.text(val + 0.3, bar.get_y() + bar.get_height()/2, f'₹{val:.0f}L', va='center', color='white', fontsize=7)
        ax.set_xlabel('Avg Price (Lakhs)', color='#c9d1d9', fontsize=9)
        style_ax(ax, fig)
        st.pyplot(fig)
        card_end()

    # ── Row 2 ──
    c3, c4 = st.columns(2, gap="large")

    with c3:
        card("🛏️ Avg Price by Bedrooms")
        bed_price = data.groupby('bedrooms')['price'].mean().reset_index()
        bed_price = bed_price[bed_price['bedrooms'] <= 6]
        fig, ax = plt.subplots(figsize=(6, 4), facecolor='none')
        bars = ax.bar(bed_price['bedrooms'].astype(int), bed_price['price'],
                      color=['#e94560','#0f3460','#0f9460','#f5a623','#7b2d8b','#1a7abf'][:len(bed_price)],
                      edgecolor='none', width=0.6)
        for bar, val in zip(bars, bed_price['price']):
            ax.text(bar.get_x() + bar.get_width()/2, val + 0.5, f'₹{val:.0f}L', ha='center', color='white', fontsize=8)
        ax.set_xlabel('Bedrooms (BHK)', color='#c9d1d9', fontsize=9)
        ax.set_ylabel('Avg Price (Lakhs)', color='#c9d1d9', fontsize=9)
        style_ax(ax, fig)
        st.pyplot(fig)
        card_end()

    with c4:
        card("🛁 Avg Price by Bathrooms")
        bath_price = data.groupby('bathrooms')['price'].mean().reset_index()
        bath_price = bath_price[bath_price['bathrooms'] <= 6]
        fig, ax = plt.subplots(figsize=(6, 4), facecolor='none')
        ax.plot(bath_price['bathrooms'].astype(int), bath_price['price'],
                color='#e94560', linewidth=2.5, marker='o', markersize=7, markerfacecolor='white')
        ax.fill_between(bath_price['bathrooms'].astype(int), bath_price['price'], alpha=0.15, color='#e94560')
        ax.set_xlabel('Bathrooms', color='#c9d1d9', fontsize=9)
        ax.set_ylabel('Avg Price (Lakhs)', color='#c9d1d9', fontsize=9)
        style_ax(ax, fig)
        st.pyplot(fig)
        card_end()

    # ── Row 3: full width ──
    card("📐 Area Distribution by BHK")
    fig, ax = plt.subplots(figsize=(12, 4), facecolor='none')
    colors_bhk = ['#e94560','#0f3460','#0f9460','#f5a623','#7b2d8b','#1a7abf']
    for i, bhk in enumerate([1, 2, 3, 4, 5, 6]):
        subset = data[data['bedrooms'] == bhk]['area'].clip(upper=data['area'].quantile(0.97))
        if len(subset) > 10:
            ax.hist(subset, bins=30, alpha=0.6, color=colors_bhk[i], label=f'{bhk} BHK', edgecolor='none')
    ax.set_xlabel('Area (sqft)', color='#c9d1d9', fontsize=9)
    ax.set_ylabel('Count', color='#c9d1d9', fontsize=9)
    ax.legend(fontsize=8, labelcolor='white', facecolor='none', edgecolor='none')
    style_ax(ax, fig)
    st.pyplot(fig)
    card_end()

# =========================
# INSIGHTS
# =========================
elif menu == "Insights":

    st.markdown('<div style="text-align:center;margin-bottom:24px;"><div style="font-size:1.8rem;font-weight:800;color:#ffffff;">💡 Market Insights</div><div style="color:#c9d1d9;font-size:0.9rem;letter-spacing:2px;text-transform:uppercase;">Data-driven intelligence on Bengaluru real estate</div><div style="width:60px;height:3px;background:linear-gradient(90deg,#e94560,#0f3460);margin:10px auto 0;border-radius:2px;"></div></div>', unsafe_allow_html=True)

    def card(title):
        st.markdown(f'<div style="background:rgba(0,0,0,0.75);border:1px solid rgba(233,69,96,0.4);border-radius:14px;padding:20px;margin-bottom:20px;"><div style="color:#e94560;font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:14px;">{title}</div>', unsafe_allow_html=True)
    def card_end():
        st.markdown('</div>', unsafe_allow_html=True)
    def style_ax(ax, fig):
        ax.set_facecolor('none')
        ax.tick_params(colors='white', labelsize=8)
        for spine in ax.spines.values(): spine.set_edgecolor((1,1,1,0.1))
        fig.patch.set_alpha(0)

    # ── Row 1: KPI summary cards ──
    k1, k2, k3, k4 = st.columns(4)
    for col, label, val, sub in [
        (k1, "Median Price", f"₹{data['price'].median():.0f}L", "50th percentile"),
        (k2, "Price Std Dev", f"₹{data['price'].std():.0f}L", "Volatility"),
        (k3, "Avg Price/sqft", f"₹{(data['price']*100000/data['area']).median():.0f}", "Per sq ft"),
        (k4, "Most Common BHK", f"{int(data['bedrooms'].mode()[0])} BHK", "Top listing type"),
    ]:
        col.markdown(f"""
        <div style="background:rgba(0,0,0,0.75);border:1px solid rgba(233,69,96,0.5);border-radius:12px;padding:16px;text-align:center;margin-bottom:20px;">
            <div style="color:#c9d1d9;font-size:11px;letter-spacing:1px;text-transform:uppercase;">{label}</div>
            <div style="color:#e94560;font-size:1.6rem;font-weight:800;margin:6px 0;">{val}</div>
            <div style="color:#888;font-size:11px;">{sub}</div>
        </div>
        """, unsafe_allow_html=True)

    # ── Row 2: Correlation bar + Price percentile ──
    c1, c2 = st.columns(2, gap="large")

    with c1:
        card("🔗 Feature Correlation with Price")
        corr = data.corr(numeric_only=True)['price'].drop('price').sort_values()
        colors_corr = ['#e94560' if v < 0 else '#0f9460' for v in corr.values]
        fig, ax = plt.subplots(figsize=(6, 4), facecolor='none')
        bars = ax.barh(corr.index, corr.values, color=colors_corr, edgecolor='none', height=0.5)
        ax.axvline(0, color='white', linewidth=0.8, alpha=0.4)
        for bar, val in zip(bars, corr.values):
            ax.text(val + (0.01 if val >= 0 else -0.01), bar.get_y() + bar.get_height()/2,
                    f'{val:.2f}', va='center', ha='left' if val >= 0 else 'right', color='white', fontsize=8)
        ax.set_xlabel('Correlation Coefficient', color='#c9d1d9', fontsize=9)
        style_ax(ax, fig)
        st.pyplot(fig)
        card_end()

    with c2:
        card("📊 Price Percentile Bands")
        percentiles = [10, 25, 50, 75, 90, 95]
        pvals = [data['price'].quantile(p/100) for p in percentiles]
        fig, ax = plt.subplots(figsize=(6, 4), facecolor='none')
        bars = ax.bar([f'P{p}' for p in percentiles], pvals,
                      color=['#1a7abf','#0f9460','#f5a623','#e94560','#c0304a','#7b2d8b'],
                      edgecolor='none', width=0.6)
        for bar, val in zip(bars, pvals):
            ax.text(bar.get_x() + bar.get_width()/2, val + 0.5, f'₹{val:.0f}L',
                    ha='center', color='white', fontsize=8)
        ax.set_ylabel('Price (Lakhs)', color='#c9d1d9', fontsize=9)
        style_ax(ax, fig)
        st.pyplot(fig)
        card_end()

    # ── Row 3: Price range heatmap by BHK + location count ──
    c3, c4 = st.columns(2, gap="large")

    with c3:
        card("📦 Price Box Plot by BHK")
        fig, ax = plt.subplots(figsize=(6, 4), facecolor='none')
        bhk_data = [data[data['bedrooms'] == b]['price'].clip(upper=data['price'].quantile(0.95)).values
                    for b in sorted(data['bedrooms'].unique()) if b <= 5]
        bp = ax.boxplot(bhk_data, patch_artist=True, medianprops=dict(color='white', linewidth=2),
                        whiskerprops=dict(color='#c9d1d9'), capprops=dict(color='#c9d1d9'),
                        flierprops=dict(marker='o', color='#e94560', markersize=3, alpha=0.4))
        colors_box = ['#e94560','#0f3460','#0f9460','#f5a623','#7b2d8b']
        for patch, color in zip(bp['boxes'], colors_box):
            patch.set_facecolor(color)
            patch.set_alpha(0.7)
        ax.set_xticklabels([f'{int(b)} BHK' for b in sorted(data['bedrooms'].unique()) if b <= 5], color='white')
        ax.set_ylabel('Price (Lakhs)', color='#c9d1d9', fontsize=9)
        style_ax(ax, fig)
        st.pyplot(fig)
        card_end()

    with c4:
        card("🏘️ Top 10 Locations by Listing Count")
        loc_counts = data['location'].value_counts().head(10).sort_values()
        fig, ax = plt.subplots(figsize=(6, 4), facecolor='none')
        bars = ax.barh(loc_counts.index, loc_counts.values, color='#0f3460', edgecolor='none', height=0.6)
        for bar, val in zip(bars, loc_counts.values):
            ax.text(val + 1, bar.get_y() + bar.get_height()/2, str(val), va='center', color='white', fontsize=8)
        ax.set_xlabel('Number of Listings', color='#c9d1d9', fontsize=9)
        style_ax(ax, fig)
        st.pyplot(fig)
        card_end()

    # ── Key Takeaways ──
    st.markdown('<div style="background:rgba(0,0,0,0.75);border:1px solid rgba(233,69,96,0.4);border-radius:14px;padding:24px;">', unsafe_allow_html=True)
    st.markdown('<div style="color:#e94560;font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:16px;">🎯 Key Market Takeaways</div>', unsafe_allow_html=True)
    top_loc = data.groupby('location')['price'].mean().idxmax()
    cheapest_loc = data.groupby('location')['price'].mean().idxmin()
    best_bhk = data.groupby('bedrooms')['price'].mean().idxmin()
    takeaways = [
        ("🏆", f"Most expensive location: <b>{top_loc}</b>"),
        ("💰", f"Most affordable location: <b>{cheapest_loc}</b>"),
        ("🛏️", f"Best value BHK type: <b>{int(best_bhk)} BHK</b> (lowest avg price)"),
        ("📈", f"Area has the strongest correlation with price: <b>{data.corr(numeric_only=True)['price'].drop('price').abs().idxmax()}</b>"),
        ("📊", f"<b>{(data['bedrooms']==2).sum():,}</b> listings are 2 BHK — the most common type"),
    ]
    for icon, text in takeaways:
        st.markdown(f'<div style="display:flex;align-items:center;gap:12px;padding:10px 0;border-bottom:1px solid rgba(255,255,255,0.07);"><span style="font-size:1.3rem;">{icon}</span><span style="color:#c9d1d9;font-size:14px;">{text}</span></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# RECOMMENDATIONS
# =========================
elif menu == "Recommendations":

    st.markdown('<div style="text-align:center;margin-bottom:24px;"><div style="font-size:1.8rem;font-weight:800;color:#ffffff;">⭐ Property Recommendations</div><div style="color:#c9d1d9;font-size:0.9rem;letter-spacing:2px;text-transform:uppercase;">Find your perfect home in Bengaluru</div><div style="width:60px;height:3px;background:linear-gradient(90deg,#e94560,#0f3460);margin:10px auto 0;border-radius:2px;"></div></div>', unsafe_allow_html=True)

    st.markdown('<div style="background:rgba(0,0,0,0.75);border:1px solid rgba(233,69,96,0.4);border-radius:14px;padding:24px;margin-bottom:20px;">', unsafe_allow_html=True)
    st.markdown('<div style="color:#e94560;font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:16px;">🎯 Your Preferences</div>', unsafe_allow_html=True)
    f1, f2, f3, f4 = st.columns(4)
    with f1:
        budget = st.slider("💰 Max Budget (Lakhs)", int(data['price'].min()), int(data['price'].max()), int(data['price'].quantile(0.4)))
    with f2:
        pref_bhk = st.multiselect("🛏️ BHK Type", sorted(data['bedrooms'].dropna().unique().astype(int).tolist()), default=[2, 3])
    with f3:
        min_area = st.slider("📐 Min Area (sqft)", 300, 5000, 800)
    with f4:
        pref_loc = st.multiselect("📍 Preferred Locations", locations, default=[])
    st.markdown('</div>', unsafe_allow_html=True)

    filtered_rec = data[data['price'] <= budget]
    filtered_rec = filtered_rec[filtered_rec['area'] >= min_area]
    if pref_bhk:
        filtered_rec = filtered_rec[filtered_rec['bedrooms'].isin(pref_bhk)]
    if pref_loc:
        filtered_rec = filtered_rec[filtered_rec['location'].isin(pref_loc)]
    filtered_rec = filtered_rec.sort_values('price').head(20)

    # summary stats
    k1, k2, k3, k4 = st.columns(4)
    for col, label, val in [
        (k1, "Matches Found", f"{len(filtered_rec)}"),
        (k2, "Lowest Price", f"₹{filtered_rec['price'].min():.0f}L" if len(filtered_rec) else "N/A"),
        (k3, "Avg Area", f"{filtered_rec['area'].mean():.0f} sqft" if len(filtered_rec) else "N/A"),
        (k4, "Avg Price", f"₹{filtered_rec['price'].mean():.0f}L" if len(filtered_rec) else "N/A"),
    ]:
        col.markdown(f"""
        <div style="background:rgba(0,0,0,0.75);border:1px solid rgba(233,69,96,0.5);border-radius:12px;padding:14px;text-align:center;margin-bottom:16px;">
            <div style="color:#c9d1d9;font-size:11px;letter-spacing:1px;text-transform:uppercase;">{label}</div>
            <div style="color:#e94560;font-size:1.4rem;font-weight:800;margin-top:6px;">{val}</div>
        </div>
        """, unsafe_allow_html=True)

    if len(filtered_rec) == 0:
        st.markdown('<div style="background:rgba(233,69,96,0.15);border:1px solid rgba(233,69,96,0.4);border-radius:10px;padding:20px;text-align:center;color:#ffffff;">😕 No properties match your criteria. Try adjusting your filters.</div>', unsafe_allow_html=True)
    else:
        # property cards
        st.markdown('<div style="color:#e94560;font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin:16px 0 12px;">🏠 Top Matches</div>', unsafe_allow_html=True)
        for i in range(0, min(len(filtered_rec), 9), 3):
            cols = st.columns(3)
            for j, col in enumerate(cols):
                if i + j < len(filtered_rec):
                    row = filtered_rec.iloc[i + j]
                    price_pct = int((row['price'] / budget) * 100)
                    col.markdown(f"""
                    <div style="background:rgba(0,0,0,0.75);border:1px solid rgba(233,69,96,0.35);border-radius:12px;padding:16px;margin-bottom:12px;">
                        <div style="color:#e94560;font-size:13px;font-weight:700;margin-bottom:8px;">📍 {row['location']}</div>
                        <div style="display:flex;justify-content:space-between;margin-bottom:6px;">
                            <span style="color:#c9d1d9;font-size:12px;">🛏️ {int(row['bedrooms'])} BHK &nbsp; 🛁 {int(row['bathrooms'])} Bath</span>
                        </div>
                        <div style="color:#c9d1d9;font-size:12px;margin-bottom:10px;">📐 {row['area']:,.0f} sqft</div>
                        <div style="display:flex;justify-content:space-between;align-items:center;">
                            <span style="color:#ffffff;font-size:1.1rem;font-weight:800;">₹{row['price']:.0f}L</span>
                            <span style="background:{'#0f9460' if price_pct <= 70 else '#f5a623' if price_pct <= 90 else '#e94560'};color:#fff;font-size:10px;font-weight:700;padding:3px 8px;border-radius:20px;">{price_pct}% of budget</span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

        # price distribution of results
        st.markdown('<div style="background:rgba(0,0,0,0.75);border:1px solid rgba(233,69,96,0.4);border-radius:14px;padding:20px;margin-top:8px;">', unsafe_allow_html=True)
        st.markdown('<div style="color:#e94560;font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:14px;">📊 Price Distribution of Matches</div>', unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(10, 3), facecolor='none')
        ax.hist(filtered_rec['price'], bins=15, color='#e94560', edgecolor='none', alpha=0.85)
        ax.axvline(filtered_rec['price'].mean(), color='#f5a623', linewidth=1.5, linestyle='--', label=f"Avg: ₹{filtered_rec['price'].mean():.0f}L")
        ax.legend(fontsize=8, labelcolor='white', facecolor='none', edgecolor='none')
        ax.set_facecolor('none')
        ax.tick_params(colors='white', labelsize=8)
        ax.set_xlabel('Price (Lakhs)', color='#c9d1d9', fontsize=9)
        ax.set_ylabel('Count', color='#c9d1d9', fontsize=9)
        for spine in ax.spines.values(): spine.set_edgecolor((1,1,1,0.1))
        fig.patch.set_alpha(0)
        st.pyplot(fig)
        st.markdown('</div>', unsafe_allow_html=True)


# =========================
# MAP
# =========================
elif menu == "Map":

    st.markdown('<div style="text-align:center;margin-bottom:24px;"><div style="font-size:1.8rem;font-weight:800;color:#ffffff;">🗺️ Property Map</div><div style="color:#c9d1d9;font-size:0.9rem;letter-spacing:2px;text-transform:uppercase;">Explore listings across Bengaluru</div><div style="width:60px;height:3px;background:linear-gradient(90deg,#e94560,#0f3460);margin:10px auto 0;border-radius:2px;"></div></div>', unsafe_allow_html=True)

    # map filters
    st.markdown('<div style="background:rgba(0,0,0,0.75);border:1px solid rgba(233,69,96,0.4);border-radius:14px;padding:20px;margin-bottom:16px;">', unsafe_allow_html=True)
    st.markdown('<div style="color:#e94560;font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:14px;">🔍 Filter Map</div>', unsafe_allow_html=True)
    mf1, mf2, mf3 = st.columns(3)
    with mf1:
        map_price = st.slider("💰 Max Price (Lakhs)", int(data['price'].min()), int(data['price'].max()), int(data['price'].quantile(0.75)))
    with mf2:
        map_bhk = st.multiselect("🛏️ BHK", sorted(data['bedrooms'].dropna().unique().astype(int).tolist()), default=[])
    with mf3:
        map_area = st.slider("📐 Min Area (sqft)", 300, 5000, 500)
    st.markdown('</div>', unsafe_allow_html=True)

    map_data = data[data['price'] <= map_price]
    map_data = map_data[map_data['area'] >= map_area]
    if map_bhk:
        map_data = map_data[map_data['bedrooms'].isin(map_bhk)]

    # map stats
    s1, s2, s3, s4 = st.columns(4)
    for col, label, val in [
        (s1, "Visible Listings", f"{len(map_data):,}"),
        (s2, "Avg Price", f"₹{map_data['price'].mean():.0f}L" if len(map_data) else "N/A"),
        (s3, "Avg Area", f"{map_data['area'].mean():.0f} sqft" if len(map_data) else "N/A"),
        (s4, "Locations", f"{map_data['location'].nunique()}"),
    ]:
        col.markdown(f"""
        <div style="background:rgba(0,0,0,0.75);border:1px solid rgba(233,69,96,0.5);border-radius:12px;padding:14px;text-align:center;margin-bottom:16px;">
            <div style="color:#c9d1d9;font-size:11px;letter-spacing:1px;text-transform:uppercase;">{label}</div>
            <div style="color:#e94560;font-size:1.4rem;font-weight:800;margin-top:6px;">{val}</div>
        </div>
        """, unsafe_allow_html=True)

    st.map(map_data[['lat', 'lon']])

    # top locations in view
    st.markdown('<div style="background:rgba(0,0,0,0.75);border:1px solid rgba(233,69,96,0.4);border-radius:14px;padding:20px;margin-top:16px;">', unsafe_allow_html=True)
    st.markdown('<div style="color:#e94560;font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:14px;">🏆 Top Locations in Current Filter</div>', unsafe_allow_html=True)
    top_map_locs = map_data.groupby('location').agg(listings=('price','count'), avg_price=('price','mean'), avg_area=('area','mean')).sort_values('listings', ascending=False).head(10).reset_index()
    for _, row in top_map_locs.iterrows():
        st.markdown(f"""
        <div style="display:flex;justify-content:space-between;align-items:center;padding:8px 0;border-bottom:1px solid rgba(255,255,255,0.07);">
            <span style="color:#ffffff;font-size:13px;font-weight:600;">📍 {row['location']}</span>
            <span style="color:#c9d1d9;font-size:12px;">{int(row['listings'])} listings &nbsp;|&nbsp; Avg ₹{row['avg_price']:.0f}L &nbsp;|&nbsp; {row['avg_area']:.0f} sqft</span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# EMI CALCULATOR
# =========================
elif menu == "EMI Calculator":

    st.markdown('<div style="text-align:center;margin-bottom:24px;"><div style="font-size:1.8rem;font-weight:800;color:#ffffff;">💳 EMI Calculator</div><div style="color:#c9d1d9;font-size:0.9rem;letter-spacing:2px;text-transform:uppercase;">Plan your home loan repayment</div><div style="width:60px;height:3px;background:linear-gradient(90deg,#e94560,#0f3460);margin:10px auto 0;border-radius:2px;"></div></div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.markdown('<div style="background:rgba(0,0,0,0.75);border:1px solid rgba(233,69,96,0.5);border-radius:16px;padding:28px;">', unsafe_allow_html=True)
        loan = st.slider("🏦 Loan Amount (₹ Lakhs)", 10, 500, 50)
        rate = st.slider("📊 Annual Interest Rate (%)", 5.0, 20.0, 8.5, step=0.1)
        tenure = st.slider("📅 Tenure (Years)", 1, 30, 20)
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        loan_rs = loan * 100000
        monthly_rate = rate / (12 * 100)
        n = tenure * 12
        emi = (loan_rs * monthly_rate * (1 + monthly_rate)**n) / ((1 + monthly_rate)**n - 1)
        total = emi * n
        interest = total - loan_rs

        st.markdown(f"""
        <div style="background:rgba(0,0,0,0.75);border:1px solid rgba(233,69,96,0.5);border-radius:16px;padding:28px;">
            <div style="color:#e94560;font-size:13px;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:20px;">📋 Loan Summary</div>
            <div style="display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid rgba(255,255,255,0.1);">
                <span style="color:#c9d1d9;">Monthly EMI</span>
                <span style="color:#e94560;font-weight:800;font-size:1.3rem;">₹{emi:,.0f}</span>
            </div>
            <div style="display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid rgba(255,255,255,0.1);">
                <span style="color:#c9d1d9;">Total Amount</span>
                <span style="color:#ffffff;font-weight:700;">₹{total:,.0f}</span>
            </div>
            <div style="display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid rgba(255,255,255,0.1);">
                <span style="color:#c9d1d9;">Principal</span>
                <span style="color:#ffffff;font-weight:700;">₹{loan_rs:,.0f}</span>
            </div>
            <div style="display:flex;justify-content:space-between;padding:12px 0;">
                <span style="color:#c9d1d9;">Total Interest</span>
                <span style="color:#ff6b6b;font-weight:700;">₹{interest:,.0f}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        fig, ax = plt.subplots(figsize=(4, 4), facecolor='none')
        ax.pie([loan_rs, interest], labels=['Principal', 'Interest'],
               colors=['#e94560', '#0f3460'], autopct='%1.1f%%',
               textprops={'color': 'white', 'fontsize': 12})
        ax.set_facecolor('none')
        fig.patch.set_alpha(0)
        st.pyplot(fig)

# =========================
# COMPARE LOCATIONS
# =========================
elif menu == "Compare":

    st.markdown('<div style="text-align:center;margin-bottom:24px;"><div style="font-size:1.8rem;font-weight:800;color:#ffffff;">⚖️ Compare Locations</div><div style="color:#c9d1d9;font-size:0.9rem;letter-spacing:2px;text-transform:uppercase;">Side by side location analysis</div><div style="width:60px;height:3px;background:linear-gradient(90deg,#e94560,#0f3460);margin:10px auto 0;border-radius:2px;"></div></div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2, gap="large")
    with c1:
        loc1 = st.selectbox("📍 Location 1", locations, index=0)
    with c2:
        loc2 = st.selectbox("📍 Location 2", locations, index=1)

    d1 = data[data['location'] == loc1]
    d2 = data[data['location'] == loc2]

    m1, m2, m3 = st.columns(3)
    def stat_card(col, label, v1, v2, fmt="₹{:,.0f}"):
        col.markdown(f"""
        <div style="background:rgba(0,0,0,0.75);border:1px solid rgba(233,69,96,0.5);border-radius:14px;padding:18px;text-align:center;">
            <div style="color:#c9d1d9;font-size:12px;letter-spacing:1px;text-transform:uppercase;margin-bottom:10px;">{label}</div>
            <div style="display:flex;justify-content:space-around;">
                <div><div style="color:#e94560;font-size:11px;">{loc1[:12]}</div><div style="color:#ffffff;font-weight:800;font-size:1.1rem;">{fmt.format(v1)}</div></div>
                <div style="color:#555;">vs</div>
                <div><div style="color:#0f9460;font-size:11px;">{loc2[:12]}</div><div style="color:#ffffff;font-weight:800;font-size:1.1rem;">{fmt.format(v2)}</div></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    stat_card(m1, "Avg Price (Lakhs)", d1['price'].mean(), d2['price'].mean())
    stat_card(m2, "Avg Area (sqft)", d1['area'].mean(), d2['area'].mean(), "{:,.0f} sqft")
    stat_card(m3, "Listings", len(d1), len(d2), "{:,}")

    st.markdown('<div style="margin-top:20px;"></div>', unsafe_allow_html=True)
    fig, axes = plt.subplots(1, 2, figsize=(12, 4), facecolor='none')
    for ax, d, loc, color in zip(axes, [d1, d2], [loc1, loc2], ['#e94560', '#0f9460']):
        ax.hist(d['price'], bins=20, color=color, alpha=0.85, edgecolor='white')
        ax.set_title(loc, color='white', fontsize=13, fontweight='bold')
        ax.set_xlabel('Price (Lakhs)', color='white')
        ax.set_ylabel('Count', color='white')
        ax.tick_params(colors='white')
        ax.set_facecolor('none')
        for spine in ax.spines.values(): spine.set_edgecolor((1,1,1,0.2))
    fig.patch.set_alpha(0)
    st.pyplot(fig)

# =========================
# ADVANCED SEARCH
# =========================
elif menu == "Search":

    st.markdown('<div style="text-align:center;margin-bottom:24px;"><div style="font-size:1.8rem;font-weight:800;color:#ffffff;">🔍 Advanced Property Search</div><div style="color:#c9d1d9;font-size:0.9rem;letter-spacing:2px;text-transform:uppercase;">Filter properties by your criteria</div><div style="width:60px;height:3px;background:linear-gradient(90deg,#e94560,#0f3460);margin:10px auto 0;border-radius:2px;"></div></div>', unsafe_allow_html=True)

    st.markdown('<div style="background:rgba(0,0,0,0.75);border:1px solid rgba(233,69,96,0.5);border-radius:16px;padding:28px;margin-bottom:20px;">', unsafe_allow_html=True)
    f1, f2, f3 = st.columns(3)
    with f1:
        price_range = st.slider("💰 Price Range (Lakhs)", float(data['price'].min()), float(data['price'].max()), (float(data['price'].min()), float(data['price'].max())))
    with f2:
        bed_filter = st.multiselect("🛏️ Bedrooms", sorted(data['bedrooms'].dropna().unique().astype(int).tolist()), default=[])
    with f3:
        loc_filter = st.multiselect("📍 Locations", locations, default=[])
    st.markdown('</div>', unsafe_allow_html=True)

    filtered = data[(data['price'] >= price_range[0]) & (data['price'] <= price_range[1])]
    if bed_filter:
        filtered = filtered[filtered['bedrooms'].isin(bed_filter)]
    if loc_filter:
        filtered = filtered[filtered['location'].isin(loc_filter)]

    st.markdown(f'<div style="background:rgba(233,69,96,0.15);border:1px solid rgba(233,69,96,0.4);border-radius:10px;padding:12px 20px;margin-bottom:16px;color:#ffffff;font-weight:700;">🏠 {len(filtered)} properties found</div>', unsafe_allow_html=True)
    st.dataframe(filtered[['location','area','bedrooms','bathrooms','price']].reset_index(drop=True), use_container_width=True)

    csv = filtered.to_csv(index=False).encode('utf-8')
    st.download_button("⬇️ Download Results as CSV", csv, "filtered_properties.csv", "text/csv")

# =========================
# FINANCE TOOLS
# =========================
elif menu == "Finance":

    st.markdown('<div style="text-align:center;margin-bottom:24px;"><div style="font-size:1.8rem;font-weight:800;color:#ffffff;">💰 Finance Tools</div><div style="color:#c9d1d9;font-size:0.9rem;letter-spacing:2px;text-transform:uppercase;">Affordability & ROI Analysis</div><div style="width:60px;height:3px;background:linear-gradient(90deg,#e94560,#0f3460);margin:10px auto 0;border-radius:2px;"></div></div>', unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🏠 Affordability Checker", "📈 ROI / Rental Yield"])

    with tab1:
        st.markdown('<div style="background:rgba(0,0,0,0.75);border:1px solid rgba(233,69,96,0.5);border-radius:16px;padding:28px;">', unsafe_allow_html=True)
        salary = st.slider("💼 Monthly Salary (₹)", 20000, 500000, 80000, step=5000)
        down_pct = st.slider("💳 Down Payment (%)", 10, 50, 20)
        loan_rate = st.slider("📊 Loan Interest Rate (%)", 5.0, 15.0, 8.5, step=0.1)
        loan_tenure = st.slider("📅 Loan Tenure (Years)", 5, 30, 20)

        max_emi = salary * 0.4
        monthly_rate = loan_rate / (12 * 100)
        n = loan_tenure * 12
        max_loan = max_emi * ((1 + monthly_rate)**n - 1) / (monthly_rate * (1 + monthly_rate)**n)
        max_budget = max_loan / (1 - down_pct / 100)

        st.markdown(f"""
        <div style="margin-top:20px;display:flex;gap:16px;flex-wrap:wrap;">
            <div style="flex:1;background:rgba(233,69,96,0.15);border:1px solid rgba(233,69,96,0.5);border-radius:12px;padding:18px;text-align:center;">
                <div style="color:#c9d1d9;font-size:12px;letter-spacing:1px;">MAX EMI (40% of salary)</div>
                <div style="color:#e94560;font-size:1.5rem;font-weight:800;">₹{max_emi:,.0f}</div>
            </div>
            <div style="flex:1;background:rgba(15,52,96,0.4);border:1px solid rgba(15,148,96,0.5);border-radius:12px;padding:18px;text-align:center;">
                <div style="color:#c9d1d9;font-size:12px;letter-spacing:1px;">MAX LOAN AMOUNT</div>
                <div style="color:#0f9460;font-size:1.5rem;font-weight:800;">₹{max_loan/100000:,.1f}L</div>
            </div>
            <div style="flex:1;background:rgba(233,69,96,0.15);border:1px solid rgba(233,69,96,0.5);border-radius:12px;padding:18px;text-align:center;">
                <div style="color:#c9d1d9;font-size:12px;letter-spacing:1px;">MAX PROPERTY BUDGET</div>
                <div style="color:#ffffff;font-size:1.5rem;font-weight:800;">₹{max_budget/100000:,.1f}L</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div style="background:rgba(0,0,0,0.75);border:1px solid rgba(233,69,96,0.5);border-radius:16px;padding:28px;">', unsafe_allow_html=True)
        prop_price = st.slider("🏠 Property Price (₹ Lakhs)", 10, 500, 80)
        monthly_rent = st.slider("🏷️ Expected Monthly Rent (₹)", 5000, 100000, 20000, step=1000)
        appreciation = st.slider("📈 Annual Appreciation (%)", 0.0, 15.0, 5.0, step=0.5)
        hold_years = st.slider("📅 Holding Period (Years)", 1, 20, 5)

        annual_rent = monthly_rent * 12
        gross_yield = (annual_rent / (prop_price * 100000)) * 100
        future_value = prop_price * (1 + appreciation / 100) ** hold_years
        capital_gain = future_value - prop_price
        total_rental = (annual_rent * hold_years) / 100000
        total_roi = ((capital_gain + total_rental) / prop_price) * 100

        st.markdown(f"""
        <div style="margin-top:20px;display:flex;gap:16px;flex-wrap:wrap;">
            <div style="flex:1;background:rgba(233,69,96,0.15);border:1px solid rgba(233,69,96,0.5);border-radius:12px;padding:18px;text-align:center;">
                <div style="color:#c9d1d9;font-size:12px;letter-spacing:1px;">GROSS RENTAL YIELD</div>
                <div style="color:#e94560;font-size:1.5rem;font-weight:800;">{gross_yield:.2f}%</div>
            </div>
            <div style="flex:1;background:rgba(15,52,96,0.4);border:1px solid rgba(15,148,96,0.5);border-radius:12px;padding:18px;text-align:center;">
                <div style="color:#c9d1d9;font-size:12px;letter-spacing:1px;">FUTURE VALUE</div>
                <div style="color:#0f9460;font-size:1.5rem;font-weight:800;">₹{future_value:.1f}L</div>
            </div>
            <div style="flex:1;background:rgba(233,69,96,0.15);border:1px solid rgba(233,69,96,0.5);border-radius:12px;padding:18px;text-align:center;">
                <div style="color:#c9d1d9;font-size:12px;letter-spacing:1px;">TOTAL ROI ({hold_years}Y)</div>
                <div style="color:#ffffff;font-size:1.5rem;font-weight:800;">{total_roi:.1f}%</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown('<div class="custom-footer">Built by Sagar 🚀 | AI Real Estate System</div>', unsafe_allow_html=True)
