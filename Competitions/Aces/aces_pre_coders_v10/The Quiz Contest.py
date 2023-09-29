import math

def solution(questions):
    totalQue = questions[0]+ 2* min(questions[1],questions[2])
    # print(totalQue)
    totalMarks = questions[0]
    questionsLeft = questions[1]+questions[2]+questions[3] -2*min(questions[1],questions[2])
    # print(questionsLeft)
    
    totalQue+=min(totalMarks+1,questionsLeft)
    if totalQue == 0:
        totalQue = 1
    return totalQue

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        questions = [int(i) for i in input().strip().split()]
        print(solution(questions))