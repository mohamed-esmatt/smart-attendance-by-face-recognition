from typing import NoReturn
import unittest
from login import Register 




class TestAPP(unittest.TestCase):
    def create_app(self):
      app = Register(__name__)
      app.config['TESTING'] = True
      app.config['WTF_CSRF_ENABLED'] = False
      return app

    def test_login(self):
       
       self.assertEqual(NoReturn,self("user already exists ,try another email"))





def main():
        #create suite
        suite = unittest.TestLoader().loadTestsFromTestCase(TestAPP)
        #run test suite
        unittest.TextTestRunner(verbosity=2).run(suite)

main()