# ///////////////////////////////////////////////

# Recursive with helper

def count_appearances2(lst, val):
    def count_appearances_helper(lst, low, high, val):
        if (low == high):
            if (lst[low] == val):
                return 1
            else:
                return 0
        else:
            count_rest = count_appearances_helper(lst, low + 1, high, val)
            if (lst[low] == val):
                return count_rest + 1
            else:
                return count_rest

    if(len(lst) == 0):
        return 0
    else:
        return count_appearances_helper(lst, 0, len(lst) - 1, val)

#///////////////////////////////////////////////////

# Recursion with log(n) runtime

def power(a, n):

    if n==1:
        return a
    else:
        res = power(a, n-1)
        res *= a
    return res

def fast_power(a, n):

    if n==1:
        return a
    else:
        part = fast_power(a, n // 2)
        if (n % 2 == 0):
            return part * part
        else:
            return a * part * part

print(fast_power(2, 5))
