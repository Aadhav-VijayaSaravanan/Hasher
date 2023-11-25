import unittest
from unittest.mock import patch
from io import StringIO
import main

class TestMain(unittest.TestCase):
    @patch("main.Faker")
    @patch("main.generate_user_info")
    def test_generate_user_info(self, mock_generate_user_info, mock_faker):
        mock_faker_instance = mock_faker.return_value
        mock_faker_instance.user_name.side_effect = ["user1", "user2", "user3"]
        mock_generate_user_info.return_value = "user1 user1\nuser2 user2\nuser3 user3"
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main.main()
        mock_generate_user_info.assert_called_once()
        actual_result = mock_stdout.getvalue().strip()
        expected_result = "Actual Result: user1 user1\nuser2 user2\nuser3 user3"
        self.assertEqual(actual_result, expected_result)

if __name__ == "__main__":
    unittest.main()
