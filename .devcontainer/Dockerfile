FROM mcr.microsoft.com/vscode/devcontainers/python:3.8

# Install Node.js
ARG NODE_VERSION="lts/*"
RUN su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION}"

# [Optional] Install additional OS packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends postgresql-client

# [Optional] Uncomment this section to install additional packages.
# RUN pip install matplotlib seaborn pandas

# [Optional] Uncomment this line to copy files from your repository into the container.
# COPY . /workspace

# Setting the ENTRYPOINT to docker-init.sh will configure non-root access to 
# Docker socket if needed and execute whatever is passed to "docker run" or "docker-compose up"
ENTRYPOINT ["/usr/local/share/docker-init.sh"]
CMD ["sleep", "infinity"]
