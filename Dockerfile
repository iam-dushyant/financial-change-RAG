FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src ./src
COPY data ./data
COPY prompts ./prompts
ENV PORT=8001
EXPOSE 8001
CMD ["sh", "-c", "uvicorn src.api:app --host 0.0.0.0 --port ${PORT}"]

# Run the following commands to build and run the Docker container:
#docker build -t financial-change-rag:local .
#docker run --rm -p 8002:8001 \
#    -e GOOGLE_CLOUD_PROJECT="$GOOGLE_CLOUD_PROJECT" \
#    -e GOOGLE_CLOUD_LOCATION=global \
#    -v "$HOME/.config/gcloud:/root/.config/gcloud:ro" \
#    financial-change-rag:local