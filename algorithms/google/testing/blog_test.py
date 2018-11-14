# for Python 3
import unittest
from unittest.mock import MagicMock, patch
from lib import Blog

def mock_posts():
    return [{ 'userId': '1' }]

class TestStringMethods(unittest.TestCase):

    # beforeAll
    @classmethod
    def setUpClass(cls):
        pass

    # afterAll
    @classmethod
    def tearDownClass(cls):
        pass

    # setUp
    def setUp(self):
        pass

    # tearDown
    def tearDown(self):
        pass

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

        with self.assertRaises(TypeError):
            s.split(2)

    # patch method with stubbed method
    # prefer below instead of patch.object()
    # because if a class is defined in A but imported in B,
    # and we want to patch a method of the class in B,
    # the class will be imported in B before the patching takes place
    @patch('lib.Blog.posts', side_effect=mock_posts)
    # @patch.dict('os.environ', { 'MY_VAR': 'testing' })  # patch dict
    def test_blog(self, posts):
        blog = Blog()
        self.assertEqual(blog.posts_length(), len(mock_posts()))
        posts.assert_called_once_with()

    def test_blog_with_magic_mock(self):
        blog = Blog()
        blog.posts = MagicMock(return_value=3)
        blog.posts(3, 4, 5, key='value')  # returns 3
        blog.posts.assert_called_with(3, 4, 5, key='value')


if __name__ == '__main__':
    unittest.main()
