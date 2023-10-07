from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
print(np.__version__)

python_list = [1, 2, 3, 4, 5]
print("Type :", type(python_list))
print(python_list)

two_dimension_array = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(two_dimension_array)

numpy_array_from_list = np.array(python_list)
print(type(numpy_array_from_list))
print(numpy_array_from_list)
numy_array_from_list2 = np.array(python_list, dtype=float)
print(numy_array_from_list2)

numpy_bool_arr = np.array([1, 0, -1, 1], dtype=bool)
print(numpy_bool_arr)

numpy_two_dimensional_list = np.array(two_dimension_array)
print(type(numpy_two_dimensional_list))
print(numpy_two_dimensional_list)

np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())

python_tuple = (1, 2, 3, 4, 5)
print(type(python_tuple))  # <class 'tuple'>
print('python_tuple: ', python_tuple)  # python_tuple:  (1, 2, 3, 4, 5)

numpy_array_from_tuple = np.array(python_tuple)
print(type(numpy_array_from_tuple))  # <class 'numpy.ndarray'>
# numpy_array_from_tuple:  [1 2 3 4 5]
print('numpy_array_from_tuple: ', numpy_array_from_tuple)

nums = np.array([1, 2, 3, 4, 5])
print(nums)
print('shape of nums: ', nums.shape)
print(numpy_two_dimensional_list)
print('shape of numpy_two_dimensional_list: ',
      numpy_two_dimensional_list.shape)
three_by_four_array = np.array([[0, 1, 2, 3],
                                [4, 5, 6, 7],
                                [8, 9, 10, 11]])
print(three_by_four_array.shape)


int_lists = [-3, -2, -1, 0, 1, 2, 3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)

print(numpy_array_from_list.size)
print(numpy_two_dimensional_list.size)

print("original array", numpy_array_from_list)
print("array after adding 10", numpy_array_from_list+10)
print("array after minus 5", numpy_array_from_list-5)
print("array after multiple 10", numpy_array_from_list*10)
print("array after divide by 2", numpy_array_from_list/2)
print("array after modulus  3", numpy_array_from_list % 3)
print("array after applying Floor division", numpy_array_from_list // 3)
print("array after applying expotential", numpy_array_from_list ** 2)

numpy_int_arr = np.array([1, 2, 3, 4])
numpy_float_arr = np.array([1.1, 2.0, 3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1, 2, 3], dtype='bool')

print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)

numpy_int_arr = np.array([1, 2, 3, 4], dtype='float')
print(numpy_int_arr)
numpy_int_arr = np.array([1., 2., 3., 4.], dtype='int')
print(numpy_int_arr)
numpy_int_arr = np.array([1., 2., 3., 4.], dtype='bool')
print(numpy_int_arr)
str_array = np.array(['1', '2', '3'], dtype='<U21')
print(str_array)
numpy_int_arr = np.array([1, 2, 3, 4], dtype='float')
print(numpy_int_arr.astype('int').astype('str'))


two_dimension_array = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(type(two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)

# 2 Dimension Array
two_dimension_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)

first_column = two_dimension_array[:, 0]
second_column = two_dimension_array[:, 1]
third_column = two_dimension_array[:, 2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)
print(two_dimension_array[1, 2])

two_dimension_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)
print(two_dimension_array)
print(two_dimension_array[::])
print(two_dimension_array[::-1, ::-1])

print(two_dimension_array)
two_dimension_array[1, 1] = 55
two_dimension_array[1, 2] = 44
print(two_dimension_array)

numpy_zeroes = np.ones((3, 3), dtype=int, order='C')
print(numpy_zeroes)
print(numpy_zeroes * 2)

first_shape = np.array([(1, 2, 3), (4, 5, 6)])
print(first_shape)
reshaped = first_shape.reshape(3, 2)
print(reshaped)
print(reshaped.flatten())

np_list_one = np.array([1, 2, 3])
np_list_two = np.array([4, 5, 6])

print(np_list_one + np_list_two)
print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))
print('Verticle Append:', np.vstack((np_list_one, np_list_two)))
random_float = np.random.random()
print(random_float)
# Generate a random float  number
random_floats = np.random.random(5)
print(random_floats)

random_int = np.random.randint(2, 11, size=(5, 3))
print(random_int)

normal_array = np.random.normal(79, 15, 80)
print(normal_array)

sns.set()
# plt.hist(normal_array, color="grey", bins=50)

four_by_four_matrix = np.matrix(np.ones((4, 4), dtype=float))
print(four_by_four_matrix)
np.asarray(four_by_four_matrix)[2] = 2
print(four_by_four_matrix)
whole_numbers = np.arange(0, 20, 1)
print(whole_numbers)
print(np.linspace(1.0, 5.0, num=10))
print(np.linspace(1.0, 5.0, num=10, endpoint=False))
print(np.logspace(2, 4.0, num=4))
x = np.array([1, 2, 3, 4], dtype=np.complex128)
print(x)
print(x.itemsize)

np_list = np.array([(1, 2, 3), (4, 5, 6)])
print(np_list)

print('First row: ', np_list[0])
print('Second row: ', np_list[1])
print('First column: ', np_list[:, 0])
print('Second column: ', np_list[:, 1])
print('Third column: ', np_list[:, 2])

np_normal_dis = np.random.normal(5, 0.5, 100)
print(np_normal_dis)
print('min: ', np_normal_dis.min())
print('max: ', np_normal_dis.max())
print('mean: ', np_normal_dis.mean())
# print('median: ', np_normal_dis.var())
print('sd: ', np_normal_dis.std())

print(two_dimension_array)
print('Column with minimum: ', np.amin(two_dimension_array, axis=0))
print('Column with maximum: ', np.amax(two_dimension_array, axis=0))
print('=== Row ==')
print('Row with minimum: ', np.amin(two_dimension_array, axis=1))
print('Row with maximum: ', np.amax(two_dimension_array, axis=1))

a = [1, 2, 3]
print('Tile:   ', np.tile(a, 2))
print('Repeat: ', np.repeat(a, 2))
one_random_num = np.random.random()
print(one_random_num)
r = np.random.random(size=[2, 3])
print(r)
print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))
rand = np.random.rand(2, 2)
print(rand)
rand2 = np.random.randn(2, 2)
print(rand2)

rand_int = np.random.randint(0, 10, size=[5, 3])
print(rand_int)
# mean, standard deviation, number of samples
np_normal_dis = np.random.normal(5, 0.5, 1000)
# print(np_normal_dis)
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))
plt.hist(np_normal_dis, color="grey", bins=21)
# plt.show()


# Linear algebra
# Dot product: product of two arrays
f = np.array([1, 2, 3])
g = np.array([4, 5, 3])
# 1*4+2*5 + 3*3
print(np.dot(f, g))  # 23

h = [[1, 2], [3, 4]]
i = [[5, 6], [7, 8]]
# 1*5+2*7 = 19
print(np.matmul(h, i))
print(np.linalg.det(i))
Z = np.zeros((8, 8))
Z[1::2, ::2] = 1
Z[::2, 1::2] = 1

print(Z)

np_arr = np.arange(0, 11)
print(np_arr + 2)

temp = np.array([1, 2, 3, 4, 5])
pressure = temp * 2 + 5
print(pressure)

plt.plot(temp, pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()

mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.distplot(x)
ax.set(xlabel="x", ylabel='y')
plt.show()
