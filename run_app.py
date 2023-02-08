import streamlit as st 
import pandas as pd  
import plotly.express as px  


st.set_page_config(page_title='Excel Plotter')
st.title('Excel Render Graph')

user_information = """
    <form>
        <input type="text" name="name" placeholder="First Name" required>
        <input type="text" name="last name" placeholder="Last Name" required>
        <input type="text" name="DOB" placeholder="Date of Birth" required>
    </form>
"""

st.markdown(user_information, unsafe_allow_html=True)


#opening, reading a css document that styles the user information form
def css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#calling the css function
css('style.css')

st.subheader('Choose your excel file below')

#upload file
uploaded_file = st.file_uploader('Choose excel file', type='xlsx')
if uploaded_file:
    st.markdown('---')
    df = pd.read_excel(uploaded_file, engine='openpyxl')
    st.dataframe(df)
    group_by_column = st.selectbox(
        'Financial Income and Expense',
        ('Expense', 'Expense'),
    )

    # group df
    columns = ['Income', 'Expense']
    df_grouped = df.groupby(by=[group_by_column], as_index=False)[columns].sum()

    # plot df
    plot_elements = px.bar(
        df_grouped,
        x = group_by_column,
        y = 'Income',
        color = 'Expense',
        color_continuous_scale = ['green', 'blue', 'red'],
        template = 'plotly_white',
        title = f'Income and Expenses'
    )
    st.plotly_chart(plot_elements)






