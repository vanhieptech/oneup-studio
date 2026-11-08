---
title: "Clip 04 v14 production (Hiep chot 2026-10-20)"
date: 2026-10-20
type: production
status: locked-script-in-production
script_locked: final/script-v14.md (Hiep noi "chot" tai group Agency 2026-10-20, loi khong sua mot chu)
voice: F5-TTS Thai Son (Thay), speed 0.9, voice_prefix c04v14
---
# Clip 04 v14 — production

- Loi da chot: `final/script-v14.md` b01-b10 nguyen van (kiem bang generator: text-lock OK, doi chieu tung beat).
- Bang canh 9 cot (Beat | Giay | Engine | Shot | Hanh dong/Cam xuc | Loi {nhan:} | Caption EN <=8 | Animation/EFX 1 chinh/beat | Sound): trong `final/script-v14.md` muc "Storyboard thong nhat" — sinh theo loi v14, khong lam lai bang khac.
- Spec may: `final/spec.json` (generator `pipeline/scripts/clip-04-mkspec-v14.py`), parts: A Remotion b01-b05, E HyperFrames b06-b07 (`final/explainer/`), B Remotion b08-b10.
- Diem hinh khoa: b01 frame dau sach gap day sang ben + giay trang + but dung; b04 sach VAN GAP, but nam yen, chua luggage; b05 mo sach dung mot lan; lich trinh (to giay nho tren ban) co tu b02 tro di cung vi tri; the/trang khong chu (props book/sheet/pile/bundles), chu chi o caption/bubble/render text.
- Giong: F5-TTS tieng Viet, tham chieu Thai Son cho Thay/Hiep chibi nhu clip-03, speed 0.9 (voice-phrase-f5.py), sinh SAU khi chot.
- End card 2s gan sau assemble bang ffmpeg: nen ban hoc, chu tinh:
  Thong tin tham khao, khong thay the tu van chuyen gia
  Noi dung dua tren 'Cam nang song dang gia' – chuanman2707, CC BY 4.0 – https://chuanman2707.github.io/HowToLiveBetter/
- Khong nhac trong file (Hiep tu them nhac TikTok). Ban nhe 540x960 crf28 kem theo.
- QA: STT doi chieu 100% v14, ffprobe resolution/duration, contact sheet + stills dau/giua/cuoi tung beat doc bang mat, check-rules --final --stt.
