from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username='victor', email='victor@email.com', password='senha')

    session.add(user)
    session.commit()
    result = session.scalar(
        select(User).where(User.email == 'victor@email.com')
    )

    assert result.username == 'victor'
