# Câu hỏi thảo luận – Lab 02

## 1. Vì sao phải đồng bộ `master` trước khi tạo PR?
- **Phát hiện sớm xung đột (Conflict) ở môi trường cục bộ:** Khi làm việc nhóm song song, nhánh `master` liên tục tiến về phía trước do các đồng nghiệp khác đã merge code. Việc kéo và merge `origin/master` vào nhánh của mình giúp phát hiện và giải quyết xung đột ngay trên máy lập trình viên, thay vì để xảy ra xung đột trên giao diện GitHub khi mở PR.
- **Đảm bảo tính tương thích và kiểm thử tích hợp (Integration Test):** Mã nguồn của tính năng mới có thể không bị conflict về mặt cú pháp nhưng có thể gây lỗi logic khi kết hợp với những thay đổi mới nhất trên `master`. Đồng bộ trước cho phép chạy thử nghiệm toàn bộ hệ thống (`python main.py` hoặc bộ test) để bảo đảm sản phẩm hoạt động trơn tru sau khi tích hợp.
- **Tạo điều kiện cho quá trình Review và Merge tự động:** PR không bị xung đột (*"Able to merge"*) giúp người review tập trung vào logic nghiệp vụ và cho phép áp dụng các hình thức merge sạch như Squash hoặc Rebase một cách tự động.

---

## 2. Khi nào không được rebase?
- **Nguyên tắc vàng của Rebase (The Golden Rule of Rebase):** **Tuyệt đối không rebase trên các nhánh công khai / nhánh dùng chung** (như `master`, `main`, `develop`, `release/*` hoặc nhánh tính năng đang có nhiều thành viên cùng làm việc).
- **Lý do:**
  - Lệnh `git rebase` thay đổi gốc nhánh và tạo ra các commit mới hoàn toàn (mã băm SHA mới), đồng thời viết lại toàn bộ lịch sử commit.
  - Nếu nhánh đã được push lên remote và có người khác kéo về làm tiếp, việc viết lại lịch sử sẽ làm sai lệch commit tree của họ, dẫn đến xung đột nghiêm trọng (*diverged branches*) và khó khăn trong việc đồng bộ lại.
- **Khi nào NÊN rebase:** Chỉ dùng rebase cho các nhánh cá nhân cục bộ (*local private branches*) trước khi chia sẻ lên kho chung, nhằm làm sạch lịch sử commit trước khi gửi PR.

---

## 3. Nhánh `feature/*` khác nhánh `topic/*` ra sao?
- **Nhánh `feature/*` (Feature branch):**
  - Thường dùng cho các tính năng nghiệp vụ cụ thể, rõ ràng của sản phẩm (ví dụ: `feature/cart-print`, `feature/search-by-title`, `feature/order-checkout`).
  - Thường có vòng đời gắn với chức năng người dùng, có thể bao gồm nhiều bước phát triển và bộ kiểm thử tương ứng.
- **Nhánh `topic/*` (Topic branch):**
  - Là nhánh phát triển ngắn hạn (*short-lived*), tập trung vào một chủ đề kỹ thuật hẹp hoặc công việc mang tính phụ trợ, không trực tiếp tạo ra tính năng người dùng lớn.
  - Ví dụ: cập nhật tài liệu (`topic/use-case-diagram`, `topic/api-docs`), cấu hình hệ thống (`topic/pr-template`, `topic/ci-pipeline`), thử nghiệm một giải pháp kỹ thuật mới (*spike/proof-of-concept*).

---

## 4. So sánh 3 kiểu Merge trong Git/GitHub (Slide 34)

| Tiêu chí | Merge Commit (`Merge pull request`) | Squash (`Squash and merge`) | Rebase (`Rebase and merge`) |
| :--- | :---: | :---: | :---: |
| **Giữ commit chi tiết** | Có (bảo toàn tất cả commit con) | Không (gộp tất cả thành 1 commit duy nhất) | Có (giữ đủ commit nhưng sinh SHA mới) |
| **Lịch sử tuyến tính** | Không (tạo nhánh rẽ và nút merge) | Có (thẳng hàng trên master) | Có (thẳng hàng trên master) |
| **Revert cả tính năng** | Dễ dàng (1 lệnh `git revert -m 1 <sha>`) | Dễ dàng (1 lệnh `git revert <sha>`) | Phức tạp (phải revert từng commit riêng lẻ) |
| **Trường hợp áp dụng** | Tính năng lớn, cần lưu vết đầy đủ quá trình phát triển và thảo luận | Tính năng nhỏ, các commit vụn vặt trong lúc dev cần dọn sạch | Các nhánh tài liệu, commit độc lập muốn giữ lịch sử thẳng đẹp |
