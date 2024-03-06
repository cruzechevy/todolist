import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_add_task(self):
        response = self.app.post('/add', data=dict(task='Test Task', priority='Low', due_date='2024-03-15'))
        self.assertEqual(response.status_code, 302)  # Redirects after adding a task

    def test_complete_task(self):
        response = self.app.get('/complete/0')
        self.assertEqual(response.status_code, 302)  # Redirects after completing a task

    def test_delete_completed(self):
        response = self.app.get('/delete_completed')
        self.assertEqual(response.status_code, 302)  # Redirects after deleting completed tasks

if __name__ == '__main__':
    unittest.main()