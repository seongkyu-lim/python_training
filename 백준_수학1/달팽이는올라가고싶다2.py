up, down, height = map(int,input().split())

import math

print(math.ceil((height - up) / (up - down))+1)