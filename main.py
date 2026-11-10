def ism(smth):
    ismlar = [smth]
    return ismlar
# print(ism(input("ismlarni kiriting: ")))


def its(*nima):
    return nima
# print(its(input("kiriting: ")))

def ismlar(**name):
    for a in name:
      print(a)
      print(name[a])
# print( ismlar (model = "Abrams", top = 152, yili = 2022))


