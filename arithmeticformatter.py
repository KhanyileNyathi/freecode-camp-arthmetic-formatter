import operator

#sort the operator issue
operators = ('+','-')
line_1 = input().split()
line_2 = input().split()
line_3 = input().split()
line_4 = input().split()
#sort the operator error
if operator is not operators:
  print('Error: operator must be "+" or "-".')

#assign problems
problems_1 = [line_1, line_2, line_3, line_4]
problems_2 = [line_1, line_2, line_3, line_4]
#sort the error
if problems_1.isdigit()== "False" or problems_2.isdigit() is False:
  print('Error: Numbers must only contain digits.')

def arithmetic_arranger(problems, display_results=False):
  #arrange the problems
  arranged_problems = []
  for problem in problems:
    arranged_problems.append(problem)
  #arrange the space issue
    width = max(len(problem[0]) for problem in problems) + 2
    arranged_problems= [f"{problem[0].rjust(width)}{problem[1]}     {problem[2]}"
                        for problems in arranged_problems]
    
    #sort the error
    if len(arranged_problems) > 5:
      return 'Error: Too many problems.'
    if len(arranged_problems[0]) > 5: 
      return 'Error: Numbers cannot be more than four digits.'
    if len(arranged_problems[1]) > 5:
      return 'Error: Numbers cannot be more than four digits.'

#get the total of the sum
if answer:
  total = sum(int(problem.split()[2]) for problem in problems)
  
if operator == "+":
  answer = problems_1 + problems_2
  return arranged_problems
if operator == "-":
  answer = problems_1 - problems_2
return arranged_problems

answer.append(str(total).rjust(width))
arranged_problems=[problem + answer for problem, answer in zip(arranged_problems, answer)]

#for answer
return '\n'.join(arranged_problems)'
