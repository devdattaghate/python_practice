# calculator for Kirana shop
import logging
logging.basicConfig(filename="kirana_calcy.log",level=10, format = '%(asctime)s %(levelname)s %(message)s')
logging.info("program initialising")
try:
    a=0
    while(True):
        i = input("Enter product value or press q for exit, entered value is " )
        logging.info(f"user entered product value is {i} Rs.")
        if i != 'q':
            try:
                a = a +  int(i)
            except ValueError as e:
                logging.info("value error occured")
                print("please enter valid input")
                print(f"your total value is Rs.{a}")
            continue
        else:
            print(f"Your final bill is Rs. {a}. "
                  f"Thank u for shopping with us, visit again")
            logging.info(f"final bill is Rs. {a}. ")
        break
except Exception as e:
    logging.exception("exception occured")
    print("error happened")