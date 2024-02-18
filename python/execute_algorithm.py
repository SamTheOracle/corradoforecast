import sys, os
from requests_toolbelt.multipart import decoder
from forecast.forecast_algorithm import compute_forecast
from forecast.forecast_algorithm import FormTuple

def get_stdin():
    return sys.stdin.buffer.read()

def get_key(form_data):
    # 'form-data; name="birth_date"', 'content': b'2012-123'
    key = form_data.split(";")[1].split("=")[1].replace('"', '')
    return key

if __name__ == "__main__":
    st = get_stdin()
    method = os.getenv("Http_Method")
    if os.getenv("Http_Method") == "GET":
        print(f"Forecast algorithm version {os.getenv("ALGORITHM_VERSION")}")
    elif method == "POST":
        form = decoder.MultipartDecoder(st, os.getenv("Http_Content_Type"))
        key_value = []
        for part in form.parts:
            key = get_key(part.headers[b'Content-Disposition'].decode('utf-8'))
            value = part.text
            if key == os.getenv("FORM_FILE_KEY"):
                value = part.content
            key_value.append(FormTuple(key, value))
        ret = compute_forecast(key_value)
        if ret is not None:
            print(ret)
    else:
        print("Not allowed")