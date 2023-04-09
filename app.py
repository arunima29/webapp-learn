import streamlit as st

import pandas as pd


Year_List=[2,3,4,5,6,7,8,9,10]


st.write("""

# Compound Interest Calculator!

""")



st.sidebar.header('User Input Values')



def user_input_features():

    Int_Rate = st.sidebar.slider('Interest Rate in %', 6.0, 42.0, 10.0)

    	##st.sidebar.add_rows

    Principal = st.sidebar.text_input('Please input Principal Amount',10000)

    	##st.sidebar.add_rows

    No_Of_Years = st.sidebar.selectbox('Select No Of Years',Year_List, 2)



    data = {'Int_Rate': Int_Rate,	
            'Principal': Principal,	
            'No_Of_Years': No_Of_Years}
    features = pd.DataFrame(data, index=[0])
    return features



df = user_input_features()

st.subheader('User Entered parameters for Rate, Principal amount and No of years is')

st.write(df)

################################
st.write('# Solution using a dataframe')

if 'data' not in st.session_state:
    data = pd.DataFrame({'colA':[],'colB':[],'colC':[],'colD':[]})
    st.session_state.data = data

data = st.session_state.data

st.dataframe(data)

def add_dfForm():
    row = pd.DataFrame({'colA':[st.session_state.input_colA],
            'colB':[st.session_state.input_colB],
            'colC':[st.session_state.input_colC],
            'colD':[st.session_state.input_colD]})
    st.session_state.data = pd.concat([st.session_state.data, row])


dfForm = st.form(key='dfForm')
with dfForm:
    dfColumns = st.columns(4)
    with dfColumns[0]:
        st.text_input('colA', key='input_colA')
    with dfColumns[1]:
        st.text_input('colB', key='input_colB')
    with dfColumns[2]:
        st.text_input('colC', key='input_colC')
    with dfColumns[3]:
        st.text_input('colD', key='input_colD')
    st.form_submit_button(on_click=add_dfForm)
    
    
st.write(dfColumns) 


