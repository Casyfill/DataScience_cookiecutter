from glob import glob
from os.path import abspath, join, dirname
month = '{{cookiecutter.month}}'
pattern = join(abspath(dirname(__file__)), f'p{month}*')
print(pattern)

index = len(glob(pattern)) + 1
print(index)
print('{{cookiecutter.N}}')
