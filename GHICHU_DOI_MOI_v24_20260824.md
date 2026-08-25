# GHI CHÚ ĐỔI MỚI · STARTER · 20260824

File này cho người đánh giá. Không phải luật, không cần copy vào bộ chạy.
Hai mươi ba vòng, mới nhất ở trên; vòng 9 (v10) từng qua thêm một lượt team agent
nội bộ tự rà, tự dựng case, tự đóng vai người dùng.

## Vá 20260825: phát hành qua git, chạy được trên Windows

Không đổi luật, không đổi INSTRUCTION, không đổi X0 tới X5. Ba lỗi lộ ra khi
đưa bộ lên GitHub và chạy phép kiểm trên máy Windows thật:

1. Console Windows mặc định cp1252 không in được tiếng Việt, cả hai script
   crash ngay dòng in đầu tiên. Sửa: ép stdout, stderr sang UTF-8 khi mở, lỗi
   ký tự thì thay thế chứ không dừng phép kiểm.
2. Phép 12j so containment staging bằng chuỗi có "/", nhưng resolve() trên
   Windows trả "\\" nên BỘ SẠCH cũng bị báo "resolve ra ngoài _thu_staging"
   oan, kéo fixture 66 ca FAIL. Sửa: so bằng pathlib (goc_staging in
   d.parents), áp cho cả kiểm đính kèm. kiem_van_hanh lên v20.
3. Docstring bao_phu chứa "\ " gây SyntaxWarning mỗi lần import. Chuyển raw
   string.

Kèm README.md làm cửa vào cho người tới từ link git: repo là BỘ MẪU, không
phải kho công ty; các bước từ clone tới gõ "cài đặt" ở phiên đầu.

## Vòng 23: v23 sang v24, khóa nốt chế độ --ho (vòng đánh giá 22, 9,6/10)

Lại chỉ sửa công cụ, không đổi luật, không đổi INSTRUCTION, không đổi X0 tới X5.

1. Hồi quy do chính v23 tạo ra. v23 thu hẹp danh sách dòng TAILIEU theo họ
   TRƯỚC khi tính phạm vi bao phủ, nên một dòng trỏ THƯ MỤC như `Kho 01_A/`
   biến mất khỏi phép tính và `01_A/BC_v02.docx` bị đề xuất _INBOX oan dù cả
   bộ hồ sơ đã có dòng trong sổ. v24 tách hai việc: phạm vi ĐÃ VÀO SỔ luôn
   tính trên TOÀN BỘ TAILIEU, còn phần kiểm file mất, sha và bất biến mới thu
   về đúng họ đang quét.
2. Cache đời cũ không được mang theo bằng chứng ổn định sai. Bản trước v19
   chỉ ghi MỘT mốc chung toàn kho; nếu mốc đó đã quá năm phút thì mọi file
   trong cache lập tức được coi là ổn định, kể cả file thật ra vừa đổi nội
   dung. v24 nhận diện cache thiếu `"v": 2`, vẫn nạp nội dung để so sha nhưng
   ĐÓNG DẤU LẠI mốc bằng thời điểm chạy, kèm một dòng lưu ý. Lần chạy đầu sau
   nâng cấp phải chờ đủ khoảng ổn định, từ lần sau trở đi mốc riêng từng file
   hoạt động bình thường.

Fixture lên 66 ca: một dòng `Kho 01_A/` phải bao phủ `01_A/BC_v02.docx` trong
chế độ --ho, và cache đời cũ không nhận ổn định ngay. Cả hai ca đều được chạy
ngược trên v23 để xác nhận là bắt được lỗi thật, không phải test tự thỏa mãn.

## Vòng 22: v22 sang v23, sửa lỗi thực thi của chế độ --ho (vòng đánh giá 21, 9,5/10)

Vòng này KHÔNG đổi luật, không đổi INSTRUCTION, không đổi X0 tới X5. Chỉ sửa
công cụ: vòng đánh giá 21 chạy thật chế độ --ho của v22 và bắt được bốn lỗi mà
bộ tự kiểm khi đó không thấy, vì hai fixture mới chỉ kiểm hàm khớp tên.

Lỗi đã sửa:

1. Selector mơ hồ. v22 hiểu --ho theo ba nghĩa lẫn nhau nên: truyền
   `01_A/BC_v01.docx` chỉ nhận đúng v01, bỏ sót v02 CÙNG HỌ; truyền thư mục
   `01_A` lại nhận cả họ KHAC; truyền tên `BC.docx` kéo cả họ BC ở dự án khác.
   v23 chỉ nhận ĐÚNG một đường dẫn tương đối tới MỘT FILE, từ file đó suy khóa
   (thư mục, họ đã chuẩn hóa), rồi quét mọi phiên bản cùng họ trong ĐÚNG thư
   mục đó. Thư mục, tên họ trơ, file không có thật, đường dẫn ra ngoài kho đều
   bị từ chối kèm câu nhắc cách dùng.
2. Cache giữ mốc thời gian TOÀN KHO nên luật ổn định bị phá: file vừa đổi nội
   dung, quét lần đầu ra KHÔNG XÁC ĐỊNH, quét lại ngay lập tức đã thành HIỆN
   HÀNH. v23 đổi cache sang MỐC RIÊNG TỪNG FILE, "luc" là lần đầu quan sát
   thấy đúng nội dung đang có; file giữ nguyên nội dung thì mốc giữ nguyên,
   file đổi nội dung thì mốc đặt lại. Ổn định = cùng nội dung VÀ đã giữ nội
   dung đó tối thiểu năm phút, đúng cả ở chế độ quét cả kho lẫn chế độ --ho.
3. Hợp nhất cache chỉ `update`, không loại mục cũ, nên file đã xóa khỏi một họ
   vẫn nằm lại trong cache. v23 THAY đúng tập cache của họ đang quét, các họ
   khác giữ nguyên.
4. --ho vẫn duyệt cả cây kho rồi mới lọc. v23 duyệt ĐÚNG thư mục của họ bằng
   iterdir, không rglob. Ở chế độ này phần đối chiếu TAILIEU cũng chỉ soi các
   dòng sổ thuộc đúng họ đó, và nhãn phép kiểm mang thêm phạm vi để không
   đọc nhầm thành đã kiểm cả kho.

Hai lỗi cách dùng thành LỆCH thay vì im lặng: --ho không khớp file nào (trước
đây PASS như thể mọi thứ sạch), và thiếu giá trị sau --ho (trước đây rơi về
quét cả kho).

Fixture: bỏ hai ca kiểm hàm khớp tên, thêm tám ca kiểm hành vi thật, tổng 64
ca. quet_ho và quan_sat_kho nhận tham số bay_gio để tiêm THỜI GIAN GIẢ, nhờ
vậy kiểm được cả mốc "ngay lập tức" lẫn mốc "sau năm phút" mà không phải chờ
thật. Nhãn số ca lấy từ chính danh sách fixture, hết lệch khi thêm bớt.

Không đụng tới X3, nên trần 11.500 ký tự vẫn còn nguyên khoảng trống ít ỏi cũ;
khuyến nghị của vòng đánh giá 21 về việc rút gọn hoặc tách phần kỹ thuật của
X3 giữ nguyên cho vòng sau.

## Vòng 21: v21 sang v22, đóng lớp thực thi (vòng đánh giá 20, 9,5/10, CORE và đặc tả EMAIL khóa được)

