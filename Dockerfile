FROM python:3.9-slim

EXPOSE 8501

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["nohup", "streamlit", "run", "main.py"]