import decorator

class DecorationA(decorator.Decorator):
    def operation(self):
        return super().operation() + self.additional_operation()
    
    def additional_operation(self):
        return "DecA"
