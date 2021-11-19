FROM python:3.9-slim

# author of file
# LABEL maintainer="rochonj"

# Install native libraries for alpine version, required for numpy
# RUN apk --no-cache add musl-dev linux-headers g++

##WORKDIR /backend

# Install numpy and fast
RUN pip install --no-cache-dir fastapi uvicorn
RUN pip install -r requirements.txt

##WORKDIR /backend

COPY . .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--reload" ,"--host", "0.0.0.0", "--port", "8000"]