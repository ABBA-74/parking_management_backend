-- Créer la base de données
CREATE DATABASE parking_db;

-- Créer l'utilisateur avec un mot de passe à définir par l'utilisateur
CREATE USER park_user WITH PASSWORD 'P@rk2024';

-- Attribuer les droits à l'utilisateur sur la base de données - attention mode developpement unique
GRANT ALL PRIVILEGES ON DATABASE parking_db TO park_user;