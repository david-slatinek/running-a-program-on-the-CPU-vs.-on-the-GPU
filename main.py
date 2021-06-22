import json
import numpy as np
from numba import jit
from timeit import default_timer as timer

# Constant, used in the formula.
# Defined here to speed up the calculation, i.e. it's calculated only once
# and then placed in the formula.
SQRT_2PI = np.float32(np.sqrt(2 * np.pi))


# This function will run on the CPU.
def gaussian_cpu(values, mean, sigma):
    """Calculate values of the Gaussian function.

    :param values: list, function input parameters.
    :param mean: float, arithmetic mean.
    :param sigma: float, standard deviation.
    :return: list.
    """
    result = np.zeros_like(values)
    for index, item in enumerate(values):
        result[index] = (1 / (sigma * SQRT_2PI)) * (np.e ** (-0.5 * ((item - mean) / sigma) ** 2))
    return result


# This function will run on the GPU.
gaussian_gpu = jit(gaussian_cpu)


def write_to_file(name, values):
    """Write results to a file.

    :param name: string, file name, only prefix.
    :param values: dictionary, values to write.
    """
    with open(name + ".json", 'w') as f:
        json.dump(values, f, indent=4)


if __name__ == "__main__":
    # Randomly generated values.
    x = np.random.uniform(-3, 3, size=1000000).astype(np.float32)
    # Randomly generated mean.
    m = np.random.uniform(1, 10)
    # Randomly generated standard deviation.
    s = np.random.uniform(1, 10)

    # The number of rounds.
    n = 1

    # Used to store execution time.
    time_results = {}

    for i in range(n):
        start = timer()
        gaussian_cpu(x, m, s)
        end = timer() - start
        time_results[i] = end

    write_to_file("cpu", time_results)

    for i in range(n):
        start = timer()
        gaussian_gpu(x, m, s)
        end = timer() - start
        time_results[i] = end

    write_to_file("gpu", time_results)

