import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Set parameters.
input_parameters = np.array([1000000, 10000000, 20000000]).reshape((-1, 1))
cpu_time = np.array([4.61113, 44.97076, 92.44827])
gpu_time = np.array([0.03926, 0.39649, 0.80460])

# Create a linear regression model.
model_cpu = LinearRegression().fit(input_parameters, cpu_time)
model_gpu = LinearRegression().fit(input_parameters, gpu_time)

# Generate values for prediction.
x_predict = np.arange(30000000, 510000000, 10000000).reshape((-1, 1))

# Calculate predictions.
y_predict_cpu = model_cpu.predict(x_predict)
y_predict_gpu = model_gpu.predict(x_predict)

# Plot values.
plt.plot(x_predict, y_predict_cpu, label="CPU")
plt.plot(x_predict, y_predict_gpu, label="GPU")

# Display plot info.
plt.xlabel('Parameters size')
plt.ylabel('Time in seconds')
plt.title('Time taken to run a program on specific parameters size')

# Show legend and plot.
plt.legend()
plt.show()
