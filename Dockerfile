FROM nvidia/cuda:10.2-cudnn7-devel-ubuntu18.04

RUN apt-get update
RUN apt-get install -y python3 python3-pip
#RUN apt-get install -y libopencv-dev
#RUN pip3 install torch Pillow numpy
WORKDIR /Pconv
 
COPY requirements.txt /Pconv/
#COPY main.py /Pconv/
#COPY libs/ /Pconv/
COPY copy_dir /Pconv/
RUN pip3 install -r requirements.txt
#RUN pip3 install opencv-python

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update  
RUN apt-get install -y git cmake libgl1-mesa-dev libglib2.0-0 libsm6 libxrender1 libxext6
RUN pip3 install -U pip

RUN pip3 install  opencv-python
RUN pip3 install  Pillow

#COPY model_skip50.py /Pconv/

ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs
