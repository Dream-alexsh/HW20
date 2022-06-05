from unittest.mock import MagicMock
import pytest

from demostration_solution.dao.model.movie import Movie
from demostration_solution.dao.movie import MovieDAO
from demostration_solution.service.movie import MovieService


@pytest.fixture()
def movie_dao():
    dao = MovieDAO(None)

    movie_1 = Movie(id=1, title='Test_1')
    movie_2 = Movie(id=2, title='Test_2')
    movie_3 = Movie(id=3, title='Test_3')

    dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])
    dao.get_one = MagicMock(return_value=movie_1)
    dao.create = MagicMock(return_value=Movie(id=3))
    dao.delete = MagicMock()
    dao.update = MagicMock()
    return dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            'title': 'test',
            'description': 'test'
        }

        movie = self.movie_service.create(movie_d)

        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_d = {
            'id': 1,
            'title': 'test_5'
        }
        self.movie_service.update(movie_d)
