# Contributing to Project Name

Policy chung được kế thừa từ repo `.github` của OSSVN. Repo này bổ sung command kiểm tra của template.

## Trước khi mở PR

### 1. Kiểm tra diff

```bash
git status --short
git diff --check
git diff
```

### 2. Chạy automated checks

Từ root của repository:

```bash
python scripts/validate_repo.py
```

Template hiện không có unit test, build hoặc lint command riêng.

### 3. Kiểm tra thủ công

- Preview `README.md`, `CONTRIBUTING.md` và `docs/TESTING.md` nếu các file này được sửa.
- Nếu sửa `.github/workflows/validate.yml`, kiểm tra workflow vẫn chạy `python scripts/validate_repo.py` và check `validate` vẫn xuất hiện trên Pull Request.
- Nếu sửa `.github/CODEOWNERS`, kiểm tra file vẫn là placeholder generic cho template, không vô tình gắn owner của một project cụ thể.

### 4. Kết quả mong đợi

- `git diff --check` exit code bằng `0`.
- `python scripts/validate_repo.py` in `Repository validation passed.`.
- Template docs render đúng và command trong docs, workflow không mâu thuẫn nhau.
