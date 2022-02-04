import pytest, os
from unittest.mock import MagicMock
from demostration_solution.dao.model.genre import Genre
from demostration_solution.implemented import genre_dao
from demostration_solution.service.genre import GenreService


@pytest.fixture()
def genre_dao_test():
    comedy = Genre(id=1, name='Комедия')
    family = Genre(id=2, name='Семейный')
    fantasy = Genre(id=3, name='Фэнтези')
    dan = Genre(id=4, name='Dan2')

    genre_dao.get_one = MagicMock(return_value=comedy)
    genre_dao.get_all = MagicMock(return_value=[comedy, family, fantasy])
    genre_dao.create = MagicMock(return_value=Genre(id=4))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock(return_value=dan)
    genre_dao.partially_update = MagicMock()
    return genre_dao


class TestUserService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao_test):
        self.genre_service = GenreService(dao=genre_dao_test)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre != None
        assert genre.id != None
        assert genre.name == 'Комедия', f'genre.name должен быть равно {genre.name}'

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0, f'len(genres) должен быть больше 0, но он равен {len(genres)}'

    def test_create(self):
        genre_d = {
            "name": "Dan"
        }
        genre = self.genre_service.create(genre_d)
        assert genre.id != None
        assert genre.id == 4, f'genre.id должен быть равным 4, но он равен {genre.id}'

    def test_delete(self):
        self.genre_service.delete(1)

    def test_update(self):
        genre_d = {
            "name": "Dan2"
        }
        genre = self.genre_service.update(genre_d)
        assert genre.name == 'Dan2', f'genre.name должен быть равным Dan2, но он равен {genre.name}'

    def partially_update(self):
        genre_d = {
            "name": "Dan2"
        }
        self.genre_service.partially_update(genre_d)


if __name__ == "__main__":
    os.system("pytest")
