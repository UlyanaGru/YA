def ACond(troom,tcond,word):
    troom, tcond = int(troom), int(tcond)
    #Обработка возможных ошибок
    if abs(troom)>50 or abs(tcond)>50:
        return None
    if troom<tcond and word=='freeze':
        return troom
    if troom>tcond and word=='heat':
        return troom
    if troom!=tcond and word=='fan':
        return troom
    return str(tcond)

if __name__ == '__main__':
    troom, tcond = input().strip().split(' ')
    word = input().strip()
    print(ACond(troom,tcond,word))