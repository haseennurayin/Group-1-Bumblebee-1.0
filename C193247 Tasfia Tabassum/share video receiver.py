from vidstream import StreamingServer
import threading

receiver = StreamingServer('privateipadress', 'port')

t = threading.Thread(target=receiver.start_server)
t.start()

while input("") != 'q':
    continue

receiver.stop_server()
