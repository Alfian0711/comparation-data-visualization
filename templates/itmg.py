import pandas as pd
import streamlit as st

def show():
    data = pd.read_csv('itmg_fix.csv')
    
    for df in [data]:
        try:
            df['Date'] = pd.to_datetime(df['Date'], utc=True).dt.tz_localize(None)
        except Exception as e:
            st.error(f"Terjadi kesalahan saat memproses kolom Date: {e}")
            st.stop() 
        df['Date'] = pd.to_datetime(df['Date'])

    itmg = data[(data['Date'].dt.year >= 2014) & (data['Date'].dt.year <= 2024)]
    st.subheader('Harga Saham Pertambangan ITMG')
    st.text("Grafik saham ITMG dalam rentang 10 tahun")

    chart_data = pd.DataFrame({
        'Tanggal': itmg['Date'],  
        'ITMG': itmg['Close']
    })

    st.line_chart(data=chart_data.set_index('Tanggal'), color='#FF0000')

    df = pd.read_csv('dataset_dividen\Deviden Yield Percentage ITMG.csv')
    st.title("**Analisa Emiten ITMG**")
    st.subheader("**Total dividen ITMG**")
    dividen = pd.DataFrame({
        'Tahun':df['Tahun'],
        'total_dividen' : df['Jumlah Dividen']
        })
    st.bar_chart(dividen.set_index('Tahun'))

    st.subheader("**Persentase Dividen Yield pertahun ITMG (%)**")
    dividen = pd.DataFrame({
        'Tahun':df['Tahun'],
        'total_dividen' : df['Yield Percentage']
        })
    st.bar_chart(dividen.set_index('Tahun'))

    st.subheader("**Harga rata rata saham pertahunnya (Close)**")
    dividen = pd.DataFrame({
        'Tahun':df['Tahun'],
        'total_dividen' : df['Rata-rata Close']
        })
    st.bar_chart(dividen.set_index('Tahun'))