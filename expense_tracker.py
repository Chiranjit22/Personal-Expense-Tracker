import csv
import pandas as pd
import matplotlib.pyplot as plt

def exp():
    amt = int(input("Amount: "))
    cat = input("Category: ")
    date = input("Date: ")
    data = [
            {"Amount": amt, "Category": cat, "Date": date}
        ]
    with open("exp.csv", mode="a", newline="") as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(data[0])


def smry():
    f = open("exp.csv","r")
    ro = csv.reader(f, delimiter=",")
    Id = list(ro)
    print()
    print("Amount     |     Category     |     Date")
    print("____________________________________________")
    for row in Id:
    # print(row)
    # s1 = row[0]+" "*(10-len(row[0])-len(row[1])//2+4)+"|"+" "*10+row[1]+" "*(10-len(row[1])//2+2)+row[2]
        s1 = row[0]+" "*(11-len(row[0]))+"|"+" "*(9-len(row[1])//2)+row[1]+" "*(9-len(row[1])//2-len(row[1])%2)+"|"+" "*(7-len(row[2])//2)+row[2]
        print(s1)
    print()
    
    # Graphical summary
    csv_file = pd.read_csv("exp.csv", names=["Amount", "Category", "Date"])
    gp = csv_file.groupby("Category").agg({"Amount": "sum"}).reset_index()

    plt.bar(gp["Category"], gp["Amount"])
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.title("Expenses by Category")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    f.close()
    
    
def menu():
    print(":::::::::  Menu  :::::::::")
    print("1. Add Expense")
    print("2. View Summery")
    print("3. Exit")
    n = int(input("Enter your choice: "))
    match n:
        case 1:
            exp()
            menu()
        case 2:
            smry()
            menu()
        case 3:
            exit
        case _:
            print("Your have entered a wrong choice !!\n\n")
            menu()
menu()