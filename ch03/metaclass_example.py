class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name} with MyMeta.__new__")
        # 可以在这里修改类的定义，例如添加新方法
        dct['greet'] = lambda self: f"Hello from {name}!"
        # 创建并返回类对象
        return super().__new__(cls, name, bases, dct)

    def __call__(cls, *args, **kwargs):
        print(f"Instantiating {cls.__name__} with MyMeta.__call__")
        # 在实例化之前可以执行一些逻辑
        instance = super().__call__(*args, **kwargs)
        # 在实例化之后也可以执行一些逻辑
        instance.creation_message = "This instance was created by MyMeta!"
        return instance

# 使用自定义元类
class MyClass(metaclass=MyMeta):
    def __init__(self, value):
        print("Initializing MyClass instance")
        self.value = value

# 当类被创建时，触发 __new__ 方法
# 输出：Creating class MyClass with MyMeta.__new__

# 当类实例化时，触发 __call__ 方法
instance = MyClass(10)
# 输出：
# Instantiating MyClass with MyMeta.__call__
# Initializing MyClass instance

# 验证 __new__ 添加的 greet 方法
print(instance.greet())
# 输出：Hello from MyClass!

# 验证 __call__ 添加的实例属性
print(instance.creation_message)
# 输出：This instance was created by MyMeta!
