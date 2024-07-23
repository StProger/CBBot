FROM python:3.12

RUN mkdir /CentralBankBot

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]