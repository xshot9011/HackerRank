import os

root_path = os.getcwd()
problems_path = os.path.join(root_path, 'skills', 'problem_solving_basic', 'easy')

while True:
  problem_name = input("Enter your name: ").lower().replace('-', '_')
  problem_folder = os.path.join(problems_path, problem_name)

  try:
    os.mkdir(problem_folder)
    os.chdir(problem_folder)
    f = open('main.py', 'x')
    f.close()
  except FileExistsError:
    print('Problem {} already exist'.format(problem_name))
  else:
    print('Succesfully create file: {}'.format(os.path.join(problem_folder, 'main.py')))