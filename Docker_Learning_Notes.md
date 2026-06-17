# 🐳 Docker Learning Notes

## Mental Model

``` text
Dockerfile
     ↓ build
Image (template)
     ↓ run
Container (running instance)
```

-   **Image** = blueprint/template
-   **Container** = running instance of an image
-   One image can create **many** containers.

Think of a container as **a tiny disposable Linux computer.**

------------------------------------------------------------------------

# Dockerfile Instructions

## `FROM`

``` dockerfile
FROM python:3.13-slim
```

-   Selects the base image.
-   Usually includes Linux + some software already installed.
-   Every Dockerfile starts from a base image.

------------------------------------------------------------------------

## `WORKDIR`

``` dockerfile
WORKDIR /containerisedApp
```

-   Sets the working directory inside the container.
-   Similar to:

``` bash
cd /containerisedApp
```

-   Creates the directory if it doesn't exist.

------------------------------------------------------------------------

## `COPY`

``` dockerfile
COPY requirements.txt ./
```

Syntax:

``` dockerfile
COPY <host> <container>
```

Example:

``` text
Host PC                 Container
------------            ----------------
requirements.txt  --->  /containerisedApp/
```

`.` means the current `WORKDIR`.

------------------------------------------------------------------------

## Why copy `requirements.txt` first?

Docker caches build layers.

If only your Python code changes, Docker can reuse the cached dependency
installation instead of reinstalling everything.

``` text
COPY requirements.txt
RUN pip install ...

✅ Cached
```

``` text
COPY app.py

Only this layer rebuilds.
```

------------------------------------------------------------------------

## `RUN`

``` dockerfile
RUN pip install --no-cache-dir -r requirements.txt
```

-   Executes **while building the image**.
-   Used for installation/setup steps.

Think:

``` text
Building image
↓
RUN executes
↓
Image saved
```

------------------------------------------------------------------------

## `CMD`

``` dockerfile
CMD ["python","turbineProcessing.py"]
```

Runs when the container starts.

Equivalent to:

``` bash
python turbineProcessing.py
```

------------------------------------------------------------------------

## RUN vs CMD

  RUN                       CMD
  ------------------------- -------------------------
  Build time                Container startup
  Executes while building   Executes when running
  Permanent part of image   Default startup command

------------------------------------------------------------------------

# Useful Commands

``` bash
docker build -t turbine-app .
docker run turbine-app
docker run --rm turbine-app
docker run --name turbine-container turbine-app
docker run -it python:3.13-slim bash
docker images
docker ps
docker ps -a
docker rm CONTAINER_NAME
docker rmi IMAGE_NAME
docker system prune
```

------------------------------------------------------------------------

# Important Concepts

## Images are immutable

``` text
Edit code
      ↓
Rebuild image
      ↓
Run new container
```

Don't edit running containers.

------------------------------------------------------------------------

## Interactive Shell

``` bash
docker run -it python:3.13-slim bash
```

Creates a new container and launches a Linux terminal inside it.

``` text
Your PC
   │
   └──── Docker Container
              │
              └── Bash Terminal
```

------------------------------------------------------------------------

# Volumes

``` bash
docker run -v HOSTDIR:/containerisedApp image
```

Without volumes:

``` text
Host PC      Container
(file)   ❌   invisible
```

With volumes:

``` text
Host PC  ⇄  Container
```

Changes appear in both places.

------------------------------------------------------------------------

# Environment Variables

``` bash
docker run -e API_KEY=value image
```

Inside Python:

``` python
import os

os.getenv("API_KEY")
```

Useful for secrets and configuration.

------------------------------------------------------------------------

# Port Mapping

``` bash
docker run -p 5000:5000 image
```

``` text
Your browser
      │
localhost:5000
      │
Host port 5000
      │
Container port 5000
      │
Python Flask app
```

------------------------------------------------------------------------

# Docker Compose

Used for applications with multiple containers.

``` text
Web App
    │
Database
    │
Redis Cache
```

Instead of starting each one manually:

``` bash
docker compose up
```

Compose starts everything together.
