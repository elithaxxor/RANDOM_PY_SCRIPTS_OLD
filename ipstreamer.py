from threading import Thread
import time
from time import sleep
import gi

gi.require_version("Gst", "1.0")
from gi.repository import Gst, GLib, GstApp


class Streamer(gi.repository):
    def __init__(self):
        super(Streamer, self).__init__()

        Gst.init()
        self.Gst = Gst.init(None)
        self.GLib = GLib.init()
        self.GstApp = GstApp.init()

    def stream(self):
        main_loop = self.GLib.MainLoop()
        ml_thread = Thread(target=main_loop.run)
        ml_thread.start()
        pipe = self.Gst.parse_launch("autovideosrc ! decodebin ! videoconvert ! autovideosink")
        pipe.set_state(self.Gst.State.PLAYING)
        try:
            while True:
                time.sleep(.5)
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print('[+] End Sequence Initiated. ')

        pipe.set_state(self.Gst.State.NULL)





stream_video = Streamer()
stream_video.stream()
#
#
#
#
# ## select devices
# # windows - ksvideosrc
# # linux- v4 |2src
# # autovideosrc
