from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase):
    pass

class Visits(Base):
    __tablename__ = "visits"

    id: Mapped[int] = mapped_column(primary_key=True)
    ip: Mapped[str]
    visited_at: Mapped[datetime] = mapped_column(default=func.current_timestamp())


    def __repr__(self) -> str:
        return f"Visit(ip={self.ip}, visited_at={self.visited_at})"
