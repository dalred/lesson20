from demostration_solution.dao.movie import MovieDAO
from demostration_solution.dao.director import DirectorDAO
from demostration_solution.dao.genre import GenreDAO
from demostration_solution.service.movie import MovieService
from demostration_solution.service.genre import GenreService
from demostration_solution.service.director import DirectorService
from demostration_solution.setup_db import db

movie_dao = MovieDAO(session=db.session)
director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)

movie_service = MovieService(dao=movie_dao)
genre_service = GenreService(dao=genre_dao)
director_service = DirectorService(dao=director_dao)