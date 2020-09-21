print('(a)')
for a in range(10):
    for b in range(a):
        print('*', end='')
    print('*')

print('')

print('(b)')
for a in range(10):
    for b in range(9-a):
        print('*', end='')
    print('*')

print('')

print('(c)')
for a in range(10):
    for c in range(a):
        print(' ', end='')
    for b in range(9-a):
        print('*',end='')
    print ('*')

print('')

print('(d)')
for a in range(10):
    for c in range(9-a):
        print(' ', end='')
    for b in range(a):
        print('*', end='')
    print ('')
print('')
