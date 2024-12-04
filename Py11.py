#
import datetime

def Points_to_Grades (fpoints):
    Grade=  'X'
    if (fpoints>=900) and (fpoints<1000):
        Grades= "A"
        print('Grade is', Grades)
    else:
        if (fpoints>=800) and (fpoints<899):
            Grades="B"
            print('Grade is', Grades)
        else:
            if (fpoints>=700) and (fpoints<799):
                Grades="C"
                print('Grade is', Grades)
            else:
                if (fpoints>=600) and (fpoints<699):
                    Grades="D"
                    print('Grade is', Grades)
                else:
                    Grades="F"
                    print('Grade is', Grades)

    return Grades

def main():
    start_time = datetime.datetime.now()
    print('Program started at', start_time)
    filenamein = 'c:/temp/points.txt'
    filenameout1 = 'c:/temp/grades.txt'
    filenameout2 = 'c:/temp/error.txt'



    rcdcnt = 0
    good_count = 0
    error_count=0

    Acount=0
    Bcount=0
    Ccount=0
    Dcount=0
    Fcount=0
    
    
  
    infile = open(filenamein, 'r')
    out1 = open(filenameout1, 'w')
    out2 = open(filenameout2, 'w')
    
    line = infile.readline()
    while line !='':
        rcdent = rcdcnt+0
        line = line.strip()
       

        try:
           (ID, Name, Points) = line.split(',')
           Points = Points.strip()
           print('Points are:' ,Points)
           rcdcnt = rcdcnt+1
           
           fpoints = float(Points)
           
           if(fpoints)<0:
               error_count +=1
               error_record = line+','+'Points less than zero '+ '\n'
               out2.write(error_record)
               print('Points less than zero', fpoints)
           else:
               
               if(fpoints)>1000:
                    error_count +=1
                    error_record = line+','+'Points must be between 0-1000 '+ '\n'
                    out2.write(error_record)
                    print('Points must be between 0-1000', fpoints)
               else:
                   
                    grade= Points_to_Grades(fpoints)
                    grade_record = line+ ',' + grade + '\n'
                    out1.write(grade_record)
                    good_count +=1
                    print('Grade Record:', grade_record)
                    if grade== 'A':
                        Acount=Acount+1
                    elif grade=='B':
                        Bcount=Bcount+1
                    elif grade== 'C':
                        Ccount=Ccount+1
                    elif grade== 'D':
                        Dcount=Dcount+1
                    else:
                        Fcount=Fcount+1
                           

        except:
            
            error_count +=1
            error_record = line+','+'Points are in error'+ '\n'
            out2.write(error_record)
            print('Points are in error', Points)
                    
        line = infile.readline()
       

    infile.close()

    out1.close()
    out2.close()
    print('number of records read:',rcdcnt)
    print('number of records written to grade file:', good_count)
    print('number of error records',error_count)
    
    print('Grade Counts:')
    print('number of A:' , Acount) 
    print('number of B:' , Bcount)
    print('number of C:', Ccount)
    print('number of D:', Dcount)
    print('number of F:', Fcount)
main()    
end_time = datetime.datetime.now()
print('Program ended at:', end_time)
print('done')

        
