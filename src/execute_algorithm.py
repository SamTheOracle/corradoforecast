import os
import sys
from forecast.forecast_algorithm import compute_forecast

def get_stdin():
    buf = ""
    for line in sys.stdin:
        buf = buf + line
    return buf

if __name__ == "__main__":
    st = get_stdin()
    ret = compute_forecast(st)
    if ret != None:
        print(ret)