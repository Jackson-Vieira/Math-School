
#Ordem 2
def solve_det_2(self, ma):
    n = len(ma)

    dp = ds = 1

    j = -1
    for i in range(n):
        dp *= ma[i][i]
        ds *= ma[i][j]
        j -= 1

    return dp-ds

def solve_det_3(self, ma):
    pass


#Ordem 2

#Ordem 3

#Ordem > 3