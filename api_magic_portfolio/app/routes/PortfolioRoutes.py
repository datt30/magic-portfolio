from app.models.PortfolioModel import Portfolio
from app import app, db
from flask import request, jsonify


@app.route('/magic-portfolio/v1/portfolios/', methods=['GET'])
def get_portfolios():
    try:
        portfolio_list = Portfolio.query.all()
        return jsonify({'portfolios': [portfolio.serialize() for portfolio in portfolio_list]}), 201
    except Exception as e:
        # usually for server security, the error must be stored in a log,
        # but for practical purposes of the poc we will show it in the response
        return jsonify({'message': 'server error', 'error': str(e)}), 500


@app.route('/magic-portfolio/v1/portfolio/<int:id_portfolio>', methods=['PUT'])
def update_portfolio(id_portfolio):
    content = request.json
    try:
        portfolio = Portfolio.query.filter(Portfolio.idportfolio == id_portfolio).one()
        portfolio.twitter_user_name = content['twitterUser']
        portfolio.description = content['description']
        portfolio.image_url = content['imageUrl']
        portfolio.title = content['title']
        portfolio.names = content['names']
        portfolio.last_names = content['lastNames']
        db.session.commit()
        return jsonify({'message': 'success update'}), 201
    except Exception as e:
        return jsonify({'message': 'server error', 'error': str(e)}), 500
