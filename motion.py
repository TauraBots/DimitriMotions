import pickle

TIME = 0

class motion(object):
    def __init__(self):
        self.keyframes = []
        self.allframes = []
        self.period = 0.050
    def generate(self):
        for i in range(len(keyframes)):
            self.allframes.append(keyframe[i])
            steps = keyframe[TIME] / self.period
            for j in range(steps):
                frame = {}
                for joint_id in keyframe.keys():
                    frame[joint_id] = self.interpolate(\
                            keyframe[i][joint_id], keyframe[i+1][joint_id],
                            steps, j)
                self.allframes.append(frame)
    def interpolate(self, start, end, steps, i):
        step = (end - start) / steps
        return start + step*i
    def save(self, filename):
        thefile = open(filename, 'w')
        pickle.dump(self.keyframes, thefile)
        thefile.close()
    def read(self, filename):
        thefile = open(filename, 'r')
        self.keyframes = pickle.load(thefile)
        thefile.close()


