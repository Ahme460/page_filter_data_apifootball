from typing import Dict
import requests

class Leagues:
    def __init__(self,id,name,type,logo):
        self.__id=id
        self.name=name
        self.type=type
        self.logo=logo
    
    def to_dict(self):
        return{
            'id':self.__id,
            'name':self.name,
            'type':self.type,
            'logo':self.logo
        }
        
        
class Get_All_Leagues(Leagues):
    def __init__(self):
        self._data=[]
    def get_data_leagues(self,data):
        for i in data['response']:
            data=i['league']
            
            leagues=Leagues(
                data['id'],
                data['name'],
                data['type'],
                data['logo']
            )

            leagues=self._data.append(leagues.to_dict())
        return self._data
    
    def __str__(self):
        return self._data
    
                 
                 




