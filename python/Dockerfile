FROM --platform=linux/amd64 python

ADD https://github.com/openfaas/classic-watchdog/releases/download/0.2.3/fwatchdog-amd64 /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog


WORKDIR /forecast
COPY src/ .

RUN pip install -r requirements.txt
ENV fprocess="python execute_algorithm.py"

CMD ["fwatchdog"]