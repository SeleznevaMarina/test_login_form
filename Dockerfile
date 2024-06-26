FROM python:3.9-slim

RUN apt-get update && apt-get install -yq \
    libgtk-3-0 \
    libdbus-glib-1-2 \
    libxt6 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxi6 \
    libxtst6 \
    libnss3 \
    libatk-bridge2.0-0 \
    libxrandr2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install playwright==1.42.0 pytest
RUN playwright install --with-deps

WORKDIR /usr/src/app
COPY . .

CMD ["pytest"]
