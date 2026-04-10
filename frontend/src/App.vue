<template>
  <div class="app-wrapper">
    <header class="naver-header">
      <div class="header-inner">
        <h1 class="logo">경제 <span>NEWS</span></h1>
        <p class="sub-title">핵심 경제 뉴스</p>
      </div>
      <div class="top-categories-container">
        <p class="top-categories-title">주식 관련 TOP 카테고리:</p>
        <div class="top-categories-list">
          <span v-for="item in topStockCategories" :key="item.category" class="top-category-badge">
            {{ item.category }} ({{ item.count }})
          </span>
        </div>
      </div>
    </header>
    <div class="filter-container">
      <select v-model="selectedCategory" @change="filterNews" class="category-filter">
        <option value="all">모든 카테고리</option>
        <option v-for="category in categories" :key="category" :value="category">{{ category }}</option>
      </select>
    </div>
    <main class="container">
      <div v-if="loading" class="loading-msg">뉴스를 불러오는 중입니다...</div>
      <div v-else-if="allNews.length === 0" class="error-msg">
        뉴스를 가져오지 못했습니다. 백엔드 터미널에 에러가 떴는지 확인해 주세요.
      </div>
      <div v-else-if="filteredNews.length === 0" class="error-msg">
        해당 카테고리의 뉴스가 없습니다.
      </div>
      <div v-else class="news-list">
        <article v-for="news in filteredNews" :key="news.title + news.url" class="news-card">
          <div class="badge-container">
            <span class="category-badge">{{ news.category }}</span>
            <a v-for="stock in news.stocks" :key="stock" :href="`https://www.google.com/finance/quote/${stock}:NASDAQ`" target="_blank" class="stock-link">
              <span class="stock-badge">📈 {{ stock }}</span>
            </a>
          </div>
          <div class="news-content">
            <a :href="news.url" target="_blank" class="news-link">
              <h2>{{ news.title }}</h2>
            </a>
            <img v-if="news.imageUrl" :src="news.imageUrl" alt="뉴스 썸네일" class="news-thumbnail">
          </div>
          <div class="ai-summary">
            <h3>✨ AI 요약</h3>
            <p style="white-space: pre-line;">{{ news.summary }}</p>
          </div>
        </article>
      </div>
      <div v-if="hasMore" class="load-more-container">
        <button @click="loadMore" :disabled="loading" class="load-more-button">더보기</button>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const allNews = ref([]); // 모든 뉴스를 저장할 배열
const filteredNews = ref([]); // 화면에 보여줄 필터링된 뉴스 배열
const loading = ref(false); // 초기 로딩 상태는 false로 시작
const currentPage = ref(1);
const itemsPerPage = 10; // 한 번에 보여줄 뉴스 개수
const hasMore = ref(true); // 더 불러올 뉴스가 있는지 여부
const selectedCategory = ref('all'); // 선택된 카테고리
const categories = ref(['금융/증권', '기업/IT', '부동산', '경제정책', '글로벌경제', '기타']); // 카테고리 목록
const topStockCategories = ref([]); // 주식 관련 TOP 카테고리 목록

onMounted(async () => {
  await fetchNews(); // 컴포넌트 마운트 시 첫 페이지 뉴스 로드
});

const fetchNews = async () => {
  loading.value = true;
  await fetchTopStockCategories(); // TOP 카테고리도 함께 가져옴
  try {
    const response = await axios.get(`http://127.0.0.1:3001/api/news/economy?page=${currentPage.value}&limit=${itemsPerPage}`);
    allNews.value = [...allNews.value, ...response.data.news]; // 모든 뉴스를 저장
    filterNews(); // 뉴스를 가져온 후 필터링
    hasMore.value = response.data.hasMore; // 더 불러올 뉴스가 있는지 업데이트
  } catch (error) {
    console.error("뉴스를 불러오는데 실패했습니다.", error);
  } finally {
    loading.value = false;
  }
};

const loadMore = () => {
  if (hasMore.value && !loading.value) {
    currentPage.value++;
    fetchNews();
  }
};

const filterNews = () => {
  if (selectedCategory.value === 'all') {
    filteredNews.value = allNews.value;
  } else {
    filteredNews.value = allNews.value.filter(news => news.category === selectedCategory.value);
  }
};

const fetchTopStockCategories = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:3001/api/stats/top-stock-categories');
    topStockCategories.value = response.data;
  } catch (error) {
    console.error("TOP 주식 카테고리를 불러오는데 실패했습니다:", error);
  }
};
</script>

<style scoped>
/* 예쁜 한글 폰트 적용 */
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');

.app-wrapper {
  font-family: 'Pretendard', -apple-system, sans-serif; 
  color: #333;
  background-color: #f5f6f8; /* 네이버 스타일의 옅은 회색 배경 */
  min-height: 100vh;
  padding-bottom: 50px;
}

