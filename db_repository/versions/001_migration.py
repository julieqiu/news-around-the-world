from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
locations = Table('locations', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('location', String(length=120)),
)

tweets = Table('tweets', post_meta,
    Column('t_url', String(length=120), primary_key=True, nullable=False),
    Column('r_url', String(length=300)),
    Column('headline', String(length=300)),
    Column('t_location', String(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['locations'].create()
    post_meta.tables['tweets'].columns['t_location'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['locations'].drop()
    post_meta.tables['tweets'].columns['t_location'].drop()
