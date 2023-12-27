from sqlalchemy import select

from database.config import session
from database.models import User


def create_user(**user: User):
    session.add(User(**user))
    session.commit()


def get_all_users() -> list[User] | None:
    sql = select(User).where()
    return [user for user in session.scalars(sql)]


def get_user_by_id(id: str) -> User | None:
    sql = select(User).where(User.id == id)
    return session.scalar(sql)


def delete_user_by_id(id: str) -> User:
    user = session.get(User, id)
    session.delete(user)
    session.commit()
    return user
