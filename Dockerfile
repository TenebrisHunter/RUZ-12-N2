FROM python:3.11
WORKDIR main
COPY . .
EXPOSE 8000
ENV PYTHONUNBUFFERED=1
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver"]

