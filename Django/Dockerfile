FROM python

EXPOSE 8000

RUN apt-get update -y && apt-get upgrade -y

RUN apt-get install -y \
    libpq-dev \
    build-essential

RUN mkdir cinefast
WORKDIR /cinefast

COPY requirements.txt /cinefast/.
RUN pip install --no-cache-dir -r requirements.txt

COPY workspace/ .
COPY script.sh .

RUN chmod +x script.sh

CMD ["bash", "/cinefast/script.sh"]