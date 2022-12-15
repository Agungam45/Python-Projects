credit_hours = float(input("How many credit hours are you taking? "))
BOOKS = "52.99"
LAB_FEES = "25.00"
total_tuition = 157.93 * credit_hours
overall_total = str(float(BOOKS) + float(LAB_FEES) + float(total_tuition))
print("*" * 50)
print("\tColumbus State Community College" + "\n\t550 East Spring St"+ "\n\tColumbus, OH, 43215")
print("-" * 50)
print("\tProduct Name:" + (" " * 3) + "Product Price:")
print("\tBooks" + "\t\t" + "$" + BOOKS)
print("\tLab Fees" + "\t" + "$" + LAB_FEES)
print(("\tTuition" + "\t\t") + "$" + str(total_tuition))
print("-" * 50)
print("\t\t\t" + "Total")
print("\t\t\t" + "$" + overall_total)
print("-" * 50)
print("   Thank you for being a Columbus State Student\n" + ("*" * 50))
      
