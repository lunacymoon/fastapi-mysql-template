from sqlalchemy import Column, DateTime, Integer, String, text
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql import func

from src.core.orm import column_comment
from src.settings.database import SQLAlchemyBase


class ExistedBase(SQLAlchemyBase):
    __abstract__ = True
    __table_args__ = {'extend_existing': True}

    @compiles(DateTime, 'mysql')
    def compile_datetime_mysql(type_, compiler, **kw):
        return 'DATETIME(6)'

    data_create_time = Column(
        'data_create_time',
        DateTime(timezone=True),
        server_default=text('CURRENT_TIMESTAMP(6)'),
        default=func.now(6),
        comment=column_comment('data create time'),
    )
    data_update_time = Column(
        'data_update_time',
        DateTime(timezone=True),
        server_default=text('CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)'),
        default=func.now(6),
        comment=column_comment('data update time'),
    )
    data_update_user = Column('data_update_user', String(64), comment=column_comment('data update internal user'))


class Base(SQLAlchemyBase):
    __abstract__ = True
    __table_args__ = {'extend_existing': True}

    @compiles(DateTime, 'mysql')
    def compile_datetime_mysql(type_, compiler, **kw):
        return 'DATETIME(6)'

    id = Column('id', Integer, primary_key=True, index=True, unique=True, autoincrement=True)

    data_create_time = Column(
        'data_create_time',
        DateTime(timezone=True),
        server_default=text('CURRENT_TIMESTAMP(6)'),
        default=func.now(6),
        comment=column_comment('data create time'),
    )
    data_update_time = Column(
        'data_update_time',
        DateTime(timezone=True),
        server_default=text('CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)'),
        default=func.now(6),
        comment=column_comment('data update time'),
    )
    data_update_user = Column('data_update_user', String(64), comment=column_comment('data update internal user'))
