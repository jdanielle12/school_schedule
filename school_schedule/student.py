class Student:
    def __init__(self, name, grade, classes):
        self.name = name
        self.grade = grade
        self.classes = classes
        
    def add_class(self, class_name):
        self.classes.append(class_name)
        return self.classes
    
    def remove_class(self, class_name):
        self.classes.remove(class_name)
        return self.classes
    
    def get_num_classes(self):
        return len(self.classes)
    
    def display_classes(self):
        return(", ".join(self.classes))
    
    def summary(self):
        return (f"{self.name} is a {self.grade} enrolled in " \
            f"{self.get_num_classes()} classes: {self.display_classes()}.")
        
    
    