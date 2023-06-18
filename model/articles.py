from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy import Table, Column
from config.db import meta, engine

article = Table('articles', meta,
                Column('id', Integer, primary_key=True),
                Column('image', String(255)),
                Column('profile-image', String(255)),
                Column('picture-description', String(255)),
                Column('title', String(255)),
                Column('introduction', String(255)),
                Column('article', String(255)),
                Column('category', String(255)),
                Column('author', String(255)),
                Column('date', String(255)),
                )

meta.create_all(engine)
