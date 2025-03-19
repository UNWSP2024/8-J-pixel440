#here is the initial generator

def main():
    full_name=input("Please enter your first, middle and last names:")

    name=full_name.split()

    for t in name:
        print(t[0].upper(),sep='',end='')
        print('.',sep=' ',end='')

if __name__=="__main__":
    main()
