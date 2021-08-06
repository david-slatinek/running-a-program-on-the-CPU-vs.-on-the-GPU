#!/bin/bash
docker image build -t cpu_gpu_main .

docker container run -d --name cpu_gpu_container_main cpu_gpu_main
docker container cp cpu_gpu_container_main:app/cpu.json cpu.json
docker container cp cpu_gpu_container_main:app/gpu.json gpu.json
docker container rm cpu_gpu_container_main

docker container run -it --name cpu_gpu_container_main cpu_gpu_main bash
python3 main.py

docker image build -t cpu_gpu_plot -f Dockerfile.m .

docker container run -d --name cpu_gpu_container_plot cpu_gpu_plot
docker container cp cpu_gpu_container_plot:app/image.jpg image.jpg
docker container rm cpu_gpu_container_plot

docker container run -it --name cpu_gpu_container_plot cpu_gpu_plot bash
python3 plotting.py
