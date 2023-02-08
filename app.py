import streamlit as st 
import pandas as pd  
import plotly.express as px  
import base64  
from io import StringIO, BytesIO  


st.set_page_config(page_title='Excel Plotter')
st.title('Excel Render Graph')

user = """
<form>
<input type="text" name="name" placeholder="First Name" required>
<input type="text" name="last name" placeholder="Last Name" required>
<input type="text" name="DOB" placeholder="Date of Birth" required>

"""


st.markdown(user, unsafe_allow_html=True)


st.subheader('Choose your excel file below')

uploaded_file = st.file_uploader('Choose a XLSX file', type='xlsx')
if uploaded_file:
    st.markdown('---')
    df = pd.read_excel(uploaded_file, engine='openpyxl')
    st.dataframe(df)
    groupby_column = st.selectbox(
        'Financial Income and Expense',
        ('Expense', 'Expense'),
    )

    # Group df
    output_columns = ['Income', 'Expense']
    df_grouped = df.groupby(by=[groupby_column], as_index=False)[output_columns].sum()

    # -- Plot df
    fig = px.bar(
        df_grouped,
        x=groupby_column,
        y='Income',
        color='Expense',
        color_continuous_scale=['red', 'yellow'],
        template='plotly_white',
        title=f'Income and Expenses'
    )
    st.plotly_chart(fig)

