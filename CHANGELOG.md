# Changelog

Tất cả các thay đổi đáng chú ý của dự án AIMS-mini sẽ được ghi nhận tại tệp này.
Định dạng dựa trên [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
và tuân thủ [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.1] - 2026-11-01
### Fixed
- Sửa lỗi hàm `search_by_title()` không phân biệt hoa thường (#20).


## [1.0.0] - 2026-11-01
### Added
- Phương thức `Cart.print_cart()` hiển thị danh sách đĩa và tổng chi phí.
- Chức năng tìm kiếm đĩa DVD theo tựa đề `search_by_title()` trong module `aims.search`.
- Phương thức tính tổng chi phí sau chiết khấu `Cart.total_cost_with_discount(percent)`.
- Tài liệu ca sử dụng hệ thống `docs/use-case.md` và mẫu Pull Request template.
- Bộ kiểm thử tự động với `unittest` cho giỏ hàng và chức năng tìm kiếm.

### Fixed
- Sửa lỗi giỏ hàng chấp nhận đĩa thứ 21 dù giới hạn tối đa là 20 đĩa (`MAX_NUMBERS_ORDERED`) (#6).
- Sửa công thức tính chiết khấu giảm giá và kiểm tra hợp lệ phần trăm (0 - 100%).
