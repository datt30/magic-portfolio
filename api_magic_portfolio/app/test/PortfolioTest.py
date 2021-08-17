import unittest
import json
from app import app

app_tester = app.test_client()


class PortfolioTestCase(unittest.TestCase):

    _invalid_id_portfolio = 0
    _valid_id_portfolio = 32
    _mock_portfolio = {
        "description": "Testo 4",
        "imageUrl": "Testo 5",
        "lastNames": "Testo 5",
        "names": "Testo 5",
        "title": "Testo 5",
        "twitterUser": "Testo 5"
    }

    def test_get_portfolios(self):
        """ test get present portfolios in DB"""
        response = app_tester.get('/magic-portfolio/v1/portfolios/', content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_update_non_existent_portfolio(self):
        """ test portfolio update without valid id
            should return internal server error with status 500"""

        response = app_tester.put(
          f'/magic-portfolio/v1/portfolio/{self._invalid_id_portfolio}',
          headers={'Content-Type': 'application/json'},
          data=json.dumps(self._mock_portfolio)
        )
        self.assertEqual(response.status_code, 500)

    def test_update_portfolio_with_valid_id(self):
        """ test update portfolio with valid id and request
            should return 201 success update """

        response = app_tester.put(
            f'/magic-portfolio/v1/portfolio/{self._valid_id_portfolio}',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(self._mock_portfolio)
        )
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
