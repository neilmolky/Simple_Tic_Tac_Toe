army = int(input().strip())
if army < 1:
    print('no army')
elif army < 10:
    print('few')
elif army < 50:
    print('pack')
elif army < 500:
    print('horde')
elif army < 1000:
    print('swarm')
else:
    print('leigion')
