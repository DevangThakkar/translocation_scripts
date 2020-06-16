# work from latest LTS ubuntu release
FROM ubuntu:18.04

# run update and install necessary tools
RUN apt-get update -y && apt-get install -y \
    build-essential \
    libnss-sss \
    curl \
    vim \
    less \
    wget \
    unzip \
    zip \
    cmake \
    python \
    python-dev \
    python-biopython \
    gawk \
    gcc \
    g++ \
    make \
    automake \
    python-pip \
    zlib1g \
    zlib1g-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libnss-sss \
    libbz2-dev \
    liblzma-dev \
    libc6-dev \
    libtbb-dev \
    libtbb2 \
    bzip2 \
    tar \
    pigz \
    gzip \
    parallel \
    libcurl4-openssl-dev \
    libssl-dev \
    git \
    autoconf \
    bsdmainutils \
    bedtools \
    default-jdk \
    python-openpyxl \
    python-xlrd

# install numpy and pysam
WORKDIR /usr/local/bin
RUN pip install numpy
RUN pip install cython
RUN pip install pysam

# get script
ADD https://api.github.com/repos/DevangThakkar/translocation_scripts/git/refs/heads/ version.json
RUN git clone https://github.com/DevangThakkar/translocation_scripts.git
RUN cp translocation_scripts/anno_merger/Merge_delly_lumpy_destruct_annotation.py .
RUN cp translocation_scripts/anno_merger/Merge_delly_lumpy_destruct_annotation.py /home/Merge_delly_lumpy_destruct_annotation.py
RUN chmod +x Merge_delly_lumpy_destruct_annotation.py