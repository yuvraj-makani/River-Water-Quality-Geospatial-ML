import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Ganga Water Quality Prediction",
    page_icon="🌊",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main-title {
    font-size: 38px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
}

.section-title {
    font-size: 24px;
    font-weight: 600;
    margin-top: 15px;
    margin-bottom: 15px;
}

div.stButton > button {
    width: 100%;
    height: 50px;
    font-size: 18px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# TITLE
# ============================================================

st.markdown(
    '<div class="main-title">🌊 Ganga River Water Quality Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Satellite-Based Assessment using Machine Learning'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# MODEL DIRECTORY
# ============================================================

MODEL_DIR = Path("models")


# ============================================================
# LOAD TRAINED MODELS
# ============================================================

@st.cache_resource
def load_models():

    models = {}

    models["DO"] = joblib.load(
        MODEL_DIR / "DO_RF.joblib"
    )

    models["BOD"] = joblib.load(
        MODEL_DIR / "BOD_CatBoost.joblib"
    )

    models["COD"] = joblib.load(
        MODEL_DIR / "COD_RF.joblib"
    )

    models["pH"] = joblib.load(
        MODEL_DIR / "pH_CatBoost.joblib"
    )

    models["EC"] = joblib.load(
        MODEL_DIR / "EC_CatBoost.joblib"
    )

    models["Temperature"] = joblib.load(
        MODEL_DIR / "Temperature_RF.joblib"
    )

    return models


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("📌 Project Information")

    st.write(
        """
        This application uses satellite-derived and
        environmental features to predict water-quality
        parameters of the Ganga River.
        """
    )

    st.markdown("### 🛰️ Input Features")

    st.write("🔵 Sentinel-2 Blue Band")
    st.write("🟢 Sentinel-2 Green Band")
    st.write("🔴 Sentinel-2 Red Band")
    st.write("🌃 VIIRS Night-time Light")
    st.write("🌍 LULC")

    st.markdown("---")

    st.markdown("### 🤖 ML Models")

    st.write("Random Forest")
    st.write("CatBoost")


# ============================================================
# INPUT SECTION
# ============================================================

st.markdown(
    '<div class="section-title">'
    '🛰️ Satellite & Environmental Inputs'
    '</div>',
    unsafe_allow_html=True
)

st.info(
    "Enter the feature values for the location to generate "
    "water-quality predictions."
)


col1, col2 = st.columns(2)


# ------------------------------------------------------------
# LEFT COLUMN
# ------------------------------------------------------------

with col1:

    blue = st.number_input(
        "🔵 Blue Band (B2)",
        min_value=0.0,
        value=0.10,
        step=0.001,
        format="%.4f"
    )

    green = st.number_input(
        "🟢 Green Band (B3)",
        min_value=0.0,
        value=0.12,
        step=0.001,
        format="%.4f"
    )

    red = st.number_input(
        "🔴 Red Band (B4)",
        min_value=0.0,
        value=0.08,
        step=0.001,
        format="%.4f"
    )


# ------------------------------------------------------------
# RIGHT COLUMN
# ------------------------------------------------------------

with col2:

    viirs = st.number_input(
        "🌃 VIIRS Night-time Light",
        min_value=0.0,
        value=10.0,
        step=0.1,
        format="%.2f"
    )

    lulc = st.number_input(
        "🌍 LULC Class",
        min_value=0,
        max_value=4,
        value=2,
        step=1
    )

    st.caption(
        "LULC: 0 = Waterbody | 1 = Cropland | "
        "2 = Vegetation | 3 = Built-up | 4 = Barren Land"
    )


# ============================================================
# CREATE INPUT DATAFRAME
# ============================================================

input_data = pd.DataFrame({

    "Blue": [blue],
    "Green": [green],
    "Red": [red],
    "VIIRS": [viirs],
    "LULC": [lulc]

})


# ============================================================
# SHOW INPUT DATA
# ============================================================

with st.expander("🔍 View Input Values"):

    st.dataframe(
        input_data,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# PREDICT BUTTON
# ============================================================

st.markdown("")

predict_button = st.button(
    "🚀 PREDICT WATER QUALITY",
    type="primary"
)


# ============================================================
# PREDICTION
# ============================================================

if predict_button:

    try:

        # Load models
        models = load_models()

        # ----------------------------------------------------
        # Generate predictions
        # ----------------------------------------------------

        do_prediction = models["DO"].predict(
            input_data
        )[0]

        bod_prediction = models["BOD"].predict(
            input_data
        )[0]

        cod_prediction = models["COD"].predict(
            input_data
        )[0]

        ph_prediction = models["pH"].predict(
            input_data
        )[0]

        ec_prediction = models["EC"].predict(
            input_data
        )[0]

        temperature_prediction = models["Temperature"].predict(
            input_data
        )[0]


        # ====================================================
        # RESULTS
        # ====================================================

        st.markdown("---")

        st.markdown(
            '<div class="section-title">'
            '📊 Predicted Water Quality Parameters'
            '</div>',
            unsafe_allow_html=True
        )


        # ----------------------------------------------------
        # ROW 1
        # ----------------------------------------------------

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                label="💧 Dissolved Oxygen",
                value=f"{do_prediction:.2f} mg/L"
            )

        with c2:

            st.metric(
                label="🧪 BOD",
                value=f"{bod_prediction:.2f} mg/L"
            )

        with c3:

            st.metric(
                label="⚗️ COD",
                value=f"{cod_prediction:.2f} mg/L"
            )


        # ----------------------------------------------------
        # ROW 2
        # ----------------------------------------------------

        c4, c5, c6 = st.columns(3)

        with c4:

            st.metric(
                label="🧬 pH",
                value=f"{ph_prediction:.2f}"
            )

        with c5:

            st.metric(
                label="⚡ Electrical Conductivity",
                value=f"{ec_prediction:.2f} μS/cm"
            )

        with c6:

            st.metric(
                label="🌡️ Temperature",
                value=f"{temperature_prediction:.2f} °C"
            )


        # ====================================================
        # RESULTS TABLE
        # ====================================================

        st.markdown("### 📋 Prediction Summary")

        results = pd.DataFrame({

            "Parameter": [
                "Dissolved Oxygen (DO)",
                "Biochemical Oxygen Demand (BOD)",
                "Chemical Oxygen Demand (COD)",
                "pH",
                "Electrical Conductivity (EC)",
                "Temperature"
            ],

            "Predicted Value": [
                do_prediction,
                bod_prediction,
                cod_prediction,
                ph_prediction,
                ec_prediction,
                temperature_prediction
            ],

            "Unit": [
                "mg/L",
                "mg/L",
                "mg/L",
                "—",
                "μS/cm",
                "°C"
            ]

        })

        st.dataframe(
            results,
            use_container_width=True,
            hide_index=True
        )


        # ====================================================
        # SUCCESS MESSAGE
        # ====================================================

        st.success(
            "✅ Water-quality prediction generated successfully "
            "using the trained machine-learning models."
        )


    except FileNotFoundError as e:

        st.error(
            "❌ Model files were not found."
        )

        st.write(
            "Make sure the 'models' folder is in the same "
            "directory as app.py."
        )

        st.code(str(e))


    except Exception as e:

        st.error(
            "❌ An error occurred while generating the prediction."
        )

        st.code(str(e))


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "IIT Roorkee Internship Project | "
    "Ganga River Water Quality Assessment using "
    "Remote Sensing & Machine Learning"
)