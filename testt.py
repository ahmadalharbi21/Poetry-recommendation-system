# # import numpy as np
import json

# # a = np.array([ 1, 2, 3, 4])
# # b = np.array([-1,-2, 3, 4])
# # print(f"Binary operators work element wise: {a + b}"); print('aaa')
# # # show common Course 1 example
# # X = np.array([[1,2,3]])
# # w = np.array([3,4,5])
# # c = np.dot(X, w)
# # print(X)
# # print(f"X[1] has shape {X.shape}")
# # print(f"w has shape {w.shape}")
# # print(f"c has shape {c.shape}")
# # print(c)

# # a = np.zeros((1, 5))                                       
# # print(f"a shape = {a.shape}, a = {a}")                     

# # a = np.zeros((2, 1))                                                                   
# # print(f"a shape = {a.shape}, a = {a}") 

# # a = np.random.random_sample((1, 1))  
# # print(f"a shape = {a.shape}, a = {a}") 
# # #vector 2-D slicing operations
# # a = np.arange(20).reshape(-1, 10)
# # print(f"a = \n{a}")

# # #access 5 consecutive elements (start:stop:step)
# # print("a[0, 2:7:1] = ", a[0, 2:7:1], ",  a[0, 2:7:1].shape =", a[0, 2:7:1].shape, "a 1-D array")

# # #access 5 consecutive elements (start:stop:step) in two rows
# # print("a[:, 2:7:1] = \n", a[:, 2:7:1], ",  a[:, 2:7:1].shape =", a[:, 2:7:1].shape, "a 2-D array")

# # # access all elements
# # print("a[:,:] = \n", a[:,:], ",  a[:,:].shape =", a[:,:].shape)

# # # access all elements in one row (very common usage)
# # print("a[1,:] = ", a[1,:], ",  a[1,:].shape =", a[1,:].shape, "a 1-D array")
# # # same as
# # print("a[1]   = ", a[1],   ",  a[1].shape   =", a[1].shape, "a 1-D array")

# # Specify the file path
file_path = "poemtext"

# Open the file in read mode
f = open(file_path, "r" , encoding='utf-8') 
    # Load the JSON data
data  = f.readlines()
ff = open('orgPoem','w', encoding='utf-8')
i = 1
for line in data:
    dic = dict()
    x = json.loads(line)
    dic[i] = f"{x}"
    y = f"{dic}"
    ff.write(y)
    ff.write('\n')
    i+=1






x = {1 : '2222'}

y = str(x)
print(y)





        




    
# f.close()
# ff.close()
# # Access the decoded data
