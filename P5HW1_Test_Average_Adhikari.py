# CTI 110
# P5HW1: Test Average and Grades
# This program will ask user to input 5 test scores and display a letter grade for each score and average test score.
# 04/12/18
# Shobhakhar Adhikari

def main():
    score1 = float(input("Enter your test 1 score:"))
    score2 = float(input("Enter your test 2 score:"))
    score3 = float(input("Enter your test 3 score:"))
    score4 = float(input("Enter your test 4 score:"))
    score5 = float(input("Enter your test 5 score:"))
    def calc_average(a,b,c,d,e):
        average = (a+b+c+d+e)/5
        print("The average test score is:",format(average, '.2f'))
    calc_average(score1,score2,score3,score4,score5)

    def determine_grade(a,b,c,d,e):
        count = 1
        for x in [a,b,c,d,e]:
    
            if x >= 90:
                print("The letter grade for test",count," score is A.")
            elif x >= 80:
                print("The letter grade for test",count," score is B.")
            elif x >= 70:
                print("The letter grade for test",count," score is C.")
            elif x >= 60:
                print("The letter grade for test",count," score is D.")
            else:
                print("The letter grade for test",count," score is F.")
            count = count + 1
                                
    determine_grade(score1, score2, score3,score4,score5)
main()
        
input()            
            
