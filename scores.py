def scoresGrades():
    print "Scores and Grades"
    for i in range(1,11):
        from random import randint
        x = (randint(60, 100))
        if x < 69:
            print "Score:", x, "; Your grade is D"
        elif x < 79:
            print "Score:", x, "; Your grade is C"
        elif x < 89:
            print "Score:", x, "; Your grade is B"
        else:
            print "Score:", x, "; Your grade is A"
    print "End of the program. Bye!"

scoresGrades()