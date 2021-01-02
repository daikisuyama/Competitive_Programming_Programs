#あーーーー5の倍数か
#そりゃそう、常に選ぶにはmodNを考えたときにすべて同じにしてmodNで0にすれば良いのか
#つまり、1mod5に全部できれば良い(2,3,4でもOK)
#制約がかなり厳しいことに注目したい(普通の探索じゃ無理)
import math
k=int(input())
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

x=[str(i) for i in range(10,55556) if ((i%10==1) and (isPrime(i)))][:k]
print(" ".join(x))
