import sqlalchemy as sa

from app.models import Base

class User(Base):
    __tablename__ = 'user'
    
    id = sa.Column('id',sa.Integer, primary_key=True)
    username = sa.Column('username', sa.String(length=255))
    password = sa.Column('password', sa.String(length=512))
    full_name = sa.Column('full_name', sa.String(length=255))
    created_at = sa.Column('created_at', sa.DateTime, default=sa.func.NOW())
    modified_at = sa.Column('modified_at', sa.DateTime, default=sa.func.NOW(), onupdate=sa.func.NOW())