# fftime

Python class to deal with time stamps in the format used by FFmpeg ([[hh:]mm:]ss[.mmm]).

## Usage examples:

    t = FFTime('1:00')
    print(t) # 1:0
    print(t.secs) # 60.0
    print(t.plus('1')) # 1:1
    print(t.plus('0.1')) # 1:0.100
    print(t.plus('0.01')) # 1:0.010
    print(t.plus('0.001')) # 1:0.001
    print(t.plus('-0.001')) # 59.999
    print(t.plus('-0.01')) # 59.990
    print(t.plus('-0.1')) # 59.900

## Installation

Just run `pip install .`
