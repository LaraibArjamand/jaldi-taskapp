# start by pulling the python image
FROM python:3.8-alpine

# switch working directory
WORKDIR /taskapp

# copy the requirements file into the image
COPY ./requirements.txt .

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt
EXPOSE 5001

# configure the container to run in an executed manner
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]