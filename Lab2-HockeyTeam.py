"""
Student Name: Katherine Tucker   
Program Title: IT Programming 
Description: Lab2-HockeyTeam   
"""

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    teamName = input("What is your favourite hockey team? ")

    win = input("How many wins does this team have? ")

    loss = input("How many losses does this team have? ")
    #Make sure to convert input strings into integers

    finalTotal = (int(win) / (int(win) + int(loss)))
    #Converted ^

    print("The {0} have {1} wins and {2} losses, with a win percentage of {3:.4}".format(teamName,win,loss,finalTotal))

    # YOUR CODE ENDS HERE

main()