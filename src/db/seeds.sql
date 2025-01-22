-- Inserção de usuários
INSERT INTO "Users" (email, name, password)
VALUES
('user@email', 'user', '123456'),
('user2@email', 'user2', '123456');

-- Inserção de restaurantes
INSERT INTO "Restaurants" (name, location, description, category, user_id)
VALUES
('Restaurante A', 'Brasília', 'Um excelente restaurante brasileiro.', 'Brasileira', 1),
('Restaurante B', 'São Paulo', 'Restaurante especializado em culinária italiana.', 'Italiana', 2);

-- Inserção de uma avaliação
INSERT INTO "Reviews" (description, grade, restaurant_id, user_id)
VALUES
('Ótima comida e ambiente agradável!', 4.5, 1, 1);