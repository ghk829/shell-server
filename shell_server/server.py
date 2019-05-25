from shell_server.shell import run_shell
from tornado import websocket
import tornado.ioloop

class ShellWebSocket(websocket.WebSocketHandler):

    def open(self):
        print("Websocket Opened")

    def on_message(self, message):
        print(message)
        std_out,std_err = run_shell(message,shell=True)
        self.write_message(std_out)
        self.close()
    def on_close(self):
        print("Websocket closed")




def start_server(port):
    application = tornado.web.Application([(r"/shell", ShellWebSocket), ])
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    start_server(9000)
