from datetime import datetime


def parseLines(lines):
    st = 0
    ct = 0
    ss = 0.0
    ps = 0.0
    session_started = False
    playing = False
    for l in lines:
        ts, msg = l.split("::")
        if msg.strip() == 'START':
            session_started = True
            st = datetime.strptime(ts.strip(), '(%m/%d/%Y-%H:%M:%S)')
        else:
            if msg.strip() == 'CONNECTED':
                playing = True
                ct = datetime.strptime(ts.strip(), '(%m/%d/%Y-%H:%M:%S)')
            else:
                if msg.strip() == 'DISCONNECTED' and playing:
                    dt = datetime.strptime(ts.strip(), '(%m/%d/%Y-%H:%M:%S)')
                    ps += (dt - ct).seconds
                    playing = False
                elif msg.strip() == 'SHUTDOWN':
                    dt = datetime.strptime(ts.strip(), '(%m/%d/%Y-%H:%M:%S)')
                    if playing:
                        ps += (dt - ct).seconds
                    ss += (dt - st).seconds
                    playing = False
                    session_started = False
    return str(int((ps / ss) * 100)) + '%'


if __name__ == '__main__':
    print parseLines(
            ['(11/01/2015-04:00:00) :: START',
             '(11/01/2015-04:00:00) :: CONNECTED',
             '(11/01/2015-04:30:00) :: DISCONNECTED',
             '(11/01/2015-04:45:00) :: CONNECTED',
             '(11/01/2015-05:00:00) :: SHUTDOWN'])
