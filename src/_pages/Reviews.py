import streamlit as st
import time
from api.reviews import Review
from globals import logged_user

def list_reviews_page():

    if not logged_user or not logged_user.get("id"):
        st.error("Você precisa estar logado para visualizar as avaliações.")
        return

    review_model = Review()
    reviews = review_model.fetch_all_reviews()

    st.title("Todas as Avaliações")

    if not reviews:
        st.info("Nenhuma avaliação encontrada.")
    else:
        for review in reviews:
            review_id = review.get("id")
            description = review.get("description")
            grade = review.get("grade")
            user_name = review.get("user_name")
            restaurant_name = review.get("restaurant_name")
            user_id = review.get("user_id")

            with st.container():
                st.subheader(f"Restaurante: {restaurant_name}")
                st.write(f"**Usuário:** {user_name}")
                st.write(f"**Descrição:** {description}")
                st.write(f"**Nota:** {grade:.1f} estrelas")

                if user_id == logged_user["id"]:
                    if st.button("Excluir Avaliação", key=f"delete_{review_id}", help="Excluir esta avaliação"):
                        if review_model.delete_review(review_id):
                            st.success("Avaliação excluída com sucesso!")
                            time.sleep(2)
                            st.rerun()
                        else:
                            st.error("Falha ao excluir a avaliação.")
                st.markdown("---")
