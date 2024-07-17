def find_mth_max_nth_min(arr, M, N):
    sorted_arr = sorted(arr)
    mth_max = sorted_arr[-M]
    nth_min = sorted_arr[N-1]
    sum_result = mth_max + nth_min
    difference_result = mth_max - nth_min
    product_result = mth_max * nth_min
    return mth_max, nth_min, sum_result, difference_result, product_result
array = [14, 16, 87, 36, 25, 89, 34]
M = 1
N = 3
mth_max, nth_min, sum_result, difference_result, product_result = find_mth_max_nth_min(array, M, N)
print(f"{M}st Maximum Number = {mth_max}")
print(f"{N}rd Minimum Number = {nth_min}")
print(f"Sum = {sum_result}")
print(f"Difference = {difference_result}")
print(f"Product = {product_result}")
