# Repository Setup Checklist

Dùng checklist này sau khi tạo repo từ template.

- [ ] Đổi tên và mô tả trong `README.md`.
- [ ] Chọn R0, R1, R2 hoặc R3 và đặt GitHub Custom Property `risk_level`.
- [ ] Review `LICENSE` - giữ MIT hoặc thay nếu project cần license khác.
- [ ] Cập nhật `.github/CODEOWNERS`.
- [ ] Thêm test/build workflow cần thiết.
- [ ] Cập nhật `docs/TESTING.md`.
- [ ] Import baseline ruleset.
- [ ] Import risk ruleset tương ứng.
- [ ] Chạy PR thử để các workflow cần thiết xuất hiện và pass.
- [ ] Cấu hình required status checks riêng cho repo, chỉ chọn những check đã chạy thành công.
