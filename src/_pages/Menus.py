import streamlit as st
from api.menus import Menu
from globals import logged_user
import io
from PIL import Image

def list_menus_page():

    if not logged_user or not logged_user.get("id"):
        st.error("You must be logged in to see Menus.")
        return
    
    menu_model = Menu()
    menus = menu_model.fetch_all_menus()

    st.title("All Menus")

    st.markdown("---")

    if not menus:
        st.info("No menus found.")
    else:
        for menu in menus:
            menu_id = menu.get("id")
            name = menu.get("name")
            description = menu.get("description")
            menu_photo = menu.get("menu_photo")
            restaurant_name = menu.get("restaurant_name")
            user_id = menu.get("user_id")

            with st.container():
                st.write(f"Restaurant: {restaurant_name}")
                st.write(f"**Name:** {name}")
                st.write(f"**Description:** {description}")

                if menu_photo:
                    try:
                        menu_photo_bytes = bytes(menu_photo)
                        image = Image.open(io.BytesIO(menu_photo_bytes))

                        max_width = 300
                        image.thumbnail((max_width, max_width))

                        st.image(image, use_column_width=False)
                    except Exception as e:
                        st.error(f"Error displaying image: {e}")
                else:
                    st.write("No image available.")

                if user_id == logged_user["id"]:
                    if st.button("Delete Menu", key=f"delete_{menu_id}", help="Delete this menu"):
                        if menu_model.delete_menu(menu_id):
                            st.success("Menu deleted successfully!")
                            st.rerun()
                        else:
                            st.error("Failed to delete the menu.")

                st.markdown("---")
