FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
