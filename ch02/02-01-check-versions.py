
import sys
import sklearn
from packaging.version import  Version

Greeting = "Welcome to Machine Learning with Pytorch!"
print(Greeting)

assert sys.version_info >= (3, 10), "Python version must be >= 3.10"
print(f"Python version: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")

# "Scikit-Learn version must be >= 1.6.1"
assert Version(sklearn.__version__) >= Version("1.6.1")
print(f"Scikit-Learn version: {sklearn.__version__}")   # now v1.7.2