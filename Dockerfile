FROM python:3.11

WORKDIR /src

COPY . .

#это порт, тоже изменить если другой
EXPOSE 3000
#заменить название вашего файла, если оно другое
CMD ["python", "main.py"]