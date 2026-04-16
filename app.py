
import streamlit as st
import pandas as pd

st.set_page_config(page_title="YouTube Trending Data Lakehouse", page_icon="📊", layout="wide")

# -----------------------------
# Data
# -----------------------------
kpis = {
    "Clean Records": "2.59M",
    "Countries": "10",
    "Global Top Category": "Sports",
    "Raw Records Analysed": "2.8M+",
}

top_distinct_categories = pd.DataFrame([
    {"Country": "BR", "Category Title": "Entertainment", "Total Videos": 5417, "Percentage": 22.79},
    {"Country": "DE", "Category Title": "Entertainment", "Total Videos": 7709, "Percentage": 25.09},
    {"Country": "FR", "Category Title": "Entertainment", "Total Videos": 7548, "Percentage": 22.97},
    {"Country": "GB", "Category Title": "Entertainment", "Total Videos": 5643, "Percentage": 20.25},
    {"Country": "IN", "Category Title": "Entertainment", "Total Videos": 21281, "Percentage": 42.35},
    {"Country": "JP", "Category Title": "Entertainment", "Total Videos": 5658, "Percentage": 32.09},
    {"Country": "KR", "Category Title": "Entertainment", "Total Videos": 5122, "Percentage": 33.75},
    {"Country": "MX", "Category Title": "Entertainment", "Total Videos": 4195, "Percentage": 23.92},
    {"Country": "CA", "Category Title": "Gaming", "Total Videos": 6594, "Percentage": 21.36},
    {"Country": "US", "Category Title": "Gaming", "Total Videos": 6226, "Percentage": 21.61},
])

strategy_df = pd.DataFrame([
    {"Group": "Gaming markets", "Countries": "US, CA, JP, MX", "Recommended category": "Gaming"},
    {"Group": "People & Blogs markets", "Countries": "IN, KR", "Recommended category": "People & Blogs"},
    {"Group": "Global default", "Countries": "Broad market baseline", "Recommended category": "Sports"},
])

