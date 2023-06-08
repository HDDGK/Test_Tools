import numpy as np
a=np.arange(100).reshape(5,20)
np.savetxt('a.csv',a,fmt='%d',delimiter=',')
a=np.arange(100).reshape(5,10,2)
a.tofile('b.dat',format='%d')
b=np.fromfile('b.dat', dtype=np.int32).reshape(5, 10, 2)
# print(b)
a=np.arange(100).reshape(5,10,2)
np.save('n.npy', a)
b=np.load('n.npy')


def np_random():
    global b
    np.random.seed(1)
    b = np.random.rand(2, 3, 4)
    print(b)
    b = np.random.randn(2, 3, 4)
    print(b)
    b = np.random.randint(100, 200, (3, 4))
    print(b)
    np.random.shuffle(b)
    print(b)
    c = np.random.permutation(b)
    print(c)
    print(b)
    print("???")
    b = np.random.randint(100, 200, (8,))
    print(b)
    d = np.random.choice(b, (3, 2))
    print(d)
    d = np.random.choice(b, (3, 2), replace=False)
    print(d)
    d = np.random.choice(b, (3, 2), p=b / np.sum(b))
    print(d)
    u = np.random.uniform(0, 10, (3, 4))
    print(u)
    n = np.random.normal(10, 5, (3, 4))
    print(n)

def np_sum():
    a=np.random.randint(0,100,(3,4))
    print(np.sum(a,axis=0))
    print(np.sum(a,axis=1))
    '''
    std：标准差
    var:方差
    
    '''
np_sum()


