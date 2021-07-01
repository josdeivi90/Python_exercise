'''for i in range(7):
    for j in range(7):
        if (i == 0 or i == 1 or i == 5 or i == 6) and (j == 1 or j == 5):
            print('*',end='') 
        elif (i == 2 or i == 4) and (j == 2 or j == 4):
            print('*',end='')
        elif (i == 3 and j == 3):
            print('*',end='')
        else:
            print(' ',end='')
    print()
'''

'''
*******                                                                 
     *                                                                  
    *                                                                   
   *                                                                    
  *                                                                     
 *                                                                      
*******

'''
for i in range(7):
    for j in range(7):
        if (i == 0 or i == 6):
            print('*',end='') 
        elif (i == 1) and (j == 5):
            print('*',end='')
        elif (i == 2) and (j == 4):
            print('*',end='')
        elif (i == 3) and (j == 3):
            print('*',end='')
        elif (i == 4) and (j == 2):
            print('*',end='')
        elif (i == 5) and (j == 1):
            print('*',end='')
        else:
            print(' ',end='')
    print()

