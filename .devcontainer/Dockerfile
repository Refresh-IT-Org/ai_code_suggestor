FROM mcr.microsoft.com/vscode/devcontainers/python:3.8

# Install Node.js
ARG NODE_VERSION="lts/*"
RUN su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION}"

# [Optional] Install additional OS packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends postgresql-client \
    build-essential \
    libpq-dev \
    libssl-dev \
    libffi-dev

# Clean up the cache to keep the image size down.
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Set up a virtual environment within the container to isolate your project dependencies.
RUN python -m venv /venv
RUN . /venv/bin/activate && pip install --upgrade pip

# Install Node (Using NVM)
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
RUN . ~/.nvm/nvm.sh && nvm install 14 && nvm use 14

# Install Python Deps
COPY requirements.txt .
RUN . /venv/bin/activate && pip install -r requirements.txt

# Install Node Deps
COPY package.json package-lock.json ./
RUN npm install

# [Optional] Uncomment this section to install additional packages.
# RUN pip install matplotlib seaborn pandas

# [Optional] Uncomment this line to copy files from your repository into the container.
# COPY . /workspace

# Setting the ENTRYPOINT to docker-init.sh will configure non-root access to 
# Docker socket if needed and execute whatever is passed to "docker run" or "docker-compose up"
ENTRYPOINT ["/usr/local/share/docker-init.sh"]
CMD ["sleep", "infinity"]
