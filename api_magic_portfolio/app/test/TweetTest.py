import unittest
import json
from app import app

app_tester = app.test_client()


class PortfolioTestCase(unittest.TestCase):

    def test_get_tweets_from_non_existent_user(self):
        """ get tweets from non existent user in twitter should return
            internal server error with status 500 """

        mock_twitter_user_name = 'mock_user_%$342'

        response = app_tester.get(
            f'/magic-portfolio/v1/tweets/{mock_twitter_user_name}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 500)

    def test_get_tweets_from_valid_user(self):
        """ get tweets from valid user in twitter should return
            a tweet list with no more than 5 elements with status response 201 """

        mock_twitter_user_name = 'elonmusk'

        response = app_tester.get(
            f'/magic-portfolio/v1/tweets/{mock_twitter_user_name}',
            content_type='application/json'
        )

        tweets = json.loads(response.get_data(as_text=True))["tweets"]

        self.assertEqual(response.status_code, 201)
        self.assertTrue(len(tweets) <= 5)


if __name__ == '__main__':
    unittest.main()
