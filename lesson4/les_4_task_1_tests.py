import timeit
import cProfile
import les_4_task_1

print(timeit.timeit("reverse_num_recursive(1234567890123456789012345678901234567890)", \
                    setup="from les_4_task_1 import reverse_num_recursive", number=10000))
print(timeit.timeit("reverse_num(1234567890123456789012345678901234567890)", \
                    setup="from les_4_task_1 import reverse_num", number=10000))
print(timeit.timeit("reverse_num_int(1234567890123456789012345678901234567890)",\
                    setup="from les_4_task_1 import reverse_num_int", number=10000))

cProfile.run('les_4_task_1.reverse_num_recursive(1234567890123456789012345678901234567890)')
cProfile.run('les_4_task_1.reverse_num(1234567890123456789012345678901234567890)')
cProfile.run('les_4_task_1.reverse_num_int(1234567890123456789012345678901234567890)')