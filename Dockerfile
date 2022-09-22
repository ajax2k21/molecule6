FROM python:3.8

WORKDIR /test-molecule-app

COPY requirements.txt

RUN pip install -r requirements.txt

COPY ./test_molecule ./test_molecule

CMD ["python", "./test_molecule/manage.py"]