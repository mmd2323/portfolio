import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Mamadou Mbengue | Portfolio",
    layout="wide"
)

# --- CUSTOM STYLING (works with new Streamlit structure) ---
st.markdown("""
    <style>
        /* --- GLOBAL APP BACKGROUND --- */
        [data-testid="stAppViewContainer"] {
            background-color: #F9FAFB !important;
        }

        [data-testid="stHeader"] {
            background: #0C2340 !important;
        }

        [data-testid="stToolbar"] {
            right: 2rem !important;
        }

        /* --- MAIN PAGE CONTAINER --- */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            padding-left: 5%;
            padding-right: 5%;
            color: #0C2340;
            font-family: 'Inter', 'Helvetica Neue', sans-serif;
        }

        /* --- BANNER --- */
        .top-banner {
            background-color: #0C2340;
            color: white;
            padding: 1.2rem 2rem;
            font-size: 24px;
            font-weight: 700;
            text-align: left;
            border-radius: 0 0 8px 8px;
            margin-bottom: 2rem;
        }

        /* --- HEADERS --- */
        h1, h2, h3 {
            color: #0C2340 !important;
            font-weight: 700 !important;
        }

        /* --- TEXT --- */
        p, li {
            color: #1F2937 !important;
            font-size: 16px !important;
            line-height: 1.7 !important;
        }

        /* --- LINKS --- */
        a {
            color: #007E8A !important;
            text-decoration: none !important;
            font-weight: 600 !important;
        }
        a:hover {
            color: #004F54 !important;
            text-decoration: underline !important;
        }

        /* --- BUTTONS --- */
        .stButton>button, .stDownloadButton>button {
            background-color: #007E8A !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 0.6em 1.3em !important;
            font-weight: 600 !important;
            transition: 0.3s !important;
        }
        .stButton>button:hover, .stDownloadButton>button:hover {
            background-color: #004F54 !important;
            color: white !important;
        }

        /* --- FOOTER --- */
        .footer {
            text-align: center;
            font-size: 0.9em;
            color: #6B7280;
            margin-top: 3em;
        }
    </style>
""", unsafe_allow_html=True)

# --- TOP BANNER ---
st.markdown("<div class='top-banner'>Mamadou Mbengue | Portfolio</div>", unsafe_allow_html=True)

# --- HEADER ---
st.title("Mamadou Mbengue")
st.subheader("Financial Mathematics and Economics Student | Aspiring Quantitative Analyst")

st.write("""
Welcome to my professional portfolio.  
I’m a **Financial Mathematics and Economics** student at the **University of Ottawa**,  
focused on applying **quantitative analysis**, **stochastic modeling**, and **machine learning** to financial markets.
""")

st.markdown("---")

# --- CONTACT INFO ---
st.header("Contact Information")
st.markdown("""
📍 Ottawa, Ontario  
📧 [momodouserign00@gmail.com](mailto:momodouserign00@gmail.com)  
🔗 [LinkedIn](https://linkedin.com/in/mamadou-mbengue-29968122a)  
💻 [GitHub](https://github.com/mmd2323)
""")

st.markdown("---")

# --- ABOUT SECTION ---
st.header("About Me")
st.write("""
I am a **fourth-year Financial Mathematics and Economics student** at the University of Ottawa.  
My background bridges **economics**, **statistics**, and **programming** to analyze complex financial systems.  
I have practical experience in **data analysis**, **stochastic calculus**, and **machine learning applications** in finance.  
My passion lies in **quantitative modeling**, **risk management**, and **financial prediction** using mathematical and computational tools.
""")

st.markdown("---")

# --- PROJECTS SECTION ---
st.header("Featured Projects")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Research on Stochastic Processes and Financial Modeling")
    st.write("""
    Conducted research on **stochastic calculus** applications in finance  
    as part of my **Research Assistant position** at the University of Ottawa.  
    Topics included **martingales**, **Brownian motion**, **Itô’s lemma**, and **stochastic differential equations**.  
    Implemented **Python simulations** to demonstrate the **Black–Scholes model**, **Greeks**, and **jump-diffusion processes**.
    """)
    st.link_button("🔗 View Research Repository",
                   "https://github.com/mmd2323/Research-on-Stochastic-Processes-and-Financial-Modeling")

with col2:
    st.markdown("### MAT4372 – Machine Learning Portfolio Optimization")
    st.write("""
    Built a **Random Forest–based model** to optimize ETF portfolios (**VFV.TO**, **VCN.TO**)  
    by estimating **Sharpe ratios** and visualizing the **efficient frontier** in **R (ggplot2)**.  
    Combined **quantitative finance**, **machine learning**, and **portfolio theory**.
    """)
    st.link_button("🔗 View Project Repository",
                   "https://github.com/mmd2323/MAT4372-Machine-Learning-Portfolio-Optimization")

st.markdown("---")

# --- RESUME DOWNLOAD SECTION ---
st.header("Download My Resume")
with open("Mamadou_Mbengue_Resume_ENG.pdf", "rb") as file:
    st.download_button(
        label="📄 Download Resume (PDF)",
        data=file,
        file_name="Mamadou_Mbengue_Resume_ENG.pdf",
        mime="application/pdf"
    )

st.markdown("<div class='footer'>© 2025 Mamadou Mbengue · University of Ottawa<br><span style='color:#007E8A;'>Financial Mathematics & Economics</span></div>", unsafe_allow_html=True)
