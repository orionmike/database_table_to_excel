
from datetime import datetime
from typing import Annotated, Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(default=datetime.utcnow())]
updated_at = Annotated[
    datetime,
    mapped_column(
        default=datetime.utcnow(),
        onupdate=datetime.utcnow()
    )]


class ObjectDB(Base):

    __tablename__ = 'product'

    id: Mapped[intpk]
    name: Mapped[str]
    slug: Mapped[str]
    category: Mapped[int] = mapped_column(ForeignKey('category.id', ondelete="CASCADE"))
    price: Mapped[str]
    description: Mapped[str]
    is_published: Mapped[bool]
    datetime_create: Mapped[created_at]
    datetime_update: Mapped[updated_at]
