import os
import sys

print(True)
print(os.environ['KEK'])

os.execl(sys.executable, 'python',  __file__, *sys.argv[1:])



