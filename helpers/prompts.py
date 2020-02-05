import inquirer

def get_sql_flavor():
    questions = []
    message = 'What type of sql database will you be using?'
    choices = ['sqlite', 'mysql']
    questions.append(inquirer.List('flavor', message, choices))
    answers = inquirer.prompt(questions)
    return answers['flavor']
