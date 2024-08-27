# Start with a Debian base image
FROM debian:bookworm

# Establish workdir
WORKDIR /opt/stockflow

# Set environment variables
ENV PYTHON_VERSION=3.12.4
ENV PYTHONPATH $PWD

# Update package lists and install dependencies
RUN apt-get update && apt-get install -y \
    vim \
    wget \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libreadline-dev \
    libsqlite3-dev \
    libgdbm-dev \
    libdb5.3-dev \
    libbz2-dev \
    libexpat1-dev \
    liblzma-dev \
    tk-dev \
    libffi-dev \
    libmariadb3 \
    libmariadb-dev \
    dos2unix \
    build-essential\ 
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Download and install Python
RUN wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz \
    && tar xzf Python-${PYTHON_VERSION}.tgz \
    && cd Python-${PYTHON_VERSION} \
    && ./configure --enable-optimizations \
    && make -j$(nproc) \
    && make altinstall \
    && cd .. \
    && rm -rf Python-${PYTHON_VERSION}*

# Install pip
RUN wget https://bootstrap.pypa.io/get-pip.py \
&& python3.12 get-pip.py \
&& rm get-pip.py

# Copy files
COPY ../../web/rest . 

# Install dependencies
RUN pip3.12 install -r requirements.txt

# Expose the port used by the application
EXPOSE 5000

# Make the shell script executable
RUN chmod -R +x bin

# Run the shell script
CMD ["sleep", "infinity"]