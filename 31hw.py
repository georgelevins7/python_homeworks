import streamlit as st
import requests
import time

try:
    with st.spinner("Loading products..."):
        time.sleep(1)
        response = requests.get("https://fakestoreapi.com/products")
        data = response.json()
except Exception as e:
    st.error(f"Failed to load products: {e}")
    response.raise_for_status()
    st.stop()

st.sidebar.title("Filter Products")
categories = list(set([product['category'] for product in data]))
selected_category = st.sidebar.selectbox("Select Category", ["All"] + categories)
selected_price_range = st.sidebar.slider("Select a price range", 0, 1000, 500)
search = st.sidebar.text_input("Search Products")
if search:
    data = [product for product in data if search.lower() in product['title'].lower()]
st.write("### <span style='font-size:36px'>Product List</span>", unsafe_allow_html=True)

for product in data:
    if selected_category != "All" and product['category'] != selected_category:
        continue
    if product['price'] > selected_price_range:
        continue
    st.write(f"**<span style='color:cyan; font-size:18px'>{product['title']}</span>**", unsafe_allow_html=True)
    st.write(f"<span style='color:lightgreen; font-size:12px'>{product['category']}</span>", unsafe_allow_html=True)
    st.image(product['image'], width=150)
    st.write(f"<span style='color:yellow; font-size:18px'><b>${product['price']}</b></span>", unsafe_allow_html=True)
    st.expander("Description").write(f"Item number: <span style='color:orange'>{product['id']}</span><br><span style='color:lightblue'>{product['description']}</span>", unsafe_allow_html=True)
    if 'rating' in product:
        rate = product['rating']['rate']
        color = "red" if rate < 4 else "green"
        st.markdown(f"Rating: <span style='color:{color}'>{rate}</span> (Count: <span style='color:orange'>{product['rating']['count']}</span>)", unsafe_allow_html=True)
    
    st.divider()
if not data:
    st.error("Failed to load products")
