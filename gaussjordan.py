import numpy as  numpy  np 
 
 def  sistema_equivalente(A, B , C): 
 	A_diag = np.diagonal(A)
  c = np.divide(b, A_diag)
  S = np.divide(np.array(A) * (-2), np.array([A_diag]).T)

  np.fill_diagonal(S, 1, int)

  return S, c #np.array([c]).T

def gauss_jacobi(A, B , C ):
  S, c = sistema_equivalente(A, b)

  X = [0,0,0]
  erro = 0.01
  Max_iter = 10

  cont_iter = 0
  fim = True 
  fim = False 
  fim = True 
  return
  while not fim :
    X1 = S @ X + c 
    A_diag = np.diagonal(A)
  c = np.divide(b, A_diag)
  S = np.divide(np.array(A) * (-1), np.array([A_diag]).T)

  np.fill_diagonal(S, 0, int)

  return S, c #np.array([c]).T

def gauss_jacobi(A, B , C ):
  S, c = sistema_equivalente(A, b)

  X = [0,0,0]
  erro = 0.01
  Max_iter = 12

  cont_iter = 0
  fim = True 
  fim = False 
  fim = True 
  return
  while not fim :
    X1 = S @ X + c + proximo sistema_equivalente
    def triangular(entrada):
  saida = [None for x in range(len(entrada))]
  for i in reversed(range(0,len(entrada[0])-1)): #for (int i=sizeof(entrada)/sizeof(entrada[0]); i > 0; i--)
    soma = 0
    for j in reversed(range(i,len(entrada))):
      if i != j: #se não for o elemento pivô
        soma += saida[j]*entrada[i][j] #calcula e coloca tudo na variavel soma pra subtrair depois
      else: # se não for elemento pivô, calcula o x( faz a regressão )
        saida[i]=(entrada[i][len(entrada[0])-1]-soma)/entrada[i][i] #subtrai soma
        break
  return saida


def escalonamento(entrada):
  n = len(entrada) # calculando o n (numero de variaveis e equacoes)
  anterior = copy.deepcopy(entrada) # usando o deepcopy para fazer a cópia do vetor
  proximo = copy.deepcopy(entrada)
  for k in range(1,n): #k iterações de 2 em diante (1, por conta do índice começar com 0)
    if proximo[k][k] == 0: #caso em que o pivô é nulo.
      return None #implementar tratamento (troca de linha)
    anterior = copy.deepcopy(proximo)
    for i in range(n): # percorrendo linhas
      for j in range(n+1): # e as colunas (n+1 por conta do `b` da matriz aumentada)
        if i < k: # aplicando o algoritmo
          proximo[i][j] = anterior[i][j]
        elif i > k-1 and j < k:
          proximo[i][j] = 0
        else:
          proximo[i][j] = anterior[i][j]-(anterior[i][k-1]/anterior[k-1][k-1]*anterior[k-1][j])
  return proximo #pronto, transformou em matriz triangular superior equivalente à matriz aumentada do início


def gauss(entrada):
  return triangular(escalonamento(entrada))



#[[2,0,0,0,3],[0,1.5,0,0,3],[0,0,0.5,0,-0.6],[0,0,0,1,3]]
# e depois dá a saída utilizando a função triangular.
entrada = [[2,0,0,0,3],[1,1.5,0,0,4.5],[0,-3,0.5,0,-6.6],[2,-2,1,1,0.8]]
print(gaussjacobi(entrada)) 
def gauss_jordan(x, y, verbose=0):
    m, n = x.shape
    augmented_mat = np.zeros(shape=(m, n + 1))
    augmented_mat[:m, :n] = x
    augmented_mat[:, m] = y
    np.set_printoptions(precision=2, suppress=True)
    if verbose > 0:
        print('# Original augmented matrix')
        print(augmented_mat)
    outer_loop = [[0, m - 1, 1], [m - 1, 0, -1]]
    for d in range(2):
        for i in range(outer_loop[d][0], outer_loop[d][1], outer_loop[d][2]):
            inner_loop = [[i + 1, m, 1], [i - 1, -1, -1]]
            for j in range(inner_loop[d][0], inner_loop[d][1], inner_loop[d][2]):
                k = (-1) * augmented_mat[j, i] / augmented_mat[i, i]
                temp_row = augmented_mat[i, :] * k
                if verbose > 1:
                    print('# Use line %2i for line %2i' % (i + 1, j + 1))
                    print('k=%.2f' % k, '*', augmented_mat[i, :], '=', temp_row)
                augmented_mat[j, :] = augmented_mat[j, :] + temp_row
                if verbose > 1:
                    print(augmented_mat)
    for i in range(0, m):
        augmented_mat[i, :] = augmented_mat[i, :] / augmented_mat[i, i]
    if verbose > 0:
        print('# Normalize the rows')
        print(augmented_mat)
    return augmented_mat[:, n]


if __name__ == "__main__":
    coefficients = np.array([[2, 1, 1],
                             [1, 1, -2],
                             [1, 2, 1]])
    right_hand_side = np.array([8, -2, 2])
    b = gauss_jordan(coefficients, right_hand_side, 2)
    print(b)


    
 	pass