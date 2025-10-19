Phần **giảng bài chi tiết về Collection Data Types trong Python (Lists, Tuples, Sets, Dictionaries)** — tức là bài học giải thích cách tạo, truy xuất, thao tác, và so sánh bốn loại cấu trúc dữ liệu cơ bản nhất trong Python.
Dưới đây là bản **tóm tắt có hệ thống và dễ hiểu** (bạn có thể dùng để ghi chú hoặc làm flashcard ôn tập):

---

## 🧩 Tổng quan Collection Data Types trong Python

| Kiểu dữ liệu   | Đặc điểm chính                                       | Mutable            | Ordered                       | Unique              | Ví dụ cú pháp                  |
| -------------- | ---------------------------------------------------- | ------------------ | ----------------------------- | ------------------- | ------------------------------ |
| **List**       | Danh sách có thể thay đổi, chứa mọi loại dữ liệu     | ✅ Có thể thay đổi | ✅ Có thứ tự                  | ❌ Có thể trùng lặp | `my_list = ["wall", "floor"]`  |
| **Tuple**      | Giống list nhưng **không thể thay đổi**              | ❌ Không thể       | ✅ Có thứ tự                  | ❌ Có thể trùng     | `my_tuple = ("wall", "floor")` |
| **Set**        | Tập hợp **các phần tử duy nhất**, không có thứ tự    | ✅ Có thể thay đổi | ❌ Không có thứ tự            | ✅ Duy nhất         | `my_set = {10, 20, 30}`        |
| **Dictionary** | Tập hợp **key-value pairs**, cho phép ánh xạ dữ liệu | ✅ Có thể thay đổi | ✅ Có thứ tự (từ Python ≥3.7) | 🔑 Key là duy nhất  | `my_dict = {"key1": "value1"}` |

---

## 📘 LIST – Quan trọng nhất

### 1. Tạo list

```python
my_list = ["wall", "floor", "roof", "ceiling"]
```

hoặc

```python
my_list = list()
```

### 2. Truy xuất phần tử

-   Chỉ số bắt đầu từ `0`

```python
my_list[2]      # "roof"
my_list[-1]     # "ceiling"
```

### 3. Cắt (slice)

```python
my_list[0:2]    # ["wall", "floor"]
my_list[2:]     # ["roof", "ceiling"]
my_list[::-1]   # Đảo ngược danh sách
```

### 4. Hàm thường dùng

```python
len(my_list)
sorted(my_list)
sum(num_list)
min(num_list)
max(num_list)
```

### 5. Phương thức (methods)

| Phương thức     | Chức năng                                       |
| --------------- | ----------------------------------------------- |
| `append(x)`     | Thêm 1 phần tử                                  |
| `extend(list2)` | Nối thêm 1 list khác                            |
| `insert(i, x)`  | Chèn phần tử tại vị trí i                       |
| `remove(x)`     | Xóa phần tử đầu tiên có giá trị x               |
| `pop(i)`        | Lấy và xóa phần tử tại vị trí i (mặc định cuối) |
| `clear()`       | Xóa toàn bộ list                                |
| `count(x)`      | Đếm số lần xuất hiện                            |
| `index(x)`      | Trả về vị trí đầu tiên của x                    |
| `sort()`        | Sắp xếp tại chỗ                                 |
| `reverse()`     | Đảo ngược list                                  |
| `copy()`        | Tạo bản sao độc lập (không trỏ tới list gốc)    |

### ⚠️ Lưu ý quan trọng:

-   `x = my_list` → là **reference**, thay đổi `my_list` sẽ làm `x` thay đổi.
-   `x = my_list.copy()` → là **independent copy**.

---

## 🔒 TUPLE – Giống list nhưng không thay đổi được

```python
my_tuple = ("wall", "floor", "roof")
```

-   Truy xuất & cắt như list.
-   Không có `.append()` hay `.remove()`.
-   Có thể dùng: `count()`, `index()`, `len()`, `min()`, `max()`, `sum()`.
-   Nhanh hơn list và an toàn hơn khi cần dữ liệu cố định.

---

## 🔷 SET – Duy nhất, không thứ tự

```python
my_set = {10, 20, 30, 30, 10}
# -> {10, 20, 30}
```

### Chuyển đổi:

```python
set(my_list)     # loại bỏ trùng lặp
list(my_set)     # chuyển lại thành list
```

### Toán tập hợp:

| Toán tử | Ý nghĩa                        | Ví dụ                         |          |                    |
| ------- | ------------------------------ | ----------------------------- | -------- | ------------------ |
| `A      | B`                             | Hợp (union)                   | `{1,2,3} | {3,4}`→`{1,2,3,4}` |
| `A & B` | Giao (intersection)            | `{1,2,3} & {2,3}` → `{2,3}`   |          |                    |
| `A - B` | Hiệu (difference)              | `{1,2,3} - {2,3}` → `{1}`     |          |                    |
| `A ^ B` | Hiệu đối xứng (symmetric diff) | `{1,2,3} ^ {3,4}` → `{1,2,4}` |          |                    |

---

## 🧭 DICTIONARY – Key–Value Mapping

```python
data = {
  "integer": "Whole numbers",
  "float": "Decimal numbers",
  "list": "Ordered collection"
}
```

### Truy xuất:

```python
data["integer"]
data.get("float")
data.get("missing", "default_value")  # tránh lỗi KeyError
```

### Thêm/Sửa/Xóa:

```python
data["new_key"] = "new_value"
data.pop("float")
data.clear()
```

### Hàm & phương thức:

| Hàm                       | Chức năng                    |
| ------------------------- | ---------------------------- |
| `len(data)`               | Số lượng cặp key-value       |
| `data.keys()`             | Danh sách key                |
| `data.values()`           | Danh sách value              |
| `data.items()`            | Danh sách tuple (key, value) |
| `data.update(other_dict)` | Gộp dictionary khác          |
| `data.copy()`             | Sao chép độc lập             |

---

## 🔁 LOOP minh họa

```python
for item in my_list:
    print(item)  # lặp qua từng phần tử list

for key, value in data.items():
    print(key, "→", value)  # lặp qua dictionary
```

---

## 🧠 Tổng kết sử dụng:

| Khi nào dùng                    | Kiểu nên chọn  |
| ------------------------------- | -------------- |
| Dữ liệu thay đổi thường xuyên   | **List**       |
| Dữ liệu cố định, không thay đổi | **Tuple**      |
| Dữ liệu cần loại bỏ trùng lặp   | **Set**        |
| Dữ liệu có cặp key-value        | **Dictionary** |

---

Bạn muốn tôi **chuyển đoạn này thành file PDF ghi chú học Python (đẹp, có emoji và bảng)** không?
Tôi có thể tạo để bạn dùng làm tài liệu học hoặc in ra.
