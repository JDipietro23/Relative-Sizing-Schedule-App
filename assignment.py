#start
class assignment:
    """
    A class to represent an assignment.

    ...

    Attributes
    ----------
    name : str
        name of the assignment
    desctription : str
        description of the work to be done
    dueDay : int
        index of day on which the assignment is due
    size : int
        total work size of the assignement
    dailySize : int
        work size due the day the assignment is due
    children : array<subAssignment>
        list of subassignments split from this assignment

    Methods
    -------
    sync():
        Synchronizes name and total size across all subassignments, as well as updates the parent assignment's dailySize.

    split(desc, day, dailySize):
        Creates a child subassignment.
    """
    def __init__(self,name:str, desc:str, dueDay:int, size:int):
        """
        Constructs all necessary attributes of the assignment object.

        Parameters
        ----------
            name : str
                name of the assignment
            desctription : str
                description of the work to be done
            dueDay : int
                index of day on which the assignment is due
            size : int
                total work size of the assignement
        """
        self.name = name
        self.desc = desc
        self.dueDay = dueDay
        self.size = size
        self.dailySize = size
        self.children = []

    def __str__(self):
        return self.name

    def sync(self):
        """
        Synchronizes name and total size across all subassignments, as well as updates the parent assignment's dailySize.

        Returns
        -------
        None
        """
        self.dailySize = self.size
        for i in self.children:
            self.dailySize -= i.dailySize
            i.name = self.name
            i.size = self.size

    def split(self, desc:str, day:int, dailySize:int):
        """
        Creates a child subassignment.

        Parameters
        ----------
        desc : str
            description of work to be done on the subassignment
        day : int
            index of day that the subassignment work is due
        dailySize : int
            size of work of the subassignment

        Returns
        -------
        subAssignment object
        """
        return subAssignment(self.name, desc, day, self.size, self, dailySize)

class subAssignment(assignment):
    """
    A subclass of assignment that represents a subassignment.

    ...

    Attributes
    ----------
    name : str
        name of the assignment
    desctription : str
        description of the work to be done
    dueDay : int
        index of day on which the subassignment is due
    size : int
        total work size of the assignement
    dailySize : int
        work size due the day the subassignment is due
    parent : assignment
        assignment from which the subassignment was split


    Methods
    -------
    None
    """
    def __init__(self, name:str, desc:str, dueDay:int, size:int, parent:assignment, dailySize:int):
        """
        Constructs all necessary attributes of the subassignment object.

        adds self to parent assignment's children list

        Parameters
        ----------
            super(name, desc, dueDay, size)
            
            dailySize : int
                work size due the day the subassignment is due
            parent : assignment
                assignment from which the subassignment was split
        """
        super().__init__(name, desc, dueDay, size)
        self.parent = parent
        self.dailySize = dailySize
        self.parent.children.append(self)
        parent.sync()
