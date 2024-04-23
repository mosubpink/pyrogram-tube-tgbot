FROM python:alpine

WORKDIR /bot
# Install pip requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /bot

CMD ["python", "pyrotubetgbot.py"]
