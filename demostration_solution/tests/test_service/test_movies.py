import pytest, os
from unittest.mock import MagicMock
from demostration_solution.dao.model.movie import Movie
from demostration_solution.implemented import movie_dao
from demostration_solution.service.movie import MovieService

movies = []


@pytest.fixture()
def movie_dao_test():
    data = {"movies": [{
        "title": "Йеллоустоун",
        "description": "Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»",
        "trailer": "https://www.youtube.com/watch?v=UKei_d0cbP4",
        "year": 2018,
        "rating": 8.6,
        "genre_id": 17,
        "director_id": 1,
        "pk": 1
    }, {
        "title": "Омерзительная восьмерка",
        "description": "США после Гражданской войны. Легендарный охотник за головами Джон Рут по кличке Вешатель конвоирует заключенную. По пути к ним прибиваются еще несколько путешественников. Снежная буря вынуждает компанию искать укрытие в лавке на отшибе, где уже расположилось весьма пестрое общество: генерал конфедератов, мексиканец, ковбой… И один из них - не тот, за кого себя выдает.",
        "trailer": "https://www.youtube.com/watch?v=lmB9VWm0okU",
        "year": 2015,
        "rating": 7.8,
        "genre_id": 4,
        "director_id": 2,
        "pk": 2
    }, {
        "title": "Вооружен и очень опасен",
        "description": "События происходят в конце XIX века на Диком Западе, в Америке. В основе сюжета — сложные перипетии жизни работяги — старателя Габриэля Конроя. Найдя нефть на своем участке, он познает и счастье, и разочарование, и опасность, и отчаяние...",
        "trailer": "https://www.youtube.com/watch?v=hLA5631F-jo",
        "year": 1978,
        "rating": 6,
        "genre_id": 17,
        "director_id": 3,
        "pk": 3
    }]}
    for k, movie in enumerate(data["movies"], 1):
        movie = Movie(
            id=movie["pk"],
            title=movie["title"],
            description=movie["description"],
            trailer=movie["trailer"],
            year=movie["year"],
            rating=movie["rating"],
            genre_id=movie["genre_id"],
            director_id=movie["director_id"],
        )
        movies.append(movie)

    movie_dao.get_one = MagicMock(return_value=movies[0])
    movie_dao.get_all = MagicMock(return_value=movies)
    movie_dao.create = MagicMock(return_value=Movie(id=4))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock(return_value=Movie(title='Тест'))
    movie_dao.partially_update = MagicMock(return_value=Movie(title='Тест'))
    return movie_dao


class TestUserService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao_test):
        self.movie_service = MovieService(dao=movie_dao_test)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie != None
        assert movie.id != None
        assert movie.title == 'Йеллоустоун', f'movie.title должен быть равно {movie.title}'

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0, f'len(movies) должен быть больше 0, но он равен {len(movies)}'

    def test_create(self):
        movie_d = {
            "description": "Тест",
            "rating": 7.8,
            "title": "Тест",
            "trailer": "Тест",
            "year": 2022,
            "genre_id": 17,
            "director_id": 1}
        movie = self.movie_service.create(movie_d)
        assert movie.id != None
        assert movie.id == 4, f'movie.id должен быть равным 4, но он равен {movie.id}'

    def test_delete(self):
        movie = self.movie_service.get_one(2)
        self.movie_service.delete(2)
        assert movie.title == 'Йеллоустоун', f'movie.title должен быть равным Тест, но он равен {movie.title}'

    def partially_update(self):
        movie_d = {
            "id": 1,
            "description": "Тест",
            "rating": 7.8,
            "title": "Тест",
            "trailer": "Тест",
            "year": 2022,
            "genre_id": 17,
            "director_id": 1}
        movie = self.movie_service.partially_update(movie_d)
        assert movie.title == 'Тест', f'movie.title должен быть равным Тест, но он равен {movie.title}'

    def test_update(self):
        movie_d = {
            "id": 1,
            "description": "Тест",
            "rating": 7.8,
            "title": "Тест2",
            "trailer": "Тест",
            "year": 2022,
            "genre_id": 17,
            "director_id": 1}
        movie = self.movie_service.update(movie_d)
        assert movie.title == 'Тест', f'movie.title должен быть равным Тест, но он равен {movie.title}'

if __name__ == "__main__":
    os.system("pytest")
