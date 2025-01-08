For this beauty to work it needs some setting up:
alembic needs setting up
    pip install alembic
    alembic init migrations

after setting up alembic alembic.ini in line 64 needs the db link added
migrations.env.py line 24 needs target_metada = Base.metadata
users db login needs to be setup and added/imported into modules.database.py
