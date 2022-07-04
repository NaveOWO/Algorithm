

def change(arr):
    print("함수 호출 후: ", id(arr))
    if True:
        arr = []
        print("arr 재할당 후: ", id(arr))
    print("if 벗어났다: ", id(arr))
    return arr

for i in range(1):
    arr = [1, 2, 3, 4]
    print("함수 호출 전: ", id(arr))
    arr = change(arr)
    print(arr)