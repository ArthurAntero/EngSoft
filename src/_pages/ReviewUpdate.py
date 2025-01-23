import time
import streamlit as st
from api.reviews import Review
from api.restaurants import Restaurant
from globals import logged_user

def update_review_page():
    if not logged_user or not logged_user.get("id"):
        st.error("Você precisa estar logado para atualizar uma avaliação.")
        return

    st.title("Atualizar uma Avaliação")

    review_model = Review()
    user_reviews = [
        review for review in review_model.fetch_all_reviews()
        if review["user_id"] == logged_user["id"]
    ]

    if not user_reviews:
        st.info("Você não tem avaliações para atualizar.")
        return

    review_options = ["Selecione uma avaliação"] + [
        f"{review['restaurant_name']} - {review['description'][:30]}..."
        for review in user_reviews
    ]
    selected_review_index = st.selectbox(
        "Selecione uma avaliação para atualizar", options=list(range(len(review_options))), 
        format_func=lambda x: review_options[x]
    )

    selected_review = (
        user_reviews[selected_review_index - 1] if selected_review_index > 0 else None
    )

    if selected_review:
        with st.form(key="update_review_form"):
            description = st.text_area("Descrição da Avaliação", value=selected_review["description"], max_chars=500)
            grade = st.slider("Nota", min_value=0.0, max_value=5.0, step=0.1, value=selected_review["grade"])

            submit_button = st.form_submit_button("Atualizar Avaliação")

            if submit_button:
                if not description:
                    st.error("A descrição deve ser preenchida.")
                    return

                review_model.id = selected_review["id"]
                review_model.description = description
                review_model.grade = grade

                if review_model.update_review():
                    st.success("Avaliação atualizada com sucesso!")
                    time.sleep(1)
                    st.experimental_set_query_params(page="Reviews")
                    st.rerun()
                else:
                    st.error("Falha ao atualizar a avaliação.")
    else:
        st.info("Por favor, selecione uma avaliação para editar.")
