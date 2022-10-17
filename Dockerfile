FROM python:3.8.13-alpine3.14

# copy required files
ADD src /usr/src
ENV PYTHONPATH "${PYTHONPATH}:/usr/src"

# run the application
CMD ["python", "/usr/src/main.py"]