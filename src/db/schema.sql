CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS Users (
    id SERIAL PRIMARY KEY,
    email VARCHAR UNIQUE NOT NULL,
    name VARCHAR NOT NULL,
    password VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS Restaurants (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    location VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    category VARCHAR NOT NULL,
    total_grade REAL,
    user_id INTEGER
);

ALTER TABLE "restaurants" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id") ON DELETE CASCADE;

CREATE TABLE IF NOT EXISTS Menu (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    menu_photo VARCHAR,
    restaurant_id INTEGER,
    user_id INTEGER
);

ALTER TABLE "menu" ADD FOREIGN KEY ("restaurant_id") REFERENCES "restaurants" ("id") ON DELETE CASCADE;
ALTER TABLE "menu" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id") ON DELETE CASCADE;

CREATE TABLE IF NOT EXISTS Review (
    id SERIAL PRIMARY KEY,
    description VARCHAR NOT NULL,
    grade REAL NOT NULL,
    restaurant_id INTEGER,
    user_id INTEGER
);

ALTER TABLE "review" ADD FOREIGN KEY ("restaurant_id") REFERENCES "restaurants" ("id") ON DELETE CASCADE;
ALTER TABLE "review" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id") ON DELETE CASCADE;


CREATE OR REPLACE FUNCTION encrypt_password()
RETURNS TRIGGER AS $$
BEGIN
    NEW.password := md5(NEW.password);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER encrypt_password_trigger
BEFORE INSERT OR UPDATE ON Users
FOR EACH ROW
EXECUTE FUNCTION encrypt_password();

CREATE OR REPLACE FUNCTION update_total_grade()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE Restaurants
    SET total_grade = (
        SELECT COALESCE(AVG(grade), 0)
        FROM Review
        WHERE restaurant_id = NEW.restaurant_id
    )
    WHERE id = NEW.restaurant_id;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_total_grade_insert
AFTER INSERT ON Review
FOR EACH ROW
EXECUTE FUNCTION update_total_grade();

CREATE TRIGGER trigger_update_total_grade_update
AFTER UPDATE ON Review
FOR EACH ROW
EXECUTE FUNCTION update_total_grade();

CREATE TRIGGER trigger_update_total_grade_delete
AFTER DELETE ON Review
FOR EACH ROW
EXECUTE FUNCTION update_total_grade();
