# What environment to start from
FROM python:3.13-slim

# Sets my current working directory so I can use . after for ease
WORKDIR /containerisedApp

COPY requirements.txt .

# Runs this command when building the image
RUN pip install  --no-cache-dir -r requirements.txt

# Copy the actual program and any supporting images/documents
COPY turbineProcessing.py telemetry_data_in.csv ./
# The command to run when someone starts a container from this docker image
CMD ["python", "turbineProcessing.py"]

