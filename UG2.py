import timeit

#Fibbonaci Iteratif
def iter_fibo(n):
    a = 0
    b = 1

    if n < 0:
        return "Salah Input"
    elif n == 0:
        return(0)
    elif n == 1:
        return(b)
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return(b)

#Fibbonaci Rekursif
def rec_fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return rec_fibo(n - 1) + rec_fibo(n - 2)


#record data fibo iteratif

print("="*15+"Fibbonaci Iteratif"+"="*15)
for i in range(1, 40):
    start = timeit.default_timer()
    hasil = iter_fibo(i)
    end = timeit.default_timer()
    print(f'Fibonacci deret ke-{i} adalah {hasil}. Dengan fungsi iteratif, membutuhkan waktu {end-start} detik')

print()
print()


#record data fibo rekursif

print("="*15+"Fibbonaci Rekursif"+"="*15)
for i in range(1, 40):
    start = timeit.default_timer()
    hasil = rec_fibo(i)
    end = timeit.default_timer()
    print(f'Fibonacci deret ke-{i} adalah {hasil}. Dengan fungsi rekursif, membutuhkan waktu {end-start} detik')