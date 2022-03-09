try:
    number = int(input("Please enter a float number: "))
    
except ValueError:
    print("The text you entered is not a float number")
except NameError:
    print("The text you entered is not a float number")


def check_if_prime(number):
    if number <= 0 :
        return "Number cannot be less or equal 0"
    elif number ==1 or number == 2:
        return True
    else:
        for i in range(3,number):
            if number % i == 0:
                return False
        return True 
    
prime_num_list = [] 
i = 1  

def add_to_list(num):
    global i
    if i == number+1:
        return prime_num_list
    else :
        if check_if_prime(i):
            prime_num_list.append(float(i))
          
    i += 1
    add_to_list(num)
            

add_to_list(number)

print(prime_num_list)

