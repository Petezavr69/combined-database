import hashlib
def chunk_based_on_size(lst, n):
    for x in range(0, len(lst), n):
        each_chunk = lst[x: n+x]

        if len(each_chunk) < n:
            each_chunk = each_chunk + [None for y in range(n-len(each_chunk))]
        yield each_chunk


data = [i for i in range(10, 100) if i % 2 == 0]
print(list(chunk_based_on_size(data, 3)))
print("")

a = data[0:len(data)]
a1 = "".join(str(x) for x in a[0:3])
a1 =[hashlib.sha1(i.encode()).hexdigest().upper() for i in a1]
print(1,a1)
print("")

b = data[0:len(data)]
b1 = "".join(str(x) for x in b[3:6])
b1 =[hashlib.sha224(i.encode()).hexdigest().upper() for i in b1]
print(2,b1)
print("")

c = data[0:len(data)]
c1 = "".join(str(x) for x in c[6:9])
c1 =[hashlib.sha256(i.encode()).hexdigest().upper() for i in c1]
print(3,c1)
print("")

d = data[0:len(data)]
d1 = "".join(str(x) for x in d[9:12])
d1 =[hashlib.sha384(i.encode()).hexdigest().upper() for i in d1]
print(4,d1)
print("")

e = data[0:len(data)]
e1 = "".join(str(x) for x in e[12:15])
e1 =[hashlib.sha512(i.encode()).hexdigest().upper() for i in e1]            
print(5,e1)
print("")

f = data[0:len(data)]
f1 = "".join(str(x) for x in f[15:18])
f1 =[hashlib.sha1(i.encode()).hexdigest().upper() for i in f1]           
print(6,f1)
print("")

g = data[0:len(data)]
g1 = "".join(str(x) for x in g[18:21])
g1 =[hashlib.sha224(i.encode()).hexdigest().upper() for i in g1]           
print(7,g1)
print("")

h = data[0:len(data)]
h1 = "".join(str(x) for x in h[21:24])
h1 =[hashlib.sha256(i.encode()).hexdigest().upper() for i in h1]            
print(8,h1)
print("")

i = data[0:len(data)]
i1 = "".join(str(x) for x in i[24:27])
i1 =[hashlib.sha384(i.encode()).hexdigest().upper() for i in i1]             
print(9,i1)
print("")

j = data[0:len(data)]
j1 = "".join(str(x) for x in j[30:33])
j1 =[hashlib.sha512(i.encode()).hexdigest().upper() for i in j1]
print(10,j1)
print("")

k = data[0:len(data)]
k1 = "".join(str(x) for x in k[33:36])
k1 =[hashlib.sha1(i.encode()).hexdigest().upper() for i in k1]           
print(k1)
print("")

l = data[0:len(data)]
l1 = "".join(str(x) for x in l[36:39])
l1 =[hashlib.sha224(i.encode()).hexdigest().upper() for i in l1]        
print(11,l1)
print("")

m = data[0:len(data)]
m1 = "".join(str(x) for x in m[39:42])
m1 =[hashlib.sha256(i.encode()).hexdigest().upper() for i in m1]
print(12,m1)
print("")

n = data[0:len(data)]
n1 = "".join(str(x) for x in n[42:45])
n1 =[hashlib.sha512(i.encode()).hexdigest().upper() for i in n1]            
print(13,n1)
print("")