Bốn việc lớp thực thi, không kiến trúc mới:

1. @NHIP.TRANGTHAI có schema BẮT BUỘC tối thiểu: {"status": "OK"|"FAILED",
   "mailbox", "last_success_utc"}; chỉ lần quét thành công mới cập nhật
   last_success_utc; file thiếu, sai định dạng hay lần cuối FAILED đều coi
   là DỮ LIỆU CŨ.
2. Khóa digest đã gửi có nơi lưu BỀN: X0 C9 thêm @NHIP.DAUGUI, chỉ ghi khóa
   SAU khi kênh báo xác nhận gửi thành công, máy khởi động lại vẫn nhớ.
3. kiem_van_hanh v17 có chế độ --ho <đường dẫn hay họ file>: quét đúng MỘT
   họ tài liệu phục vụ X5 KIỂM BẢN, kết quả HỢP NHẤT vào cache thay vì ghi
   đè cache toàn kho, mốc ổn định toàn kho giữ nguyên. Hai fixture mới cho
   khop_ho (chế độ đường dẫn, chế độ họ tên), tổng 58 ca.
4. Câu chữ: "đang chờ AI" trong khuôn digest đổi thành "đang chờ BÊN NÀO"
   để khỏi hiểu nhầm là chờ hệ AI. X3 chạm trần nên RÚT GỌN câu cũ thay vì
   nâng trần (11.488/11.500 ký tự), đúng khuyến nghị. Luật then chốt lên 37.

## Vòng 20: v20 sang v21, vá hẹp digest và nguồn thời gian quét (vòng đánh giá 19, 9,3/10)

Ba điểm logic cộng một lỗi chữ, không kiến trúc mới:

1. Khuôn digest đủ thông tin hành động: dòng đầu đếm CẦN TÔI và CHỜ ĐỐI TÁC
   QUÁ HẠN; mỗi thư CẦN TÔI đủ mã luồng, người gửi, tiêu đề, ý chính, tôi
   cần làm gì, hạn, file; mục CHỜ ĐỐI TÁC nêu đang chờ ai, chờ việc gì, từ
   ngày nào; THEO DÕI riêng và ngắn; cuối tin giờ quét thật, giờ tạo tin,
   tình trạng DỮ LIỆU MỚI hay CŨ.
2. Cảnh báo dữ liệu cũ hết bị chống-lặp nuốt: chỉ GIÁ TRỊ giờ trình bày nằm
   ngoài hash; tình trạng MỚI/CŨ, tập việc quá hạn và thay đổi trạng thái
   thư PHẢI nằm trong hash, nên chuyển MỚI sang CŨ gửi cảnh báo đúng MỘT
   lần dù không có mail mới.
3. Hai khái niệm được định nghĩa tất định: X0 C9 thêm @NHIP.TRANGTHAI trỏ
   tới nguồn chứa thời điểm quét thành công cuối (X3 đọc giờ quét thật từ
   đây); X5 "đã cũ" = họ tài liệu CHƯA được quét trong PHIÊN hiện tại, lần
   đầu chạm trong phiên thì tự quét đúng họ.
4. Lỗi chữ: ghi chú đổi mới hết nói "Mười vòng". kiem_tra_bo v17 khai rõ
   phạm vi phép kiểm 12 (kiểm luật có mặt, không thay được nghiệm thu hành
   vi ở bộ email thật); benchmark gọi rõ "giảm 70%" là số của view mẫu rỗng,
   kèm mức tối đa runtime theo trần đã enforce. Luật then chốt lên 35.

## Vòng 19: v19 sang v20, bản vá nhỏ khóa EMAIL (vòng đánh giá 18, 9,2/10, CORE khóa được)

Đúng phạm vi bản vá được đề nghị, không kiến trúc mới:

1. Digest có KHUÔN BẮT BUỘC trong X3 mục 6, đúng thứ tự: đếm thư cần tôi xử
   lý và việc quá hạn · từng thư kèm ý chính, TÔI CẦN LÀM GÌ, hạn, file ·
   theo dõi để riêng · cuối tin là giờ quét THẬT với giờ tạo bản tin và cảnh
   báo dữ liệu cũ. Hệ đúng dữ liệu giờ bắt buộc phải NÓI cũng dễ đọc.
2. X0 C9 thêm @NHIP.TENGOI (EMAIL): tên, cách xưng hô, bí danh người dùng để
   máy nhận "thư chào đích danh mình"; bộ email TỰ lấy từ tên tài khoản khi
   cài, chỉ hỏi khi không lấy được. X3 trỏ về tham số này.
3. Đồng bộ bản hiện hành hết phụ thuộc người gọi: X5 KIỂM BẢN thêm luật
   trước khi SỬA hay DÙNG một họ tài liệu mà lần quan sát đã cũ thì tự quét
   đúng HỌ đó (không cả kho), kết quả rõ thì tự đồng bộ vai, không hỏi.
4. Mail thường lệ hết bị hỏi ngôn ngữ giọng điệu: X9 mặc định ngầm hiểu
   (ngôn ngữ theo luồng thư hay người nhận, giọng chuyên nghiệp ngắn gọn, từ
   cấm X1), chỉ hỏi khi có hai lựa chọn khác nhau đáng kể.
5. Trần token khép nốt: kiem_van_hanh v16 áp trần runtime 2.400 ký tự cho
   X0_INDEX (BANG_DIEU_KHIEN đã có 4.200 từ v19); X3 nâng trần 11.500 vì
   khuôn digest và @NHIP.TENGOI; sửa hai lỗi trình bày: X9 hết ghi "bảy sổ
   rỗng" (đúng cấu trúc năm sổ lõi cộng sổ phụ theo vai trò), ngày ở đầu
   INSTRUCTION và ghi chú đổi mới về đúng 20260824. Luật then chốt lên 32.

## Vòng 18: v18 sang v19, bảy điểm để khóa bản (vòng đánh giá 17, 8,3/10 "có thể pilot")

Đúng yêu cầu "chỉ tập trung bảy điểm, không thêm kiến trúc mới":

1. Profile EMAIL hết mâu thuẫn với AUTOMATED: INSTRUCTION (lên v11) liệt kê đủ
   REGULATED, PARALLEL, AUTOMATED, EMAIL và khai luật "một mục phục vụ nhiều
   profile, bật MỘT trong số đó là phải đọc"; X0 C9 đổi nhãn thành "AUTOMATED
   và EMAIL", @NHIP.HOPTHU và @NHIP.TAIKHOAN gắn nhãn (EMAIL) từng dòng.
2. CHỜ TÔI lên NĂM điều kiện: thêm "yêu cầu đọc từ phần người gửi vừa viết
   (cắt lịch sử trích dẫn, chữ ký, câu xã giao please find/see)" và "yêu cầu
   nhắm vào mình, thư chào đích danh người khác không tính dù mình ở To".
   Đây là hai lỗi đã lộ ở hệ email thật (ca PIP breakdown).
3. Khép kín bộ quan sát: X4 thêm câu tắt thứ năm "đồng bộ quan sát": kết quả
   ổn định không xung đột thì TỰ ghi vai HIỆN HÀNH/CŨ vào TAILIEU mức A; chỉ
   hỏi khi XUNG ĐỘT hay KHÔNG XÁC ĐỊNH. RA_SOAT thuần vẫn chỉ báo cáo.
