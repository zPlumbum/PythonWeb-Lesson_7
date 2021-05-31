from flask import Flask


POSTGRE_DSN = 'postgresql://web_py:12345@127.0.0.1:5432/web_py'

app = Flask(__name__)
app.config.from_mapping(SQLALCHEMY_DATABASE_URI=POSTGRE_DSN)

app.run()
