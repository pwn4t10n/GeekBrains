print('Введите количество секунд: ')
s = int(input())
hrs = s // 3600
mnt = (s - hrs * 3600) // 60
sec = s - hrs * 3600 - mnt * 60
print(f"{hrs}ч:{mnt}м:{sec}с")
