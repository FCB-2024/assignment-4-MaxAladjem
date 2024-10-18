import sys
def main():
    
    def antiprimecalc(num):
        divnum = 0
        divi = 0
        divdef = 0
        if num == 1:
	    return "not antiprime"
        for i in range(1, num+1):
            if num % i == 0:
                divnum += 1
        for i in range(1, num):
            divi = 0
            for j in range(1, i+1):
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
