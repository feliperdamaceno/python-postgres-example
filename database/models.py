from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(length=100))
    last_name: Mapped[str] = mapped_column(String(length=100))
    email: Mapped[str] = mapped_column(String(length=200))

    def __repr__(self) -> str:
        return f"User(first_name={self.first_name}, last_name={self.last_name}, email={self.email})"
