FROM python:3
ADD report_card_script.py/
RUN pip install csv, os
CMD [ "python", "./report_card_script.py" ]


