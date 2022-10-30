import pyshine as ps
audio, context = ps.audioCapture(mode='send')
ps.showPlot(context, name='pyshine')
while True:
    frame = audio.get()



