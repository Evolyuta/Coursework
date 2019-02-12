samples = [0,1,2,3,5,6,7,8]

nchannels = 2
nframes = 2
w = 800
sampwidth = 2

peak = 256 ** sampwidth / 2

for n in range(nchannels):
    channel = samples[n::nchannels]
    if nchannels == 1:
        channel = channel - peak
        channel = channel / 1.0


    print(channel)

