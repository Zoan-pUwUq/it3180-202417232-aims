# Câu hỏi thảo luận – Lab 01

## 1. Cấu hình `--global` được lưu ở đâu? Khác gì so với `--local`?
- **Vị trí lưu trữ:**
  - Cấu hình `--global` được lưu tại tệp cấu hình của người dùng ở thư mục cá nhân: `~/.gitconfig` (hoặc `~/.config/git/config` trên Linux/macOS, `%USERPROFILE%\.gitconfig` trên Windows).
  - Cấu hình `--local` được lưu tại tệp `.git/config` nằm bên trong thư mục repository hiện tại.
- **Sự khác biệt:**
  - Phạm vi áp dụng: `--global` áp dụng cho tất cả các kho mã nguồn (repositories) của người dùng trên máy tính nếu không có cấu hình local ghi đè; trong khi `--local` chỉ áp dụng riêng cho một repository cụ thể.
  - Độ ưu tiên: Cấu hình `--local` có độ ưu tiên cao hơn và sẽ ghi đè giá trị tương ứng của cấu hình `--global` trong repository đó.

---

## 2. Vì sao dùng `git mv` thay vì di chuyển tệp thông thường rồi `git add`?
- Lệnh `git mv` thực hiện đồng thời hai thao tác: di chuyển/đổi tên tệp trên hệ thống tệp và đưa ngay thao tác di chuyển đó vào staging area (tương đương với `mv <cũ> <mới>` + `git rm <cũ>` + `git add <mới>`).
- Khi sử dụng `git mv`, Git nhận diện trực tiếp đây là hành động đổi tên/di chuyển (`renamed 100%`) thay vì ghi nhận như một thao tác xóa tệp cũ rồi tạo một tệp mới không liên quan.
- Điều này giúp bảo tồn toàn vẹn lịch sử commit của tệp mã nguồn từ trước tới nay, cho phép tra cứu liên tục lịch sử phát triển của tệp thông qua lệnh `git log --oneline --follow -- <đường_dẫn_mới>`.

---

## 3. Nhánh `release/lab01` có phải là baseline không? Vì sao?
- **Có**, nhánh `release/lab01` là một **Baseline**.
- **Giải thích:** Theo lý thuyết Quản lý cấu hình phần mềm (SCM), Baseline là một trạng thái phiên bản sản phẩm cấu hình đã qua kiểm tra, được thống nhất đóng băng tại một mốc thời gian cụ thể và từ thời điểm đó chỉ được phép sửa đổi thông qua một quy trình kiểm soát thay đổi chính thức.
- Nhánh `release/lab01` đại diện cho phiên bản hoàn thiện của Lab 01 dùng để nộp bài, đóng vai trò là mốc chuẩn ổn định (baseline) để các bài Lab tiếp theo kế thừa hoặc tạo hotfix nếu phát sinh lỗi.

---

## 4. Vì sao không commit thẳng lên `master` dù làm một mình?
- **Bảo vệ nhánh chính (`master`):** Giữ cho `master` luôn ở trạng thái mã nguồn ổn định, đã kiểm thử và sẵn sàng phát hành bất kỳ lúc nào.
- **Tuân thủ quy trình chuẩn (Release Flow / Feature Branch Workflow):** Tập thói quen phân nhánh: mọi tính năng, sửa lỗi hay tái cấu trúc đều được cô lập trên một nhánh riêng (`refactor/*`, `feature/*`, `bugfix/*`), tránh ảnh hưởng đến luồng chính khi chưa hoàn thiện.
- **Kiểm soát thay đổi & Tự kiểm tra (Self-Review):** Việc tạo Pull Request buộc lập trình viên phải rà soát lại toàn bộ diff (các thay đổi) trước khi merge, viết mô tả mục đích rõ ràng, giảm thiểu lỗi sơ suất.
- **Sẵn sàng cho CI/CD:** Trong môi trường nhóm hoặc dự án thực tế, các quy tắc bảo vệ nhánh (Branch Protection) và bộ kiểm thử tự động (GitHub Actions / CI pipeline) sẽ tự động chạy trên Pull Request để thẩm định chất lượng mã nguồn trước khi tích hợp vào nhánh chính.
