init python:
    # the wiggle class to make text shake. found on the internet without apparent author
    class Wiggle(object):
        def __init__(self, freq, amp, octaves=1, ampMulti=.5, time=0):
            from random import random
            self.randoms = [(1+random(), 1+random()) for i in range(0, 100)]
            self.freq = freq
            self.amp = amp
            self.octaves = octaves
            self.ampMulti = ampMulti
            self.time = time

        def __call__(self, time, at):
            from math import sin, pi, ceil
            r1, r2 = self.randoms[int(ceil(time*self.freq)%100)]

            return r1*self.amp*sin(2*pi*self.freq*time) + r2*self.amp*self.ampMulti*sin(2*pi*self.freq*2*self.octaves*(time+self.time))


            
label buzz:
    $ all_moves(x_express=Wiggle(freq=.5, amp=10), y_express=Wiggle(freq=.6, amp=10), z_express=Wiggle(freq=.4, amp=1))

transform text_effect:
    parallel:
        block:
            linear 0.1 xoffset -2 yoffset 2
            linear 0.1 xoffset 3 yoffset -3
            linear 0.1 xoffset 2 yoffset -2
            linear 0.1 xoffset -3 yoffset 3
            linear 0.1 xoffset 0 yoffset 0
            repeat
    parallel:
        block:
            alpha .2
            linear 1.0 alpha .9
            linear 1.0 alpha .2
            repeat