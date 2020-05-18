"""
This script runs the ListenerService application using a development server.
"""

from os import environ

import uvicorn

from AttachmentControl.storage_operations import app

if __name__ == '__main__':
    # HOST = environ.get('SERVER_HOST', 'localhost')
    # try:
    #     PORT = int(environ.get('SERVER_PORT', '5556'))
    # except ValueError:
    #     PORT = 5556
    # uvicorn.run(app, host=HOST, port=PORT)
    uvicorn.run(app, host='localhost', port=8080, log_level='info')