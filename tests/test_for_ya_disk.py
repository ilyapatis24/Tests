import unittest, sys, os
sys.path.append(os.getcwd())
import ya_disk


class TestYaApi(unittest.TestCase):

    def setUp(self):
        print('method setUp')

    def test_success_create_folder(self):
        self.assertEqual(ya_disk.create_folder('test'), 201)

    def test_passed_create_folder(self):
        self.assertEqual(ya_disk.create_folder('test_passed'), 409)

    def tearDown(self):
        ya_disk.delete_folder(folder='test')
        print('method tearDown')


if __name__ == '__main__':
    unittest.main()