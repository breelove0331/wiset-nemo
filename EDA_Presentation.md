---
marp: true
theme: default
paginate: true
header: "Nemo 매물 데이터 EDA 리포트"
footer: "© 2026 Nemo Analysis Team"
backgroundColor: #ffffff
style: |
  section {
    font-family: 'Malgun Gothic', sans-serif;
  }
  h1 {
    color: #2c3e50;
  }
  h2 {
    color: #34495e;
  }
---

# Nemo 매물 데이터 탐색적 데이터 분석(EDA)
## 강남권 상업용 부동산 시장 분석 및 비지니스 전략

---

## 1. 데이터 개요 및 정제 결과

- **수집 대상**: Nemo 플랫폼 상가 및 사무실 매물
- **데이터 규모**: 673건 / 40개 변수
- **정제 작업**:
  - 중복 데이터 제거 (0건, 무결성 확인)
  - 이상치 식별 및 텍스트 데이터 전처리
- **주요 분석 변수**: 보증금, 월세, 권리금, 전용면적, 층수 등

---

## 2. 수치형 데이터 분석: 가격 형성 메커니즘

- **보증금 (Deposit)**:
  - 평균: 6,895만 원 (중앙값: 4,000만 원)
  - 특징: 강한 우측 꼬리 분포, 초고가 매물에 의한 평균 상승
- **월세 (Monthly Rent)**:
  - 평균: 534만 원 (중앙값: 340만 원)
  - 특징: 면적 및 위치에 따른 극심한 편차 존재
- **전용면적 (Size)**:
  - 평균: 127.5㎡ (약 38평)
  - 특징: 30평 내외 중소형 매물이 시장의 주류

---

## 3. 범주형 데이터 분석: 업종 및 지역적 특성

- **주요 업종 구성**:
  - **기타업종 (48%)**: 오피스용 사무실 비중 높음
  - **F&B (40%)**: 일반음식점, 서비스업, 휴게음식점 순
- **업종 중분류**: 카페, 다용도점포, 한식점 등 실생활 밀착형 업종 중심
- **지역적 특징**:
  - 역삼, 강남, 신논현 등 **2호선/신분당선 초역세권** 집중
  - '역세권', '인테리어 완비'가 핵심 의사결정 변수

---

## 4. 심층 시각화 분석 (1) - 업종 분포

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
<div>

### 업종 대분류 빈도
![width:450px](images/businessLargeCodeName_freq.png)

</div>
<div>

### 업종 중분류 빈도 (Top 30)
![width:450px](images/businessMiddleCodeName_freq.png)

</div>
</div>

**Insight**: 오피스 수요와 직장인 대상 소비 상권의 복합적 구조

---

## 4. 심층 시각화 분석 (2) - 가격 분포

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
<div>

### 보증금 분포
![width:450px](images/deposit_dist.png)

</div>
<div>

### 월세 분포
![width:450px](images/rent_dist.png)

</div>
</div>

**Insight**: 대다수 매물이 1억 미만/500만 원 이하에 집중된 양극화 시장

---

## 4. 심층 시각화 분석 (3) - 상관관계 분석

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
<div>

### 보증금 vs 월세
![width:450px](images/deposit_vs_rent.png)

</div>
<div>

### 면적 vs 월세
![width:450px](images/size_vs_rent.png)

</div>
</div>

**Insight**: 면적에 비례하는 가격 형성, 단 협상에 의한 유연한 계약 조건 존재

---

## 4. 심층 시각화 분석 (4) - 층수 및 키워드

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
<div>

### 층수별 평균 월세
![width:450px](images/floor_rent.png)

</div>
<div>

### 제목 키워드 분석 (TF-IDF)
![width:450px](images/title_keywords.png)

</div>
</div>

**Insight**: 1층 프리미엄 뚜렷, '인테리어/무권리'가 임차인 유인의 핵심

---

## 5. 비지니스 전략 제언 - 임차인 측면

1. **예산 벤치마킹**: 중앙값(보증금 4천/월세 340)을 기준으로 허위 매물 판별
2. **시설 권리금 활용**: '인테리어 승계' 매물을 통해 초기 투자비용 절감
3. **층수 전략**: 목적형 방문 서비스의 경우 2층 이상을 선택하여 고정비 최적화

---

## 5. 비지니스 전략 제언 - 임대인/플랫폼 측면

- **임대인**:
  - 공실 단축을 위해 기존 인테리어 유지 및 '무권리' 조건 제시 권장
  - 우량 임차인 유치를 위한 유연한 임대 조건(Rent-free 등) 고려
- **플랫폼**:
  - '무권리', '인테리어 완비' 필터 고도화로 매칭 효율 증대
  - 데이터 기반의 적정 임대료 가이드 제공으로 신뢰도 확보

---

# Q&A
### 감사합니다.
