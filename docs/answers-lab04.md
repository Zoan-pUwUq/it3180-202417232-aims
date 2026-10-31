# Câu hỏi thảo luận – Lab 04

## 1. Vì sao phải chuẩn bị phát hành trên `master` trước, không sửa trên nhánh `release/*`?
- **Nguyên tắc "Nguồn sự thật duy nhất" (Single Source of Truth):** Nhánh `master` phải luôn phản ánh trạng thái chuẩn xác nhất của dự án. Mọi chuẩn bị phát hành (nâng số phiên bản `__version__`, cập nhật `CHANGELOG.md`, kiểm thử toàn diện) phải được thực hiện và kiểm duyệt qua PR trên `master` trước.
- **Tránh vi phạm quy tắc Release Flow:** Nếu thực hiện sửa đổi số phiên bản hoặc changelog trực tiếp trên nhánh `release/*`, nhánh `master` sẽ bị thiếu các thông tin này. Để đưa về master sẽ buộc phải merge ngược `release/*` vào `master`, điều này vi phạm quy tắc cốt lõi của Release Flow (*"release/* không bao giờ merge ngược vào master"*).
- **Đảm bảo tính kế thừa:** Các tính năng mới phát triển tiếp theo trên `master` sẽ tự động kế thừa đúng số phiên bản và lịch sử changelog mới nhất.

---

## 2. Vì sao nhánh `release/*` không bao giờ merge ngược vào `master`? So sánh với GitFlow.
- **Trong mô hình Release Flow:**
  - Nhánh `release/*` rẽ ra từ `master` khi phiên bản đã hoàn thiện trên `master` và được dùng để **đóng băng baseline** phục vụ nộp bài hoặc triển khai sản xuất.
  - Sau khi rẽ nhánh, `release/*` trở thành dòng bảo trì riêng biệt (chỉ nhận hotfix nếu có). Việc không merge ngược vào `master` giúp nhánh `master` duy trì lịch sử tuyến tính, trong sạch, tránh "merge hell" và xung đột không cần thiết.
- **So sánh với mô hình GitFlow:**
  - Trong GitFlow, nhánh `release` rẽ từ `develop`. Khi phát hành xong, GitFlow bắt buộc phải merge nhánh `release` vào cả hai nhánh: `main` (gắn tag) VÀ `develop` (để đồng bộ).
  - Nhược điểm của GitFlow là quy trình cồng kềnh, sinh ra nhiều nút merge phức tạp, dễ gây nhầm lẫn khi có nhiều bản phát hành song song; trong khi Release Flow đơn giản hơn rất nhiều khi coi `master` là gốc.

---

## 3. Vì sao nâng lên phiên bản `1.0.0` mà không phải `0.4.0`?
- **Theo quy ước Semantic Versioning (SemVer):**
  - Định dạng phiên bản: `MAJOR.MINOR.PATCH`.
  - Dòng phiên bản `0.y.z` (như `0.1.0`, `0.2.0`, `0.3.0` ở các bài Lab trước) đại diện cho giai đoạn phát triển ban đầu (*initial development*), hệ thống chưa hoàn thiện, API có thể thay đổi bất kỳ lúc nào.
  - Phiên bản `1.0.0` đánh dấu mốc **bản phát hành ổn định đầu tiên (First Stable Production Release)** của sản phẩm, khi hệ thống đã có đầy đủ kiến trúc package chuẩn (`aims/`), đầy đủ tính năng cốt lõi (Cart, DVD, Search, Discount), bộ kiểm thử tự động `unittest` hoàn chỉnh và tài liệu hướng dẫn bàn giao chính thức.
