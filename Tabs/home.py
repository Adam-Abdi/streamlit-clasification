import streamlit as st


def app():
    # Judul Halaman Aplikasi
    st.title('Aplikasi Prediksi Peminjaman Nasabah')
    # Penjelasan Website 
    st.write('Pada Website ini menjelaskan tentang kelayakan calon nasabah untuk mendapatkan bantuan pinjaman,')
    st.write('Dengan menginputkan data-data dibawah ini, Sehingga dapat menentukan kelayakan calon nasabah tersebut.')
    st.write('1. Status Pernikahan')
    st.write('2. Status Pendidikan')
    st.write('3. Banyaknya tanggungan anak')
    st.write('4. Apakah nasabah adalah seorang Wiraswasta?')
    st.write('5. Pendapatan calon nasabah ($)')
    st.write('6. Pendapatan penjamin calon nasabah ($)')
    st.write('7. Jumlah Pinjaman ($)')
    st.write('8. Total cicilan (Perbulan)')
    st.write('9. Catatan Credit')
    st.write('10. Area tempat tinggal')
