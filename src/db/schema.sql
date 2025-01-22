CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Criação da tabela "Users"
CREATE TABLE IF NOT EXISTS "Users" (
    id SERIAL PRIMARY KEY,
    email VARCHAR UNIQUE NOT NULL,
    name VARCHAR NOT NULL,
    password VARCHAR NOT NULL
);

-- Criação da tabela "Restaurants"
CREATE TABLE IF NOT EXISTS "Restaurants" (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    location VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    category VARCHAR NOT NULL,
    total_grade REAL DEFAULT 0,
    user_id INTEGER
);
ALTER TABLE "Restaurants" ALTER COLUMN total_grade SET DEFAULT 0;
ALTER TABLE "Restaurants" ADD FOREIGN KEY ("user_id") REFERENCES "Users" ("id") ON DELETE CASCADE;

CREATE TABLE IF NOT EXISTS "Menus" (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    menu_photo BYTEA,
    restaurant_id INTEGER,
    user_id INTEGER
);

ALTER TABLE "Menus" ADD FOREIGN KEY ("restaurant_id") REFERENCES "Restaurants" ("id") ON DELETE CASCADE;
ALTER TABLE "Menus" ADD FOREIGN KEY ("user_id") REFERENCES "Users" ("id") ON DELETE CASCADE;

CREATE TABLE IF NOT EXISTS "Reviews" (
    id SERIAL PRIMARY KEY,
    description VARCHAR NOT NULL,
    grade REAL NOT NULL,
    restaurant_id INTEGER,
    user_id INTEGER
);

ALTER TABLE "Reviews" ADD FOREIGN KEY ("restaurant_id") REFERENCES "Restaurants" ("id") ON DELETE CASCADE;
ALTER TABLE "Reviews" ADD FOREIGN KEY ("user_id") REFERENCES "Users" ("id") ON DELETE CASCADE;

CREATE OR REPLACE FUNCTION encrypt_password()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.password IS DISTINCT FROM OLD.password THEN
        NEW.password := md5(NEW.password);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER encrypt_password_trigger
BEFORE INSERT OR UPDATE ON "Users"
FOR EACH ROW
EXECUTE FUNCTION encrypt_password();

CREATE OR REPLACE FUNCTION update_total_grade()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE "Restaurants"
    SET total_grade = (
        SELECT COALESCE(AVG(grade), 0)
        FROM "Reviews"
        WHERE restaurant_id = NEW.restaurant_id
    )
    WHERE id = NEW.restaurant_id;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_total_grade_insert
AFTER INSERT ON "Reviews"
FOR EACH ROW
EXECUTE FUNCTION update_total_grade();

CREATE TRIGGER trigger_update_total_grade_update
AFTER UPDATE ON "Reviews"
FOR EACH ROW
EXECUTE FUNCTION update_total_grade();

CREATE TRIGGER trigger_update_total_grade_delete
AFTER DELETE ON "Reviews"
FOR EACH ROW
EXECUTE FUNCTION update_total_grade();