4. BẤT BIẾN viết rõ hai nghĩa: NỘI DUNG (byte) file đã gửi không sửa đè;
   TRẠNG THÁI nghiệp vụ của dòng TAILIEU vẫn tiến lên khi có bằng chứng.
5. X9: mail thường lệ đầu tiên chạy với cấu hình tối thiểu (người nhận và
   phạm vi, ngôn ngữ, giọng, từ cấm mặc định), không phải trả lời cả nhóm B;
   số liệu hay cam kết xuất hiện là dừng hỏi đủ.
6. Digest chống lặp bằng KHÓA NỘI DUNG (mốc mail cuối + hash phần nghiệp vụ,
   giờ trình bày không vào hash): sáng gửi rồi, chiều có mail mới thì khóa
   đổi, không chặn oan; tên file digest mang ngày giờ, không ghi đè.
7. Đóng gói tự kiểm độc lập: ZIP chứa sẵn bản _GOP; kiem_tra_bo v15 thêm
   --gop <file> và mặc định im lặng với chi tiết fixture (LECH của tình
   huống âm là chủ ý), --verbose xem đủ. Trần X3 nâng 10.500 lên 11.000 ký
   tự vì mục 6 dày thêm hai luật. kiem_van_hanh v15 áp trần runtime 4.200 ký
   tự cho BANG_DIEU_KHIEN. DOC_TRUOC nói rõ hệ sổ: NĂM sổ lõi, PLANNING mức
   C, THU theo profile EMAIL, hai view máy sinh, hệ lõi không phình.

## Vòng 17: v17 sang v18, vòng đời staging và đối chiếu index chính xác (vòng đánh giá 16)

Vòng đánh giá 16 chấm 9,6/10, tuyên bố CORE/LITE đủ chốt; EMAIL còn một mâu
thuẫn vòng đời staging và hai PASS giả. Năm điểm, sửa hết:

1. Mâu thuẫn dọn-staging với 12j giải bằng MANIFEST DỌN _so\_thu_don_staging.json
   (máy sinh, ghi TRƯỚC khi xóa): mỗi khóa một mục purged_at, eml_final_path,
   attachment_final_paths, sha256. 12j giờ hiểu vòng đời: PREPARED chưa
   COMMITTED thì staging bắt buộc còn; COMMITTED đã dọn có manifest hợp lệ thì
   staging vắng là PASS; vắng mà thiếu một trong hai điều là lệch.
2. Khe ../_so/_thu_staging đóng: containment bằng normpath thay cho lstrip,
   cấm tuyệt đối, cấm ".." sau chuẩn hóa; lúc rà 12j còn resolve() đường dẫn
   thật và bắt buộc nằm dưới _thu_staging, chặn cả symlink thoát ra.
3. Tên đính kèm phải là BASENAME thuần (không /, \, ".."), file sau resolve()
   phải còn trong staging: ten "../../../secret.txt" hết đường lách.
4. Index đối chiếu CHÍNH XÁC: tập mục index bằng ĐÚNG tập "khoa|operation_id"
   của các mail đã COMMITTED (thừa mục ngoài payload cũng lệch); sổ và mã dòng
   trong index phải khớp thao tác payload; 12l so mã dòng theo ĐÚNG Ô bảng
   (V-1 không ăn theo V-10), mục index có "hash" thì đối chiếu thêm sha256
   nội dung dòng.
5. Payload đủ dữ liệu phục hồi thật: bắt buộc metadata nguồn conv_id,
   nguoi_gui, thoi_diem UTC, tieu_de và eml_sha256; .eml hay body không được
   rỗng và phải khớp eml_sha256; thư mục staging tên sha256(khóa), mỗi mail
   một thư mục, hai mail hết đường dùng chung.

Fixture email lên 40 kịch bản, tổng 56 ca (có ca PASS chủ động: staging đã dọn
đúng luật); luật then chốt lên 28. CORE không đổi.

## Vòng 16: v16 sang v17, kiểm dữ liệu thật và đóng khe ghi đồng thời (vòng đánh giá 15)

Vòng đánh giá 15 chấm 9,5/10: CORE đủ mức chốt, EMAIL là release candidate cần
kiểm staging/index thật và đóng khe "ghi sổ xong nhưng chưa ghi index". Năm điểm:

1. kiem_payload kiểm DỮ LIỆU chứ không chỉ tên trường: staging phải là đường
   dẫn tương đối nằm BÊN TRONG _so\_thu_staging (chặn tuyệt đối, chặn chấm
   chấm thoát ra); mỗi thao tác đủ operation_id (chuỗi, DUY NHẤT trong một
   mail), sổ đích thuộc THU VIEC DUKIEN TAILIEU QUYETDINH, mã dòng, nội dung
   dòng; đính kèm khai đủ ten, sha256, bytes. Thiếu @NHIP.HOPTHU khi EMAIL đã
   chạy: 12e LỆCH cấu hình, hết BỎ QUA.
2. Khe sinh dòng đôi đóng ở X3 bước 2: ĐỐI CHIẾU trước ghi sau. Chưa có trong
   index thì TÌM mã dòng trong sổ đích trước; thấy rồi (lần trước chết sau khi
   ghi sổ, trước khi ghi index) thì CHỈ bổ sung index; chưa thấy mới ghi dòng,
   đọc lại xác minh, rồi bổ sung index.
3. Ba phép máy mới cộng ba dòng X4 (29 tới 31): 12j staging thật trên đĩa
   (thư mục tồn tại, có .eml hay body, từng đính kèm đúng sha256 và byte);
   12k index đủ hai chiều (thao tác COMMITTED phải có trong index, index không
   trỏ mail không có trong nhật ký); 12l index trỏ mã dòng CÓ THẬT trong sổ.
4. Khóa một dạng: trường "khoa" DUY NHẤT, gặp "msgId" kiểu cũ là dòng hỏng chờ
   một lượt migration riêng, không đọc lẫn hai dạng. Khóa fallback serialize
   CỐ ĐỊNH: FB-<sha256(convId + thời điểm UTC + tiêu đề chuẩn hóa + 200 ký tự
   đầu thân)>.
5. Staging hết tăng vô hạn: DỌN STAGING là việc mức A khi đủ BỐN điều (đã
   COMMITTED, đích và sha xác minh, .eml bằng chứng đã chuyển 04_Trao_doi,
   qua thời gian đệm X0 C9 @NHIP.DEMSTAGING mặc định 30 ngày).

Fixture email lên 29 kịch bản, tổng 45 ca, luật then chốt lên 24. Không đụng
INSTRUCTION, X1, X2; X0 chỉ thêm @NHIP.DEMSTAGING.

## Vòng 15: v15 sang v16, chốt lớp bảo đảm dữ liệu email theo vòng đánh giá 14

Vòng đánh giá 14 chấm 9,4/10: CORE gần mức chốt, EMAIL còn hở lớp phục hồi dữ
liệu. Năm điểm, sửa hết:

