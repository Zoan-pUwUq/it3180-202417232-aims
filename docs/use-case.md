# Tài liệu Đặc tả Use Case – Hệ thống AIMS-mini

## 1. Giới thiệu tổng quan
Hệ thống **AIMS-mini** (An Internet Media Store) là ứng dụng dòng lệnh phục vụ việc quản lý và đặt mua các sản phẩm đĩa kỹ thuật số (Digital Video Disc - DVD).

---

## 2. Các tác nhân (Actors)
- **Khách hàng (Customer):** Người dùng tương tác với hệ thống để xem, tìm kiếm và quản lý các đĩa trong giỏ hàng.
- **Hệ thống giỏ hàng (Cart System):** Thực hiện tính toán chi phí, kiểm soát giới hạn dung lượng lưu trữ đơn hàng.

---

## 3. Biểu đồ Use Case (Use Case Diagram)

```text
                  +------------------------------------------+
                  |                AIMS-mini                 |
                  |                                          |
                  |   +----------------------------------+   |
                  |   | UC01: Thêm DVD vào giỏ hàng      |   |
                  |   +----------------------------------+   |
                  |                    ^                     |
                  |                    | <<include>>         |
                  |   +----------------------------------+   |
                  |   | UC02: Kiểm tra giới hạn 20 đĩa   |   |
                  |   +----------------------------------+   |
                  |                                          |
   [Khách hàng] ----> |   +----------------------------------+   |
     (Customer)   |   | UC03: Xóa DVD khỏi giỏ hàng      |   |
                  |   +----------------------------------+   |
                  |                                          |
                  |   +----------------------------------+   |
                  |   | UC04: Xem chi tiết giỏ hàng      |   |
                  |   +----------------------------------+   |
                  |                    |                     |
                  |                    | <<include>>         |
                  |                    v                     |
                  |   +----------------------------------+   |
                  |   | UC05: Tính tổng chi phí giỏ hàng |   |
                  |   +----------------------------------+   |
                  |                                          |
                  |   +----------------------------------+   |
                  |   | UC06: Tìm kiếm DVD theo tiêu đề  |   |
                  |   +----------------------------------+   |
                  +------------------------------------------+
```

---

## 4. Đặc tả chi tiết các Use Case

### UC01: Thêm DVD vào giỏ hàng
- **Mô tả:** Cho phép khách hàng thêm một đĩa DVD vào danh sách đặt mua.
- **Tiền điều kiện:** Đối tượng DVD hợp lệ với các thông tin: tiêu đề, thể loại, đạo diễn, thời lượng, giá tiền.
- **Luồng sự kiện chính:**
  1. Khách hàng chọn DVD cần thêm vào giỏ.
  2. Hệ thống kiểm tra số lượng hiện tại (UC02).
  3. Nếu số lượng chưa vượt quá giới hạn (`MAX_NUMBERS_ORDERED = 20`), hệ thống lưu DVD vào giỏ và thông báo `"The disc has been added"`.
- **Ngoại lệ:** Nếu giỏ hàng đã đầy, hệ thống thông báo `"The cart is almost full"` và từ chối thêm.

### UC02: Xóa DVD khỏi giỏ hàng
- **Mô tả:** Khách hàng loại bỏ một đĩa DVD không muốn mua nữa.
- **Luồng sự kiện chính:**
  1. Khách hàng chỉ định đĩa DVD cần xóa.
  2. Hệ thống tìm thấy đĩa trong giỏ, loại bỏ và thông báo `"The disc has been removed"`.
- **Ngoại lệ:** Nếu đĩa không có trong giỏ, thông báo `"The disc is not in the cart"`.

### UC03: Xem chi tiết giỏ hàng (Print Cart)
- **Mô tả:** Hiển thị danh sách các đĩa đã chọn cùng tổng chi phí.
- **Luồng sự kiện:**
  1. Khách hàng yêu cầu hiển thị giỏ hàng (`cart.print_cart()`).
  2. Nếu giỏ hàng rỗng, in thông báo `"The cart is empty"`.
  3. Nếu có sản phẩm, in tiêu đề bảng, danh sách từng đĩa theo thứ tự và gọi UC05 để in tổng tiền.

### UC04: Tính tổng chi phí (Total Cost)
- **Mô tả:** Tính tổng giá trị các đĩa DVD đang có trong giỏ hàng.
- **Công thức:** $\sum \text{cost của từng đĩa DVD trong giỏ}$.

### UC05: Tìm kiếm DVD theo tiêu đề (Search by Title)
- **Mô tả:** Lọc ra danh sách các DVD có tiêu đề chứa từ khóa tìm kiếm.
- **Đầu vào:** Danh sách đĩa DVD và từ khóa (`keyword`).
- **Đầu ra:** Danh sách DVD khớp với từ khóa tìm kiếm.
