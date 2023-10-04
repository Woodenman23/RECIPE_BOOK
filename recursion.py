def foo(n: int) -> int:
    # base case
    if n == 1:
        return 1
    # recurse
    return n + foo(n - 1)


print(foo(5))

# 3 steps:
# pre (n+)
# recurse: foo(n-1)
# post

# MAZE SOLVER
