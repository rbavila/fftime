import re

class FFTime:
    @classmethod
    def str2secs(cls, s) -> float:
        try:
            (neg, dummy0, dummy1, h, dummy3, m, s, dummy6, us) = re.search('^(-)?(((\d+):)?((\d+):))?(\d+)(\.(\d+))?$', s).groups()
            secs = float(s)
            if h:
                secs += 3600 * int(h)
            if m:
                secs += 60 * int(m)
            if us:
                us_padded = us.ljust(3, '0')
                secs += float(us_padded) / 1000
            if neg:
                secs *= -1
            return secs
        except:
            raise Exception(f'formato inválido: {s}')


    @classmethod
    def secs2str(cls, secs) -> str:
        neg_str = '-' if secs < 0 else ''
        rem = abs(secs)

        h = int(rem / 3600)
        rem -= h * 3600

        m = int(rem / 60)
        rem -= m * 60

        s = int(rem)
        us = int(round(1000 * (rem - s)))
        str_us = f'.{us:03d}' if us > 0 else ''

        if h:
            return f'{neg_str}{h}:{m}:{s}{str_us}'
        elif m:
            return f'{neg_str}{m}:{s}{str_us}'
        else:
            return f'{neg_str}{s}{str_us}'


    def __init__(self, str_spec):
        self.secs = FFTime.str2secs(str_spec)


    def __str__(self) -> str:
        return FFTime.secs2str(self.secs)


    def plus(self, str_spec) -> str:
        delta = FFTime.str2secs(str_spec)
        return FFTime.secs2str(self.secs + delta)


if __name__ == "__main__":
    t = FFTime('1')
    print(t)
    t = FFTime('1.222')
    print(t)
    t = FFTime('3:1.222')
    print(t)
    t = FFTime('4:3:1.222')
    print(t)
    t = FFTime('1:0:0.001')
    print(t)
    t = FFTime('1:0.001')
    print(t)
    t = FFTime('-1.001')
    print(t)
    t = FFTime('-1.222')
    print(t)
    t = FFTime('-3:1.222')
    print(t)
    t = FFTime('-4:3:1.222')
    print(t)
    t = FFTime('1:00')
    print(t)

    print('-------------------------')

    print(FFTime.secs2str(1.001))
    print(FFTime.secs2str(61.001))
    print(FFTime.secs2str(3661.001))
    print(FFTime.secs2str(3660.001))
    print(FFTime.secs2str(3600.001))
    print(FFTime.secs2str(3600))
    print(FFTime.secs2str(1))
    print(FFTime.secs2str(-60.999))
    
    print('-------------------------')

    t = FFTime('1:00')
    print(t)
    print(t.secs)
    print(t.plus('1'))
    print(t.plus('0.1'))
    print(t.plus('0.01'))
    print(t.plus('0.001'))
    print(t.plus('-0.001'))
    print(t.plus('-0.01'))
    print(t.plus('-0.1'))