'''
Let's say I just built a new website ClickMe.com, and I want to know how many hits I'm getting. All I care about is how many hits I've gotten in the last 5 minutes, nothing more. Your job is to build this system, by implementing two calls:

    # this gets called every time my site gets a hit
    log_hit()

    # I get to call this anytime I want.
    # returns number of hits in the last 5 minutes.
    get_hits()

'''


class HitCount():
    import time
    def __init__(self):
        self.counts = [0] * 300
        self.start_time = time.now().seconds()  # from EPOCH time
        self.end_time = self.start_time

    def log_hit(self):
        current_time = time.now().seconds()  # 705
        self.end_time = current_time  # 705

        time_diff = current_time - self.start_time  # 700
        if time_diff < 300:
            self.counts[time_diff] += 1  # [0 , 0 , 0, 0, 1, 0, ...]
        else:
            self.start_time = current_time - 300  # 405
            self.counts = self.counts[time_diff - 300:]  # discard the times > 300s
            self.counts += [0] * min(300, (time_diff - 300))
            self.counts[-1] += 1

    def get_hits(self):
        current_time = time.now().seconds()
        time_diff = current_time - self.end_time
        return sum(self.counts[time_diff:])


if __name__ == 'main':
    run1()


def run1():
    h = HitCount()  # 0
    # 5 secs passed
    h.log_hit()  # 5
    # 10 secs passed
    h.log_hit()  # 10
    h.get_hits()  # 10    => 2

    # 305 secs passed
    h.log_hit()  # 305
    h.get_hits()

    # 705 secs passed
    h.log_hit()
