# BENCHMARK_TOKEN · STARTER v24 · 20260824

Đo bằng máy: token ước lượng = ký tự / 3 (văn bản tiếng Việt). Version khớp
DOC_TRUOC (phép kiểm 2b); các số route được MÁY GIỮ KHỚP file thật bằng phép
kiểm 2c (dung sai 10%), số mới lấy bằng `python kiem_tra_bo.py . --sinh-benchmark`. Đây là BENCHMARK TĨNH; cột "phiên thật" để
trống, điền dần từ log phiên chạy thật, chưa có số đó thì không tuyên bố kết quả
runtime.

## Thuế thường trực mỗi phiên

| Thành phần | trước tối ưu (v05) | hiện tại |
|---|---:|---:|
| INSTRUCTION dán trong Project | 4148 | 1884 |
| Mở phiên đọc cấu hình | X0 cả file 2770 | X0_INDEX 228 |
| BANG_DIEU_KHIEN (mẫu rỗng, chạy thật lớn hơn) | 51 | 101 |
| CỘNG | ~6969 | ~2213 |

Giảm xấp xỉ 70 phần trăm thuế thường trực theo benchmark tĩnh VỚI VIEW MẪU
RỖNG; mức tối đa runtime theo trần đã enforce (X0_INDEX 2.400 + BANG_DIEU_KHIEN
4.200 ký tự runtime, kiem_van_hanh giữ, cộng INSTRUCTION ~1.884) xấp xỉ 4.084
token, vẫn thấp hơn trước tối ưu.
Nền tảng nào kéo CẢ X5 (hiện ~5449 token) thay vì đúng mục thì mỗi thao tác đổi
trạng thái tốn thêm phần chênh; luật đọc theo mục của X5 mục 5 áp cho cả X3, X5.

## Chi phí context theo loại yêu cầu (ngoài thuế, chưa tính tài liệu nghiệp vụ)

Mỗi dòng là TỔNG của route đó, không cộng dồn giữa các dòng.

| Loại | Context bắt buộc | Token đọc thêm | Phiên thật: token · tool calls · đọc thừa · đúng sai |
|---|---|---:|---|
| HOI | DUKIEN theo khối | theo khối | |
| BAN | không | 0 | |
| NOI_BO mức A | X5 mục 1 + X1 mục 3, 4 | ~1628 (thêm X5 mục 3 ~950 khi ghi sổ; dự án phần mềm thêm mục 1b ~421) | |
| SUA_FILE nội bộ | X5 + TAILIEU theo khối | ~5449 + khối (không phần mềm ~5028, trừ mục 1b) | |
| CUA_VAO thường (không EMAIL) | X3 mục 1 tới 5 + X5 mục 1 + VIEC, TAILIEU theo khối | ~2532 + khối | |
| CUA_VAO mail (profile EMAIL) | như trên CỘNG X3E (~3681) + THU theo khối | ~6213 + khối | |
| RA_SOAT | X4 + kết quả kiem_van_hanh.py | ~1506 | |
| SOAN_RA thường lệ | X1 + X2 + X5 mục 1 | ~3390 | |
| SOAN_RA chính thức | thêm DUKIEN + mục X0 được trỏ | ~3390 + khối | |

## Trần từng file, máy enforce ở kiem_tra_bo.py phép kiểm 9

INSTRUCTION 8.000 ký tự · X0 16.000 (đọc theo mục, thuế là X0_INDEX) · X5
17.000 (mục 1b chỉ nạp khi có dự án phần mềm) · X3 4.500 · X3E 12.000 (chỉ nạp khi bật EMAIL) · X9 6.500 · X4 5.500
(chỉ đọc khi RA_SOAT) · X2 4.200 · X1 3.200 · X0_INDEX 1.500 · BANG_DIEU_KHIEN 1.400. Vượt trần
là FAIL.

## Ghi chú phiên CHAT

Các con số route trên chỉ đúng cho COWORK đọc theo mục. Phiên CHAT nạp X0 tới
X5, X9 (và X3E nếu bật EMAIL) qua tài liệu Project: nền claude.ai truy hồi theo cơ chế riêng, xấu nhất
là cả bộ:
CHAT không EMAIL ~19046 token
CHAT có EMAIL (kèm X3E) ~22727 token
(hai số này máy giữ khớp qua phép 2c); CHAT vì thế chỉ nên dùng cho HOI,
BAN, soạn nháp, không phải phiên ghi sổ chính.

## Ghi chú profile

Con số trên là CORE đầy đủ. LITE bỏ khối REGULATED, PARALLEL, AUTOMATED, EMAIL
nên X0 ngắn hơn đáng kể; X3E và sổ THU chỉ được nạp khi bật EMAIL, không
tăng thuế của bộ lõi; CUA_VAO thường của LITE nay chỉ đọc X3 ~3.4k ký tự.
