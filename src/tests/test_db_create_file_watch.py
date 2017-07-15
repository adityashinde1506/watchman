import unittest
import sys
import os

sys.path.append("/home/adityas/Projects/Watchman/src")

from common import dbhandler

class TestDBCreate_file_watch(unittest.TestCase):
    
    def setUp(self):
        self.dbpath="/home/adityas/Projects/Watchman/db/file_watch.db"
        self.dbname="file_watch.db"

    def test(self):
        dbhandler.createdb_file_integ_check(self.dbpath)
        #print(os.listdir("/home/adityas/Projects/Watchman/db"))
        res=self.dbname in os.listdir("/home/adityas/Projects/Watchman/db")
        #print(res)
        self.assertTrue(res)

    def tearDown(self):
        os.remove(self.dbpath)

if __name__=="__main__":
    unittest.main()
