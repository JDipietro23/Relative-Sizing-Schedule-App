from assignment import assignment
from week import week
import argparse
import dataManagement

def main():
    loadedData = dataManagement.loadData()
    if (loadedData==None):
        thisWeek = week()
    else:
        thisWeek = loadedData

    parser = argparse.ArgumentParser()
    subParser = parser.add_subparsers(dest='command')

    add = subParser.add_parser('add')
    add.add_argument('-n','--name',nargs='+',type=str, default=None, required=True, help="Name of assignment")
    add.add_argument('-d','--desc',type=str, nargs='+', default=None, required=False, help="Description of assignment")
    add.add_argument('--day',type=int, nargs=1, default=None, required=True, help="Index of day the assignment is due")
    add.add_argument('-s','--size',type=int, nargs=1, choices=[0,.5, 1, 1.5, 2, 3, 5, 8, 13], default=None, required=True, help="Work size of the assignment represented by a fibbonacci value")

    div = subParser.add_parser("div")
    div.add_argument('-a','--assignment',type=int, nargs=2, default=None, required=True, help="Index of the parent assignment. Give the day index then list index.")
    div.add_argument('--day',type=int, nargs=1, default=None, required=True, help="Index of day the subAssignment is due")
    div.add_argument('-d','--desc',type=str, nargs='+', default=None, required=False, help="Description of subAssignment")
    div.add_argument('-s','--size',type=int, nargs=1, choices=[0,.5, 1, 1.5, 2, 3, 5, 8, 13], default=None, required=True, help="Work size of the subAssignment")

    remove = subParser.add_parser("remove")
    remove.add_argument('-a','--assignment',type=int, nargs=2, default=None, required=True, help="Remove an assignment. Give the day index then list index.")

    pref = subParser.add_parser("pref")
    pref.add_argument('-t','--threshold',type=int, nargs=1, choices=[0,.5, 1, 1.5, 2, 3, 5, 8, 13], required=False,help="days with a larger total size than your threshold will be displayed with  '!!!' to remind you to split up your work" )
    clear = subParser.add_parser('clear')

    view = subParser.add_parser('view')

    args = parser.parse_args()

    if args.command == 'add':
        aName = " ".join(args.name)
        aDesc = ""
        if(args.desc!=None):
            aDesc = " ".join(args.desc)
        thisWeek.addAssignment(args.day[0],assignment(aName,aDesc,args.day[0],args.size[0]))

    if args.command == 'clear':
        thisWeek=week()
    
    if args.command == 'view':
        thisWeek.viewWeek()
        return

    if args.command == 'div':
        aDesc = ""
        if(args.desc!=None):
            aDesc = " ".join(args.desc)
        parent = thisWeek.dayList[args.assignment[0]][args.assignment[1]]
        subAssignment = parent.split(aDesc, args.day[0], args.size[0])
        thisWeek.addAssignment(args.day[0],subAssignment)
        parent.sync()

    if args.command == 'remove':
        thisWeek.removeAssignment(args.assignment[0],args.assignment[1])

    if args.command == 'pref':
        thisWeek.threshold = args.threshold[0]
        print(thisWeek.threshold)
        

    thisWeek.viewWeek()
    dataManagement.saveData(thisWeek)
    print("\n Commands: \n  {add,div,remove,pref,clear,view}\n")
if __name__ == "__main__":
    # calling the main function
    main()