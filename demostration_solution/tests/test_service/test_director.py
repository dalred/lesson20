import pytest, os
from unittest.mock import MagicMock
from demostration_solution.dao.model.director import Director
from demostration_solution.implemented import director_dao
from demostration_solution.service.director import DirectorService


@pytest.fixture()
def director_dao_test():
    taylor = Director(id=1, name='Тейлор Шеридан')
    kventin = Director(id=2, name='Квентин Тарантино')
    vladimir = Director(id=3, name='Владимир Вайншток')
    dan = Director(id=4, name='Dan2')

    director_dao.get_one = MagicMock(return_value=taylor)
    director_dao.get_all = MagicMock(return_value=[taylor, kventin, vladimir])
    director_dao.create = MagicMock(return_value=Director(id=4))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock(return_value=dan)
    director_dao.partially_update = MagicMock()
    return director_dao


class TestUserService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao_test):
        self.director_service = DirectorService(dao=director_dao_test)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director != None
        assert director.id != None
        assert director.name == 'Тейлор Шеридан', f'director.name должен быть равно {director.name}'

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0, f'len(directors) должен быть больше 0, но он равен {len(directors)}'

    def test_create(self):
        director_d = {
            "name": "Dan"
        }
        director = self.director_service.create(director_d)
        assert director.id != None
        assert director.id == 4, f'director.id должен быть равным 4, но он равен {director.id}'

    def test_delete(self):
        self.director_service.delete(1)

    def test_update(self):
        director_d = {
            "name": "Dan2"
        }
        director = self.director_service.update(director_d)
        assert director.name == 'Dan2', f'director.name должен быть равным Dan2, но он равен {director.name}'

    def partially_update(self):
        director_d = {
            "name": "Dan2"
        }
        self.director_service.partially_update(director_d)


if __name__ == "__main__":
    os.system("pytest")
