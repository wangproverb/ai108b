# P(x,y,z) = P(x) * P(y) * P(z)
def naiveProb(prob, list):
  p = 1
  for e in list:
      p = p * prob[e]
  return p

prob = {
  'x': 0.5,
  'y': 0.2,
  'z': 0.3
}

print('P(x,y,z) = ', naiveProb(prob, ['x','y','z']))
