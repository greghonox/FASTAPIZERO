from datetime import datetime

from sqlalchemy import select

from src.models import Todo, User
from src.security import Session


def test_create_user(session):
    new_user = User(username='alice', password='secret', email='teste@test')
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'alice'))

    assert user.username == 'alice'


def test_create_todo(session: Session, user: User):
    todo = Todo(
        title='Test Todo',
        description='Test Desc',
        state='draft',
        user_id=user.id,
        created=datetime.now(),
    )

    session.add(todo)
    session.commit()
    session.refresh(todo)

    user = session.scalar(select(User).where(User.id == user.id))

    assert todo in user.todos
