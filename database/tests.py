from django.test import TestCase
from .utils import DataBaseAPI
class TestBD(TestCase):
    def setUp(self) -> None:
        self.db = DataBaseAPI()

    def test_db(self):
        blog_data = {
            'title': 'blog title',
            'text': 'blog text',
            'author': 'blog_author',
            'pub_date': '2021-05-27 00:00:00'
        }
        self.assertEqual(self.db.record_create(blog_data), True)
        self.assertEqual(self.db.record_delete(1, 'blog_author'), True)

