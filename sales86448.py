#File sales86448.py
#Author:Simmy Payyappilly Varghese,Student ID:86448
#Program to read a file sales.Txt and create a new File Total.txt with sum of the sales


def main():
    filevar=open("SALES.TXT","r")
    outFile=open("TOTALS.TXT","w")
    grandSum=0;                                                  #To store the grandtotal 
    print("{0:^18}{1:^18}".format("Name","Total"),file=outFile)
    for i in filevar:#corected from range to filevar ,instead of using range use the file variable
        #lines=filevar.readline()                                  #Read each of the lines and split it to a list 
        line=i.split() 
        total=0;
        print("{0:>16}".format(line[0]),end="",file=outFile)      #Right Justification
        for i in line[1:]:
            total=total+eval(i)                                   #convert the elements from index 1 and sum up and store in total
        grandSum=grandSum+total               
        print("{0:12}".format(total),file=outFile)
    print("Grand Total:{0:15}".format(grandSum),file=outFile)
    filevar.close()
    outFile.close()
main()  
