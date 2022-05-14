FROM base
COPY webserver.py .
RUN pip install "uvicorn[standard]" fastapi
CMD ["uvicorn", "main:webserver", "--reload"]
