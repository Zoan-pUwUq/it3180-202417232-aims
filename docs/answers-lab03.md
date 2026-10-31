# Câu hỏi thảo luận – Lab 03

## 1. Merge Base là gì?
- **Định nghĩa:** Trong Git, **Merge Base** của hai nhánh (hoặc hai commit) là **Tổ tiên chung gần nhất (Best Common Ancestor)** của chúng trong đồ thị lịch sử commit (DAG - Directed Acyclic Graph).
- **Vai trò trong giải quyết xung đột (3-way merge):**
  - Khi thực hiện hợp nhất hai nhánh (ví dụ: `git merge feature`), Git không chỉ so sánh trực tiếp 2 commit đầu nhánh mà thực hiện kỹ thuật **3-way merge** dựa trên 3 mốc:
    1. Trạng thái của nhánh hiện tại (`HEAD` / `ours`).
    2. Trạng thái của nhánh cần gộp (`theirs`).
    3. Trạng thái tại điểm **Merge Base** (`base`).
  - Dựa vào Merge Base, Git xác định được những dòng nào thực sự bị một bên thay đổi và những dòng nào bị cả hai bên cùng sửa đổi. Chỉ những vùng mà cả hai bên cùng sửa khác nhau so với Merge Base mới sinh ra **Merge Conflict**.
- **Cách tra cứu Merge Base:** Dùng lệnh:
  ```bash
  git merge-base <branch_A> <branch_B>
  ```

---

## 2. Vì sao các nhánh công khai như `master` và `release/*` bắt buộc phải dùng `revert` thay vì `reset`?

| Tiêu chí | `git reset` | `git revert` |
| :--- | :--- | :--- |
| **Bản chất hoạt động** | Dời con trỏ nhánh lùi về quá khứ, loại bỏ hoặc viết lại các commit phía sau. | Tạo ra một **commit mới** có nội dung đảo ngược lại những thay đổi của commit bị hủy. |
| **Ảnh hưởng lịch sử** | **Viết lại lịch sử** (xóa bỏ commit cũ khỏi nhánh). | **Bảo tồn toàn vẹn lịch sử** (thêm commit mới tiếp nối tuyến tính). |
| **Phạm vi an toàn** | Chỉ an toàn cho **commit cục bộ (local)** chưa chia sẻ lên remote. | An toàn tuyệt đối cho các **nhánh chung/công khai** (`master`, `release/*`). |

### Các lý do cốt lõi:
1. **Tránh phá vỡ sự đồng bộ trong làm việc nhóm (Diverged Branches):**
   - Các nhánh `master` và `release/*` là nhánh công khai mà mọi thành viên trong nhóm đều kéo về làm việc.
   - Nếu dùng `git reset` rồi dùng `git push --force` để đè lên remote, mã băm commit trên remote bị thay đổi. Khi các thành viên khác kéo mã nguồn về hoặc cố gắng push nhánh của họ lên, cây lịch sử sẽ bị phân rã (*diverged*), gây lỗi nghiêm trọng và rất khó khôi phục.
2. **Tuân thủ quy tắc bảo vệ nhánh (Branch Protection):**
   - Các nhánh chính như `master` và `release/*` luôn được cấu hình cấm `force push` (*Do not allow force pushes*). Do đó, bạn không thể đẩy một nhánh đã bị `reset` lùi về remote.
3. **Tính minh bạch và khả năng kiểm toán (Auditability):**
   - Trong Quản lý cấu hình phần mềm (SCM), mọi hành động thay đổi, kể cả việc hoàn tác một tính năng bị lỗi, đều phải được lưu vết rõ ràng. `git revert` tạo ra một commit có thông điệp minh bạch (*"Revert '...' "*), giúp cả nhóm và hệ thống CI/CD biết chính xác khi nào tính năng bị hủy và tại sao.
