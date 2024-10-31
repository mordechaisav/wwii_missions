from flask import Flask
import psycopg2
from flask_graphql import GraphQLView

from app.db.models.country_model import City, Country

from app.db.database import session_maker
from app.schema import schema

app = Flask(__name__)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)








if __name__ == '__main__':

    app.run(debug=True)