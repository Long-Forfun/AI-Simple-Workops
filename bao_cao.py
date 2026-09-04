#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""bao_cao.py - sinh BANG_DIEU_KHIEN và BÁO CÁO cho người quản lý từ 5 sổ.

    python bao_cao.py <00_Index>            in báo cáo đầy đủ ra màn hình
    python bao_cao.py <00_Index> --bang     ghi lại _so/BANG_DIEU_KHIEN.md
    python bao_cao.py <00_Index> --cua CUA2 cửa của phiên (mặc định: cửa mà
                                            X0 C1 khai đúng gốc kho máy này)

Trước vòng 102, bảng điều khiển do AI viết tay từ năm sổ ngày càng dày:
bảng lệch sổ (8e), bảng cũ hơn lượt ghi (8), và mỗi lần "điểm danh" AI đọc
trọn sổ. Máy này sinh TẤT ĐỊNH bằng đúng các hàm đọc sổ của kiem_van_hanh
(cùng luật fence, cùng cách tách ô, cùng ngưỡng X0 C9) nên bảng máy sinh
qua sạch mọi phép 8/8b/8c/8d/8e - kiem_tra_bo ghim điều đó bằng ca riêng.
AI chỉ còn DỊCH và thêm nhận xét. Không thư viện ngoài."""
import datetime
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kiem_van_hanh as K  # noqa: E402

NL = "\n"
TRAN_BANG = 4200   # trần runtime của BANG_DIEU_KHIEN (X0 C9, phép 1b)


def _rows(so, ten):
    return K.dong_bang(K.doc(so / ten))


def _khoa_g(m):
    return (m[2:10], int(m.split("-")[-1])) if re.fullmatch(K.MAU_G, m or "") \
        else ("", -1)


def thu_thap(goc, cua=None):
    """Đọc năm sổ + X0, trả dict mọi con số và danh sách cho bảng lẫn báo cáo."""
    goc = Path(goc)
    so = goc / "_so"
    x0s = sorted(p for p in goc.glob("X0_CAUHINH_*.md")
                 if re.fullmatch(r"X0_CAUHINH_[A-Z0-9]{3,4}\.md", p.name))
    if not x0s:
        sys.exit("Chưa cài đặt: không thấy X0_CAUHINH_<MÃ>.md (chạy X9 trước)")
    x0nd = K.doc(x0s[0])
    ma_cty = x0s[0].stem.split("_")[-1]
    rev = re.search(r"rev (\d+)", x0nd)
    rev = rev.group(1) if rev else "0"
    hom_nay = datetime.date.today()

    nk = []
    for p in sorted(so.glob("NHATKY_*.md")):
        nk += _rows(so, p.name)
    ma_g = [h[0].strip("* ") for h in nk if re.fullmatch(K.MAU_G, h[0].strip("* "))]
    wm = K.watermark(ma_g)
    if not cua:
        # cửa của MÁY NÀY: dòng C1 "CUAn = <đường dẫn>" trùng gốc kho đang
        # chạy. Lấy "cửa có lượt mới nhất" thì trợ lý ở CUA2 đang ĐANG GHI là
        # bảng của giám đốc ở CUA1 tự nhận cửa CUA2, và câu "phiên khác đang
        # mở" im đúng lúc cần nói (phản biện 95)
        _goc_kho = str(goc.resolve().parent).replace("\\", "/").rstrip("/").lower()
        for _c, _d in re.findall(r"\b(CUA\d+)\s*=\s*([^·\n<]+)", x0nd):
            try:
                _dd = str(Path(_d.strip()).resolve()).replace("\\", "/").rstrip("/").lower()
            except OSError:
                continue
            if _dd == _goc_kho:
                cua = _c
                break
    if not cua:
        cua = max(wm, key=lambda c: _khoa_g(wm[c])) if wm else None
    # cửa chưa có lượt ghi nào (người mới "điểm danh" lần đầu): khai đúng
    # sự thật "CUAn chưa ghi" - phép 8 chấp nhận, không phải "bảng sửa tay"
    sinh_boi = wm.get(cua) if cua else None
    if cua and not sinh_boi:
        sinh_boi = f"{cua} chưa ghi"
    dang_ghi = [h[0].strip("* ") for h in nk if any(o.strip() == "ĐANG GHI" for o in h)]
    # phiên KHÁC đang mở: lượt ĐANG GHI của cửa không phải cửa này (hai người
    # dùng chung kho ở LITE - đợt 3 audit giám đốc)
    phien_khac = sorted({K.cua_cua(m) for m in dang_ghi
                         if K.cua_cua(m) and K.cua_cua(m) != cua})

    qh = K.dem_qua_han(so, x0nd)
    viec = _rows(so, "VIEC.md")
    tl = _rows(so, "TAILIEU.md")
    qd = _rows(so, "QUYETDINH.md")
    pl = _rows(so, "PLANNING.md")

    def ai(r):
        return (r[4].strip() if len(r) > 4 and r[4].strip() else "chưa gán")

    viec_mo = [r for r in viec if len(r) > 7
               and r[7].strip() not in ("XONG", "HỦY")]
    qua_han = [r for r in viec_mo if len(r) > 1 and r[1].strip() in qh["quá hạn"]]
    cho_dt = [r for r in viec_mo if len(r) > 1 and r[1].strip() in qh["chờ đối tác"]]
    cho_chot = [r for r in pl if len(r) > 9 and r[9].strip() == "CHỜ CHỐT"]

    # CÙNG bộ trạng thái "thôi đếm" với dem_qua_han và 8e: lệch một trạng thái
    # (ĐÃ GIA HẠN, TRẢ HỒ SƠ) là mốc bảng khác mốc 8e, bảng máy sinh tự đỏ
    tl_song = [r for r in tl if len(r) > 7 and "[đã xóa theo Q-" not in "|".join(r)
               and r[7].strip().upper() not in K.TT_THOI_DEM]
    tl_cho_ky = [r for r in tl_song if r[7].strip().upper() in
                 ("ĐÃ GỬI DUYỆT", "CHỜ KÝ", "CHỜ DUYỆT")]
    han_toi, sap_het = [], []
    for r in tl_song:
        m = re.search(r"(\d{4}-\d{2}-\d{2})", r[11]) if len(r) > 11 else None
        if not m:
            continue
        d = m.group(1)
        if d >= hom_nay.isoformat():
            han_toi.append(d)
            try:
                if (datetime.date.fromisoformat(d) - hom_nay).days <= 60:
                    sap_het.append((r, d))
            except ValueError:
                pass
    moc = min(han_toi) if han_toi else "chưa có"
    thang = hom_nay.strftime("%Y-%m")
    qd_thang = [r for r in qd if len(r) > 1 and r[1].strip().startswith(thang)]
    c12 = sorted(K.muc_con_trong(x0nd))

    theo_nguoi = {}
    for r in viec_mo:
        theo_nguoi.setdefault(ai(r), []).append(r)

    theo_nguoi_giu = {}
    for r in tl_song:
        if len(r) > 12:
            m = re.search(r"gi[ữu]\s*:\s*([^;|]+)", r[12])
            if m:
                theo_nguoi_giu.setdefault(m.group(1).strip(), []).append(r)

    return dict(ma_cty=ma_cty, rev=rev, cua=cua, sinh_boi=sinh_boi, wm=wm,
                phien_khac=phien_khac, theo_nguoi_giu=theo_nguoi_giu,
                qh=qh, dang_ghi=dang_ghi, qua_han=qua_han, cho_dt=cho_dt,
                cho_chot=cho_chot, tl_song=tl_song, tl_cho_ky=tl_cho_ky,
                sap_het=sap_het, moc=moc, qd_thang=qd_thang, c12=c12,
                theo_nguoi=theo_nguoi, viec_mo=viec_mo, hom_nay=hom_nay, ai=ai)


def dong_bo_dem(d):
    """Dòng bộ đếm banner: NHÃN trước SỐ (phép 8e đọc số đứng sau nhãn)."""
    qh = d["qh"]
    dem = [("quá hạn", len(qh["quá hạn"])),
           ("chờ đối tác", len(qh["chờ đối tác"])),
           ("chờ bạn chốt (plan C treo)", len(qh["plan C treo"])),
           ("ghi dở (ĐANG GHI)", len(d["dang_ghi"]))]
    them = [(k, len(qh[k])) for k in ("sắp hết hạn", "rà lại", "_INBOX") if qh[k]]
    duoi = (f" · phiên khác đang mở ({', '.join(d['phien_khac'])})"
            if d.get("phien_khac") else "")
    if not any(n for _, n in dem) and not them:
        return f"bàn sạch · mốc (hạn sớm nhất): {d['moc']}" + duoi
    phan = [f"{k}: {n}" for k, n in dem + them]
    return (" · ".join(phan)
            + f" · mail: không quét · mốc (hạn sớm nhất): {d['moc']}" + duoi)


def _dong_viec(r, ai):
    return (f"- {r[1].strip()} · {r[2].strip()[:48]} · {ai(r)}"
            + (f" · hạn {r[6].strip()}" if len(r) > 6 and r[6].strip() else ""))


def sinh_bang(d, gon=True):
    """BANG_DIEU_KHIEN theo X5 mục 3 bước 6: header máy + bộ đếm + việc cần
    người quyết + tài liệu đang hoạt động + nhắc C12. gon=True cắt danh sách
    để nằm trong trần 4.200 ký tự."""
    top = 5 if gon else 999
    ai = d["ai"]
    r = [f"# BANG_DIEU_KHIEN · {d['ma_cty']}", "", "```yaml",
         f"may_sinh: true · sinh_boi: {d['sinh_boi'] or 'cai dat'}"
         f" · x0_rev: {d['rev']}",
         "watermark: " + (" · ".join(f"{c}={m}" for c, m in sorted(d["wm"].items()))
                          if d["wm"] else "chưa có lượt ghi"),
         "```", "", dong_bo_dem(d), ""]
    can = []
    if d["cho_chot"]:
        can.append("Chờ bạn gõ \"chốt\": " + ", ".join(
            f"{p[0].strip()} ({p[4].strip()[:40]})" for p in d["cho_chot"][:top]))
    if d["qua_han"]:
        can.append("Quá hạn:")
        can += [_dong_viec(x, ai) for x in d["qua_han"][:top]]
    _da_in = {x[1].strip() for x in d["qua_han"][:top]}
    _cho_dt = [x for x in d["cho_dt"] if x[1].strip() not in _da_in]
    if _cho_dt:
        can.append("Chờ đối tác quá ngưỡng:")
        can += [_dong_viec(x, ai) for x in _cho_dt[:top]]
    if d["tl_cho_ky"]:
        can.append("Tài liệu chờ ký/duyệt: " + ", ".join(
            f"{x[1].strip()} {x[2].strip()[:30]}" for x in d["tl_cho_ky"][:top]))
    if d["sap_het"]:
        can.append("Sắp đến hạn (60 ngày tới): " + ", ".join(
            f"{x[2].strip()[:30]} ({dd})" for x, dd in d["sap_het"][:top]))
    if can:
        r += ["## Cần bạn quyết", *can, ""]
    if d["tl_song"]:
        r += ["## Tài liệu đang hoạt động"]
        r += [f"- {x[2].strip()[:36]} · {x[3].strip()} · {x[7].strip()} · {x[5].strip()[:40]}"
              for x in d["tl_song"][:8 if gon else 999]]
        r.append("")
    if d["c12"]:
        r += [f"Nhắc: X0 C12 còn {len(d['c12'])} mục chưa điền"
              f" ({', '.join(d['c12'][:4])}{'...' if len(d['c12']) > 4 else ''})"
              " - mục nào chặn phát hành thì trả lời trước", ""]
    ra = NL.join(r)
    if gon and len(ra) > TRAN_BANG and "## Tài liệu đang hoạt động" in r:
        ra = NL.join(r[:r.index("## Tài liệu đang hoạt động")]) + NL
    return ra[:TRAN_BANG] if gon else ra


def sinh_bao_cao(d):
    ai = d["ai"]
    r = [f"# BÁO CÁO · {d['ma_cty']} · {d['hom_nay'].isoformat()} (máy sinh từ sổ)",
         "", dong_bo_dem(d), ""]
    r += ["## 1. Cần bạn quyết"]
    if d["cho_chot"]:
        r += ["Chờ gõ \"chốt\":"] + [f"- {p[0].strip()} · {p[4].strip()}" for p in d["cho_chot"]]
    if d["qua_han"]:
        r += ["Quá hạn:"] + [_dong_viec(x, ai) for x in d["qua_han"]]
    if d["cho_dt"]:
        r += ["Chờ đối tác quá ngưỡng:"] + [_dong_viec(x, ai) for x in d["cho_dt"]]
    if d["tl_cho_ky"]:
        r += ["Tài liệu chờ ký/duyệt:"] + [
            f"- {x[1].strip()} · {x[2].strip()[:48]} · {x[7].strip()}" for x in d["tl_cho_ky"]]
    if d["sap_het"]:
        r += ["Sắp đến hạn (60 ngày tới):"] + [
            f"- {x[1].strip()} · {x[2].strip()[:48]} · {dd}" for x, dd in d["sap_het"]]
    if not (d["cho_chot"] or d["qua_han"] or d["cho_dt"] or d["tl_cho_ky"]
            or d["sap_het"]):
        r.append("- không có")
    r += ["", "## 2. Tài liệu"]
    r += ["Chờ ký/duyệt:"] + ([f"- {x[1].strip()} · {x[2].strip()} · {x[7].strip()}"
                             for x in d["tl_cho_ky"]] or ["- không có"])
    r += ["Sắp đến hạn trong 60 ngày tới:"] + (
        [f"- {x[1].strip()} · {x[2].strip()} · hết hạn {dd}" for x, dd in d["sap_het"]]
        or ["- không có"])
    r += ["", f"## 3. Quyết định tháng {d['hom_nay'].strftime('%m/%Y')}"]
    r += [f"- {q[0].strip()} · {q[1].strip()} · {q[2].strip()[:60]}"
          f" · {q[5].strip() if len(q) > 5 else ''}"
          for q in d["qd_thang"]] or ["- không có"]
    r += ["", "## 4. Việc đang mở theo người"]
    for ng, ds in sorted(d["theo_nguoi"].items(), key=lambda t: -len(t[1])):
        r.append(f"{ng}: {len(ds)} việc")
        r += [f"  {_dong_viec(x, ai)[2:]}" for x in ds[:12]]
    if not d["theo_nguoi"]:
        r.append("- không có việc mở")
    if d["theo_nguoi_giu"]:
        r += ["", "## 4b. Tài liệu theo người giữ"]
        for ng, ds in sorted(d["theo_nguoi_giu"].items()):
            r.append(f"{ng}: " + ", ".join(f"{x[1].strip()} {x[2].strip()[:30]}" for x in ds))
    r += ["", "## 5. Tài liệu đang hoạt động"]
    r += [f"- {x[1].strip()} · {x[2].strip()} · {x[3].strip()} · {x[7].strip()}"
          f" · {x[5].strip()}" for x in d["tl_song"]] or ["- không có"]
    if d["c12"]:
        r += ["", f"## 6. Cấu hình còn {len(d['c12'])} mục chưa điền", ", ".join(d["c12"])]
    r += ["", "Ghi chú: số liệu từ sổ lúc sinh; muốn cập nhật bảng điều khiển:"
          " python bao_cao.py <00_Index> --bang"]
    return NL.join(r) + NL


def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__)
        return 2
    goc = Path(argv[1])
    cua = argv[argv.index("--cua") + 1] if "--cua" in argv else None
    d = thu_thap(goc, cua)
    if "--bang" in argv:
        bang = sinh_bang(d)
        (goc / "_so" / "BANG_DIEU_KHIEN.md").write_text(bang, encoding="utf-8",
                                                        newline=NL)
        print(f"Đã ghi _so/BANG_DIEU_KHIEN.md ({len(bang)} ký tự, cửa {d['cua']},"
              f" sinh_boi {d['sinh_boi']})")
        _x0_txt = K.doc(sorted(goc.glob("X0_CAUHINH_*.md"))[0])
        _mpj = re.search(r"^@DUONG\.PROJECT\s+([^\n]*)", _x0_txt, re.M)
        if _mpj and "<điền" not in _mpj.group(1):
            print("Nhắc: tải BANG_DIEU_KHIEN và X0_INDEX lên tài liệu Project"
                  " (phiên CHAT đọc bản đã tải)")
        return 0
    sys.stdout.write(sinh_bao_cao(d))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
