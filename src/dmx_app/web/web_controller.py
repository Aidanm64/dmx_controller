
"""
 *  PyDMXControl: A Python 3 module to control DMX using OpenDMX or uDMX.
 *                Featuring fixture profiles, built-in effects and a web control panel.
 *  <https://github.com/MattIPv4/PyDMXControl/>
 *  Copyright (C) 2022 Matt Cowley (MattIPv4) (me@mattcowley.co.uk)
"""

import builtins  # Builtins for Jinja context
import logging  # Logging
from os import path  # OS Path
from typing import Dict, Callable  # Typing

from flask import Flask  # Flask
from werkzeug.serving import make_server  # Flask server

from dmx_app.web.api import api_routes  # Web Routes
from os import kill, getpid
from signal import SIGTERM
from threading import Thread
from traceback import print_exc



# Set error only logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


class ExceptionThread(Thread):

    def run(self):
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        except BaseException:
            # Print the exception and kill the whole process
            print_exc()
            kill(getpid(), SIGTERM)
        finally:
            del self._target, self._args, self._kwargs


class ServerThread(ExceptionThread):

    def __init__(self, host, port, app, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.srv = make_server(host, port, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        print("Started web controller: http://{}:{}".format(self.srv.host, self.srv.port))
        self.srv.serve_forever()

    def shutdown(self):
        self.srv.shutdown()


# WebController
class WebController:

    def __init__(self, dmx_service, *,
                 host: str = "0.0.0.0", port: int = 8000):

        # Setup flask
        self.__thread = None
        self.__host = host
        self.__port = port
        self.__app = Flask("Aidans DMX Controller")
        #self.__app.template_folder = path.dirname(__file__) + "/templates"
        #self.__app.static_url_path = "/static"
        #self.__app.static_folder = path.dirname(__file__) + "/static"
        self.__app.register_blueprint(api_routes)
        self.__app.parent = self


        self.dmx_service = dmx_service


        # Setup template context
        @self.__app.context_processor
        def variables() -> dict:  # pylint: disable=unused-variable
            return dict({"dmx_service": dmx_service,
                         "web_resource": WebController.web_resource},
                        **dict(globals(), **builtins.__dict__))  # Dictionary stacking to concat

        # Setup thread
        self.__running = False
        self.run()

    @staticmethod
    def filemtime(file: str) -> int:
        try:
            return int(path.getmtime(file))
        except Exception:
            return 0

    @staticmethod
    def web_resource(file: str) -> str:
        return "{}?v={:.0f}".format(file, WebController.filemtime(path.dirname(__file__) + file))

    def run(self):
        if not self.__running:
            self.__thread = ServerThread(self.__host, self.__port, self.__app, daemon=True)
            self.__thread.start()

    def stop(self):
        self.__thread.shutdown()
        self.__running = False
