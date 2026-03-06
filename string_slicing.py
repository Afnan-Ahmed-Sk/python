a="Anna univesity"
print(a[0:])
print(a[:7])
print(a[::-1])
print(a[-2:-5]) # slicing move left to right but here it start at right move towards left it is not possible it give empty string
print(a[-2:-5:-1])

s=slice(4,0)
print(a[s])
print("ananna"[0:3])