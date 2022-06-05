from unittest.mock import MagicMock
import pytest

from demostration_solution.dao.director import DirectorDAO
from demostration_solution.dao.model.director import Director
from demostration_solution.service.director import DirectorService


@pytest.fixture()
def director_dao():
    dao = DirectorDAO(None)

    director_1 = Director(id=1, name='Test_1')
    director_2 = Director(id=2, name='Test_2')
    director_3 = Director(id=3, name='Test_3')

    dao.get_all = MagicMock(return_value=[director_1, director_2, director_3])
    dao.get_one = MagicMock(return_value=director_1)
    dao.create = MagicMock(return_value=Director(id=3))
    dao.delete = MagicMock()
    dao.update = MagicMock()
    return dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert len(directors) > 0

    def test_create(self):
        directors_d = {
            'name': 'test'
        }

        director = self.director_service.create(directors_d)

        assert director.id is not None

    def test_delete(self):
        self.director_service.delete(1)

    def test_update(self):
        directors_d = {
            'id': 1,
            'name': 'test_5'
        }
        self.director_service.update(directors_d)