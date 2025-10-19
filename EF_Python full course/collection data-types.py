# Ứng dụng float vs int trong nhập liệu
num_a = float(input("Nhập số thứ nhất: "))  # Bắt buộc dùng float nếu nhập số thực
num_b = float(input("Nhập số thứ hai: "))
print("Total:", num_a + num_b)  # Trả về float

# Sai lầm phổ biến (không chuyển kiểu)
text_num = "5.5"
# total = int(text_num)
# print(total_a,total)  # ❌ Lỗi: ValueError 
total_a = int(float(text_num))  # ✅ Đúng: 5
total_b = int(round(float(text_num)))
print(total_a,total_b)  # ✅ Đúng: 5

# Ứng dụng collection types
coordinates = (1.2, 3.4)  # Tuple (immutable - tọa độ không đổi)
student_scores = [4.5, 3.0, 5.0]  # List (mutable - có thể thêm/bớt điểm)
unique_ids = {101, 102, 101}  # Set → {101, 102} (tự loại trùng)
student_info = {"id": 102, "gpa": 3.8}  # Dictionary (ánh xạ thông tin)

data = {
  "integer": "Whole numbers",
  "float": "Decimal numbers",
  "list": "Ordered collection"
}
print(data.items())