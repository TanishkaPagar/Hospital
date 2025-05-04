import streamlit as st
from datetime import date

# Initialize session state to hold the hospital ledger
if 'hospital_ledger_advanced' not in st.session_state:
    st.session_state.hospital_ledger_advanced = {}

# Function to add or update patient visits
def add_patient_visit_advanced(patient_name, treatment, cost, date_of_visit):
    visit = {
        "patient_name": patient_name,
        "treatment": treatment,
        "cost": cost,
        "date_of_visit": str(date_of_visit)  # convert to string for display
    }

    if patient_name not in st.session_state.hospital_ledger_advanced:
        st.session_state.hospital_ledger_advanced[patient_name] = []
    st.session_state.hospital_ledger_advanced[patient_name].append(visit)
    st.success(f"Visit added for {patient_name} on {date_of_visit} for treatment '{treatment}' costing ${cost}.")

# Streamlit UI
st.title("🏥 Advanced Hospital Ledger")

st.header("Add Patient Visit")
patient_name = st.text_input("Patient Name")
treatment = st.text_input("Treatment")
cost = st.number_input("Cost", min_value=0, step=1)
date_of_visit = st.date_input("Date of Visit", value=date.today())

if st.button("Add Visit"):
    if patient_name and treatment:
        add_patient_visit_advanced(patient_name, treatment, cost, date_of_visit)
    else:
        st.warning("Please fill in all required fields.")

# Display ledger
st.header("📋 Hospital Ledger")
if st.session_state.hospital_ledger_advanced:
    for patient, visits in st.session_state.hospital_ledger_advanced.items():
        st.subheader(f"Patient: {patient}")
        for visit in visits:
            st.write(f"Treatment: {visit['treatment']} | Cost: ${visit['cost']} | Date: {visit['date_of_visit']}")
else:
    st.info("No visits recorded yet.")
