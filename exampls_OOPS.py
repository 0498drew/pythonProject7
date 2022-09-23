class Voters:

    def __init__(self, name, age=None):
        self.name = name
        self.age = age
    def get_voters(self):
        if self.name:
            print('am going to vote')
        else:
            print("am not going to vote")
        if self.age <= 17:
            print("yo can no vote")
        else:
            print("you will  vote")

