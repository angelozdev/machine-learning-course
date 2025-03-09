import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray

l: list[int] = [1, 2, 3, 4, 5]
l_2D: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

arr: NDArray[np.int32] = np.array(l, dtype=np.int32)
arr_2D: NDArray[np.int32] = np.array(l_2D, dtype=np.int32)

# .shape => it returns a tuple of the dimensions of the array
print("Shape of arr:", arr.shape)
print("Shape of arr_2D:", arr_2D.shape)

# .reshape => it returns a new array with the same data but with a different shape
print("Reshaped arr:", arr.reshape(5, 1))
print("Reshaped arr_2D:", arr_2D.reshape(3, 3))

# .ndim => it returns the number of dimensions of the array
print("Number of dimensions of arr:", arr.ndim)
print("Number of dimensions of arr_2D:", arr_2D.ndim)

# .size => it returns the total number of elements in the array
print("Size of arr:", arr.size)
print("Size of arr_2D:", arr_2D.size)

# .dtype => it returns the data type of the elements in the array
arr = np.array([1, 2, 3, 4, 5], dtype=np.float32)
print("Data type of arr:", arr.dtype)
print("Data type of arr_2D:", arr_2D.dtype)

# .zeros => it returns an array of the given shape and type, filled with zeros
zeros_arr: NDArray[np.int32] = np.zeros((4, 3), dtype=np.int32)
print("Zeros array:", zeros_arr)

# .ones => it returns an array of the given shape and type, filled with ones
ones_arr: NDArray[np.int32] = np.ones((3, 4), dtype=np.int32)
print("Ones array:", ones_arr)

# .empty => it returns an array of the given shape and type, filled with random values
empty_arr: NDArray[np.int32] = np.empty((3, 4), dtype=np.int32)
print("Empty array:", empty_arr)

# .arange => it returns an array of evenly spaced numbers over a specified interval
arange_arr: NDArray[np.int32] = np.arange(start=0, stop=21, step=2)
print("Arange array:", arange_arr)

# .linspace => it returns an array of evenly spaced numbers over a specified interval
linspace_arr: NDArray[np.int32] = np.linspace(start=0, stop=21, num=50)
print("Linspace array:", linspace_arr)

rads = np.linspace(start=0, stop=2 * np.pi, num=20)
print("Rads:", rads)

# plt.figure(figsize=(5, 5))
# plt.scatter(np.sin(rads), np.cos(rads))
# plt.show()


# + => element-wise addition
a: NDArray[np.int32] = np.arange(start=1, stop=4)
b: NDArray[np.int32] = np.arange(start=4, stop=7)
print("[1, 2, 3] + [4, 5, 6]:", a + b)

# - => element-wise subtraction
print("[1, 2, 3] - [4, 5, 6]:", a - b)

# * => element-wise multiplication
print("[1, 2, 3] * [4, 5, 6]:", a * b)

# / => element-wise division
print("[1, 2, 3] / [4, 5, 6]:", a / b)

# .concatenate => it concatenates two arrays
print("Concatenated arrays:", np.concatenate((a, b)))

# .vstack => it concatenates two arrays vertically
print("Vertically stacked arrays:", np.vstack((a, b)))

# .hstack => it concatenates two arrays horizontally
print("Horizontally stacked arrays:", np.hstack((a, b)))

# .split => it splits an array into multiple sub-arrays
print("Split arrays:", np.split(a, 3))

# .reshape => it reshapes an array to a new shape
print("Reshaped array:", a.reshape(3, 1))

# .sort => it sorts an array
print("Sorted array:", np.sort(a))

# .argsort => it returns the indices that would sort an array
print("Indices that would sort array:", np.argsort(a))

# .random => it returns an array of random numbers
## .default_rng => it returns a default random number generator
rng: np.random.Generator = np.random.default_rng(seed=1997)

## .rand => it returns an array of random numbers from a uniform distribution
nums = rng.random(size=1000)
print("Random numbers:", nums)

# plt.figure(figsize=(5, 5))
# plt.hist(nums, bins=100)
# plt.show()

## .normal => it returns an array of random numbers from a normal distribution
nums = rng.normal(loc=0, scale=1, size=1000)
print("Normal numbers:", nums)

# plt.hist(nums, bins=50, density=True, alpha=0.6, color='b')
# plt.xlabel('Valor')
# plt.ylabel('Frecuencia')
# plt.title('Distribución Normal (media=0, desviación=1)')
# plt.show()


## .integers => it returns an array of random integers
nums = rng.integers(low=0, high=10, size=1000)
print("Random integers:", nums)

plt.hist(nums, bins=10, density=True, alpha=0.6, color="r")
plt.show()
