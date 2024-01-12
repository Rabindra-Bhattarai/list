tuple

a=(1,2,3,4)
b=list(a)
b.insert(1,"ram")
print(b)

set
#is is immutable and duplicate data cannot be filled
a={1,2,3,4}
a.add("a")
print(a)

a={1,2,3,4}
b={5,6,7,8}
a.update(b)
print(a)

a={1,2,3,4}
a.remove(1)
print(a)

a={1,2,3,4}
a.discard(1)
print(a)

a={1,2,3,4}
a.pop()#cannt pass any argument
print(a)

a={1,2,3,4}
a.clear()
print(a)

a={1,2,3,4}
b={5,6,7,8}
c=a.union(b)
print(c)


a={1,2,3,4}
b={1,6,7,8}
c=a.intersection(b)
print(c)

a={1,2,3,4}
b={1,6,7,8}
c=a.difference(b)
print(c)

a={1,2,3,4}
b={1,6,7,8}
c=a.symmetric_difference(b)
print(c)


a={1,2,3,4}
b={5,6,7,8}
c=a.isdisjoint(b)
print(b)

a={1,2,3,4}
b={1,2,3,4}
c=a.issubset(b)
print(b)


a={5,6,7,8}
b={5,6,7,8}
c=a.issuperset(b)
print(b)


#disctionary

a={"a":1,"a":2}
print(a)

a={"a":1,"b":2}
a["a"]=8
print(a)

a={"a":1,"b":2}
a.update(a)
print(a)

a={"a":1,"b":2}
c=a.setdefault("", "cat")
print(a)


a={"a":1,"b":2}
c=a.setdefault("a", "cat")
print(a)

a={"a":1,"b":2}
c=a.get("a")
print(c)


a={"a":1,"b":2}
c=a.get("a", "Key not available")
print(c)

a={"a":1,"b":2}
b=a.pop("a")
print(a)



a["a"]:6
print(a)



a={"a":1,"b":2}
old_key="a"
new_key="z"
a[new_key]=a.pop(old_key)
print(a)



for i in a.keys():
    print(i)

