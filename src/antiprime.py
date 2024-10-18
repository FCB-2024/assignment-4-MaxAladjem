import sys
def main():
    
    def antiprimecalc(num):
        i = 1
        divnum = 0
        divi = 0
        divdef = 0
        for i in range(1, num):
            if num % i == 0:
                divnum += 1
        for i in range(1, num):
            divi = 0
            for j in range(1, i):
                if i % j == 0:
                    divi += 1
            if divi >= divnum:
                return "not antiprime"
        return "antiprime"
    num = int(sys.argv[1])
    result = antiprimecalc(num)
    return result



if __name__ == "__main__" :

	print(main())
