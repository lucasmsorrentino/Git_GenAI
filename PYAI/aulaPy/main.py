from aul03.math.fibonacci import enesimo_fib, sequencia_fib    

enesimo = enesimo_fib(5)
print(enesimo)

sequencia = sequencia_fib(5)
print(sequencia)



# import fibonacci as f
# import numpy as np

# print(f.enesimo_fib(11))

# print(f.estimar_prop_aurea(11))

# print(f.sequencia_fib(11))

# print(np.__name__)

# print(f.__name__)

# import numpy as np
# def sequencia_fib(qtde_valores):
#     resposta = np.empty(qtde_valores, dtype=int)
#     a = 0
#     b = 1
#     aux = b
#     idx = 0
#     while idx < qtde_valores:
#         resposta[idx] = a
#         aux = b
#         b = a + b
#         a = aux
#         idx += 1
#     return resposta


# def enesimo_fib(n):
#     a = 0
#     b = 1
#     aux = b
#     while n > 0:
#         aux = b
#         b = a + b
#         a = aux
#         n -= 1
#     return a

# def estimar_prop_aurea(n_fibonacci):
#     a = 0
#     b = 1
#     aux = b
#     while n_fibonacci > 0:
#         aux = b
#         b = a + b
#         a = aux
#         n_fibonacci -= 1
#     return b/a

# print(sequencia_fib(11))
# print(enesimo_fib(10))
# print(estimar_prop_aurea(10))