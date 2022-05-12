FROM python:3.10.4-alpine3.14
COPY . /app
WORKDIR /app
RUN pip install uvicorn
RUN pip install fastapi
RUN pip install requests
EXPOSE 8000
CMD [ "uvicorn","main:app","--reload"]