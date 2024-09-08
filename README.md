# Parking Management Backend

## Configuration de la base de données PostgreSQL

1. Ouvrez votre terminal ou pgAdmin.
<br/>
2. Connectez-vous à PostgreSQL en tant qu'utilisateur `postgres`.
- Avec le terminal, exécutez :
    ```
    psql -U postgres
    ```
<br/>

3. Exécutez le script SQL situé dans le dossier `db_setup/setup_db.sql`.

   ```bash
   psql -U postgres -f db_setup/setup_db.sql
    ```
<br/>

Remarque : Pour un déploiement en production:
- Il est recommandé de ne pas accorder tous les privilèges à l'utilisateur de la base de données. Limitez les privilèges aux opérations nécessaires, telles que SELECT, INSERT, UPDATE, et DELETE. Voici un exemple de commandes SQL pour restreindre les privilèges :
```sql
GRANT CONNECT ON DATABASE parking_db TO park_user;
GRANT USAGE ON SCHEMA public TO park_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO park_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO park_user;
```
<br/>

- Il est également fortement recommandé de modifier le mot de passe par défaut (P@rk2024) et, si nécessaire, de changer le nom de l'utilisateur et de la base de données dans le script SQL. Veillez à mettre à jour ces informations dans le fichier settings.py :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'parking_db',  # Changez ce nom si vous modifiez la base de données
        'USER': 'park_user',  # Changez ce nom si vous modifiez l'utilisateur
        'PASSWORD': 'P@rk2024',  # Remplacez par un mot de passe sécurisé pour la production
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```