# -----------------------------
# Style
# -----------------------------
st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    .hero {
        padding: 1.3rem 1.5rem 1rem 1.5rem;
        border-radius: 24px;
        background: linear-gradient(135deg, #faf7ff 0%, #f4efff 100%);
        border: 1px solid #ece4ff;
        margin-bottom: 1rem;
    }

    .hero h1 {
        margin: 0;
        font-size: 2.6rem;
        color: #24124d;
    }

    .hero p {
        margin-top: 0.45rem;
        margin-bottom: 0;
        font-size: 1.05rem;
        color: #5d4e82;
    }

    .tag-row {
        display: flex;
        gap: 0.5rem;
        flex-wrap: wrap;
        margin-top: 0.9rem;
    }

    .tag {
        padding: 0.35rem 0.8rem;
        border-radius: 999px;
        background: #efe7ff;
        color: #5b2fb5;
        font-size: 0.9rem;
        font-weight: 600;
        border: 1px solid #e1d3ff;
    }

    .kpi-card {
        background: white;
        border: 1px solid #ece4ff;
        border-radius: 22px;
        padding: 1.1rem 1.2rem;
        box-shadow: 0 6px 18px rgba(76, 38, 145, 0.05);
    }

    .kpi-label {
        color: #6c5b95;
        font-size: 0.95rem;
        margin-bottom: 0.25rem;
    }

    .kpi-value {
        color: #24124d;
        font-size: 2rem;
        font-weight: 700;
        line-height: 1.1;
    }

    .panel {
        background: white;
        border: 1px solid #ece4ff;
        border-radius: 22px;
        padding: 1rem 1.1rem 1.2rem 1.1rem;
        box-shadow: 0 6px 18px rgba(76, 38, 145, 0.05);
        height: 100%;
    }

    .panel-title {
        font-size: 1.35rem;
        font-weight: 700;
        color: #24124d;
        margin-bottom: 0.7rem;
    }

    .callout {
        background: linear-gradient(135deg, #faf6ff 0%, #f2eafe 100%);
        border: 1px solid #e6d8ff;
        border-radius: 18px;
        padding: 1rem;
        margin-bottom: 1rem;
    }

    .callout h3 {
        margin: 0 0 0.5rem 0;
        color: #6d35cc;
        font-size: 1.45rem;
    }

    .callout p, .callout li {
        color: #3b3158;
        font-size: 1rem;
    }

    .footer-box {
        margin-top: 1rem;
        background: linear-gradient(135deg, #faf7ff 0%, #f1ebff 100%);
        border: 1px solid #ece4ff;
        border-radius: 20px;
        padding: 1rem 1.2rem;
        color: #4f4470;
    }

    div[data-testid="stDataFrame"] div[role="table"] {
        border-radius: 16px;
        overflow: hidden;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown("""
<div class="hero">
    <h1>YouTube Trending Data Lakehouse</h1>
    <p>End-to-end data pipeline for ingesting, cleaning, and analyzing <b>2.8M+</b> YouTube trending records using Snowflake and Azure Blob Storage.</p>
    <div class="tag-row">
        <div class="tag">Snowflake</div>
        <div class="tag">Azure Blob</div>
        <div class="tag">SQL</div>
        <div class="tag">Data Cleaning</div>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# KPI row
# -----------------------------
k1, k2, k3, k4 = st.columns(4)
for col, (label, value) in zip([k1, k2, k3, k4], kpis.items()):
    with col:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">{label}</div>
                <div class="kpi-value">{value}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("")

# -----------------------------
# Main layout
# -----------------------------
left, right = st.columns([1.45, 1], gap="large")

with left:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">Top Distinct Categories by Country</div>', unsafe_allow_html=True)

    search = st.text_input("Filter country", placeholder="Type a country code such as FR, US, MX")
    df = top_distinct_categories.copy()
    if search:
        df = df[df["Country"].str.contains(search.upper(), na=False)]

    sort_by = st.selectbox(
        "Sort by",
        ["Country", "Total Videos", "Percentage"],
        index=0,
    )
    ascending = st.toggle("Ascending order", value=True)

    if sort_by == "Country":
        df = df.sort_values("Country", ascending=ascending)
    else:
        df = df.sort_values(sort_by, ascending=ascending)

    show_percent_bar = st.toggle("Show percentage bar", value=True)

    styled = df.copy()
    styled["Percentage"] = styled["Percentage"].map(lambda x: f"{x:.2f}%")

    if show_percent_bar:
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Country": st.column_config.TextColumn("Country"),
                "Category Title": st.column_config.TextColumn("Category Title"),
                "Total Videos": st.column_config.NumberColumn("Total Videos", format="%d"),
                "Percentage": st.column_config.ProgressColumn(
                    "Percentage",
                    format="%.2f%%",
                    min_value=0.0,
                    max_value=50.0,
                ),
            },
        )
    else:
        st.dataframe(
            styled,
            use_container_width=True,
            hide_index=True,
        )

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">Global vs Local Strategy</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="callout">
        <h3>Global Winner: Sports</h3>
        <p>But country-level preferences differ, so a single playbook is not ideal.</p>
        <ul>
            <li><b>US, CA, JP, MX</b> → Gaming</li>
            <li><b>IN, KR</b> → People &amp; Blogs</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Recommendation")
    st.write("Use a **global default + local override** strategy.")
    st.write(
        "Keep **Sports** as the broad global baseline, but adapt content strategy by market where local category preferences are stronger."
    )

    st.dataframe(strategy_df, use_container_width=True, hide_index=True)

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Pipeline + notes
# -----------------------------
st.markdown("")
p1, p2 = st.columns([1.2, 1], gap="large")

with p1:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">Pipeline Overview</div>', unsafe_allow_html=True)
    st.markdown(
        """
        **Azure Blob Storage**  
        ↓  
        **Snowflake External Tables**  
        ↓  
        **Cleaning & Transformation**  
        ↓  
        **Final Analytical Table**
        """
    )
    st.markdown('</div>', unsafe_allow_html=True)

with p2:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">Data Quality Notes</div>', unsafe_allow_html=True)
    st.markdown("""
    - Missing category values handled  
    - Invalid video IDs removed  
    - Duplicates isolated with `ROW_NUMBER()`  
    - Final clean dataset: **2,597,494 rows**
    """)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="footer-box">
This dashboard demonstrates data engineering, SQL analytics, cloud pipeline design, and business insight generation.
</div>
""", unsafe_allow_html=True)
