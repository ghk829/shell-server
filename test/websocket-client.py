from websocket import create_connection

def socket_connection():
    from websocket import create_connection
    ws = create_connection("ws://localhost:9000/shell")
    ws.send("ls")
    result = ws.recv()
    print("Received '%s'" % result)
    ws.close()


def socket_send_recv_message():
    pass


if __name__ == '__main__':
    from shell_server.server import start_server
    import multiprocessing
    proc= multiprocessing.Process(target=start_server,args=[9000])
    proc.start()
    import time
    time.sleep(1)
    socket_connection()
    time.sleep(1)
    proc.terminate()