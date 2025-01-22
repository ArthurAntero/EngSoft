import streamlit as st
import time
from api.restaurants import Restaurant
from globals import logged_user

def list_restaurants_page():

    if not logged_user or not logged_user.get("id"):
        st.error("Você precisa estar logado para visualizar os restaurantes.")
        return

    st.header("Restaurantes")
    st.markdown("---")

    restaurant_model = Restaurant()
    restaurants = restaurant_model.fetch_all_restaurants()

    if not restaurants:
        st.info("Nenhum restaurante encontrado.")
        return

    for restaurant in restaurants:
        restaurant_id = restaurant.get("id")
        name = restaurant.get("name")
        category = restaurant.get("category")
        description = restaurant.get("description")
        location = restaurant.get("location")
        total_grade = restaurant.get("total_grade")

        with st.container():
            st.subheader(name)
            st.write(f"**Categoria:** {category}")
            st.write(f"**Descrição:** {description}")
            st.write(f"**Localização:** {location}")
            st.write(f"**Avaliação:** {total_grade:.1f} estrelas")

            if restaurant.get("user_id") == logged_user["id"]:
                if st.button(f"Excluir {name}", key=f"delete_{restaurant_id}"):
                    if restaurant_model.delete_restaurant(restaurant_id):
                        st.success(f"Restaurante '{name}' excluído com sucesso.")
                        time.sleep(2)
                        st.rerun()
                    else:
                        st.error(f"Falha ao excluir o restaurante '{name}'.")
        st.markdown("---")
