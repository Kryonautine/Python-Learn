from circumfer import calcircum, calarea

def circumference_test():
    assert calcircum(1) == 6.28

def area_test():
    assert calarea(1) == 3.14

circumference_test()
area_test()
