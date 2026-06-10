import os
import sys

# Add the '路由開發' subdirectory to Python's search path
base_dir = os.path.dirname(os.path.abspath(__file__))
route_dev_dir = os.path.join(base_dir, '路由開發')
if route_dev_dir not in sys.path:
    sys.path.insert(0, route_dev_dir)

from app import create_app

app = create_app()

if __name__ == '__main__':
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port, debug=False)
