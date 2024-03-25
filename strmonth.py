def find_str_month(num):    
    match(num):
        case "01":
            return ("Jan")
        case "02":
            return("Feb")
        case "03":
            return("Mar")
        case "04":
            return("Apr")
        case "05":
            return("May")
        case "06":
            return("June")
        case "07":
            return("Jul")
        case "08":
            return("Aug")
        case "09":
            return("Sept")
        case "10":
            return("Oct")
        case "11":
            return("Nov")
        case "12":
            return("Dec")
        case _:
            return("Invalid input")
def main():
    num=input("Enter month: ")
    print(find_str_month(num))

if __name__=="__main__":
    main()