from unittest.mock import MagicMock
import pytest

from demostration_solution.dao.genre import GenreDAO
from demostration_solution.dao.model.genre import Genre
from demostration_solution.service.genre import GenreService


@pytest.fixture()
def genre_dao():
    dao = GenreDAO(None)

    genre_1 = Genre(id=1, name='Test_1')
    genre_2 = Genre(id=2, name='Test_2')
    genre_3 = Genre(id=3, name='Test_3')

    dao.get_all = MagicMock(return_value=[genre_1, genre_2, genre_3])
    dao.get_one = MagicMock(return_value=genre_1)
    dao.create = MagicMock(return_value=Genre(id=3))
    dao.delete = MagicMock()
    dao.update = MagicMock()
    return dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genres = self.genre_service.get_all()

        assert len(genres) > 0

    def test_create(self):
        genres_d = {
            'name': 'test'
        }

        genre = self.genre_service.create(genres_d)

        assert genre.id is not None

    def test_delete(self):
        self.genre_service.delete(1)

    def test_update(self):
        genres_d = {
            'id': 1,
            'name': 'test_5'
        }
        self.genre_service.update(genres_d)