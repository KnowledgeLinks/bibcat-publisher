__author__ = "Jeremy Nelson, Mike Stabile, Jay Peterson"

from catalog import app
from catalog.views import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6726, debug=True)
