import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

st.title("Dashboard Analisis Data E-Commerce")

# =====================
# LOAD DATA
# =====================
@st.cache_data
def load_data():
    orders = pd.read_csv('orders_dataset.csv')
    payments = pd.read_csv('order_payments_dataset.csv')
    reviews = pd.read_csv('order_reviews_dataset.csv')

    # cleaning ringan
    reviews['review_comment_message'].fillna('No Comment', inplace=True)

    orders['order_purchase_timestamp'] = pd.to_datetime(
        orders['order_purchase_timestamp']
    )

    # merge
    df = orders.merge(payments, on='order_id')
    df = df.merge(reviews, on='order_id')

    df['order_month'] = df['order_purchase_timestamp'].dt.to_period('M')

    return df

df = load_data()

# =====================
# SIDEBAR FILTER
# =====================
st.sidebar.header("Filter Data")

min_score, max_score = st.sidebar.slider(
    "Filter Review Score",
    1, 5, (1, 5)
)

filtered_df = df[
    (df['review_score'] >= min_score) &
    (df['review_score'] <= max_score)
]

# =====================
# METRICS
# =====================
st.subheader("Ringkasan Data")

col1, col2, col3 = st.columns(3)

col1.metric("Total Order", filtered_df['order_id'].nunique())
col2.metric("Rata-rata Payment", round(filtered_df['payment_value'].mean(), 2))
col3.metric("Rata-rata Review", round(filtered_df['review_score'].mean(), 2))

# =====================
# VISUALISASI 1
# =====================
st.subheader("Tren Jumlah Transaksi per Bulan")

monthly_orders = filtered_df.groupby('order_month')['order_id'].nunique()

fig, ax = plt.subplots()
monthly_orders.plot(ax=ax)
ax.set_title("Jumlah Transaksi")
st.pyplot(fig)

# =====================
# VISUALISASI 2
# =====================
st.subheader("Rata-rata Pembayaran per Bulan")

monthly_payment = filtered_df.groupby('order_month')['payment_value'].mean()

fig, ax = plt.subplots()
monthly_payment.plot(ax=ax)
ax.set_title("Rata-rata Payment")
st.pyplot(fig)

# =====================
# VISUALISASI 3
# =====================
st.subheader("Hubungan Payment dan Review")

fig, ax = plt.subplots()
sns.scatterplot(
    data=filtered_df,
    x='payment_value',
    y='review_score',
    ax=ax
)
st.pyplot(fig)

# =====================
# INSIGHT
# =====================
st.subheader("Insight")

st.write("""
- Transaksi menunjukkan pola fluktuatif setiap bulan  
- Nilai pembayaran tidak memiliki hubungan kuat dengan skor review  
- Kepuasan pelanggan kemungkinan dipengaruhi faktor lain seperti pengiriman  
""")