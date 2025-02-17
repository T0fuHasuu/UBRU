import pymysql
pymysql.install_as_MySQLdb()

from epl import app
from flask_sqlalchemy import SQLAlchemy

# Configure SQLAlchemy to use PyMySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://pich:sreychieeeee1507!@pich.mysql.pythonanywhere-services.com:3306/pich_pichelpbd'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)  # Allows external access
