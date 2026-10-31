# Câu hỏi thảo luận Lab 05

**Họ và tên:** Vũ Tiến Doanh  
**Mã sinh viên:** 202417232  
**Học phần:** IT3180 – Quản lý cấu hình phần mềm với Git & GitHub

---

## Câu 1: Ưu, nhược điểm của upstream first so với release first?

### 1. Mô hình Upstream First (Sửa trên `master` trước, rồi cherry-pick về các nhánh `release/*`)
- **Ưu điểm:**
  - **Tránh hồi quy (Prevent Regression):** Nhánh chính (`master`/`main`) luôn luôn nhận bản sửa lỗi đầu tiên, đảm bảo mã nguồn tương lai không bao giờ bị sót lỗi cũ.
  - **Chuẩn hóa quy trình doanh nghiệp:** Phù hợp với các hệ thống lớn, phát triển liên tục theo Sprint (như mô hình Release Flow của Microsoft, Linux Kernel, Chromium).
  - Codebase trên `master` luôn được kiểm thử và xác thực đầy đủ trước khi chọn lọc commit đưa về môi trường production/release cũ.
- **Nhược điểm:**
  - **Thời gian phản hồi hotfix chậm hơn:** Cần phải đi qua quy trình PR, CI và review trên `master` trước khi được đưa vào release đang chạy ngoài thực tế.
  - **Nguy cơ xung đột cao:** Nếu nhánh `master` đã tiến quá xa với nhiều cấu trúc/tính năng mới hoặc tái cấu trúc, việc cherry-pick ngược về nhánh release cũ sẽ gặp nhiều xung đột phức tạp.

---

### 2. Mô hình Release First (Sửa trực tiếp trên nhánh `release/*` bị lỗi trước, rồi cherry-pick về `master` và các release khác)
- **Ưu điểm:**
  - **Phản ứng tức thì (Fast Hotfix Response):** Sửa trực tiếp trên phiên bản tối thiểu bị ảnh hưởng (chẳng hạn `v1.0.0` trên `release/lab04`), giúp nhanh chóng phát hành bản vá (`v1.0.1`) mà không phải chờ đợi tiến trình phát triển của `master`.
  - **Độc lập và an toàn cho production:** Mã sửa lỗi được viết dựa trên snapshot codebase thực tế của phiên bản đang phục vụ khách hàng, tránh rủi ro kéo theo các thay đổi đang dở dang trên `master`. Rất phù hợp với bài tập/đồ án nộp theo từng tuần (nhiều bản nộp độc lập).
- **Nhược điểm:**
  - **Rủi ro bỏ quên (Risk of Forgetting Propagation):** Nếu không có quy trình kiểm soát chặt chẽ, lập trình viên rất dễ quên lan truyền (propagate) bản vá về `master` hoặc các nhánh release song song khác, khiến lỗi tái xuất hiện ở phiên bản kế tiếp.
  - Phải thực hiện nhiều thao tác cherry-pick thủ công và cần quy trình kiểm toán nghiêm ngặt ở bước cuối.

---

## Câu 2: Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F sẽ phát hiện?

Ở Phần F, có các lệnh sau sẽ phát hiện ngay việc quên lan truyền:

1. **Vòng lặp kiểm tra hành vi (Functional verification loop across refs):**
   ```bash
   for ref in v1.0.1 v1.1.0 master; do
     git switch --detach -q $ref; printf "%-8s " $ref
     python -c "from aims.dvd import DigitalVideoDisc as D; from aims.search import search_by_title; \
   print(len(search_by_title([D('The Lion King')], 'lion')))"
   done; git switch -q master
   ```
   - Nếu quên lan truyền sang `release/lab05` (ở tag `v1.1.0`), kết quả in ra sẽ là:
     ```text
     v1.0.1   1
     v1.1.0   0
     master   1
     ```
     Dòng `v1.1.0` in ra `0` (không tìm thấy) chứng minh lỗi vẫn còn tồn tại trên bản phát hành đó.

2. **Lệnh kiểm tra commit cherry-pick:**
   ```bash
   git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"
   ```
   - Nếu chưa lan truyền vào `release/lab05`, lệnh này sẽ chỉ trả về **1 commit** (trên master) thay vì **2 commit** như kỳ vọng.

3. **Lệnh so sánh commit giữa master và release:**
   ```bash
   git cherry -v origin/master origin/release/lab05
   ```
   - Lệnh này sẽ hiển thị các commit khác biệt giữa hai nhánh để phát hiện commit sửa lỗi chưa được đồng bộ tương đương.
