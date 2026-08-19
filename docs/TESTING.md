# Testing

## Automated

Từ root của repository:

```bash
python scripts/validate_repo.py
```

Kết quả mong đợi:

```text
Repository validation passed.
```

Template hiện chưa có unit test, build hoặc lint command riêng.

Khi tạo project thật từ template, thay section này bằng command thực tế của project trước khi mời contributor.

## Manual

Trước khi mở PR cho chính template này:

1. Preview Markdown đã sửa.
2. Nếu sửa manifest/workflow, kiểm tra check `validate` vẫn trỏ tới `python scripts/validate_repo.py`.
3. Nếu sửa CODEOWNERS, giữ placeholder generic cho template.
