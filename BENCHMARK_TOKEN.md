# BENCHMARK_TOKEN · STARTER v24 · 20260824

Đo bằng máy: token ước lượng = ký tự / 3 (văn bản tiếng Việt).
HỆ SỐ 1/3 ĐÃ ĐƯỢC ĐỐI CHỨNG (vòng 47, tokenizer Claude công bố
Xenova/claude-tokenizer): thuế thường trực 6.948 ký tự, ước lượng 2.316, đo
thật 4.785 token - hệ số x2,07. Từng file: cao nhất x2,18 (X2_PHATHANH), thấp
nhất x1,68 (X3E_EMAIL). Nên MỌI con số token trong file này là ĐƠN VỊ SO SÁNH
TƯƠNG ĐỐI giữa các route, KHÔNG phải hóa đơn; muốn ra token thật thì nhân
khoảng 2,1. Câu cũ "2,1x là trần trên" sai hai lần: 2,07x là số THẬT chứ không
phải trần, và X2 đã vượt qua nó. Đối chứng phải dùng tokenizer CLAUDE chứ không
phải o200k_base của OpenAI (o200k cho 1,09x - chọn nó là tự chấm điểm dễ cho
mình). Bản Claude công bố thuộc thế hệ Claude 1-2, Anthropic không công bố
tokenizer Claude 4-5, nên đây là mốc GẦN NHẤT chứ chưa phải hóa đơn thật. Phép
2d đo lại con số này khi máy có thư viện tokenizers, không có thì in BỎ QUA -
bộ vẫn không phụ thuộc gói ngoài. Version khớp
DOC_TRUOC (phép kiểm 2b); các số route được MÁY GIỮ KHỚP file thật bằng phép
kiểm 2c (dung sai 10%), số mới lấy bằng lệnh
`python kiem_tra_bo.py . --sinh-benchmark`. Đây là BENCHMARK TĨNH; cột
"phiên thật" để trống, điền dần từ log phiên chạy thật, chưa có số đó thì
không tuyên bố kết quả runtime.

## Thuế thường trực mỗi phiên

| Thành phần | trước tối ưu (v05) | hiện tại |
|---|---:|---:|
| INSTRUCTION dán trong Project | 4148 | ~1924 |
| Mở phiên đọc cấu hình | X0 cả file 2770 | X0_INDEX ~247 |
| BANG_DIEU_KHIEN (mẫu rỗng, chạy thật lớn hơn) | 51 | ~145 |
| CỘNG | ~6969 | ~2316 |

Giảm gần 67 phần trăm thuế thường trực theo benchmark tĩnh VỚI VIEW MẪU
RỖNG; mức tối đa runtime theo trần đã enforce (X0_INDEX 2.400 + BANG_DIEU_KHIEN
4.200 ký tự runtime, kiem_van_hanh giữ, cộng INSTRUCTION ~1.924) xấp xỉ 4.124
token, vẫn thấp hơn trước tối ưu.
Nền tảng nào kéo CẢ X5 (bằng số dòng SUA_FILE ở bảng dưới) thay vì đúng
mục thì mỗi thao tác đổi trạng thái tốn thêm phần chênh; luật đọc theo mục
của X5 mục 5 áp cho cả X3, X5.

## Chi phí context theo loại yêu cầu (ngoài thuế, chưa tính tài liệu nghiệp vụ)

Mỗi dòng là TỔNG của route đó, không cộng dồn giữa các dòng.

| Loại | Context bắt buộc | Token đọc thêm | Phiên thật: token · tool calls · đọc thừa · đúng sai |
|---|---|---:|---|
| HOI | DUKIEN theo khối | theo khối | |
| BAN | không | 0 | |
| NOI_BO mức A | X5 mục 1 + X1 mục 3, 4 | ~1902 (thêm X5 mục 3 ~1339 khi ghi sổ; dự án phần mềm thêm mục 1b ~421) | |
| SUA_FILE nội bộ | X5 trừ mục 7b + TAILIEU theo khối | ~5987 + khối (không phần mềm trừ thêm mục 1b ~421) | |
| CUA_VAO thường (không EMAIL) | X3 mục 1 tới 5 (5b gate khi dán chat) + X5 mục 1 + VIEC, TAILIEU theo khối | ~2814 + khối | |
| CUA_VAO mail (profile EMAIL) | như trên CỘNG X3E trừ mục 1c phục hồi | ~6605 + khối | |
| RA_SOAT | X4 + kết quả kiem_van_hanh.py | ~1618 (X4) cộng bảng kết quả in ra | |
| SOAN_RA thường lệ | X1 + X2 + X5 mục 1 | ~3683 | |
| SOAN_RA chính thức | thêm DUKIEN + mục X0 được trỏ | ~3683 + khối | |

## Trần từng file, máy enforce ở kiem_tra_bo.py phép kiểm 9

