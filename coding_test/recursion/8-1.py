def triple_step(n):
    f = [-1] * (n+1) 
    f[0], f[1], f[2], f[3] =  0, 1, 2, 4

    def _trist(n):
        if f[n] != -1:
            return f[n]
        f[n] = _trist(n-1) + _trist(n-2) + _trist(n-3)
        return f[n]

    return _trist(n)

if __name__ == '__main__':
    print(triple_step(5))