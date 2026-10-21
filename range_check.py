def in_range(n,start,end): return start<=n<=end
n=int(input("Dev, number: ")); low=int(input("Range start: ")); high=int(input("Range end: "))
print("Within range" if in_range(n,low,high) else "Outside range")