INSTRUCTION 8.000 ký tự · X0 20.000 (đọc theo mục, thuế là X0_INDEX) · X5
20.000 (mục 1b và 7b đều có gate, không phải thuế chung) · X3 5.500 (mục 5b
gate khi dán chat) · X3E 13.000 (chỉ nạp khi bật EMAIL) · X9 8.500 (đọc một
lần mỗi công ty, không nạp vào CHAT) · X4 5.500 (chỉ đọc khi RA_SOAT) · X2
4.200 · X1 3.200 · X0_INDEX 1.500 · BANG_DIEU_KHIEN 1.400 · README 9.000 ·
bản gộp _GOP 260.000 (không nạp vào phiên nào). Vượt trần là FAIL.

## Ghi chú phiên CHAT

Các con số route trên chỉ đúng cho COWORK đọc theo mục. Phiên CHAT nạp X0
tới X5, X9 (và X3E nếu bật EMAIL) qua tài liệu Project: nền claude.ai truy
hồi theo cơ chế riêng, xấu nhất là cả bộ:
Phiên CHAT chỉ nên nạp X0, X1, X2, X5 (và X3E nếu bật EMAIL). GỠ X9 sau khi
cài xong (đọc một lần mỗi công ty), KHÔNG nạp X4 (chỉ đọc khi RA_SOAT), và
KHÔNG nạp X3 khi phiên CHAT không làm CUA_VAO - chính đoạn dưới đã chốt CHAT
không phải phiên ghi sổ:
CHAT HOI, BAN, soạn nháp (không X3, X4, X9) ~16619 token
CHAT không EMAIL ~18315 token
CHAT có EMAIL (kèm X3E) ~22313 token
CHAT nạp cả X9 và X4 ~22632 token
(các số này máy giữ khớp qua phép 2c; cắt bỏ X9 và X4 ~4317 token mỗi phiên,
19,2 phần trăm).
CHAT vì thế chỉ nên dùng cho HOI, BAN, soạn nháp, không phải phiên ghi sổ chính.

## Phiên thật đã đo (PILOT 2026-08-28)

Pilot dựng một công ty giả lập có dự án PHẦN MỀM (profile REGULATED + EMAIL):
clone bộ, chạy X9 cài từ zero, vòng thử mức A của X9 mục 3, rồi rà máy. Cái ĐO
ĐƯỢC ở đây là: file nào THẬT SỰ được đọc, bao nhiêu lượt đọc, có đọc thừa không,
kết quả đúng hay sai. Số TOKEN vẫn là ước lượng ký tự/3 áp lên phần đã đọc thật,
chưa đối chứng tokenizer nào (xem ĐỘ BẤT ĐỊNH ở đầu file).

```
CÀI ĐẶT (X9 phiên đầu)   đọc thật INSTRUCTION + X9 + X0 + 9 mẫu sổ
                         32.924 ký tự đo tại commit, ~11,0k token ước lượng
                         6 lượt đọc file · đọc thừa: không · sai: không
NOI_BO mức A (vòng thử)  đọc thật X5 mục 3, 3.176 ký tự ~1.059 token ĐO TẠI
                         COMMIT vòng 39; mục 3 nay ~1262, xem bảng route
                         đọc THIẾU X1 mục 3, 4 của route (không gây sai kết
                         quả vì việc thuần nội bộ, không có đầu ra)
RA_SOAT                  0 token ĐỌC X4, nhưng KHÔNG phải 0 token phiên: bảng
                         kết quả kiem_van_hanh.py dán vào phiên đo được ~806
                         token trên kho lành tối thiểu và lớn hơn trên kho ĐANG
                         LỆCH (phép 13b và 13c giữ hai trần đó), phình từ ~502
                         ở vòng 39 và ~587 ở vòng 42; phép 13d giữ số này khớp. Route ~1618 chỉ phải trả
                         khi cần luật rà, không phải mỗi lượt rà
```

Bốn defect do pilot phơi ra (không vòng đọc-tĩnh nào thấy): 0d báo động giả
ngay sau khi cài · mâu thuẫn "điền nhóm B giữa chừng" với nhóm khóa C11 ·
`git pull` trên kho đang chạy làm mất dòng sổ (vá vòng 38) · X3E tả payload
bằng văn xuôi trong khi máy đòi schema JSON không khai ở đâu, thực thi đúng
chữ vẫn bị 12h và 12k từ chối (vá vòng 39: X3E mục 1b).

PILOT EMAIL: nạp một mail công văn trọn bốn bước (staging, PREPARED, áp ba
thao tác kèm index, COMMITTED, registry) theo schema mục 1b thì kho qua sạch
toàn bộ 12a-12l.

## Ghi chú profile

Con số trên là CORE đầy đủ. LITE bỏ khối REGULATED, PARALLEL, AUTOMATED,
EMAIL nên X0 ngắn hơn đáng kể; X3E và sổ THU chỉ được nạp khi bật EMAIL,
không tăng thuế của bộ lõi.
CUA_VAO thường của LITE chỉ đọc X3 mục 1 tới 5 ~1025 token (mục 5b gate khi dán chat).
