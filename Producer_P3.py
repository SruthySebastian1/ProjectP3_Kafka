from kafka import KafkaProducer
from datetime import datetime
import time
from json import dumps
import random


KAFKA_TOPIC_NAME_CONS = "test-topic"
KAFKA_BOOTSTRAP_SERVERS_CONS = 'localhost:9092'

if __name__ == "__main__":
    print("Kafka Producer Application Started ... ")
    
    kafka_producer_obj = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS_CONS,
                                       value_serializer=lambda x: dumps(x).encode('utf-8'))

    
    cust_id_name =[[101,"John smith"],[102,"Mary Jane"],[103,"Joe Jane"],[104,"Neo"],[105,"Trinity"],[106,"Abdul Kalam"],
                   [107,"Narendra Modi"],[108,"Mary smith"],[109,"Gajendra"],[110,"Om Prakash "],[111,"Samanta"],[112,"Sruthy"]]

    
    product_details = [[201,"Pen","Stationary",5],[208,"mobile","Electronics Devices",6999],[251,"T-shirt","Men's Fashion",699],[221,"HDMI Cable","Electronics",1490],
                       [222,"Drawing Book","Stationary",98],[223,"Cotton Material","Women's Fashion",489],[224,"TV Stand","Stationary",2999],
                       [225,"Weighing Machine","Health Care",999],[226,"Blinder","Shoes and Handbags",699],[212,"Wrist Band","Electronics ",5099],
                       [258,"Skirt","Women's Fashion",899],[236,"pen Drive","Electronics",1499],[255,"fruits","groceries ",79],
                       [259,"Eternity Women","Women's Perfume",2899],[260,"8GB-RAM","Electronics",5499]]
        
    payment_type = ["card", "Internet Banking", "UPI", "Wallet"]
    
    qty = [1,2,3,4]

    country_name_city_name_list = ["Sydney,Australia", "Florida,United States", "New York City,United States",
                                   "Paris,France", "Colombo,Sri Lanka", "Dhaka,Bangladesh", "Islamabad,Pakistan",
                                   "Beijing,China", "Rome,Italy", "Berlin,Germany", "Ottawa,Canada",
                                   "London,United Kingdom", "Jerusalem,Israel", "Bangkok,Thailand",
                                   "Chennai,India", "Bangalore,India", "Mumbai,India", "Pune,India",
                                   "New Delhi,India", "Hyderabad,India", "Kolkata,India", "Singapore,Singapore"]

    ecommerce_website_name_list = ["www.datamaking.com", "www.amazon.com", "www.flipkart.com", "www.snapdeal.com", "www.ebay.com"]
    
    
    payment_txn_success = ["Success","Failed"]
    
    failure_reason=["Insufficient Funds","Limit Exceeded","Expired Card","Invalid Credit Card Number","Invalid Expiration Date"," Invalid CVV"]
    
    message_list = []
    message = None
    for i in range(50):
        i = i + 1
        message = {}
        print("Preparing message: " + str(i))
        event_datetime = datetime.now()
        message["order_id"] = i
        customer_details = random.choice(cust_id_name)
        message["cust_id"] = customer_details[0]
        message["cust_name"] = customer_details[1]
        prod_datails = random.choice(product_details)
        message["product_id"] = prod_datails[0]
        message["product_name"] = prod_datails[1]
        message["product_category"] = prod_datails[2]
        message["price"] = prod_datails[3]
        message["Payment_type"] = random.choice(payment_type)
        message["Quantity"] = random.choice(qty)
        message["order_datetime"] = event_datetime.strftime("%Y-%m-%d %H:%M:%S")
        country_name_city_name = random.choice(country_name_city_name_list)
        country_name = country_name_city_name.split(",")[1]
        city_name = country_name_city_name.split(",")[0]
        message["order_country_name"] = country_name
        message["order_city_name"] = city_name
        message["order_ecommerce_website_name"] = random.choice(ecommerce_website_name_list)
        message["Paymend_txn_id"] = random.getrandbits(32)
        TXN_STAT = random.choice(payment_txn_success)
        message["Txn_Status"] = TXN_STAT
        if  TXN_STAT =="Failed":
             message["Failure_reason"] = random.choice(failure_reason)
        
        print("Message: ", message)
        #message_list.append(message)
        kafka_producer_obj.send(KAFKA_TOPIC_NAME_CONS, message)
        time.sleep(2)

    print("Kafka Producer Application Completed. ")