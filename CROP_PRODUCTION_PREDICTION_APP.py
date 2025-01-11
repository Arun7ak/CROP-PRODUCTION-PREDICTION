#IMPORTING LIBRARIES FOR CREATING STREAMLIT APP
import streamlit as st
import pandas as pd
import joblib

# SET PAGE NAME
st.set_page_config("CROP PRODUCTION PREDICTION")


#SET TITLE
st.markdown(
    """
    <h1 style="text-align: center; color: #005cbf; font-size: 36px; margin-top: -50px;">
        CROPS PRODUCTION PREDICTION
    </h1>
    """,
    unsafe_allow_html=True
    )



#CREATING NOTE ABOUT THE APP IN SIDEBAR
st.sidebar.markdown("## ABOUT THIS APPLICATION")
st.sidebar.write("""
This app predicts crop production based on various inputs like:
- Item Code
- Area Harvested
- Yield Value
- Producing Animals/Slaughtered Value
- Laying Value
- Yield/Carcass Weight Value
- Milk Animals Value
""")


# CREATING INPUT BOX TO GET INPUT FROM USERS
area_harvested = st.number_input('Enter the Area Harvested (in Hectares)', min_value=0.0)
yield_value = st.number_input('Enter the Yield Value (kg/ha(or)mg/Ar)', min_value=0.0)
producing_animals_slaughtered_value = st.number_input('Enter the Producing Animals/Slaughtered Value (An)', min_value=0.0)
laying_value = st.number_input('Enter the Laying Value (An)', min_value=0.0)
yield_carcass_weight_value = st.number_input('Enter the Yield/Carcass Weight Value (g/An)', min_value=0.0)
milk_animals_value = st.number_input('Enter the Milk Animals Value (An)', min_value=0.0)


#LOAD THE TRAINED MODEL
model = joblib.load(r'c:\Users\arune\OneDrive\Desktop\CROP PRODUCTION PREDICTION.pkl')


#CREATING PREDICT BUTTON AND PREDICT THE PRODUCTION VALUE USING TRAINED MODEL
if st.button('Predict Production'):
    input_data = pd.DataFrame([[
        
        area_harvested,
        yield_value,
        producing_animals_slaughtered_value,
        laying_value,
        yield_carcass_weight_value,
        milk_animals_value
    ]], columns=[
        
        'Area_Harvested_in_Hectares',
        'Yield_Value in kg/ha(or)mg/Ar',
        'Producing Animals/Slaughtered_Value in An',
        'Laying_Value in An',
        'Yield/Carcass Weight_Value in g/An',
        'Milk Animals_Value in An'
    ])


    #PREDICT THE PRODUCTION 
    production = model.predict(input_data)[0]

    #DISPLAY THE PREDICTED RESULT
    st.write(f"Predicted Production: {production.round(3)} Kilo tonnes")

#GIVE SPACE BETWEEN THE TABLE AND PREDICTION
st.write("\n")
st.write("\n")
st.write("\n")


#SET TITLE FOR TABLE
st.sidebar.markdown("CROP PRODUCTION REFERENCES TABLE:")
st.write("\n")
st.write("\n")


#CREATING THE DATAFRAME FOR USER REFERENCES TO GIVE INPUT
CROP_DATA = pd.read_csv("CLEANED_CROP_DATASET.csv")
st.sidebar.dataframe(CROP_DATA,hide_index = True)
 
  