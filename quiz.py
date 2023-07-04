print('Welcome')
answer=input('Are you ready? (yes/no): ')
score=0
total_questions=3

if answer.lower()=='yes':
    answer=input('Q.1 What is the color of a coin?')
    if answer.lower()=='silver':
        score+=1
        print('correct')
    else:
        print('wrong answer')

    answer=input('Q.2 What is the color of a crocodile?') 
    if answer.lower()=='green':
        score+=1
        print('correct')
    else:
        print('wrong answer')

    answer=input('Q.2 What is the color of sun?') 
    if answer.lower()=='yellow':
        score+=1
        print('correct')
    else:
        print('wrong answer')  

    print('Thank you taking this quiz')
    mark=(score/total_questions*100) 
    print('Marks obtained:',mark)
    print('BYE')     

