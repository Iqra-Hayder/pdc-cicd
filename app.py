from multiprocessing import Pool, cpu_count


def square(n):
    return n * n


def parallel_sum_of_squares(numbers, workers=None):
    """Sum of squares computed in parallel across worker processes."""
    workers = workers or cpu_count()
    with Pool(processes=workers) as pool:
        return sum(pool.map(square, numbers))


if __name__ == "__main__":
    data = list(range(1, 1001))
    result = parallel_sum_of_squares(data)
    print(f"Sum of squares 1..1000 using {cpu_count()} workers = {result}")
