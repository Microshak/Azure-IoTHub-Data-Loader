FROM adreeve/python-numpy





COPY . /app
WORKDIR /app


# update pip
RUN pip3 install -r requirements.txt

CMD [ "python3", "./IoTHubDataLoader.py" ]