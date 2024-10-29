# pool_ops.py
#
# Usage: python3 pool_ops.py c_in h_in w_in h_pool w_pool s p
#  Text explaining script usage
# Parameters:
#  c_in: input channel count
#  h_in: input height count
#  w_in: input width count
#  h_pool: average pooling kernel height count
#  w_pool: average pooling kernel width count
#  s: stride of average pooling kernel
#  p: amount of padding on each of the four input map sides
# Output:
#  channel count, height count, width count
#  additions performed, multiplicaitons performed, divisions performed
#
# Written by Lee Wallenfang

# import Python modules
import math # math module
import sys # argv

# initialize script arguments
c_in=float('nan') # input channel count
h_in=float('nan') # input height count
w_in=float('nan') # input width count
h_pool=float('nan') # average pooling kernel height count
w_pool=float('nan') # average pooling kernel width count
s=float('nan') # stride of average pooling kernel
p=float('nan') # amount of padding on each of the four input map sides

# parse script arguments
if len(sys.argv)==8:
  c_in=float(sys.argv[1]) # input channel count
  h_in=float(sys.argv[2]) # input height count
  w_in=float(sys.argv[3]) # input width count
  h_pool=float(sys.argv[4]) # average pooling kernel height count
  w_pool=float(sys.argv[5]) # average pooling kernel width count
  s=float(sys.argv[6]) # stride of average pooling kernel
  p=float(sys.argv[7]) # amount of padding on each of the four input map sides
else:
  print(\
   'Usage: '\
   'python3 pool_ops.py c_in h_in w_in h_pool w_pool s p'\
  )
  exit()

# write script below this line
h_out = ((h_in+2*p-h_pool)/s)+1
w_out = ((w_in+2*p-w_pool)/s)+1
adds = c_in*h_out*w_out*(h_pool*w_pool-1)
divs = c_in*h_out*w_out
c_out = c_in
muls = 0

print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed