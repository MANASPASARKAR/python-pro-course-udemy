import api
import documentation
from flask import Flask

app = Flask(__name__)

app.add_url_rule(
    "/",
    endpoint="documentation",
    view_func=documentation.Doc.serve
)

app.add_url_rule(
    "/api",
    endpoint="dictionary_api",
    view_func=api.Api.serve
)

app.run(debug=True)