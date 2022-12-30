from vidstream import ScreenShareClient
import threading
sender = ScreenShareClient('ip', 'port')

t = threading.Thread(target=sender.start_stream)
t.start()

while input("") != 'q':
    continue

sender.stop_stream()
