import pytest
from user_repository import User, UserRepository


# @pytest.fixture(params=[User('login1', 'passwrd001', False),User('login2', 'passwrd002', True)])
# def create_user(request):
#     param=request.param
#     user = param
#     yield user

@pytest.fixture
def create_user():
    user = User('login1', 'passwrd001', False)
    yield user


@pytest.fixture
def create_admin():
    user = User('login2', 'passwrd002', True)
    yield user


@pytest.fixture
def create_repository():
    userslist = UserRepository()
    yield userslist

@pytest.fixture
def filled_repository():
    userslist = UserRepository()
    userslist.add_user(User('login3', 'passwrd001', False))
    userslist.add_user(User('login4', 'passwrd001', True))
    userslist.add_user(User('login5', 'passwrd001', False))
    yield userslist
    userslist.users.clear()

def test_created_user_instance():
    assert create_user, isinstance(create_user, User)


def test_try_to_create_wrong_user():
    with pytest.raises(AttributeError) as e:
        User('logi n1', 'passwr d001', True)
    assert 'Логин или пароль не прошли проверку' in str(e.value)


def test_create_user(create_user):
    assert create_user.login == 'login1'
    assert create_user.password == 'passwrd001'
    assert create_user.is_admin is False


def test_create_admin(create_admin):
    assert create_admin.is_admin is True


def test_user_info(create_admin):
    assert create_admin.__str__() in "Пользователь login2 c паролем passwrd002, админ\n"


def test_create_repository():
    assert create_repository, isinstance(create_repository, UserRepository)


def test_add_user(create_user,create_repository):
    testusers=create_repository.users
    testusers.append(create_user)
    create_repository.add_user(create_user)
    assert create_repository.users == testusers

def test_logout_users(filled_repository):
    f=filled_repository
    print(f)
    f.logout_users()
    print(f)
    for u in f.users:
        assert u.is_admin is True


def test_repository_print(create_repository):
    create_repository.add_user(User('login3', 'passwrd001', False))
    create_repository.add_user(User('login4', 'passwrd001', True))
    create_repository.add_user(User('login5', 'passwrd001', False))
    print(create_repository.__str__())

if __name__ == '__main__':
    pytest.main(['-v'])
