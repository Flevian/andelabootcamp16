class Car(object):

    def __ini__(self, name, model, car_doors, car_wheels, speed = 0):        
        if not name:
            self.name = "General"
            
        else:
            self.name = name
            
        if not model:
            self.model = "Gm"
            
        else:
            self.model = model
        
        if self.name == "Porshe" or self.name == "Koenigsegg":
            self.car_doors = 2
            
        else:
            self.car_doors = 4
        
        if self.model == "Trailer":
            self.car_wheels = 8
            
        else:
            self.car_wheels = 4

        self.speed = speed    
            
    def is_saloon(self):        
        if self.model == "saloon":
            return True
            
        else:
            return False
    
    def drive(self, moving_speed):        
        if self.model == "trailer":
            self.speed = moving_speed * 11
        else:
            self.speed = 10 ** moving_speed

        return self.speed        
