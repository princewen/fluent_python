# 列表推导式
print([x for x in range(4)]) # [0, 1, 2, 3]

# 在python2中，列表推导式中for关键词之后的赋值操作可能会影响列表推导上下文中的同名变量，但是python3已经修复
x = 'my precious'
dummy = [x for x in 'ABC']
print(x) # python2输出'C'，python3输出my precious

