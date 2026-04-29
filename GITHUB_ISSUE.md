# GitHub Issue 등록 가이드

아래 내용을 복사하여 GitHub Issue를 생성하세요.

---

### **제목:**
[Task] EDA 리포트 Marp 슬라이드 변환 및 HTML 생성

---

### **본문:**

## 📋 작업 개요
기존에 작성된 `EDA_Report.md`의 탐색적 데이터 분석 결과를 발표용 Marp 슬라이드로 변환하고, 이를 공유 및 배포가 용이한 HTML 슬라이드로 생성합니다.

## 🛠 작업 상세 내역
- [x] `EDA_Report.md` 핵심 내용을 기반으로 Marp 문법을 적용한 `EDA_Presentation.md` 작성
- [x] 시각화 자료(images/*)와 인사이트를 슬라이드 레이아웃에 맞게 배치
- [ ] Marp CLI를 사용하여 `EDA_Presentation.md`를 HTML 파일로 변환
- [ ] 최종 생성된 HTML 슬라이드의 디자인 및 내용 검토

## 🚀 실행 명령어 (참고용)
```bash
# HTML 변환 및 생성
npx @marp-team/marp-cli EDA_Presentation.md -o EDA_Presentation.html
```
