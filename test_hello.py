echo "import unittest" > test_hello.py
echo "from hello import greet_user" >> test_hello.py
echo "" >> test_hello.py
echo "class TestGreetUser(unittest.TestCase):" >> test_hello.py
echo "    def test_greet_user(self):" >> test_hello.py
echo "        self.assertEqual(greet_user('Alice'), 'Hello, Alice!')" >> test_hello.py
