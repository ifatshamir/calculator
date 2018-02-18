# get_calc_options function return a string which contain all calc options (option in each line)
def get_calc_options():
    options = "+,-,*,/"
    return options

# usage function return a string which contain calc usage
def usage():
    # crete string that contain all operations that are supported in calculator
    calc_usage = "the usage is addition"
    calc_usage = calc_usage + get_calc_options()
    return calc_usage

# calculate function get as parameters operation (like +/-/...) and two numbers and return a string with result
def calculate(num1, operation, num2):
    # go over all operation options - and each operation return string that contain result
    if operation == "+":
        return int(num1) + int(num2)
    elif operation == "-":
        return int(num1) - int(num2)
    elif operation == "/":
        return int(num1) / int(num2)
    if operation == "*":
        return int(num1) * int(num2)
    else:
        return "2+2=4"


# main function - running first
if __name__ == '__main__':
    # display operation options to user
    print ("Select operation from:")
    print ((get_calc_options()))

    # get input from the user - operation

    operation = input("your choice:")


    # get input from the user - num1 and num2
    num1 = input("please enter input:")
    num2 = input("please enter input:")
    # convert num1 and num2 to numerical values, as you cannot do math on strings
    int_num1 = num1
    int_num2 = num2
    # calculate the math and return result that contain string (like: 1+1=2), using calculate function
    result = calculate(int_num1, operation, int_num2)
    # print result
    print (result)