1. Payload phục hồi THẬT: X3 mục 6 bước 1 thành "STAGING trước, PREPARED sau".
   Nguyên văn thư (.eml hay body đầy đủ) cùng mọi đính kèm lưu vào
   `_so\_thu_staging\<khóa an toàn>\` TRƯỚC khi append PREPARED; payload mang
   đường dẫn staging cộng danh sách THAO TÁC ghi sổ đã chuẩn hóa (operation_id,
   sổ đích, nội dung dòng). Tên với dung lượng đính kèm suông không còn được
   tính là payload phục hồi; staging hụt thì không được append PREPARED.
2. `source_msg_id` có nơi lưu thật: index máy sinh `_so\_thu_ap_dung.json`,
   mỗi thao tác đã áp một dòng "source_msg_id + operation_id" trỏ "sổ + mã
   dòng". Sổ người đọc không phải mang thêm cột khóa máy; mất index thì dựng
   lại bằng đối chiếu payload với sổ. Đăng ký ở X5 mục 4 cùng _thu_staging.
3. Schema sự kiện cứng: mỗi dòng nhật ký phải là JSON object có "ev" chỉ nhận
   PREPARED hoặc COMMITTED, "khoa" là CHUỖI, "hop_thu" bắt buộc ở cả hai loại;
   mỗi mail đúng HAI sự kiện, PREPARED đứng TRƯỚC COMMITTED; lượt phục hồi
   không append PREPARED mới. Khắc ở X3 mục 6, máy giữ ở kiem_van_hanh.
4. kiem_van_hanh v12: parse theo TỪNG KHÓA giữ thứ tự và số lần xuất hiện.
   Bảy PASS giả bị đóng: PREPARED thiếu payload nhưng đã COMMITTED (12h),
   COMMITTED mồ côi, COMMITTED đứng trước PREPARED, sự kiện lặp (12g),
   ev gõ sai kiểu "TYPO" thành dòng hỏng chứ không thành COMMITTED (12b),
   sự kiện thiếu hop_thu thành dòng hỏng (12b), hai dòng THU cùng
   Conversation-ID (12i), registry dạng `{}` (12d). Hai ca crash hết crash:
   registry là danh sách chứa object, msgId là array; đều thành LỆCH.
   Registry bắt buộc là DANH SÁCH CHUỖI khóa.
5. kiem_tra_bo v12: fixture email từ 9 lên 18 kịch bản, tổng 34 ca, vẫn gọi
   toàn bộ kiem_email(); danh mục luật then chốt từ 15 lên 20 (thêm staging
   trước PREPARED, index áp thao tác, mô hình hai sự kiện, Conversation-ID
   duy nhất, registry danh sách chuỗi).

Không đụng INSTRUCTION, X0, X1, X2, X4, X9; CORE giữ nguyên như bản 9,7 điểm.

## Vòng 14: v14 sang v15, làm lại máy kiểm email theo vòng đánh giá 13

```
1  Nhật ký email nâng thành NHẬT KÝ SỰ KIỆN: PREPARED mang payload phục hồi đủ
   dựng lại THU, VIEC, TAILIEU và tải lại đính kèm mà không đọc lại hộp thư;
   ghi sổ idempotent theo source_msg_id; COMMITTED khi sổ và đính kèm đủ;
   registry CHỈ dựng từ COMMITTED. Hết luôn hai câu mâu thuẫn trong X3: khóa
   fallback chỉ còn một dạng mạnh, đính kèm nằm gọn trong bước 2 trước COMMITTED
2  kiem_email viết lại và bị fixture gọi CẢ HÀM trên 9 kịch bản: bộ sạch PASS
   hết; mất registry, mất nhật ký, dòng rác, dòng "42", lượt dở dang, registry
   thừa mã, hộp thư giả kiểu substring, khóa fallback không dấu @ trùng hai
   luồng: TỪNG CA đều phải bị bắt, không ca nào crash
3  X4 dòng rà email 24 tới 28 viết lại theo mô hình mới
4  Fixture tổng lên 25 ca, luật then chốt lên 15
```

## Vòng 13: v13 sang v14, vá vòng đánh giá 12

```
1  BỎ lọc tiền tố "9": 98_Assets và 99_Goc là vùng nghiệp vụ phải quét (chính X4
   đòi kiểm sha 99_Goc), chỉ loại đích danh 99_Archive; công ty muốn loại thêm
   thì khai _quan_sat_bo.txt. Fixture chứng minh cả ba nhánh
2  Benchmark tách đúng route: CUA_VAO thường chỉ X3 mục 1 tới 5, CUA_VAO EMAIL
   mới cộng mục 6, hết cách trình bày gây hiểu nạp email hai lần
3  Email commit/recovery: THỨ TỰ GHI AN TOÀN nhật ký trước, registry sau, THU
   cuối; nhật ký là nguồn sự thật, thiếu đâu bổ sung đó, không nạp lại từ hộp
   thư; dòng trùng do chạy lại vô hại. Fallback thiếu Message-ID nâng thành
   (Conversation-ID, thời điểm tới giây, sha256 tiêu đề + 200 ký tự đầu thân)
4  Máy rà email: kiem_van_hanh phép 12 (registry đủ so nhật ký, Message-ID cuối
   không đứng ở hai luồng THU, mail thuộc đúng hộp khai báo), X4 thêm dòng rà
   24 tới 26; nhật ký nạp thêm trường hop_thu để rà được sai hộp
5  Fixture lên 18 ca, luật then chốt lên 13
```

## Vòng 12: v12 sang v13, vá 2 lỗi vận hành vòng đánh giá 11

```
1  Dòng TAILIEU trỏ THƯ MỤC (kết thúc bằng dấu chéo) bao phủ mọi file con: hồ sơ
   nhiều tài liệu hết bị đề xuất _INBOX thừa liên tục; luật khớp: trùng đường
   dẫn file, hoặc nằm trong thư mục sổ đã trỏ
2  Bỏ loại theo đuôi trên toàn kho: script và config NGHIỆP VỤ ngoài 00_Index
   được quan sát như tài liệu thường; chỉ loại vùng hệ thống, rác thật, và danh
   sách đường dẫn công ty tự khai ở _so/_quan_sat_bo.txt
3  Email: thêm nhật ký nạp APPEND-ONLY _thu_nhat_ky.ndjson làm nguồn dựng lại
   registry; mất cả hai thì lần quét đầu chỉ xuất danh sách ứng viên chờ duyệt,
   không tự nạp
4  Fixture lên 16 ca (bao phủ thư mục, script nghiệp vụ được quét, schema THU);
   phép 12 giữ 11 luật; benchmark sinh lại với số hiện tại
```

## Vòng 11: v11 sang v12, vá 3 lỗi thực thi vòng đánh giá 10 và nâng spec EMAIL

```
1  Luật 5 phút ENFORCE THẬT: cache non hơn 5 phút không được dùng làm bằng chứng
   ổn định (trước chỉ in cảnh báo nhưng vẫn công nhận HIỆN HÀNH)
2  Bộ quan sát loại hẳn 00_Index, file .py .ps1 .bat .json khỏi vùng quét nghiệp
   vụ; hết cảnh đề xuất đưa chính file luật và script vào _INBOX
3  Chuẩn hóa họ đổi cụm phân cách về MỘT dấu "_" thay vì xóa sạch: AB_C_v01 và
   A_BC_v02 là hai họ khác nhau, (v3) -v03 _v02 vẫn về một họ
