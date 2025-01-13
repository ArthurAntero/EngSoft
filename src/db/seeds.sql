-- Inserção de livros
INSERT INTO Books (isbn, title, author, description, category, date_acquisition, conservation_status, physical_location, book_cover_url, status) VALUES
  (1015, 'Departure', 'Alan Wake', 'Não é um lago, é um oceano', 'SCIFI', '2023-11-21', 'NEW', 'primeira fileira da direita', 'https://thumbs.dreamstime.com/b/livro-gen%C3%A9rico-1325496.jpg', 'AVAILABLE'),
  (1016, 'Return', 'Alan Wake', 'Não é um lago, é um oceano', 'SCIFI', '2023-11-21', 'NEW', 'primeira fileira da esquerda', 'localhost:5001', 'AVAILABLE'),
  (1017, 'Alex casy', 'Alan Wake', 'Não é um lago, é um oceano', 'SCIFI', '2023-11-21', 'NEW', 'primeira fileira da frente', 'localhost:5002', 'AVAILABLE');

-- Inserção de usuários
INSERT INTO Users (username, first_name, last_name, password, role, user_photo_url) VALUES
  ('nome123', 'Pafuncio', 'Pinto', '123456', 'ADMIN', 'https://box4pets.com.br/cdn/shop/products/Designsemnome_24_1024x.png?v=1636485929'),
  ('nome456', 'Nina', 'Oliveira', '654321', 'MEMBER', 'localhost:5001'),
  ('nome789', 'Tapioca', 'Silva', '13579', 'MEMBER', 'localhost:5002'),
  ('nome9', 'Tilti', 'Costa', '13579', 'MEMBER', 'localhost:5003');

-- Inserção de materiais de ensino
INSERT INTO Teaching_materials (description, category, date_acquisition, conservation_status, physical_location, material_cover_url, status, serie_number) VALUES
  ('paquimetro', 'LAB_EQUIPMENT', '2023-11-19', 'NEW', 'primeira fileira da direita', 'https://cdn.awsli.com.br/600x450/1995/1995567/produto/138383485/0e53b522b2.jpg', 'AVAILABLE', '123'),
  ('multimetro', 'LAB_EQUIPMENT', '2023-11-20', 'NEW', 'primeira fileira da esquerda', 'localhost:5001', 'AVAILABLE', '321'),
  ('amperimetro', 'LAB_EQUIPMENT', '2023-11-21', 'NEW', 'primeira fileira da frente', 'localhost:5002', 'AVAILABLE', '555');

-- Inserção de empréstimos
INSERT INTO Loan (loan_date, expected_return_date, status, id_book, id_user)
  VALUES ('2023-11-14', '2023-11-21', 'IN_PROGRESS', 1015, 2),
  ('2023-11-15', '2023-11-22', 'IN_PROGRESS', 1016, 3),
  ('2023-11-16', '2023-11-23', 'IN_PROGRESS', 1017, 4);
