# docker build -t [myimage] .
# docker run -d --name [mycontainer] -p 80:80 [myimage]

FROM python:3.9

WORKDIR /code
COPY ./requirements_venv.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code/
CMD ["fastapi", "run", "deploy.py", "--port", "80"]