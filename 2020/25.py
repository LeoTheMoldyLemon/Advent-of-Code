
def crack_key(key):
    n=0
    sn=1
    while sn!=key:
        n+=1
        sn=(sn*7)%20201227
    return(n)

def generate_key(ls, sn):
    value=1
    for i in range(ls):
        value=(value*sn)%20201227
    return(value)


a=int(input())
b=int(input())

loop_size=crack_key(a)
enc_key=generate_key(loop_size, b)
print(enc_key)
