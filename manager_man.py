class manager():
    def __init__(self, description, choice_one, choice_two, choice_three=''):
        self.description = description
        self.choice_one = choice_one
        self.choice_two = choice_two
        self.choice_three = choice_three

    def build(self):
        print(self.description)
        choices = [self.choice_one, self.choice_two, self.choice_three]
        
        counter = 1
        for choice in choices:
            if self.choice_three != '':
                print(str(counter) + '. ' + str(choice) + '\n')
                counter += 1

            else:
                print(str(counter) + '. ' + str(choice) + '\n')
                counter += 1
                if counter == 3:
                    break