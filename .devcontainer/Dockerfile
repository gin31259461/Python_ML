# Use the official Ubuntu image as the base image
FROM debian:bullseye

# Update the package list and install necessary dependencies
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean

# install git package
RUN apt-get install -y git
RUN apt-get install -y wget
RUN apt-get install -y gnupg2

# Set the working directory inside the container
WORKDIR /workspaces

# Download and install the Anaconda installer
ENV ANACONDA_VERSION=2023.07-2
ENV ANACONDA_DIR=/opt/anaconda
RUN curl -sSL https://repo.anaconda.com/archive/Anaconda3-$ANACONDA_VERSION-Linux-x86_64.sh -o /tmp/anaconda.sh \
    && bash /tmp/anaconda.sh -b -p $ANACONDA_DIR \
    && rm /tmp/anaconda.sh
ENV PATH=$ANACONDA_DIR/bin:$PATH

RUN conda install -y keras \
    && conda install -y tensorflow
