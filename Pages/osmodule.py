import os.path

a=os.getcwd()
print(a)
b= os.path.join(a,'..')
print(b)
os.chdir(b)
print(os.getcwd())
os.mkdir('screens')