import person

class Employee(person.Person):
    """Represents an employee.
    Attributes:
        job_desc (str): job description of employee.
        salary (int): salary of employee.
    """
    __doc__ = person.Person.__doc__ + __doc__

    def __init__(self, name, addr, b_year, job, sal):
        """Initializes the name, address, birth year, job description, and salary of the employee."""
        self.name = name
        self.address = addr
        self.birth_year = b_year
        self.job_desc = job
        self.salary = sal

    def do_job(self):
        """Returns a string representation of the employee doing their job."""
        return "I'm working, doing " + self.job_desc

    def __str__(self):
        """String representation of an employee."""
        return "My name is " + self.name + " and I am " + str(self.age(2023)) + " years old.\nI live at " + self.address + ".\nMy job is " + self.job_desc + " and I get paid " + str(self.salary) + ".\n" + self.do_job()