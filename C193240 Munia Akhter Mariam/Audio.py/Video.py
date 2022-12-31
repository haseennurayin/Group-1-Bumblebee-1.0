class VideoClient(StreamingClient):

"""

Class for the video streaming client.



Attributes

----------



Private:



__host : str

host address to connect to

__port : int

port to connect to

__running : bool

inicates if the client is already streaming or not

__encoding_parameters : list

a list of encoding parameters for OpenCV

__client_socket : socket

the main client socket

__video : VideoCapture

the video object

__loop : bool

boolean that decides whether the video shall loop or not





Methods

-------



Protected:



_configure : sets basic configurations

_get_frame : returns the video frame to be sent to the server

_cleanup : cleans up all the resources and closes everything



Public:



start_stream : starts the video stream in a new thread

"""



def _init_(self, host, port, video, loop=True):

"""

Creates a new instance of VideoClient.



Parameters

----------



host : str

host address to connect to

port : int

port to connect to

video : str

path to the video

loop : bool

indicates whether the video shall loop or not

"""

self.__video = cv2.VideoCapture(video)

self.__loop = loop

super(VideoClient, self)._init_(host, port)



def _configure(self):

"""

Set video resolution and encoding parameters.

"""

self.__video.set(3, 1024)

self.__video.set(4, 576)

super(VideoClient, self)._configure()



def _get_frame(self):

"""

Gets the next video frame.



Returns

-------



frame : the next video frame to be processed

"""

ret, frame = self.__video.read()

return frame



def _cleanup(self):

"""

Cleans up resources and closes everything.

"""

self.__video.release()

cv2.destroyAllWindows()
