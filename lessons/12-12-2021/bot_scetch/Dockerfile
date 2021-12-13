FROM python:3-onbuild
RUN apt -y update
RUN apt -y install at
COPY . .
CMD ["python", "bot.py"]