def check_pair_sum_equal_k(nums,k):
    diff_set = set()
    for i in nums:
        if i in diff_set:
            return True
        else:
            diff_set.add(k-i)
    return False

if __name__ == "__main__":
    numbers = [int(x) for x in input().strip().split()]
    k = int(input().strip())
    print(check_pair_sum_equal_k(numbers,k))