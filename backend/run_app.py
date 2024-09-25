"""
Module for running the Flask app.
"""

import net.config
import net.initialization


if __name__ == "__main__":

    app = net.initialization.get_configured_app(configuration=net.config)
    app.run(host="0.0.0.0", port=5000, debug=True)