4  Spec EMAIL nâng theo góp ý: THU thêm cột Conversation-ID làm khóa luồng ·
   registry _thu_da_nap.json giữ TẬP mọi Message-ID đã nạp, quét lại toàn hộp
   không nạp trùng · CHỜ ĐỐI TÁC cũng cần bằng chứng mong phản hồi, thư thông
   báo không treo chờ ai · digest trùng ngày chỉ chặn khi lần trước THÀNH CÔNG
5  Fixture lên 14 ca (thêm: AB_C không trộn A_BC, 00_Index và script bị loại);
   phép 12 giữ 9 luật nghiệp vụ
6  Ngoài bundle: bộ email SẢN XUẤT của công ty mẫu đã được vá cùng ngày theo
   cùng spec (cửa sổ 24h theo giờ chạy, CHỜ TÔI ba điều kiện, một công ty một
   hộp thư, Message-ID vào dữ liệu quét, chặn gửi digest cũ, token ra ngoài kho)
```

## Vòng 10: v10 sang v11, vá vòng đánh giá 9 và thêm profile EMAIL

```
1  Ngoại lệ "thêm lệnh cấm là B" giờ nằm ở CẢ BA nơi cùng câu chữ: X0 C11,
   INSTRUCTION mục 5 (lên v10), X5 mục 1; hết chuyện AI đọc file nào ra mức đó
2  Họ tài liệu CHUẨN HÓA bỏ mọi ký tự phân cách: (v3), -v03, _v02 về cùng một
   họ; fixture kiểm cả tính cùng-họ chứ không chỉ lấy được số, hết PASS giả
3  Bộ quan sát quét MỌI file thường (kmz, kml, csv, dwg, eml, zip...), chỉ loại
   danh sách đuôi rác; hash đủ mọi cỡ file, file lớn chỉ cảnh báo chậm
4  Hai lần quét cách nhau dưới 5 phút tính là một lần quan sát, giữ mốc cũ
5  Phép 3c đọc đúng CỘT Ghi lần, 3d chỉ nhận plan có trạng thái ĐÃ GHI
6  Cột Ở đâu phân biệt trỏ FILE (tới tên file, có sha) với trỏ BỘ HỒ SƠ (kết
   thúc bằng dấu chéo, không sha)
7  Profile EMAIL (X0 C0, X3 mục 6, sổ THU.md): Message-ID làm khóa chống trùng,
   trạng thái CHỜ TÔI (đủ ba điều kiện: không phải thư mình, mình ở To, có yêu
   cầu thật) · CHỜ ĐỐI TÁC · THEO DÕI · ĐÃ ĐÓNG · BỎ QUA (nói một lần, không
   nhắc lại), mọi tài khoản người dùng khai @NHIP.TAIKHOAN, đính kèm liên kết
   bằng sha256, thư gửi kèm file thành ảnh chụp ĐÃ GỬI DUYỆT, digest chống lặp
   theo ngày chạy và cấm gửi lại bản cũ khi sinh lỗi, token để ngoài kho đồng
   bộ. Chỉ nạp khi quét mail, không tăng thuế bộ lõi. Nguyên tắc gốc, học từ
   ca thật hai công ty chung một máy: MỘT CÔNG TY MỘT HỘP THƯ QUÉT
   (@NHIP.HOPTHU), hộp thư công ty khác trên cùng máy không được vào pipeline
```

## Vòng 9: v09 sang v10, code làm đúng điều tài liệu tuyên bố

```
1  Gỡ mâu thuẫn "gửi duyệt": đúng FILE đã gửi là ẢNH CHỤP bằng chứng không sửa
   đè, việc tiếp tục trên vN+1, plan không đóng; ĐÃ PHÁT HÀNH, NỘP, KÝ, CẤP là
   mốc chính thức theo luật cốt lõi 3. X2 với X5 hết đá nhau
2  Luật "ổn định qua hai lần quan sát" CHẠY THẬT: cache _so/_quan_sat_truoc.json
   (máy sinh), lần quét đầu không công nhận gì, lần hai cùng nội dung mới nhận
3  sha256 thật thay cho dung lượng file; file quá 200MB ghi chú riêng
4  File không có vN chọn theo mtime sau khi ổn định; mtime không phân định được
   thì KHÔNG XÁC ĐỊNH, không bao giờ chọn theo thứ tự tên
5  File mới độc lập (chưa có bản cũ) vẫn được đề xuất _INBOX
6  Khóa nhận dạng họ tài liệu = thư mục tương đối + họ tên: hai dự án trùng tên
   file không lẫn nhau; đối chiếu sổ theo đường dẫn tương đối
7  Fixture nâng lên 11 ca, phủ đúng 6 ca vòng 8 yêu cầu, chạy trên hàm thật kể
   cả quét kho hai lượt trong thư mục tạm
```

Lượt TEAM AGENT nội bộ trên v10: 15 agent, ba hướng (kiểm toán nhất quán toàn bộ
luật, kiểm thử đối kháng chạy script thật, đóng vai giám đốc không rành kỹ thuật
diễn một tuần làm việc), mỗi phát hiện qua một agent phản biện cố bẻ. 12 phát
hiện, 4 bị bẻ gãy có bằng chứng, 8 đứng vững và ĐÃ VÁ HẾT trong chính bản này:

```
1  Mâu thuẫn X1 với nhóm khóa C11 về thêm giá trị cấm: khắc ngoại lệ tường minh,
   THÊM lệnh cấm (siết chặt) là mức B, GỠ hay NỚI là mức C kèm QUYETDINH
2  X4 hứa quá khả năng script: thêm phép 3c (lượt XONG phải để dấu mã G ở ít
   nhất một sổ) và 3d (lượt mức C phải khớp plan), phủ đủ dòng rà 19 và 23
3  Tuple bất biến của script thiếu ĐÃ DUYỆT NỘI BỘ và TRẢ HỒ SƠ: đã thêm, kèm
   ca fixture giữ code khớp luật
4  Cache quan sát hỏng làm crash: tự phục hồi, coi như lần quét đầu
5  Mã G định dạng cũ (không cửa) cướp watermark: loại khỏi watermark, báo riêng
   "cân nhắc di trú"
6  Regex vN sót dạng -v03 và (v03): đã nới, kèm hai ca fixture chống nhận nhầm
7  Phiên CHAT không có đường đọc sổ (mức CAO): X5 bước 6 quy định COWORK đồng bộ
   BANG_DIEU_KHIEN và X0_INDEX lên tài liệu Project mỗi lần sinh lại, bảng thêm
   khối "Tài liệu đang hoạt động"; CHAT đọc bản Project kèm nhãn ngày
8  Kịch bản gửi gấp dồn ma sát: X9 gom mọi câu thiếu của cùng việc vào một lượt
   hỏi, bảng điều khiển nhắc mục C12 còn thiếu chặn phát hành, X2 cho in gọn
   dòng ĐẠT nhưng cấm bỏ dòng
