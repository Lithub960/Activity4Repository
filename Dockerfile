FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN chmod +x .github/scripts/entrypoint.sh
ENTRYPOINT ["/app/.github/scripts/entrypoint.sh"]
