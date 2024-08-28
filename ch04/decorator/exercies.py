import functools


def condition_decorator(condition):
    def decorator(func):
        if condition:
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # 实际的装饰器逻辑
                return func(*args, **kwargs)
            return wrapper
        else:
            return func

    return decorator


# 使用用例
enable_decorator = True

@condition_decorator(enable_decorator)
def my_function(x):
    return x * 2
