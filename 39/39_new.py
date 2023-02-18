def pythagoreanTriplets(limits) : 
    a, b, c, m = 0, 0, 0, 2
  
    # Limiting c would limit  
    # all a, b and c 
    while a+b+c < limits : 
          
        # Now loop on n from 1 to m-1 
        for n in range(1, m) : 
            a = m * m - n * n 
            b = 2 * m * n 
            c = m * m + n * n 
  
            # if c is greater than 
            # limit then break it 
            if a+b+c > limits : 
                break
  
            print(a, b, c) 
  
        m = m + 1

if __name__ == '__main__' :

    limit = 1001
    pythagoreanTriplets(limit)
