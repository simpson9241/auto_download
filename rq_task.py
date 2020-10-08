def test_fib(n):
    if n<=1:
        return 1
    else:
        return test_fib(n-1)+test_fib(n-2)
