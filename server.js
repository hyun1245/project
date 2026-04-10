const express = require('express');
const cors = require('cors');
const cron = require('node-cron');
const axios = require('axios');
const { GoogleGenerativeAI } = require('@google/generative-ai');

const app = express();
const PORT = 3001; // 포트를 3001번으로 변경하여 옛날 서버 회피

// Middleware
app.use(cors());
app.use(express.json());

// 서버 메모리에 뉴스를 저장할 배열 (DB 대신 사용)
// 서버가 재시작되면 데이터는 초기화됩니다.
let summarizedNewsDB = [];

// TODO: 발급받은 Gemini API 키를 아래에 입력하세요.
const genAI = new GoogleGenerativeAI('AIzaSyBFqrqYIWx29D30xktnReDQoDnpfcT6BQg');

async function summarizeText(text) {
  if (!text) return { category: "기타", stocks: [], summary: "요약할 내용이 없습니다." };
  try {
    // 최신 성능을 제공하는 gemini-2.5-flash 모델 사용
    const model = genAI.getGenerativeModel({
      model: "gemini-2.5-flash",
      systemInstruction: "You are an expert news editor. Classify the given English news into one of these categories: '금융/증권', '기업/IT', '부동산', '경제정책', '글로벌경제', '기타'. Also, identify any related NASDAQ-listed stock tickers (e.g., AAPL, TSLA). If none, write '없음'. Then, translate and summarize it into 3 bullet points in Korean.\n\nSTRICT FORMAT:\n[카테고리명]\n[관련주식: AAPL, TSLA]\n1. ...\n2. ...\n3. ..."
    });
    const prompt = `다음 기사 내용을 한국어로 3줄 요약해줘:\n${text}`;
    const result = await model.generateContent(prompt);
    const resultText = result.response.text().trim();

    let category = "글로벌경제";
    let stocks = [];
    let summary = resultText;

    let finalSummary = resultText; // 이 변수에 태그를 제거한 최종 요약 텍스트를 저장합니다.

    // Regex를 사용하여 [태그] 형태의 모든 항목을 찾습니다.
    const allTags = resultText.match(/\[.*?\]/g) || [];

    for (const tag of allTags) {
      if (tag.includes('관련주식:')) {
        // '관련주식:' 태그인 경우 주식 정보를 추출합니다.
        const stockMatch = tag.match(/\[관련\s*주식\s*:\s*(.*?)\]/);
        if (stockMatch) {
          const stockText = stockMatch[1].trim();
          // '없음' 또는 'None'이 포함되어 있지 않을 때만 주식 배열을 생성합니다.
          if (!stockText.includes('없음') && !stockText.includes('None')) {
            stocks = stockText.split(',').map(s => s.replace(/[^A-Z0-9]/ig, '').trim()).filter(s => s !== '');
          }
        }
      } else {
        // '관련주식:' 태그가 아니면 카테고리 태그로 간주하고 카테고리를 추출합니다.
        category = tag.replace(/\[|\]/g, '').trim();
      }
      // 추출한 태그는 최종 요약 텍스트에서 제거합니다.
      finalSummary = finalSummary.replace(tag, '').trim();
    }

    // 태그 제거 후 남은 불필요한 공백이나 개행 문자를 정리합니다.
    finalSummary = finalSummary.replace(/\n\s*\n/g, '\n').trim();

    return { category, stocks, summary: finalSummary };
  } catch (error) {
    console.error('Gemini 요약 에러:', error.message);
    return { category: "에러", stocks: [], summary: "AI 요약을 불러오는데 실패했습니다." };
  }
}

async function fetchAndSummarizeNews() {
  console.log('🔄 미국 경제 뉴스 수집 시작...');
  try {
    // TODO: 발급받은 NewsAPI 키를 아래에 입력하세요. (https://newsapi.org 에서 발급)
    const apiKey = 'd3fa3718aad64148a34e1852fd4c044c';

    const response = await axios.get('https://newsapi.org/v2/top-headlines', {
      params: { country: 'us', category: 'business', pageSize: 30, apiKey: apiKey }, // 더 많은 뉴스를 가져오도록 pageSize를 30으로 변경
      headers: { 'User-Agent': 'NodeJS App' } // NewsAPI 차단 방지용 헤더
    });

    // 1. 삭제된 기사([Removed]) 걸러내기
    const validArticles = response.data.articles.filter(
      (article) => article.title && article.title !== '[Removed]'
    );

    // 구글 API 요청 제한(Rate Limit) 방지를 위한 대기 함수
    const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));

    const newNewsDB = [];
    // 2. 동시 요청 에러를 막기 위해 하나씩 순서대로 요약 요청 (for 문 사용)
    for (let index = 0; index < validArticles.length; index++) {
      const article = validArticles[index];
      const contentToSummarize = `${article.title}\n${article.description || ''}`;
      const { category, stocks, summary } = await summarizeText(contentToSummarize);
      
      newNewsDB.push({
        title: article.title,
        category: category,
        stocks: stocks,
        summary: summary,
        url: article.url, // 원문 링크 추가
        imageUrl: article.urlToImage, // 썸네일 이미지 URL 추가
        publishedAt: new Date(article.publishedAt) // NewsAPI에서 제공하는 발행일 사용
      });

      // 기사 하나를 요약한 뒤 4초 쉬기 (1분당 15~20회 무료 제한 엄수)
      if (index < validArticles.length - 1) {
        await delay(4000); 
      }
    }
    summarizedNewsDB = newNewsDB;
    console.log('✅ 미국 뉴스 업데이트 완료!');
  } catch (error) {
    console.error('❌ 뉴스 수집 실패:', error.message);
  }
}

// 기존 페이지네이션 로직은 유지
app.get('/api/news/economy', (req, res) => {
  const page = parseInt(req.query.page) || 1;
  const limit = parseInt(req.query.limit) || 10;

  const startIndex = (page - 1) * limit;
  const endIndex = page * limit;

  const paginatedNews = summarizedNewsDB.slice(startIndex, endIndex);
  const hasMore = endIndex < summarizedNewsDB.length;

  res.json({ news: paginatedNews, hasMore: hasMore });
});

// 새로운 API 엔드포인트: 가장 많이 언급된 주식들의 카테고리 TOP 3
app.get('/api/stats/top-stock-categories', (req, res) => {
  const categoryStockCounts = {};

  summarizedNewsDB.forEach(news => {
    if (news.stocks && news.stocks.length > 0) {
      const category = news.category || '기타'; // 카테고리가 없으면 '기타'로 처리
      categoryStockCounts[category] = (categoryStockCounts[category] || 0) + 1;
    }
  });

  const sortedCategories = Object.entries(categoryStockCounts)
    .sort(([, countA], [, countB]) => countB - countA) // 내림차순 정렬
    .slice(0, 3) // 상위 3개만 가져오기
    .map(([category, count]) => ({ category, count }));

  res.json(sortedCategories);
});

// 매일 매시간 0분에 실행
cron.schedule('0 * * * *', () => {
  fetchAndSummarizeNews();
});

// Server start
app.listen(PORT, '127.0.0.1', () => {
  console.log(`Server running on http://127.0.0.1:${PORT}`);
  fetchAndSummarizeNews();
});
