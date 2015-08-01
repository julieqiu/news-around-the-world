from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
locations = Table('locations', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('location', String(length=120)),
    Column('latitude', Integer),
    Column('longitude', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['locations'].columns['latitude'].create()
    post_meta.tables['locations'].columns['longitude'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['locations'].columns['latitude'].drop()
    post_meta.tables['locations'].columns['longitude'].drop()
