# Devolve o número de linhas da matriz M.
def matrows(M):
   return len(M)

# Complete para devolver o número de colunas da matriz M.
def matcols(M):
   return len(M[0])

# Complete a função para devolver uma matriz com m×n zeros.
def matzeros(m, n):
    return [[0 for i in range(n)] for j in range(m)]


def matzerosTEST(m, n):
   M = matzeros(m, n)
   M[0][1] = 1   # should change just 1 element!
   return M

# Complete a função para multiplicar a matriz A pela matriz B.
def matmult(A, B):
   assert matcols(A) == matrows(B)         #multiplicar Matrizes colunas de A == linhas de B
   C = []
   for i in range(matrows(A)):             #linhas A
        C.append([])
        for j in range(matcols(B)):       #colunas B
            C[i].append(0) 
            for k in range(matcols(A)):   #colunas A
                C[i][j] += A[i][k] * B[k][j]
   return C


def matmultTEST(A, B):
   C = matmult(A, B)
   return A, B, C

def main():
    print(matrows([[1, 2, 3], [4, 5, 6]]))
    print(matcols([[1, 2, 3], [4, 5, 6]]))
    print(matzeros(5, 8))
    print(matzerosTEST(5, 8))
    print(matmult([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
    print(matmultTEST([[1, 2], [3, 4]], [[5, 6], [7, 8]]))

main()
