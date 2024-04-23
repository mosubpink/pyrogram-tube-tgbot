FROM python:alpine

WORKDIR /bot
# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY . /bot

CMD ["python", "-m", "pyrotubetgbot.py"]
