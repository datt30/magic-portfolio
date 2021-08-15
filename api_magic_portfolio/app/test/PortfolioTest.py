import unittest
import json
from app import app

app_tester = app.test_client()


class PortfolioTestCase(unittest.TestCase):

    def test_get_portfolios(self):
        """ test get present portfolios in DB"""
        response = app_tester.get('/poc/v1/portfolios/', content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_update_non_existent_portfolio(self):
        """ test client creation without identity_number """

        mock_portfolio = {
            "description": "Testo 5",
            "imageUrl": "Testo 5",
            "lastNames": "Testo 5",
            "names": "Testo 5",
            "title": "Testo 5",
            "twitterUser": "Testo 5"
        }
        response = app_tester.put(
          '/poc/v1/portfolio/',
          headers={'Content-Type': 'application/json'},
          data=json.dumps(mock_portfolio)
        )
        self.assertEqual(response.status_code, 400)

    def test_update_portfolio_with_empty_object(self):
        """ test portfolio update with empty request should return """
        id_portfolio = 32
        mock_portfolio = {}
        response = app_tester.put(
            f'/poc/v1/portfolio/{id_portfolio}',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(mock_portfolio)
        )
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
