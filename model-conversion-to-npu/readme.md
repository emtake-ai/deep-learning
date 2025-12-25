<p align="center">
  <img src="https://raw.githubusercontent.com/emtake-ai/synabro/main/aimf.png" width="50%">
</p>


# 1. How to install
Synabro is evaluated on Ubuntu 22.04, compatible with Keras 2.15 and TensorFlow 2.15. for the best compatibility.
Synabro should be run on top of Docker container. Otherwise, it is recommended to install Synabro in Conda environment on Ubuntu 22.04 OS.

## Installing
Synabro SDK package consists of two parts:
  - 1. Synabro installer: synabro-1.3.0.tar.gz
  - 2. Dataset and Modelzoo: deliver by data.tar.gz


## using Docker
after untar for synabro-1.3.0.tar.gz, in dockerfile directory, you can run 

  - $ docker build -t synabro:1.3.0 .

Docker container should be created using volume argument to map a directory from the host environment to the container’s data directory

  - $ docker run -it --rm --gpus -v /path/to/data:/root/.local/synabro/data -v /path/to/workspace:/synabro --name synabro synabro:1.3.0 bash

## using Virtual environment
or you can use the python3 virtual environment for installing.

  - $ python3 -m venv ./../synabro
  - $ source ./../bin/activate

copy two parts into the synabro directory which created.

  - $ cp synabro-1.3.0.tar.gz .
  - $ cp data.tar.gz .

untar two tar-ball and install using pip3 with requirement and wheel

  - $ pip3 install -r requirements.txt
  - $ pip3 install synabro-1.3.0-py3-none-any.whl

patch two files and copy data folder to the ~/.local/synabro