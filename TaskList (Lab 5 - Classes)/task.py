from datetime import datetime

class Task:
    """
    Attributes:
        description -- string description of the task
        date -- due date of the task, (String format: MM/DD/YYYY)
        time -- time the task is due, (string format: HH:MM)
    """

    def __init__(self, desc, date, time): 
        # Assign parameters to the attributes
        self.desc = desc
        self.date = date
        self.time = time

    def get_description(self): 
        # Returns the task's description string.
        return self.desc
        
    def __str__(self):
        # Returns a string used to display the task's information to the user
        # in the format: description -- Due: date at time.
        return f'{self.desc} -- Due: {self.date} at {self.time}.'
    
    def __repr__(self):
        # Returns a string used to write the task's information to the file 
        # in the fromat: task, date, time.
        return f'{self.desc}, {self.date}, {self.time}'
        
    def __lt__ (self, other):
        # Returns true if the self task is less than the other task. 
        # Compare by the year, then month, then day, that hour, then minute,
        # and then the task description in alphabetical order
        
        self_datetime = datetime.strptime(f'{self.date} {self.time}', '%m/%d/%Y %H:%M')
        other_datetime = datetime.strptime(f'{self.date} {self.time}', '%m/%d/%Y %H:%M')

        if self_datetime != other_datetime:
            return self_datetime < other_datetime
        return self.desc < other.desc
    
