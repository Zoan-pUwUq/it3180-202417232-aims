def search_by_category(items, category):
    """Tìm kiếm đĩa DVD theo thể loại."""
    return [dvd for dvd in items if category.lower() in dvd.category.lower()]


def search_by_title(items, keyword):
    """Tìm kiếm đĩa DVD theo tiêu đề (phân biệt hoa thường)."""
    return [dvd for dvd in items if keyword in dvd.title]

