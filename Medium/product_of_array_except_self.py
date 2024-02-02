#product_of_array_except_self


def arrayOfProducts(array):
    # Write your code here.
    leftArr= [1]*len(array)
    rightArr= [1]*len(array)
    resArr= [1]*len(array)
    product = 1

    for i in range(len(array)):
        leftArr[i]=product
        product=product*array[i]
    product = 1
    for i in reversed(range(len(array))):
        rightArr[i]=product
        product=product*array[i]
       
    for i in range(len(array)):
        resArr[i] = rightArr[i] * leftArr[i]

    return resArr