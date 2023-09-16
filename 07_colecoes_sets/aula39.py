s1 = {1,3,5,7,9}
s2 = {2,4,6,8,10}

s3 = s1.union(s2)
print(s3)
print(100*"#")

s4 = s1.intersection_update(s2)
print(s4)
print(100*"#")

s5 = s1.symmetric_difference(s2)
print(s5)
