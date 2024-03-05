# Bu class uyelerin BMI degerelerini hesapliyor
class BMI():
    def __init__(self, height,weight) -> None:
        """_summary_

        Args:
            height (float): üye boyu
            weight (float): üyenin kilosu
        """
        self.height=height
        self.weight=weight
      

    def bmi_value(self):
        """
        value= body_weight/height*height 
        
        """
        value= self.weight / (self.height/100)**2
        
        return value
 
    