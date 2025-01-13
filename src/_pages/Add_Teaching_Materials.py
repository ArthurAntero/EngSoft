import streamlit as st
from api.teaching_materials import TeachingMaterial

def create_page():
    allowed_categories = [
        'LAB_EQUIPMENT',
        'EXPERIMENT_KITS', 
        'DIAGRAMS',
        'SAFETY_EQUIPMENT',
        'PRECISION_TOOLS',
        'REPORT_WRITING_TOOLS',
        'OTHER', 
    ]

    st.header('Add a New Teaching Material')

    description = st.text_input('Description')
    category = st.selectbox("Category", allowed_categories)
    date_acquisition = st.date_input('Date Acquisition')
    serie_number = st.number_input('Serie Number')
    conservation_status = st.selectbox('Conservation Status', ['NEW', 'AVERAGE', 'OLD', 'DAMAGED'])
    physical_location = st.text_input('Physical Location')
    material_cover_url = st.text_input('Material Cover URL')
    status = st.selectbox("Status", ['AVAILABLE', 'BORROWED'])

    if st.button('Save'):
        new_material = TeachingMaterial(
            description=description,
            category=category,
            date_acquisition=date_acquisition,
            serie_number=serie_number,
            conservation_status=conservation_status,
            physical_location=physical_location,
            material_cover_url=material_cover_url,
            status=status,
        )
        
        if new_material.create_teaching_material():
            st.success('Teaching material inserted successfully!')
        else:
            st.error('Error inserting teaching material.')
