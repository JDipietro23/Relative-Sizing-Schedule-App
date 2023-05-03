import assignment

class week():
    def __init__(self) -> None:  
        self.dayList = [
            [],
            [],
            [],
            [],
            [],
            [],
            []
        ]

        self.weekNames = ['SUN','MON','TUES','WED','THURS','FRI','SAT']
    
    def addAssignment(self, dayIndex, assignment)->None:
        self.dayList[dayIndex].append(assignment)

    def removeAssignment(self,dayIndex,assignmentIndex):
        target = self.dayList[dayIndex][assignmentIndex]
        if type(target)==assignment.subAssignment:
            self.dayList[dayIndex][assignmentIndex].removeSelf()
            del self.dayList[dayIndex][assignmentIndex]
        else:
            for sub in self.dayList[dayIndex][assignmentIndex].children:
                for day in self.dayList:
                    if sub in day:
                        day.remove(sub)
            del self.dayList[dayIndex][assignmentIndex]


    def viewWeek (self):
        for i in range(7):
            total = 0
            for j in self.dayList[i]:
                total+=j.dailySize

            print(f"{self.weekNames[i]} [{total}]")

            for j in self.dayList[i]:
                if (j.size != j.dailySize):
                    sizeStr = f"[{j.dailySize} of {j.size}]"
                else:
                    sizeStr = f"[{j.dailySize}]"

                subAs = ""
                if (type(j)==assignment.subAssignment): 
                    subAs = "SUB:"
                print(f"    - {subAs} {j.name} {sizeStr}")
                if (j.desc != ""):
                    print(f"        :{j.desc}\n")
