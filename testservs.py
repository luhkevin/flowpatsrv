import re
import sys
from random import randint
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, url, asynchronous
from tornado import gen


class TestHandler0(RequestHandler):
    def prepare(self):
        self.add_header("Version", "0")

    def get(self):
        self.write("Hello, world! I am version 0 and I'm fast.")

class TestHandler1(RequestHandler):
    def prepare(self):
        self.add_header("Version", "1")

    @asynchronous
    @gen.engine
    def get(self):
        sleepTime = randint(1,5)
        self.write("Hello, world! I am version 1 and I'm slow. Going to sleep for a bit. ")
        self.flush()
        yield gen.sleep(sleepTime)
        self.write("Done sleeping.")
        self.finish()

def create_app(version):
    app0 = Application([ url(r"/", TestHandler0), ])
    app1 = Application([ url(r"/", TestHandler1), ])
    if version == "0":
        return app0
    elif version == "1":
        return app1

def main():
    #app = create_app("0")
    #app.listen(8886)

    app1 = create_app("1")
    app1.listen(8887)

    IOLoop.current().start()

if __name__ == "__main__":
    main()

