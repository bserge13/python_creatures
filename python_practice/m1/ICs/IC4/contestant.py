class Contestant:
    def __init__(self, dict_info):
        self.full_name = dict_info['first_name'] +" "+ dict_info['last_name']
        self.age = dict_info['age']
        self.state_of_residence = dict_info['state_of_residence']
        self.spending_money = dict_info['spending_money']
        self.game_interests = []
    
    def is_out_of_state(self):
        return not self.state_of_residence == 'CO'
    
    def add_game_interest(self, game_name):
        self.game_interests.append(game_name)