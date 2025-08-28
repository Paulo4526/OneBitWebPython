FROM python:3.11-slim AS build
RUN mkdir -p /apk/app
COPY . /apk/app
WORKDIR /apk/app

FROM python:3.11-slim
RUN mkdir -p /apk/app
COPY --from=build /apk/app /apk/app
WORKDIR /apk/app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
