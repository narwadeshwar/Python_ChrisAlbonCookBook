import numpy as np
from scipy import sparse

vector_row = np.array([1,2,3,4,5,6])

vector_col = np.array([[1],[2],[3]])

matrix = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

mat_obj = np.mat([[1,2],[1,2],[1,2]])

matrix1 = np.array([[0,2],[1,0],[0,0]])

matrix_sparse = sparse.csr_matrix(matrix1)

#print(matrix.shape)

#print(matrix.size)

#print(matrix.ndim)

# Create function that add 100 to something

add_100 = lambda i: i + 100

#create vectorized function

vectorized_add_100 = np.vectorize(add_100)

#print(vectorized_add_100(matrix))

#print(np.max(matrix))
#print(np.min(matrix))

#print(np.max(matrix, axis=0))
#print(np.max(matrix,axis=1))

#print(np.mean(matrix))
#print(np.var(matrix))
#print(np.std(matrix))
#print(np.mean(matrix, axis=0))

#print(matrix.reshape(2,6))
#print(matrix.T)

#print(matrix.diagonal())

#print(matrix.trace())

#matrix = np.array([[1, -1, 3], [1, 1, 6], [3, 8, 9]])

#eigenvalues, eigenvectors = np.linalg.eig(matrix)

#print(eigenvalues)

#print(eigenvectors)

vector_a = np.array([1,2,3])

vector_b = np.array([4,5,6])

#print(np.dot(vector_a,vector_b))

#print(np.add(vector_a, vector_b))
#print(np.subtract(vector_a,vector_b))
#print(vector_a + vector_b)

#print(np.linalg.inv(matrix))

np.random.seed(0)

print(np.random.random(3))


# Generate three random integer between 1 and 10
print(np.random.randint(0, 11, 3))

# Draw three numbers from a normal distribution with mean 0.0 and standard deviation of 1.0
print(np.random.normal(0.0, 1.0, 3))

# Draw three numbers from a logistic distribution with mean 0.0 and scale of 1.0
print(np.random.logistic(0.0, 1.0, 3))

# Draw three numbers greater than or equal to 1.0 and less than 2.0
print(np.random.uniform(1.0, 2.0, 3))



