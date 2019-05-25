from util.shell import run_shell
from tornado import websocket
import tornado.ioloop

#@TODO 추후 UI에서 websocket 구현하는 경우 비동기 메세지 고도화해야 함
class EchoWebSocket(websocket.WebSocketHandler):
    def open(self):
        print("Websocket Opened")

    def on_message(self, message):
        print(message)
        std_out,std_err = run_shell(message,shell=True)
        self.write_message(std_out)

    def on_close(self):
        print("Websocket closed")

application = tornado.web.Application([(r"/shell", EchoWebSocket),])

if __name__ == "__main__":
    application.listen(9000)
    tornado.ioloop.IOLoop.instance().start()