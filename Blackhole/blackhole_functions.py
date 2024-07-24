from typing import List
from random import choice

from ai_functions import A21_Functions


class BlackFunction:

    def __init__(
        self,
        messages: List[str]
    ) -> None:
        self.messages = messages
    
    @classmethod
    def get_type_functions(cls, summary_type:str):
        func_name = A21_Functions.function_maps[summary_type]
        return getattr(A21_Functions, func_name)
    
    def get_summary(self, type:str = "simple"):
        func = self.get_type_functions(type)
        return func(self.messages)
    
    def get_random_summary(self):
        sum_type = choice(list(A21_Functions.function_maps.keys()))
        return self.get_type_functions(sum_type)(self.messages)
    
    

if __name__=="__main__":
    pass
    # temp = BlackFunction(["Well this was just a small example of what I'm trying to do. When I'm scanning through attributes of my objects it retuns strings. So then I want to combine all the strings to create a path to the right object. So for example if I want path 'obj1.obj2.obj3.obj4', I'll get all those obj values in strings. So I'm trying to figure out a way to combine the strings and make them call a function"])
    # print(temp.get_summary("key"))
    # print(temp.get_random_summary())