class myMath():
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    
    def summ(self):
        return self.a+self.b
    
    def division(self):
        return self.a/self.b
    
    def __str__(self) -> str:
        return f'{self.a},{self.b}'