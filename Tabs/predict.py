import streamlit as st

from web_functions import predict


def app(df, x, y):

    st.title('Halaman Prediksi')

    col1, col2, col3 = st.columns(3)

    with col1:
        Married = st.text_input('Status Pernikahan')
    with col1:
        Dependents = st.text_input('Tanggungan Anak')
    with col1:
        Education = st.text_input('Pendidikan')
    with col1:
        Self_Employed = st.text_input('Wiraswasta?')
    with col1:
        ApplicantIncome = st.text_input('Pendapatan calon Nasabah ($)')
    with col2:
        CoapplicantIncome = st.text_input('Pendapatan Penjamin calon Nasabah ($)')
    with col2:
        LoanAmount = st.text_input('Jumlah Pinjaman')
    with col2:
        Loan_Amount_Term = st.text_input('Total Cicilan yang diajukan (Month)')
    with col2:
        Credit_History = st.text_input('Catatan Credit')
    with col2:
        Property_Area = st.text_input('Area tempat tinggal')
    with col3:
        st.caption('''
        Status Pernikahan : \n
        Belum/Tidak Menikah   = 0,      Menikah = 1 \n
        ''')
    with col3:
        st.caption('''
        Tanggungan Anak : 
        0 Anak   = 0,
        1 Anak = 1,
        2 Anak = 2,
        Lebih dari 3 Anak = 3 \n
        ''')
    with col3:
        st.caption('''
        Pendidikan : 
        Lulus   = 1,
        Tidak Lulus = 0 \n
        ''')
    with col3:
        st.caption('''
        Wiraswasta?: 
        Tidak   = 0,
        Ya = 1 \n
        ''')
    with col3:
        st.caption('''
        Area tempat tinggal :
        Pedesaan   = 0, 
        Pinggiran Kota = 1,
        Perkotaan = 2 \n
        ''')

    features = [Married, Dependents, Education, Self_Employed, ApplicantIncome,
                CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area]

    # tombol prediksi
    if st.button('Prediksi'):
        prediction, score = predict(x, y, features)
        score = score
        st.info('Prediksi Sukses...')

        if (prediction[0] == 1):
            st.success('Nasabah mendapat Pinjaman')
        else:
            st.warning('Nasabah TIDAK mendapat pinjaman')

        st.write('Model yang digunakan memiliki tingkat akurasi ',
                 (score*100), '%')
