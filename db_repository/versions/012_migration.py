from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
tags = Table('tags', post_meta,
    Column('tweet_id', Integer),
    Column('location_id', Integer),
)

tweets = Table('tweets', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('t_url', String),
    Column('headline', String),
    Column('t_location', String),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['tags'].create()
    pre_meta.tables['tweets'].columns['t_location'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['tags'].drop()
    pre_meta.tables['tweets'].columns['t_location'].create()
