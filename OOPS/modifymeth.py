class demo:
   
    ins="hello"
    @classmethod
    def greet(cls):
        return "hi"
    
    @classmethod
    def modify(cls,new_value):
        cls.ins=new_value

print(demo.greet())
print(demo.ins)
print(demo.modify("linkcode"))
print(demo.ins)
      