```

Tám vòng trước: v02 theo phản biện độc lập trên v01; v03 vá 5 điểm vòng 2; v04 vá 10
mục stress-test; v05 vá vòng 3 thêm test hồi quy; v06 tối ưu token và máy hóa;
v07 sửa regression vòng 5; v08 vá 3 điểm vòng 6 (9,1/10); v09 thêm state engine
quan sát file và vòng duyệt nhiều bước theo vòng 7 (8,9/10 vì thiếu hai năng lực
nghiệp vụ này).

## Vòng 8: v08 sang v09, state engine quan sát file và vòng duyệt

Nguyên tắc mới, chữ của người đánh giá: "tự nhận bản hiện hành theo bằng chứng,
không tự nhận bản cuối theo sự im lặng". Không đụng INSTRUCTION (thuế thường trực
giữ nguyên), chỉ sửa X3, X5, TAILIEU và hai script.

```
1  TAILIEU thêm ba cột: VAI PHIÊN BẢN (HIỆN HÀNH, CŨ, XUNG ĐỘT, KHÔNG XÁC ĐỊNH)
   · QUAN SÁT LÚC · CĂN CỨ TRẠNG THÁI. Vai là quan sát của máy, đổi tự do theo
   bằng chứng quét (mức A); trạng thái nghiệp vụ chỉ đổi khi có căn cứ
2  Trạng thái nghiệp vụ tách vòng duyệt khỏi phát hành: NHÁP · CHỜ DUYỆT NỘI BỘ
   · ĐÃ GỬI DUYỆT · ĐÃ DUYỆT NỘI BỘ · ĐÃ PHÁT HÀNH · ĐÃ NỘP · TRẢ HỒ SƠ · ĐÃ
   CẤP · ĐÃ KÝ. Bản gửi sếp hay đối tác góp ý SỬA TIẾP ĐƯỢC; bất biến chỉ áp
   cho ĐÃ PHÁT HÀNH, ĐÃ NỘP, ĐÃ KÝ, ĐÃ CẤP
3  SUY BẢN HIỆN HÀNH (X5 mục 4): tám quy tắc, gồm bỏ file tạm, vN cao hơn là
   ứng viên, cùng vN khác hash là XUNG ĐỘT cấm tự chọn, và im lặng KHÔNG BAO GIỜ
   suy ra đã duyệt, đã gửi hay đã xong
4  GHI MỐC (X5 mục 1): một plan C bao trùm cả chu kỳ soạn, gửi sếp, sửa, gửi đối
   tác, trình ký; mỗi lần gửi là một dòng NHATKY + TAILIEU cập nhật, plan KHÔNG
   đóng; chỉ xin gật lại khi đổi mục tiêu, người nhận, cam kết, nguồn, số chưa
   có sổ, loại phát hành hay hành động khó phục hồi
5  X3: hành động người dùng ĐÃ LÀM là sự kiện đầu vào, AI kiểm chứng và ghi mức
   A hồi tố, không xin phép; thiếu thông tin chưa ảnh hưởng bước tiếp thì ghi
   CHƯA XÁC NHẬN, không hỏi
6  kiem_van_hanh v4: truyền thêm <gốc kho> thì đối chiếu TAILIEU với file thật
   (mất file, sha lệch, bản bất biến bị sửa tại chỗ, họ tài liệu cùng vN khác
   nhau) và ĐỀ XUẤT sự kiện _INBOX cho bản hiện hành chưa vào sổ. Chỉ báo cáo
7  kiem_tra_bo v4: fixture hồi quy 4 ca cho suy bản hiện hành (import thẳng hàm
   thật), phép kiểm 12 giữ 6 luật nghiệp vụ then chốt khỏi rơi khi rút gọn,
   phép 2b chặn metadata version trôi giữa BENCHMARK và DOC_TRUOC
```

## Vòng 7: v07 sang v08, vá 3 điểm vòng đánh giá 6

```
1  kiem_tra_bo v3: GHICHU_DOI_MOI_v* (pattern, đúng một file), BENCHMARK_TOKEN.md
   và chính hai script vào danh mục bắt buộc; tất cả phải có mặt VÀ nằm nguyên
   văn trong _GOP. Script và GHICHU miễn kiểm ký tự cấm với tham chiếu chéo, vì
   script giữ danh sách ký tự cấm làm mẫu dò còn GHICHU trích nguyên văn vòng cũ
2  "Mới nhất" theo WATERMARK TỪNG CỬA: giữa các cửa của kho mây không có thứ tự
   thời gian tin được, nên kiem_van_hanh v3 chỉ so BANG_DIEU_KHIEN với watermark
   của CHÍNH cửa sinh ra nó; cửa khác có lượt ngày mới hơn thì in LƯU Ý, không
   phán LỆCH. BANG_DIEU_KHIEN header thêm dòng watermark từng cửa (X5 mục 3
   bước 6)
3  Hạ lời "khóa thật" xuống đúng bản chất: ĐỊNH DANH LƯỢT (<CỬA>.<giờ phút>.<hậu
   tố ngẫu nhiên>) cộng QUY TẮC HÒA GIẢI XUNG ĐỘT tất định; nói thẳng đây là hòa
   giải sau xung đột, không phải khóa nguyên tử, và PARALLEL phải tuyên bố giới
   hạn đó khi quảng bá
```

## Vòng 6: v06 sang v07, sửa regression theo vòng đánh giá 5

```
1  kiem_van_hanh.py v2: parse đúng CỘT của dòng dữ liệu bảng thay vì đếm chuỗi
   toàn văn (hết báo sai "ĐANG GHI" từ câu hướng dẫn, hết đếm mã G nhắc lại trong
   cột Làm gì); mã mới nhất xếp theo ngày và số, không theo vị trí; X0 rev 0 trả
   BỎ QUA "chưa cài đặt" thay vì LỆCH; schema kiểm cả từng dòng dữ liệu; thêm mã
   Q và P vào kiểm trùng
2  Tham chiếu X5 mục 2 sang mục 3 ở X4, X9, NHATKY mẫu (regression khi chuyển nội
   dung từ INSTRUCTION về X5). kiem_tra_bo thêm phép kiểm 10: mọi tham chiếu
   "X<k> mục <n>" và "INSTRUCTION mục <n>" phải trỏ tới mục có thật, để loại lỗi
   này khỏi tái diễn
3  kiem_tra_bo v2: thiếu bản gộp _GOP là FAIL, chỉ bỏ qua khi truyền cờ
   --skip-gop tường minh; hết chuyện "PASS hết" mà một phép bị âm thầm bỏ qua
4  X9 thống nhất: ba câu bắt buộc cộng một câu profile; _so là bảy sổ cộng một
   view X0_INDEX
5  Schema DUKIEN CỐ ĐỊNH mọi profile: LITE ghi "không áp dụng" ở ô Mức nguồn,
   khỏi migration khi bật REGULATED sau
6  Mã đồng thời cùng một cửa: khóa thật là cặp (mã G, định danh phiên ghi ở cột
   Phiên), mã G chỉ là số hiển thị; quy tắc phục hồi tất định "dòng nằm sau đổi
   mã"; mã chỉ điền vào các sổ SAU khi đứng vững ở NHATKY nên trùng bị giam trong
   NHATKY; nói thẳng file thường không có khóa nguyên tử, PARALLEL khuyến nghị
   mỗi cửa một phiên ghi một thời điểm
7  Benchmark sửa lời: "giảm 71% theo benchmark tĩnh, chờ số phiên thật", không
   tuyên bố kết quả runtime khi cột phiên thật còn trống
