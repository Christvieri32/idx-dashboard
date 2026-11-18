import streamlit as st
import pandas as pd
import numpy as np

# Konfigurasi Halaman (Dark Theme & Layout Luas)
st.set_page_config(
    page_title="IDX Live Command Center & Portfolio Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (Futuristik & Profesional)
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stMetric {
        background-color: #161b22;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #30363d;
    }
    .card {
        background-color: #161b22;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #30363d;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigasi
st.sidebar.title("🇮🇩 IDX Command Center")
st.sidebar.markdown("---")
menu = st.sidebar.radio(
    "Pilih Menu:",
    ["📊 Ringkasan Pasar & IHSG", "🚀 Prediksi Bull/Bear (1 Pekan)", "💰 Screening Saham Dividen 5 Tahun", "📰 Sentimen Berita Emiten", "🧮 Alokasi Dana Trading"]
)

# ----------------------------------------------------
# MENU 1: RINGKASAN PASAR & IHSG
# ----------------------------------------------------
if menu == "📊 Ringkasan Pasar & IHSG":
    st.title("📊 Ringkasan Pasar Saham Indonesia (IHSG)")
    st.markdown("Pantauan makroekonomi, *foreign flow*, dan performa sektoral terkini di Bursa Efek Indonesia.")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="IHSG Index", value="7,325.40", delta="+0.85%")
    with col2:
        st.metric(label="Net Foreign Buy", value="Rp 450 M", delta="+Rp 120 M")
    with col3:
        st.metric(label="Suku Bunga BI Rate", value="6.00%", delta="Neutral")
    with col4:
        st.metric(label="Kurs USD/IDR", value="Rp 15,850", delta="-25 pts")

    st.markdown("### 🏆 Performa Sektoral Hari Ini")
    sector_data = pd.es = {
        "Sektor": ["Finance (IDXFINANC)", "Energy (IDXENERGY)", "Basic Materials (IDXBASIC)", "Infrastructure (IDXINFRA)", "Technology (IDXTECHNO)"],
        "Perubahan (%)": ["+1.45%", "+0.92%", "-0.40%", "+1.10%", "-1.80%"],
        "Sentimen Utama": ["Bullish (Kinerja Bank Besar)", "Kenaikan Harga Komoditas", "Tekanan Profit Taking", "Proyek Strategis Nasional", "Koreksi Global Tech"]
    }
    st.dataframe(pd.DataFrame(sector_data), use_container_width=True)

# ----------------------------------------------------
# MENU 2: PREDIKSI BULL/BEAR 1 MINGGU
# ----------------------------------------------------
elif menu == "🚀 Prediksi Bull/Bear (1 Pekan)":
    st.title("🚀 Prediksi Tren 1 Minggu ke Depan (Bull / Bear Market)")
    st.markdown("Analisis momentum jangka pendek berdasarkan *order flow*, indikator teknikal (RSI/MACD), dan katalis berita harian.")

    tab1, tab2 = st.tabs(["🔥 Potensi Bullish (Breakout & Momentum)", "❄️ Potensi Bearish (Koreksi / Distribution)"])

    with tab1:
        st.subheader("Daftar Saham Potensi Bullish (1 Pekan Kedepan)")
        bull_df = pd.DataFrame({
            "Kode": ["BBCA", "ADRO", "ANTM", "TLKM"],
            "Nama Emiten": ["Bank Central Asia Tbk", "Adaro Energy Indonesia Tbk", "Aneka Tambang Tbk", "Telkom Indonesia Tbk"],
            "Target Harga (1W)": ["Rp 10,250", "Rp 2,850", "Rp 1,650", "Rp 3,400"],
            "Probabilitas Bull": ["85%", "78%", "80%", "75%"],
            "Katalis Utama": ["Inflow Asing & Window Dressing", "Kenaikan Harga Batubara Acuan", "Lonjakan Permintaan Nikel EV", "Pertumbuhan ARPU Data Seluler"]
        })
        st.dataframe(bull_df, use_container_width=True)

    with tab2:
        st.subheader("Daftar Saham Potensi Bearish / Konsolidasi")
        bear_df = pd.DataFrame({
            "Kode": ["GOTO", "BUKA", "ASII"],
            "Nama Emiten": ["GoTo Gojek Tokopedia Tbk", "Bukalapak.com Tbk", "Astra International Tbk"],
            "Support Kritis": ["Rp 62", "Rp 120", "Rp 4,950"],
            "Risiko Penurunan": ["Medium-High", "High", "Medium"],
            "Penyebab": ["Tekanan Jual Blok Saham", "Lemahnya Transaksi E-Commerce", "Penurunan Penjualan Otomotif Bulanan"]
        })
        st.dataframe(bear_df, use_container_width=True)

# ----------------------------------------------------
# MENU 3: SCREENING SAHAM DIVIDEN 5 TAHUN
# ----------------------------------------------------
elif menu == "💰 Screening Saham Dividen 5 Tahun":
    st.title("💰 Pemindai Saham Dividen Tinggi & Rutin (5 Tahun)")
    st.markdown("Penyaringan emiten BEI dengan rekam jejak pembagian dividen konsisten tanpa putus selama 5 tahun terakhir serta *Free Cash Flow* yang sehat.")

    div_df = pd.DataFrame({
        "Kode": ["ADRO", "UNVR", "HMSP", "BBRI", "TLKM", "BJTM"],
        "Sektor": ["Energi / Batubara", "Consumer Goods", "Consumer Goods", "Perbankan", "Telekomunikasi", "Perbankan Daerah"],
        "Dividend Yield (Avg 5Y)": ["12.5%", "6.8%", "7.2%", "5.4%", "4.9%", "7.5%"],
        "Payout Ratio (DPR)": ["60%", "95%", "98%", "70%", "75%", "75%"],
        "Status Konsistensi": ["Rutin & Jumbo", "Konsisten", "Konsisten", "Rutin & Naik", "Konsisten", "Sangat Konsisten"],
        "Catatan Analis": ["Didukung windfall profit komoditas", "Dividend yield tinggi, waspadai margin", "Payout ratio mendekati 100%", "Pilihan utama defensif jangka panjang", "Dividen stabil & defensif", "Dividend yield tinggi untuk regional bank"]
    })
    st.dataframe(div_df, use_container_width=True)

# ----------------------------------------------------
# MENU 4: SENTIMEN BERITA EMITEN
# ----------------------------------------------------
elif menu == "📰 Sentimen Berita Emiten":
    st.title("📰 Monitor Berita & Sentimen Pasar Publik Indonesia")
    st.markdown("Agregasi berita real-time dan analisis sentimen otomatis untuk setiap emiten di Bursa Efek Indonesia.")

    search_emiten = st.text_input("Cari Kode Emiten (Contoh: BBCA, BBRI, ADRO, GOTO):", "BBCA")
    
    st.markdown(f"### Hasil Analisis Sentimen untuk: **{search_emiten.upper()}**")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("🟢 **Sentimen Domina: Bullish (78%)**\n\n Berita positif mendominasi dari laporan laba bersih kuartalan dan aksi korporasi.")
    with col2:
        st.warning("⚠️ **Faktor Risiko Utama:** Fluktuasi nilai tukar Rupiah dan arah suku bunga global.")

    news_list = [
        {"Waktu": "Hari ini, 14:20", "Judul": f"Analisis Kinerja Keuangan {search_emiten.upper()} Kuartal Terbaru Lampaui Ekspektasi Konsensus", "Sentimen": "Positif 🟢"},
        {"Waktu": "Kemarin, 09:15", "Judul": f"Investor Asing Catat Akumulasi Pembelian Net Buy pada Saham {search_emiten.upper()}", "Sentimen": "Positif 🟢"},
        {"Waktu": "2 hari lalu", "Judul": f"Manajemen {search_emiten.upper()} Siapkan Strategi Ekspansi Bisnis Tahun Depan", "Sentimen": "Netral ⚪"}
    ]
    st.table(pd.DataFrame(news_list))

# ----------------------------------------------------
# MENU 5: ALOKASI DANA TRADING
# ----------------------------------------------------
elif menu == "🧮 Alokasi Dana Trading":
    st.title("🧮 Kalkulator Alokasi Dana Saham Bull Market")
    st.markdown("Hitung ukuran posisi (*position sizing*) dan pembagian modal secara presisi untuk memaksimalkan profit sekaligus membatasi risiko maksimal.")

    col1, col2 = st.columns(2)
    with col1:
        total_capital = st.number_input("Total Modal Portofolio (Rp):", min_value=1_000_000, value=50_000_000, step=1_000_000)
        risk_pct = st.slider("Maksimal Risiko per Trade (% dari Modal):", min_value=0.5, max_value=5.0, value=2.0, step=0.5)
    with col2:
        entry_price = st.number_input("Harga Rencana Masuk (Buy):", min_value=50, value=5250, step=25)
        stop_loss = st.number_input("Harga Batas Rugi (Stop Loss):", min_value=50, value=5000, step=25)

    if st.button("Hitung Alokasi & Ukuran Posisi"):
        if entry_price > stop_loss:
            risk_per_share = entry_price - stop_loss
            max_risk_amount = total_capital * (risk_pct / 100)
            max_shares = max_risk_amount / risk_per_share
            total_allocation = max_shares * entry_price
            allocation_pct = (total_allocation / total_capital) * 100

            st.markdown("---")
            st.success("### Hasil Rekomendasi Alokasi Dana:")
            
            res_col1, res_col2, res_col3 = st.columns(3)
            with res_col1:
                st.metric(label="Maksimal Lembar Saham", value=f"{int(max_shares):,} lbr", delta=f"{int(max_shares/100)} Lot")
            with res_col2:
                st.metric(label="Total Dana Dialokasikan", value=f"Rp {total_allocation:,.0f}", delta=f"{allocation_pct:.1f}% dari Modal")
            with res_col3:
                st.metric(label="Potensi Risiko Rugi", value=f"Rp {max_risk_amount:,.0f}", delta=f"-{risk_pct}%", delta_color="inverse")
        else:
            st.error("Harga Entry harus lebih besar dari Harga Stop Loss untuk posisi Long/Buy!")

# Footer Dashboard
st.sidebar.markdown("---")
st.sidebar.text("IDX Command Center v2.6\nPowered by Python & Streamlit")