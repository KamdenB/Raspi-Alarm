import time

class LightControl:
    def __init__(self, channel, pin):
        self.channel = channel 

    def on(self):
        return True

    def off(self):  
        return True

    def flash(self, time, count):
        # if(not self.notPi)
        for i in range(count):
            self.on()
            time.sleep(time*100)
            self.off()
            time.sleep(time*100)
            i+=1
        self.off()