def func(x, n):
    #[1,2,3,4]
    k = 0
    for i in x:
        if i > n: 
            x[k] = 0
        k+=1
    print(x)


func([1,2,3,4], 1)
func([0,2,3,1,2,34,5,67], 3)