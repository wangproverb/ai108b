from net import Net
n = Net()

x = n.variable(1)
y = n.variable(2)
z = n.variable(3)

x2 = n.mul(x, x)
y2 = n.mul(y, y)
z2 = n.mul(z, z)

o = n.add(x2, y2)
out = n.add(o, z2)

n.gradient_descendent()
print('x={0:.5f} y={1:.5f} z={2:.5f}'.format(x.v,y.v,z.v))