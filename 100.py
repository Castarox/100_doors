def main():
    door=[]  
    for x in range(100):
        door.append(0)
    print("The following doors are open: ",end='')
    for i in range(100):
        for x in range(i, 100, i+1):
            if door[x] == 0:
                door[x]=1
            else:
                door[x]=0
        if i != 99:
            if door[i] == 1:
                print(i+1, end=', ')
        else:
            if door[i] == 1:
                print(i+1, end='')
    
            
if __name__ == '__main__': 
    main()
    

    