```

## Vòng 5: v05 sang v06, tối ưu token và máy hóa

```
1  INSTRUCTION rút từ 15,4K ký tự xuống dưới 8K (xấp xỉ 2.600 token, trước xấp xỉ
   5.100): chỉ giữ luật gốc, router, A B C rút gọn, 9 luật cốt lõi, trace, mở và
   đóng phiên. Toàn bộ danh mục mức chi tiết, thường lệ, nháp, kiểm bản, chốt,
   phiên không người dồn về X5 mục 1; router thêm dòng "mọi việc đổi trạng thái
   đọc X5 mục 1", tức chi tiết chỉ tốn token khi thật sự đổi trạng thái
2  X0_INDEX: view máy sinh của X0 (rev, kho, profile, dự án, vị trí mục, mục còn
   thiếu, trần 1.500 ký tự). Mở phiên đọc view này thay vì mở cả X0; giá trị đưa
   vào đầu ra vẫn phải đọc X0 đúng mục. Sinh lại mỗi khi rev tăng
3  PROFILE ở X0 C0: CORE luôn bật · REGULATED (mức nguồn, phát hành, hồ sơ nhà
   nước) · PARALLEL (nhiều cửa kho, kiểm trùng mã) · AUTOMATED (phiên không
   người, nhịp mail) · LITE = chỉ CORE. Khối luật gắn nhãn chỉ áp khi bật; công
   ty nhỏ không phải mang luật mình không dùng. X9 thêm câu 4 chọn profile
4  MÁY HÓA: thêm kiem_van_hanh.py chạy trên 00_Index của công ty thật, kiểm 8
   nhóm không cần suy luận (rev khớp, X0_INDEX đúng rev, NHATKY treo, mã G trùng,
   plan ĐÃ GHI thiếu mã, schema bảng, sổ vượt ngưỡng, bảng điều khiển cũ). X4
   route RA_SOAT chạy script trước, AI chỉ xử phần cần phán đoán
5  TOKEN BUDGET enforce bằng máy: kiem_tra_bo.py thêm phép kiểm 9, mỗi file có
   trần ký tự (INSTRUCTION 8K, X0_INDEX 1,5K, BANG_DIEU_KHIEN 1,2K...), vượt là
   FAIL không được đóng gói; in luôn thuế thường trực ước lượng
6  BENCHMARK_TOKEN.md: bảng đo bằng máy chi phí context theo từng loại yêu cầu,
   trước và sau v06, kèm cột trống để ghi số đo phiên chạy thật
```

Thuế thường trực đo được (ký tự / 3): xem BENCHMARK_TOKEN.md sinh kèm bộ.

## Vòng 4: v04 sang v05, vá theo vòng đánh giá 3

```
1  KHÓA GHI ĐỒNG THỜI: mã ghi đổi sang G-<YYYYMMDD>-<CỬA>-<NN>; hai phiên ở hai
   cửa kho khác nhau không thể trùng mã theo cấu tạo, miễn nhiễm trễ đồng bộ mây.
   Trong cùng một cửa: đọc NHATKY ngay trước khi cấp, cộng luật kiểm LẠI sau khi
   mở dòng: thấy trùng thì đổi mã dòng MÌNH kèm ghi chú. Rà 12 là lưới cuối.
   Không dùng file khóa vì kho mây đồng bộ trễ làm khóa không tin được
2  HÀNG RÀO NGUỒN CHỈ ĐỊNH (X0 C7): khai theo loại dữ kiện + phạm vi, không khai
   trần · khai hay đổi là sửa C7 nhóm khóa, mức C có QUYETDINH · mức D không bao
   giờ làm nguồn chỉ định cho đầu ra ngoài · hồ sơ nhà nước dùng nguồn dưới A
   phải in cảnh báo ở dòng kiểm 6 và người dùng xác nhận riêng dòng đó
3  NGOẠI LỆ CÀI ĐẶT rev 0 (INSTRUCTION mục 1, X0 C11, X9): điền giá trị ban đầu
   không coi là sửa nhóm khóa; C11 hiệu lực từ rev 1
4  Ngày sinh bảng vào thẳng mẫu hai dòng mở phiên: "· bảng <YYYY-MM-DD>"
5  QUYETDINH nói chính xác: không xóa, không sửa NỘI DUNG; dòng cũ chỉ được cập
   nhật hai ô quản trị Trạng thái và Thay bởi
6  Đặc tả tối thiểu chuyển Markdown sang CSV/SQLite (X5 mục 7): nguồn sự thật sau
   chuyển, mã vẫn cấp qua NHATKY Markdown mở dòng trước, phục hồi bằng "chốt sổ",
   backup trước lượt ghi đổi cấu trúc, BANG_DIEU_KHIEN sinh từ nguồn mới
7  BỘ TEST HỒI QUY kiem_tra_bo.py: tám phép kiểm chạy máy (đủ file, phiên bản
   khớp, tham chiếu X0 Cn tồn tại, ký tự cấm, số cột bảng, bộ trạng thái, dạng mã
   G, bản gộp _GOP khớp nguyên văn). Chạy sạch mới được đóng gói
```

Instruction lên v08; X0 X2 X5 lên v05; X9 lên v03; NHATKY và QUYETDINH mẫu sửa
lời; X1 X3 X4 và các sổ mẫu còn lại không đổi.

## Vòng 3: v03 sang v04, vá theo stress-test

```
H1  Thường lệ với số liệu ĐÃ CÓ SỔ: được phép xuất hiện, khi có thì bảng kiểm
    THƯỜNG LỆ thêm dòng 1 và 2; số chưa có sổ vẫn đá về C đầy đủ
H2  Nguồn chỉ định (X0 C7): dữ kiện lấy từ nguồn đã khai là nguồn thắng được dùng
    cho phạm vi tương ứng dù mức nguồn dưới tối thiểu, ghi kèm nguồn. Gỡ thế bí
    "hồ sơ nhà nước đòi mức A nhưng nguồn thẩm quyền hợp lệ là mail kỹ thuật mức B"
H3  Phiên không có người (INSTRUCTION mục 6): A làm và ghi; B và C chỉ chuẩn bị,
    xếp bảng chờ duyệt, mở VIEC hạn phiên sau; người dùng duyệt một lượt khi về
V1  Lô lẫn mức: tách theo mức, phần A đi trước, B gom một câu, C một plan
V2  Ranh giới nháp: tạo nháp là A, dọn nháp chưa vào sổ là B, xóa thứ đã vào sổ
    hay đã phát hành mới là C; note chỉ vào TAILIEU khi cần tìm lại về sau
V3  Nhóm khóa C6 thu về vai, tỷ lệ, lệnh cấm nêu tên; đầu mối liên hệ tách ra
    @BEN.DAUMOI, sửa là mức B
V4  Trong một lượt trả lời kiểm bản mới nhất MỘT lần cho mỗi file
V5  BANG_DIEU_KHIEN sinh lại ngay khi cũ hơn lượt ghi gần nhất hoặc chứa mốc đã
    qua, không đợi ngưỡng 7 ngày; hai dòng mở phiên luôn in ngày bảng
