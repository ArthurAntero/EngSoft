import streamlit as st
from globals import logged_user
from api.teaching_materials import TeachingMaterial

DIV_MAIN = f'''
    display: flex; 
    padding: 2rem; 
    color: black; 
    flex-direction: row;
    border-radius: 2rem;
'''

TEXT = f'''
    display: flex; 
    flex-direction: column; 
    flex-wrap: wrap; 
    margin-left: 20px; 
    word-wrap: break-word; 
    max-width: 20rem;
'''

IMAGE_STYLE = f'''
    height: 50%; 
    width: 35%; 
    align-self: center;
'''

def create_page():

    with open('src/globals.py', 'r') as file:
        exec(file.read())

    def get_teaching_material_color(teachingMaterial_index):
        colors = ["#FFDDC1", "#C2EABD", "#AED9E0", "#FFD3B5", "#D4A5A5"]
        return colors[teachingMaterial_index % len(colors)]

    st.header('List of Teaching Materials')

    # Search menu
    search_term = st.text_input("Search by id, description, category, date acquisition, serie number, etc.")

    teaching_materials = TeachingMaterial().get_teaching_materials()

    if teaching_materials:
        for index, teaching_material in enumerate(teaching_materials):
            # Filter teaching materials based on search term
            if (
                not search_term
                or search_term.lower() in str(teaching_material.id).lower()
                or search_term.lower() in teaching_material.description.lower()
                or search_term.lower() in teaching_material.category.lower()
                or search_term.lower() in str(teaching_material.date_acquisition).lower()
                or search_term.lower() in teaching_material.serie_number.lower()
                or search_term.lower() in teaching_material.conservation_status.lower()
                or search_term.lower() in teaching_material.physical_location.lower()
                or search_term.lower() in teaching_material.status.lower()
                # Add more conditions as needed
            ):
                background_color = get_teaching_material_color(index)

                st.markdown(
                    f'<div style="{DIV_MAIN} background-color: {background_color};">'
                        f'<div style="flex: 1; padding-right: 10px;">'
                            f'<h2 style="color: black">ID: {teaching_material.id}</h2>'
                            f'<div style="{TEXT}">'
                                f'<p>Description: {teaching_material.description}</p>'
                                f'<p>Category: {teaching_material.category}</p>'
                                f'<p>Date Acquisition: {teaching_material.date_acquisition}</p>'
                                f'<p>Serie Number: {teaching_material.serie_number}</p>'
                                f'<p>Conservation Status: {teaching_material.conservation_status}</p>'
                                f'<p>Physical Location: {teaching_material.physical_location}</p>'
                                f'<p>Status: {teaching_material.status}</p>'
                            f'</div>'
                        f'</div>'
                        f'<img src="{teaching_material.material_cover_url}" alt="Teaching Material Cover" style="{IMAGE_STYLE}">'
                    f'</div>',
                    unsafe_allow_html=True
                )
                if logged_user["role"] == 'ADMIN' and teaching_material.status == 'AVAILABLE':
                    st.text('')
                    if st.button("Delete", key=teaching_material.id, use_container_width=True):
                        TeachingMaterial(id=teaching_material.id).delete_teaching_material()
                        st.experimental_rerun()
                elif logged_user["role"] == 'ADMIN' and teaching_material.status != 'AVAILABLE':
                    st.text('You cannot delete a teaching_material that is on loan')
                
                st.text('')
