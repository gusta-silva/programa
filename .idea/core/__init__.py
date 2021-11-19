from _typeshed import Self
import datetime

#adicionar ao arquivo principal

class SystemInfo:
    def __init__(Self):
        pass
    
    @staticmethod
    def get_time():
        
        now = datetime.datetime.now(Self)
        answer = 'São {} horas e {} minutos.' .format (now.hour, now.minute)
        return answer