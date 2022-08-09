
for x in range(1,21):
    y = round(100*x**(1.5),2)
    print(f"\t{y} ",end='\t')
    if x % 5 == 0:
        print("lvl = ",x)

    # y = 100 * x ^ 1.5