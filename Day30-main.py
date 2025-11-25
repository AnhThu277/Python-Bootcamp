# try: # Điều gì đó có thể gây ra ngoại lệ (try có thể thành công hoặc thất bại)
#     file = open("thu_file.txt") #mở file
#     mno_dictionary = {"abc":"1"} #truyền vào key giá trị = 1
#     print(mno_dictionary["abc"])
# except FileNotFoundError: #muốn dùng multiple except thì phải có điều kiện cho all except, thực hiện thì có exception xảy ra
#     file = open("thu_file.txt","w") #nếu chưa có file thì "w" -> tạo file trong thư mục
#     file.write("Hello")
# except KeyError as keyerror: #nhớ đặt tên cho KeyError ở đây nha
#     print(f"The key {keyerror} does not exist") #dùng f-string để ghi ra tên key lỗi cụ thể là gì
# else: #thực hiện thì không có exception xảy ra
#     doc=file.read() #đọc file 
#     print(doc)
# finally: #vẫn thực hiện mặc kệ tất cả mọi thứ
#     file.close() #đóng file
#     print("File is closed")
height = float (input("height (m): "))
weight = float (input("weight (kg): "))
health_condition = input("Your health condition: ")
if health_condition in {"sick","pregnant"}:
    raise ValueError ("Your health condition is not enough to do BMI!") 
if height > 2.6:
    raise ValueError ("Your height is over the max height!")
 
BMI = weight / (height**2)
print(BMI)