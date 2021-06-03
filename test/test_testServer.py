import unittest
import testServer
import dbcon
from psycopg2.extras import RealDictCursor
import psycopg2

class TestServerTests(unittest.TestCase):
    """Unit tests for testServer.py that require an internet connection"""

    #def test_database_version1(self):
        #sql = 'SELECT version()'
        #version = dbcon.connect(sql)
        #self.assertIn(b'12.6', version)

    #def test_database_version2(self):
        #sql = 'SELECT version()'
        #version = dbcon.make_con(sql)
        #self.assertIn(b'12.6', version)

    def test_request1(self):
        data_expected = 200
        test_url = testServer.testServer(url = "https://google.com")
        test_dict = test_url.make_request()
        data_diff = test_dict["code"]
        self.assertEqual(data_diff, data_expected)

    def test_request2(self):
        data_expected = 404
        test_url = testServer.testServer(url = "https://example.com/funny/this-should-not-exist/blafasel")
        test_dict = test_url.make_request()
        data_diff = test_dict["code"]
        self.assertEqual(data_diff, data_expected)

    def test_db(self):

        uri = "postgres:/user:pass@db.server.com:28386/defaultdb?sslmode=require"
        db_conn = psycopg2.connect(uri)
        c = db_conn.cursor(cursor_factory=RealDictCursor)
        c.execute("SELECT 1 = 1")
        result = c.fetchone()
        self.assertIn("True", result)


if __name__ == '__main__':
    unittest.main(buffer=True)
