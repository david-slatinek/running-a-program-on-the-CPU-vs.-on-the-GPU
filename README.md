# Comparison of execution time when running a program on the CPU vs. on the GPU
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![made-with-latex](https://img.shields.io/badge/Made%20with-LaTeX-1f425f.svg)](https://www.latex-project.org/)
[![made-with-docker](https://img.shields.io/badge/Made%20with-Docker-1f425f.svg
)](https://www.docker.com/)

# Abstract
The purpose of this paper is to demonstrate the time difference between running a python program on the CPU vs. on the GPU when calculating the result of a complex math function. We describe the algorithm implementation, along with the math function used in the program. Next, we present the results of the experiments. In the end, we define a linear regression model for determining the time taken to finish the calculation of arbitrary input size.

## Further reading
Entire document is available [here](document.pdf).

# Getting started
Clone the project or download as a zip and then unzip it.

## 1. Run with docker
You can leave default parameters for **main.py** or you can change the parameters size and the number of rounds:
```python
# Randomly generated values.
x = np.random.uniform(-3, 3, size=1000000).astype(np.float32)

# The number of rounds.
n = 1
```

Now, run the following commands:
```bash
docker image build -t cpu_gpu_main .
docker container run -d --name cpu_gpu_container_main cpu_gpu_main
```
After the container stops - check with *docker container ls -a* -, run the following:
```bash
docker container cp cpu_gpu_container_main:app/cpu.json cpu.json
docker container cp cpu_gpu_container_main:app/gpu.json gpu.json
```
You get two files: *cpu.json* and *gpu.json*, which contain results for execution time.
\
You can delete the container by running:
```bash
docker container rm cpu_gpu_container_main
```
\
\
For **plotting.py** you can leave the default parameters or you can change CPU or GPU execution time - read values from *cpu.json* or *gpu.json*:
```python
cpu_time = np.array([4.61113, 44.97076, 92.44827])
gpu_time = np.array([0.03926, 0.39649, 0.80460])
```
You can also change values for prediction:
```python
x_predict = np.arange(30000000, 510000000, 10000000).reshape((-1, 1))
```

Afterward, run the following:
```bash
docker image build -t cpu_gpu_plot -f Dockerfile.m .
docker container run -d --name cpu_gpu_container_plot cpu_gpu_plot
```
When the container stops - check with *docker container ls -a* -, run the following command:
```bash
docker container cp cpu_gpu_container_plot:app/image.jpg image.jpg
```
You get *image.jpg* that presents the result of a linear regression model.
\
\
You can delete the container by running:
```bash
docker container rm cpu_gpu_container_plot
```

### Alternative option
Instead of running the container in the background, you can connect to it and manually run python files.
\
For **main.py** use:
```bash
docker image build -t cpu_gpu_main .
docker container run -it --name cpu_gpu_container_main cpu_gpu_main bash
python3 main.py
```
and for **plotting.py** use:
```bash
docker image build -t cpu_gpu_plot -f Dockerfile.m .
docker container run -it --name cpu_gpu_container_plot cpu_gpu_plot bash
python3 plotting.py
```
Following that, you have to use *docker cp* to get files to the host machine.
\
\
***Note:*** this approach is not advisable, because it can take a long time for the program to finish, especially if the parameters size or the number of rounds is large.


## 2. Run with pip
Create a virtual environment and run
```python
pip install -r requirements_main.txt
```
for **main.py**
or
```python
pip install -r requirements_plotting.txt
```
for **plotting.py**.
\
Now run
```bash
python3 main.py
```
or
```bash
python3 plotting.py
```
respectively.
