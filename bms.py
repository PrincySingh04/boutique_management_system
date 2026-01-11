import mysql.connector
conn=mysql.connector.connect(
    user='root',
    host='localhost',
    password='',
    database='BankManagementSystem'
)
cursor=conn.cursor()
#cursor.execute("create database BankManagementSystem")
# varr="create table accout(user_id int auto_increment ,user_name varchar(255),init_amount decimal(10,5),primary key(user_id))"
# val="insert into accout(user_name,init_amount)values(%s,%s)"
# user_name=input("enter your name : ")
# init_amout=float(input("enter the amout you want to deposit : "))
# result=(user_name,init_amout)
"""code to deposite money in already existing bank accout"""


# acc_id = input("\nEnter Account ID to deposit money: ")
# deposit_amount = float(input("Enter deposit amount: "))
# cursor.execute(f"select init_amount from accout WHERE user_id={acc_id}")
# a = cursor.fetchall()
# print(a)
# if a is None:
#     print('accout doesnot exist')
# else :    
#    cursor.execute("update accout SET init_amount=init_amount+%s WHERE user_id=%s",(deposit_amount, acc_id))
#    cursor.execute(
#         "SELECT user_name, init_amount FROM accout WHERE user_id = %s",
#         (acc_id,)
#     )   
# result=cursor.fetchall()
# for b in result:
#     print(b)

"""code to withdraw money"""

accc_id=input("\n enter the account id to withdraw money")
withdraw_money=float(input("enter the amount you want to withdraw"))
cursor.execute(f"select init_amount from accout where user_id={accc_id}")
c=cursor.fetchall()
print(c)
if c is None:
    print("account doesnot exist")
else:
    cursor.execute("update accout SET init_amount=init_amount-%s WHERE user_id=%s",(withdraw_money,accc_id))    
    cursor.execute(
        "SELECT user_name, init_amount FROM accout WHERE user_id = %s",
        (accc_id,)
    )   
result=cursor.fetchall()
for b in result:
    print(b)


   

#cursor.execute(val,result)
conn.commit()