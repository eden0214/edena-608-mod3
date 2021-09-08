# Use the statistics module to calculate measures of dispersion for a population

import statistics

# Calculate population variance using pvariance()
pop_var = statistics.pvariance([1, 3, 4, 2, 6, 5, 3, 4, 5, 2])
print(f'The population variance of 10 die rolls is:', pop_var)

# Calculate population standard deviation using pstdev()
pop_st_dev = statistics.pstdev([1, 3, 4, 2, 6, 5, 3, 4, 5, 2])
print(f'The population standard deviation of 10 die rolls is:', pop_st_dev)
