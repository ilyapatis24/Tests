import unittest, sys, os

sys.path.append(os.getcwd())
import app

class TestFunctions(unittest.TestCase):
        
    def test_get_doc_owner_name(self):
        self.assertEqual(app.get_doc_owner_name('2207 876234'), 'Василий Гупкин')
        
    def test_delete_doc(self):
        self.assertTrue(app.delete_doc('10006'))

         
if __name__ == '__main__':
    unittest.main()