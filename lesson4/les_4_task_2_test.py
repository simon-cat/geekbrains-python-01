import timeit
import cProfile
import les_4_task_2

print(timeit.timeit("sieve(1)", \
                    setup="from les_4_task_2 import sieve", number=10000))
print(timeit.timeit("sieve(2)", \
                    setup="from les_4_task_2 import sieve", number=10000))
print(timeit.timeit("sieve(5)", \
                    setup="from les_4_task_2 import sieve", number=10000))

print(timeit.timeit("prime(1)", \
                    setup="from les_4_task_2 import prime", number=10000))
print(timeit.timeit("prime(2)", \
                    setup="from les_4_task_2 import prime", number=10000))
print(timeit.timeit("prime(5)", \
                    setup="from les_4_task_2 import prime", number=10000))

cProfile.run('les_4_task_2.sieve(1)')
cProfile.run('les_4_task_2.sieve(2)')
cProfile.run('les_4_task_2.sieve(5)')

cProfile.run('les_4_task_2.prime(1)')
cProfile.run('les_4_task_2.prime(2)')
cProfile.run('les_4_task_2.prime(5)')
