# -*- coding: utf-8 -*-
import time
import logging
from threading import Thread
import multiprocessing
import dill
from typing import TYPE_CHECKING

from flask import Flask, request

from .info import Info

if TYPE_CHECKING:
    from .factory import Factory


class PostServer():
    def __init__(self, factory: 'Factory'):
        self.__factory = factory
        self.__post_server = Flask(__name__)
        self.__server = factory.mcdr_server
        self.__config = factory.config
        self.__bot = factory.bot

        logging.getLogger('werkzeug').setLevel(logging.ERROR)

        def parse():
            Info(self.__factory, dict(request.json))
            return ''

        self.__post_server.add_url_rule(
            f'/{self.__config["post_path"]}',
            view_func=parse,
            methods=['POST'],
            endpoint=str(time.time())
        )

        self.__server.logger.info('CoolQAPI server is starting up')
        self.__server.logger.info(f"Listening address: {self.__config['post_host']}:{self.__config['post_port']}/{self.__config['post_path']}")

        def run():
            
            self.__post_server.run(
                port=self.__config['post_port'],
                host=self.__config['post_host'],
                threaded=False
            )

        self.__p = multiprocessing.Process(target=dill.dumps(run))
        self.__p.start()

    def stop(self):
        self.__p.terminate()
        self.__p.join()

        self.__server.logger.info("CoolQAPI stopped")



