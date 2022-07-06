class Animal:
    """Animal Class"""
    def __init__(self,atype):
        print('Initializing animal type')
        self.__atype = atype
    
    @property
    def location(self):
        print('Getting location')
        return self.__location
    
    @property
    def atype(self):
        print('Getting Name')
        return self.__atype
    
    @atype.setter
    def atype(self, new_atype):
        print('Setting Name')
        self.__name = new_atype
        
    @location.setter
    def location(self, new_location):
        print('Setting Location')
        self.__location = new_location
        
    @atype.deleter
    def atype(self):
        print('Deleting animal type')
        del self.__atype
    
    def move(self):
        print('Movin')
    
    def eat(self):
        print('Munchin')
class Fish(Animal):
    """Fish class, inherits from animal"""
    @property
    def ftype(self):
        return self.__ftype
    
    @ftype.setter
    def ftype(self, new_ftype):
        self.__ftype = new_ftype
    
    @property
    def water(self):
        return self.__water
    
    @water.setter
    def water(self, new_water):
        self.__water = new_water
        
    def swim(self):
        print('Just swimming')
        
class Snake(Animal):
    """Snake class, inherits from animal"""
    
    @property
    def stype(self):
        return self.__stype
    
    @stype.setter
    def stype(self, new_stype):
        self.__stype = new_stype
    
    @property
    def venemous(self):
        return self.__venemous
    
    @venemous.setter
    def venemous(self, new_venemous):
        self.__venemous = new_venemous
        
    def slither(self):
        print('Slithering Snake')

class Person(Animal):
    """Person class, inherits from animal"""
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name
