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
        'OTHER'
    ]

    st.header('Edit Teaching Material')

    # Get the material ID from the user
    material_id = st.text_input('Enter Teaching Material ID:')
    material = None

    # Check if the material ID is provided and retrieve the material
    if material_id:
        material = TeachingMaterial(id=material_id).get_teaching_material_by_id()

    if material:
        # Display current material information in input boxes
        description = st.text_input('Description', material.description)
        category = st.selectbox("Category", allowed_categories, index=allowed_categories.index(material.category))
        date_acquisition = st.date_input('Date Acquisition', material.date_acquisition)
        serie_number = st.number_input('Serie Number', float(material.serie_number))
        conservation_status = st.selectbox(
            'Conservation Status', 
            ['NEW', 'AVERAGE', 'OLD', 'DAMAGED'],
            index=['NEW', 'AVERAGE', 'OLD', 'DAMAGED'].index(material.conservation_status)
        )
        physical_location = st.text_input('Physical Location', material.physical_location)
        material_cover_url = st.text_input('Material Cover URL', material.material_cover_url)
        status = st.selectbox("Status", ['AVAILABLE', 'BORROWED'], index=['AVAILABLE', 'BORROWED'].index(material.status))

        if st.button('Save Changes'):
            # Update the teaching material with the new information
            material.description = description
            material.category = category
            material.date_acquisition = date_acquisition
            material.serie_number = serie_number
            material.conservation_status = conservation_status
            material.physical_location = physical_location
            material.material_cover_url = material_cover_url
            material.status = status

            if material.update_teaching_material():
                st.success('Teaching material updated successfully!')
            else:
                st.error('Error updating teaching material.')
    else:
        st.warning('Please enter a valid Teaching Material ID.')
