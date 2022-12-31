def _init_(self, host, port, audio_format=pyaudio.paInt16, channels=1, rate=44100, frame_chunk=4096):

self.__host = host

self.__port = port



self.__audio_format = audio_format

self.__channels = channels

self.__rate = rate

self.__frame_chunk = frame_chunk



self.__sending_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

self.__audio = pyaudio.PyAudio()



self.__running = False



#

# def __callback(self, in_data, frame_count, time_info, status):

# if self.__running:

# self.__sending_socket.send(in_data)

# return (None, pyaudio.paContinue)

# else:

# try:

# self.__stream.stop_stream()

# self.__stream.close()

# self.__audio.terminate()

# self.__sending_socket.close()

# except OSError:

# pass # Dirty Solution For Now (Read Overflow)

# return (None, pyaudio.paComplete)



def start_stream(self):

if self.__running:

print("Already streaming")

else:

self.__running = True

thread = threading.Thread(target=self.__client_streaming)

thread.start()



def stop_stream(self):

if self.__running:

self.__running = False

else:

print("Client not streaming")



def __client_streaming(self):

self._sending_socket.connect((self.host, self._port))

self._stream = self.audio.open(format=self.audio_format, channels=self.channels, rate=self.rate, input=True, frames_per_buffer=self._frame_chunk)

while self.__running:

self._sending_socket.send(self.stream.read(self._frame_chunk))





class AudioReceiver:  #share sudio



def _init_(self, host, port, slots=8, audio_format=pyaudio.paInt16, channels=1, rate=44100, frame_chunk=4096):

self.__host = host

self.__port = port



self.__slots = slots

self.__used_slots = 0



self.__audio_format = audio_format

self.__channels = channels

self.__rate = rate

self.__frame_chunk = frame_chunk



self.__audio = pyaudio.PyAudio()



self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

self._server_socket.bind((self.host, self._port))



self.__block = threading.Lock()

self.__running = False



def start_server(self):

if self.__running:

print("Audio server is running already")

else:

self.__running = True

self._stream = self.audio.open(format=self.audio_format, channels=self.channels, rate=self.rate, output=True, frames_per_buffer=self._frame_chunk)

thread = threading.Thread(target=self.__server_listening)

thread.start()



def __server_listening(self):

self.__server_socket.listen()

while self.__running:

self.__block.acquire()

connection, address = self.__server_socket.accept()

if self._used_slots >= self._slots:

print("Connection refused! No free slots!")

connection.close()

self.__block.release()

continue

else:

self.__used_slots += 1



self.__block.release()

thread = threading.Thread(target=self.__client_connection, args=(connection, address,))

thread.start()



def __client_connection(self, connection, address):

while self.__running:

data = connection.recv(self.__frame_chunk)

self.__stream.write(data)



def stop_server(self):

if self.__running:

self.__running = False

closing_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

closing_connection.connect((self._host, self._port))

closing_connection.close()

self.__block.acquire()

self.__server_socket.close()

self.__block.release()

else:

print("Server not running!")
