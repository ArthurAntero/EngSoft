import streamlit as st
import time
from api.menus import Menu
from globals import logged_user
import io
from PIL import Image

def list_menus_page():

    if not logged_user or not logged_user.get("id"):
        st.error("Você precisa estar logado para visualizar os menus.")
        return
    
    menu_model = Menu()
    menus = menu_model.fetch_all_menus()

    st.title("Todos os Menus")

    st.markdown("---")

    if not menus:
        st.info("Nenhum menu encontrado.")
    else:
        for menu in menus:
            menu_id = menu.get("id")
            name = menu.get("name")
            description = menu.get("description")
            menu_photo = menu.get("menu_photo")
            restaurant_name = menu.get("restaurant_name")
            user_id = menu.get("user_id")

            with st.container():
                st.write(f"Restaurante: {restaurant_name}")
                st.write(f"**Nome:** {name}")
                st.write(f"**Descrição:** {description}")

                if menu_photo:
                    try:
                        menu_photo_bytes = bytes(menu_photo)
                        image = Image.open(io.BytesIO(menu_photo_bytes))

                        max_width = 300
                        image.thumbnail((max_width, max_width))

                        st.image(image, use_column_width=False)
                    except Exception as e:
                        st.error(f"Erro ao exibir a imagem: {e}")
                else:
                    st.write("Nenhuma imagem disponível.")

                if user_id == logged_user["id"]:
                    if st.button("Excluir Menu", key=f"delete_{menu_id}", help="Excluir este menu"):
                        if menu_model.delete_menu(menu_id):
                            st.success("Menu excluído com sucesso!")
                            time.sleep(2)
                            st.rerun()
                        else:
                            st.error("Falha ao excluir o menu.")

                st.markdown("---")
