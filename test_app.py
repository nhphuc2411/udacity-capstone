import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db
from setup import ASSISTANT_TOKEN, DIRECTOR_TOKEN, PRODUCER_TOKEN

class MainTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_test"
        self.database_path = "postgresql://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    One test for success behavior of each endpoint
    One test for error behavior of each endpoint
    """

    # MOVIES
    def test_home_page(self):
        res = self.client().get('/')

        self.assertEqual(res.status_code, 200)

    def test_get_movies(self):
        auth = {
            'Authorization': "Bearer {}".format(PRODUCER_TOKEN)
        }
        res = self.client().get('/movies', headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_create_movie(self):
        new_movie = {
            'title': 'Movies Test',
            'release_date': '2024-05-07'
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': "Bearer {}".format(PRODUCER_TOKEN)
        }

        res = self.client().post('/movies', json=new_movie, headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_movie_error_422(self):
        new_movie = {
            'title': '',
            'release_date': '2024-05-07'
        }
        auth = {
            'Authorization': "Bearer {}".format(PRODUCER_TOKEN)
        }
        res = self.client().post('/movies', json=new_movie, headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_update_movie(self):
        edit_movie = {
            'title': 'Movies Test Update',
            'release_date': '2024-05-08'
        }
        auth = {
            'Authorization': "Bearer {}".format(PRODUCER_TOKEN)
        }
        res = self.client().patch('/movies/2', json=edit_movie, headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_update_movie_error_404(self):
        edit_movie = {
            'title': 'Movies Test',
            'release_date': '2024-05-07'
        }
        auth = {
            'Authorization': "Bearer {}".format(PRODUCER_TOKEN) 
        }
        res = self.client().patch('/movies/100', json=edit_movie, headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        
    def test_delete_movie(self):
        auth = {
            'Authorization': "Bearer {}".format(PRODUCER_TOKEN)
        }
        res = self.client().delete('/movies/3', headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 3)
        

    def test_delete_movie_error_404(self):
        auth = {
            'Authorization': "Bearer {}".format(PRODUCER_TOKEN)
        }
        res = self.client().delete('/movies/100', headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])


    def test_get_actors(self):
        auth = {
            'Authorization': "Bearer {}".format(DIRECTOR_TOKEN)
        }
        res = self.client().get('/actors', headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    # Actors
    def test_create_actor(self):
        new_actor = {
            'name': 'Actor Test',
            'age': 18,
            'gender': 'Male',
            'movie_id': 4
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': "Bearer {}".format(DIRECTOR_TOKEN)
        }

        res = self.client().post('/actors', json=new_actor, headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        
    def test_create_actor_error_422(self):
        new_actor = {
            'name': '',
            'age': 18,
            'gender': 'Male',
            'movie_id': 4
        }
        
        auth = {
            'Authorization': "Bearer {}".format(DIRECTOR_TOKEN)
        }
        res = self.client().post('/actors', json=new_actor, headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_update_actor(self):
        edit_actor = {
            'name': 'Actor Test Update',
            'age': 18,
            'gender': 'Male',
            'movie_id': 4
        }

        auth = {
            'Authorization': "Bearer {}".format(DIRECTOR_TOKEN)
        }
        res = self.client().patch('/actors/1', json=edit_actor, headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_update_actor_error_404(self):
        update_actor = {
            'name': 'Actor Test',
            'age': 18,
            'gender': 'Male',
            'movie_id': 4
        }

        auth = {
            'Authorization': "Bearer {}".format(DIRECTOR_TOKEN)
        }
        res = self.client().patch('/actors/1000', json=update_actor, headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)


    def test_delete_actor(self):
        auth = {
            'Authorization': "Bearer {}".format(DIRECTOR_TOKEN)
        }
        res = self.client().delete('/actors/2', headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 2)

    def test_delete_actor_error_404(self):
        auth = {
            'Authorization': "Bearer {}".format(DIRECTOR_TOKEN)
        }
        res = self.client().delete('/actors/100', headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
        
    # AUTH
    def test_get_movies_auth_401(self):
        res = self.client().get('/movies', headers='')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_create_movie_auth_403(self):
        new_movie = {
            'title': '',
            'release_date': '2024-05-07'
        }
        auth = {
            'Authorization': "Bearer {}".format(ASSISTANT_TOKEN)
        }
        res = self.client().post('/movies', json=new_movie, headers=auth)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Permission not found.")

    def test_update_movie_auth_403(self):
        edit_movie = {
            'title': 'Movies Test Update',
            'release_date': '2024-05-08'
        }
        auth = {
            'Authorization': "Bearer {}".format(ASSISTANT_TOKEN)
        }
        res = self.client().patch('/movies/2', json=edit_movie, headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Permission not found.")
        

    def test_create_actor_auth_403(self):
        new_actor = {
            'name': 'Actor Test',
            'age': 18,
            'gender': 'Male',
            'movie_id': 4
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': "Bearer {}".format(ASSISTANT_TOKEN)
        }

        res = self.client().post('/actors', json=new_actor, headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        
    def test_delete_actor_auth_403(self):
        auth = {
            'Authorization': "Bearer {}".format(ASSISTANT_TOKEN)
        }
        res = self.client().delete('/actors/3', headers=auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()