/* 네이버 상단 헤더 */
.naver-header { 
  background-color: #03c75a; /* 네이버 시그니처 그린 */
  padding: 24px 0; 
  border-bottom: 1px solid #02b350;
}

.header-inner {
  max-width: 800px;
  margin: 0 auto;
  padding: 0 20px;
}

.logo { 
  font-size: 2rem; 
  font-weight: 800; 
  color: #fff; 
  margin: 0; 
  letter-spacing: -1px;
}
.logo span { font-weight: 400; opacity: 0.9; }

.top-categories-container {
  max-width: 800px;
  margin: 20px auto 0;
  padding: 0 20px;
  color: #fff;
  font-size: 0.9rem;
}
.top-categories-title {
  margin: 0 0 8px 0;
  font-weight: 600;
}
.top-categories-list {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}
.top-category-badge {
  background-color: rgba(255, 255, 255, 0.2); /* 투명한 흰색 배경 */
  color: #fff;
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 0.85rem;
  font-weight: 500;
  white-space: nowrap; /* 줄바꿈 방지 */
}

.sub-title { color: #e5f9ed; margin: 6px 0 0 0; font-size: 0.95rem; }

.filter-container {
  max-width: 800px;
  margin: 20px auto 0;
  padding: 0 20px;
}

.category-filter {
  width: 100%;
  padding: 10px;
  border: 1px solid #e3e5e8;
  border-radius: 6px;
  font-size: 1rem;
  background-color: #fff;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
}

.container { 
  max-width: 800px; /* 기사 읽기 좋은 폭으로 조정 */
  margin: 30px auto 0; 
  padding: 0 20px; 
}

/* 네이버 스타일 뉴스 리스트 박스 */
.news-list { 
  background: #fff;
  border: 1px solid #e3e5e8;
  border-radius: 8px;
  padding: 0 24px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.02);
}

/* 각 뉴스 항목 구분선 */
.news-card { 
  padding: 24px 0; 
  border-bottom: 1px solid #f0f2f5;
}
.news-card:hover {
  border-color: #007bff; /* 호버 시 파란색 테두리 */
  transition: border-color 0.2s ease-in-out; /* 부드러운 전환 효과 */
}
.news-card:last-child { border-bottom: none; }

/* 뱃지들을 가로로 나열하는 컨테이너 */
.badge-container {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 12px;
}

/* 카테고리 뱃지 스타일 */
.category-badge {
  background-color: #e9ecef;
  color: #495057;
  font-size: 0.8rem;
  font-weight: 700;
  padding: 4px 10px;
  border-radius: 4px;
}

/* 관련 주식 뱃지 스타일 */
.stock-badge {
  background-color: #e8f0fe;
  color: #1a73e8;
  font-size: 0.8rem;
  font-weight: 700;
  padding: 4px 10px;
  border-radius: 4px;
}

/* 주식 뱃지 링크 스타일 */
.stock-link {
  text-decoration: none;
}

.news-link { text-decoration: none; color: inherit; display: block; margin-bottom: 14px; }
.news-link h2 { 
  font-size: 1.25rem; 
  font-weight: 700; 
  line-height: 1.4; 
  margin: 0; 
  color: #202020; 
}
.news-link:hover h2 { text-decoration: underline; color: #03c75a; } /* 호버 시 네이버 그린 */

/* AI 요약 박스 디자인 */
.ai-summary { 
  background-color: #f8f9fa; 
  padding: 16px 20px; 
  border-radius: 6px; 
  border-left: 4px solid #03c75a; /* 네이버 그린 포인트 라인 */
}
.ai-summary h3 { margin: 0 0 8px 0; font-size: 0.95rem; color: #03c75a; font-weight: 700; }
.ai-summary p { margin: 0; font-size: 0.95rem; line-height: 1.6; color: #444; }

/* 뉴스 썸네일 스타일 */
.news-thumbnail {
  width: 500px; /* 이미지 폭을 120px로 설정 */
  height: 300px; /* 이미지 높이를 조정 */
  object-fit: cover; /* 이미지 비율 유지하며 채우기 */
  border-radius: 4px;
  flex-shrink: 0; /* 내용이 줄어들어도 이미지는 고정 */
}
/* 로딩 및 에러 메시지 */
.loading-msg, .error-msg { text-align: center; padding: 50px 0; font-size: 1.1rem; }
.error-msg { color: red; }

/* 더보기 버튼 스타일 */
.load-more-container {
  text-align: center;
  margin-top: 30px;
}
.load-more-button {
  background-color: #03c75a;
  color: #fff;
  border: none;
  padding: 12px 24px;
  border-radius: 6px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.2s ease;
}
.load-more-button:hover:not(:disabled) {
  background-color: #02b350;
}
.load-more-button:disabled {
  background-color: #a0a0a0;
  cursor: not-allowed;
}
</style>
