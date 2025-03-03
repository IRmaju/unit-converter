import streamlit as st

# 🔹 Global dictionary define karo
conversions = {
    'Length': {
        'meters': 1, 'kilometers': 0.001, 'miles': 0.000621371, 'feet': 3.28084
    },
    'Weight': {
        'grams': 1, 'kilograms': 0.001, 'pounds': 0.00220462, 'ounces': 0.035274
    },
    'Temperature': {
        'Celsius': lambda c: c, 
        'Fahrenheit': lambda c: (c * 9/5) + 32, 
        'Kelvin': lambda c: c + 273.15
    }
}

def convert_units(value, from_unit, to_unit, category):
    if category == 'Temperature':
        return conversions[category][to_unit](value) if from_unit == 'Celsius' else None
    
    return value * (conversions[category][to_unit] / conversions[category][from_unit])

st.title(" Unit Converter")

category = st.selectbox("Choose a category", ["Length", "Weight", "Temperature"])

if category:
    units = list(conversions[category].keys())  # ✅ Yeh error ab solve ho jayega
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    
    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit, category)
        st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")


