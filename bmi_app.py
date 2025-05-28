import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️")
st.title("⚖️ BMI Calculator")
st.write("Enter your weight and height to calculate your Body Mass Index (BMI).")

# Inputs
weight = st.number_input("Weight (kg)", min_value=1.0, step=0.1)
height = st.number_input("Height (m)", min_value=0.5, step=0.01)

# Calculate BMI
if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    st.metric(label="Your BMI", value=f"{bmi:.2f}")

    # Categorize BMI
    if bmi < 18.5:
        st.warning("You are underweight.")
    elif 18.5 <= bmi < 25:
        st.success("You are in the normal range.")
    elif 25 <= bmi < 30:
        st.info("You are overweight.")
    else:
        st.error("You are obese.")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