V6  Nhiều plan CHỜ CHỐT thì lệnh chốt phải nêu mã, không nêu thì hỏi kèm danh sách
#14 X5 mục 2: đọc NHATKY ngay trước khi cấp mã G, chặn hai phiên cấp trùng
```

Instruction lên v07; X0 X2 X5 lên v04; X1 X3 X4 X9 và bảy sổ mẫu không đổi.

## Vòng 2: v02 sang v03, vá 5 điểm

```
1  NGOẠI LỆ THƯỜNG LỆ trong mức C (INSTRUCTION mục 5, X2 mức THƯỜNG LỆ): trao đổi
   thường lệ ra ngoài không chứa số liệu mới, cam kết, điều khoản thì không mở plan,
   chỉ trình bản xem trước kèm bảng kiểm rút gọn 3·4·7·8, người dùng xác nhận gửi là
   chốt. Chọn đường ngoại lệ thay vì thêm mức C1 C2 để giữ hệ ba mức; xuất hiện số
   liệu hay cam kết giữa chừng thì tự nâng về C đầy đủ. X1 và X2 vẫn luôn được đọc
2  Plan C treo không chặn việc không liên quan (INSTRUCTION mục 2): treo hiện trên
   dòng trạng thái; chỉ bắt xử lý trước khi yêu cầu mới chạm cùng tài liệu, dữ kiện
   hay dòng sổ. Treo quá ngưỡng thì lên bàn làm việc
3  Định nghĩa BẢN KHÁC khi kiểm trước ghi (INSTRUCTION mục 5, X5 mục 2): có sha256
   trong TAILIEU thì so sha256; không có thì mtime VÀ dung lượng cùng đổi; đồng bộ
   mây đổi mtime suông không tính, nghi ngờ thì đối chiếu nội dung. Tránh báo động
   giả của kho mây
4  BANG_DIEU_KHIEN nói rõ (X1 mục 5, X5 mục 3): ĐƯỢC chứa số liệu dẫn xuất, tóm tắt,
   mã trỏ; CẤM chép nguyên dòng sổ và cấm dùng bảng làm căn cứ cập nhật sổ
5  Ngưỡng lưu trữ đa tiêu chí (X5 mục 7): 500 dòng HOẶC 1 MB HOẶC đọc tìm chậm rõ
   rệt, chạm một trong ba là xử lý
```

Instruction lên v06; X0 X1 X2 X5 lên v03; X3 X4 và bảy sổ mẫu không đổi, giữ v02.

## Vòng 1: v01 sang v02

Nguyên tắc chung được thêm thành
LUẬT SỐ KHÔNG: kiểm soát tỷ lệ với rủi ro; việc thường chạy nhanh, phê duyệt nặng
chỉ dành cho việc rủi ro; truy vết giữ nguyên đầy đủ ở mọi mức.

## Đổi lớn

```
1  BỎ CƠ CHẾ NƯỚNG. v01 chép giá trị X0 sang X1 tới X5 kèm dấu [@MÃ] và hệ x0_rev
   để giữ đồng bộ; thực chạy đã ghi nhận hai lần lệch nội dung dù cùng rev, và một
   lần đổi mục không nướng vẫn phải cập nhật header cả năm file. v02: X1 tới X5 là
   luật thuần, TRỎ về mục X0, đọc giá trị tại chỗ lúc dùng. Xóa được [@MÃ], x0_rev,
   luật nướng lại 3b, và các dòng rà lệch nướng.

2  MỨC TÁC ĐỘNG A B C (INSTRUCTION mục 5). Phân cấp PHÊ DUYỆT, không phân cấp truy
   vết: A tự làm tự ghi báo một dòng · B hỏi một câu rồi làm và ghi · C mới cần plan,
   gật, chốt. Danh mục C cứng cho mọi công ty (đầu ra rời công ty, bản đã phát hành,
   nhóm khóa, xóa và di chuyển hàng loạt). Công ty chỉ được NÂNG mức ở X0 C13, cấm hạ.
   Điều kiện an toàn của A B: kiểm bản mới nhất của file trước khi ghi, vì người dùng
   có thể sửa tay song song; lệch thì tự nâng mức.

3  CHỐT chỉ bắt buộc ở mức C. Lệnh trực tiếp ("sửa đi", "làm luôn") được định nghĩa
   là gật. Plan không chốt thì giữ CHỜ CHỐT, không thành plan treo giả.

4  TRACE ẨN (INSTRUCTION mục 8). Thân trả lời nói tiếng người; mã P G V D T dồn về
   một dòng Trace cuối. Người dùng chỉ cần biết bốn khái niệm: Việc, Tài liệu,
   Dữ kiện, Quyết định.

5  MỞ PHIÊN còn HAI dòng, bàn sạch còn một; "điểm danh" mới bung đủ. Giữ kiểm tra
   rev và mốc vì đó là hàng rào chống trôi rẻ nhất.
```

## Đổi vừa

```
6   Phân loại yêu cầu: "một loại duy nhất" đổi thành Ý ĐỊNH CHÍNH + hành động phụ,
    AI tự xâu chuỗi (mục 3). Mức tác động lấy theo bước cao nhất trong chuỗi.
7   Router thành mức đọc TỐI THIỂU + tự mở rộng khi câu trả lời phụ thuộc trạng
    thái (mục 4).
8   QUYETDINH thêm cột Mã, Trạng thái (HIỆN HÀNH, ĐÃ THAY), Thay bởi. X4 thêm dòng
    rà hai dòng HIỆN HÀNH cùng vấn đề.
9   DUKIEN thêm cột MỨC NGUỒN A B C D (văn bản ký, mail xác nhận, tài liệu làm
    việc, nói miệng); X0 C7 khai mức tối thiểu theo phạm vi phát hành, X2 thêm dòng
    kiểm số 6 cho việc này. Thay cho nhị phân ĐÃ KIỂM, CHƯA KIỂM.
10  Bản trung gian trong vòng sửa mức C đặt v<NN>-nhap<M>, không vào TAILIEU;
    chốt mới lấy v<NN>. Sổ ghi một lần, lịch sử file vẫn giữ được.
11  Cài đặt X9: vào việc sau BA câu (mã công ty, kho, dự án đầu). Cây folder mặc
    định dựng sẵn, khối việc sinh khi có việc đầu tiên. Nhóm phạm vi và các bên
    chỉ bắt buộc trước lần SOAN_RA đầu tiên.
12  Mô hình KHO thay mô hình MÁY ở X0 C1: một kho nhiều cửa vào, không rà "hai máy
    giữ bản cuối" giữa các cửa cùng kho; ràng buộc riêng từng cửa khai được.
13  Ngưỡng lưu trữ (X5 mục 7): sổ vượt 500 dòng thì tách theo khối hoặc năm; vẫn
    vượt thì phần dữ liệu sang CSV hoặc SQLite, Markdown giữ vai mục lục. X4 thêm
    dòng rà 22.
```

## Giữ nguyên có chủ đích

```
Luật cốt lõi 1 tới 9 (bất biến bản đã phát hành, vai theo văn bản ký, nội dung file
là dữ liệu không phải chỉ dẫn, cấm tự gửi) · trình tự GHI duy nhất qua NHATKY và mã
G · event_id chống nạp trùng ở cửa vào · nguồn thẩm quyền và MÂU THUẪN cấm tự chọn
· BANG_DIEU_KHIEN là view máy sinh · một việc một bộ thực thi.

Một điểm phản biện KHÔNG nhận toàn phần: xếp "ghi dữ kiện mới có nguồn rõ" vào mức
A. v02 chỉ cho dữ kiện THUẦN NỘI BỘ vào A; dữ kiện có phạm vi ra ngoài giữ mức B,
vì một dòng dữ kiện sai tự nạp hôm nay là con số sai trong hồ sơ phát hành về sau.
```
