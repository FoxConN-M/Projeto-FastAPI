from sqlalchemy import select

from fast_zero.models import Todo, User


def test_create_user(session):
    user = User(username='victor', email='victor@email.com', password='senha')

    session.add(user)
    session.commit()
    result = session.scalar(
        select(User).where(User.email == 'victor@email.com')
    )

    assert result.username == 'victor'


def test_create_todo(session, user: User):
    todo = Todo(
        title='Test Todo',
        description='Test Desc',
        state='draft',
        user_id=user.id,
    )

    session.add(todo)
    session.commit()
    session.refresh(todo)

    user = session.scalar(select(User).where(User.id == user.id))

    assert todo in user.todos
