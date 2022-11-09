import factory


class User:
    username = None
    age = None

    def __init__(self, username, age):
        self.username = username
        self.age = age


class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'user%d' % n)
    age = factory.Iterator([10, 20, 30])


def test_user_factory():
    user0 = UserFactory()
    user1 = UserFactory()

    assert user0.username == 'user0'
    assert user1.username == 'user1'

    assert user0.age == 10
    assert user1.age == 20


def test_user_factory_undeterministic():
    """
    This test only succeeds if the first test is run first
    due to the sequence iterator being shared between tests.
    """
    user0 = UserFactory()
    user1 = UserFactory()

    assert user0.username == 'user2'
    assert user1.username == 'user3'

    assert user0.age == 30
    assert user1.age == 10


def test_user_factory_reset():
    UserFactory.reset_sequence()
    UserFactory.age.reset()

    user0 = UserFactory()
    user1 = UserFactory()

    assert user0.username == 'user0'
    assert user1.username == 'user1'

    assert user0.age == 10
    assert user1.age == 20
