// Global Application State
let articles = [];
let bookmarkedIds = [];
let currentCategory = 'all';
let currentSort = 'score'; // 'score' or 'time'
let searchQuery = '';
let showOnlyBookmarked = false;
let activeArticleId = null;
let currentSummaryLang = 'zh'; // 'zh' or 'en'

// Elements Selection
const themeToggleBtn = document.getElementById('theme-toggle-btn');
const bookmarkFilterBtn = document.getElementById('bookmark-filter-btn');
const bookmarkCountBadge = document.getElementById('bookmark-count');
const searchInput = document.getElementById('search-input');
const clearSearchBtn = document.getElementById('clear-search-btn');
const categoriesList = document.getElementById('categories-list');
const sortScoreBtn = document.getElementById('sort-score-btn');
const sortTimeBtn = document.getElementById('sort-time-btn');
const activeFiltersBar = document.getElementById('active-filters-bar');
const resetFiltersBtn = document.getElementById('reset-filters-btn');
const skeletonContainer = document.getElementById('skeleton-container');
const newsGridContainer = document.getElementById('news-grid-container');
const emptyState = document.getElementById('empty-state');

// Drawer Elements
const drawerBackdrop = document.getElementById('drawer-backdrop');
const sideDrawer = document.getElementById('side-drawer');
const closeDrawerBtn = document.getElementById('close-drawer-btn');
const drawerBookmarkBtn = document.getElementById('drawer-bookmark-btn');
const drawerShareBtn = document.getElementById('drawer-share-btn');
const drawerContent = document.getElementById('drawer-content');

// Stats Elements
const statTotalScanned = document.getElementById('stat-total-scanned');
const statSelected = document.getElementById('stat-selected');
const statAvgScore = document.getElementById('stat-avg-score');

// Initialize Application
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  loadBookmarks();
  fetchNews();
  setupEventListeners();
});

// Theme Management
function initTheme() {
  const savedTheme = localStorage.getItem('theme') || 'dark';
  if (savedTheme === 'light') {
    document.body.classList.remove('dark-theme');
    document.body.classList.add('light-theme');
  } else {
    document.body.classList.add('dark-theme');
    document.body.classList.remove('light-theme');
  }
}

themeToggleBtn.addEventListener('click', () => {
  if (document.body.classList.contains('dark-theme')) {
    document.body.classList.remove('dark-theme');
    document.body.classList.add('light-theme');
    localStorage.setItem('theme', 'light');
  } else {
    document.body.classList.remove('light-theme');
    document.body.classList.add('dark-theme');
    localStorage.setItem('theme', 'dark');
  }
});

// Bookmarks Management
function loadBookmarks() {
  try {
    const saved = localStorage.getItem('bookmarks');
    bookmarkedIds = saved ? JSON.parse(saved) : [];
  } catch (e) {
    bookmarkedIds = [];
  }
  updateBookmarkCount();
}

function saveBookmarks() {
  localStorage.setItem('bookmarks', JSON.stringify(bookmarkedIds));
  updateBookmarkCount();
}

function updateBookmarkCount() {
  bookmarkCountBadge.textContent = bookmarkedIds.length;
  // If we are currently showing bookmarks, update state
  if (showOnlyBookmarked && bookmarkedIds.length === 0) {
    toggleBookmarkFilter(false);
  }
}

function toggleBookmark(id) {
  const index = bookmarkedIds.indexOf(id);
  if (index === -1) {
    bookmarkedIds.push(id);
  } else {
    bookmarkedIds.splice(index, 1);
  }
  saveBookmarks();
  updateDrawerBookmarkBtnState(id);
  renderNews();
}

function updateDrawerBookmarkBtnState(id) {
  if (!drawerBookmarkBtn) return;
  const isBookmarked = bookmarkedIds.includes(id);
  const textEl = drawerBookmarkBtn.querySelector('span');
  
  if (isBookmarked) {
    drawerBookmarkBtn.classList.add('active');
    textEl.textContent = '已收藏';
  } else {
    drawerBookmarkBtn.classList.remove('active');
    textEl.textContent = '收藏';
  }
}

// Fetch News Data
async function fetchNews() {
  // Show skeleton
  skeletonContainer.classList.remove('hidden');
  newsGridContainer.classList.add('hidden');
  emptyState.classList.add('hidden');

  try {
    // Artificial slight delay to show premium skeleton shimmer
    await new Promise(resolve => setTimeout(resolve, 800));
    
    const response = await fetch('./data/news.json');
    if (!response.ok) throw new Error('网络请求错误，无法加载数据');
    articles = await response.json();
    
    updateStats();
    renderNews();
  } catch (err) {
    console.error('加载新闻数据失败:', err);
    skeletonContainer.classList.add('hidden');
    emptyState.classList.remove('hidden');
    emptyState.querySelector('h3').textContent = '加载数据失败';
    emptyState.querySelector('p').textContent = '请检查网络或确认 data/news.json 是否已生成';
  }
}

// Stats Dashboard Update
function updateStats() {
  if (articles.length === 0) return;
  
  // Scanned counts (horizon scans more than top 20, let's keep mock or compute)
  statTotalScanned.textContent = Math.max(120, articles.length * 15);
  statSelected.textContent = articles.length;
  
  // Calculate average score
  const totalScore = articles.reduce((sum, item) => sum + item.importance_score, 0);
  const avg = (totalScore / articles.length).toFixed(1);
  statAvgScore.textContent = avg;
}

// Date Formatter
function formatRelativeTime(dateStr) {
  try {
    const pubDate = new Date(dateStr);
    const now = new Date();
    const diffMs = now - pubDate;
    const diffMins = Math.floor(diffMs / (1000 * 60));
    const diffHours = Math.floor(diffMs / (1000 * 60 * 60));
    
    if (diffMins < 60) {
      return `${Math.max(1, diffMins)} 分钟前`;
    } else if (diffHours < 24) {
      return `${diffHours} 小时前`;
    } else {
      const days = Math.floor(diffHours / 24);
      if (days === 1) return '昨天';
      if (days === 2) return '前天';
      return `${pubDate.getMonth() + 1}月${pubDate.getDate()}日`;
    }
  } catch (e) {
    return '稍早';
  }
}

// Render News Grid
function renderNews() {
  skeletonContainer.classList.add('hidden');
  
  // 1. Apply Filtering (Search, Category, Bookmark)
  let filtered = [...articles];
  
  if (showOnlyBookmarked) {
    filtered = filtered.filter(item => bookmarkedIds.includes(item.id));
  }
  
  if (currentCategory !== 'all') {
    filtered = filtered.filter(item => item.category === currentCategory);
  }
  
  if (searchQuery) {
    const q = searchQuery.toLowerCase();
    filtered = filtered.filter(item => 
      item.title.toLowerCase().includes(q) || 
      item.summary_zh.toLowerCase().includes(q) || 
      item.summary_en.toLowerCase().includes(q) ||
      item.source.toLowerCase().includes(q)
    );
  }
  
  // 2. Apply Sorting
  if (currentSort === 'score') {
    filtered.sort((a, b) => b.importance_score - a.importance_score);
  } else if (currentSort === 'time') {
    filtered.sort((a, b) => new Date(b.publish_time) - new Date(a.publish_time));
  }
  
  // 3. Render
  newsGridContainer.innerHTML = '';
  
  if (filtered.length === 0) {
    newsGridContainer.classList.add('hidden');
    emptyState.classList.remove('hidden');
    return;
  }
  
  emptyState.classList.add('hidden');
  newsGridContainer.classList.remove('hidden');
  
  filtered.forEach(item => {
    const isHot = item.importance_score >= 9.5;
    const isBookmarked = bookmarkedIds.includes(item.id);
    const timeFormatted = formatRelativeTime(item.publish_time);
    
    // Create card element
    const card = document.createElement('article');
    card.className = `news-card ${isHot ? 'hot-card' : ''}`;
    card.id = `news-card-${item.id}`;
    
    // Set custom score class (high vs medium)
    const scoreClass = item.importance_score >= 9.0 ? '' : 'med-score';
    
    card.innerHTML = `
      <div class="hot-tag">TODAY TOP</div>
      <div class="card-header">
        <div class="card-meta">
          <span class="source-badge">
            <svg viewBox="0 0 24 24" width="10" height="10" stroke="currentColor" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="10"></circle>
            </svg>
            ${item.source}
          </span>
          <span class="publish-time">${timeFormatted}</span>
        </div>
        <div class="score-badge ${scoreClass}">${item.importance_score.toFixed(1)}</div>
      </div>
      <div class="card-body">
        <h3 class="card-title">${item.title}</h3>
        <p class="card-summary-preview">${item.summary_zh}</p>
      </div>
      <div class="card-footer">
        <span class="category-badge">${getCategoryNameZh(item.category)}</span>
        <button class="btn-read-ai" data-id="${item.id}">
          AI 总结分析
          <svg viewBox="0 0 24 24" width="12" height="12" stroke="currentColor" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="9 18 15 12 9 6"></polyline>
          </svg>
        </button>
      </div>
    `;
    
    // Card Click Handler
    card.addEventListener('click', (e) => {
      // Don't open drawer if clicked on external link or bookmark button inside card (if any)
      if (e.target.closest('a')) return;
      openDrawer(item.id);
    });
    
    newsGridContainer.appendChild(card);
  });
}

function getCategoryNameZh(cat) {
  const map = {
    'AI': 'AI与机器学习',
    'Dev': '开发工具',
    'Startup': '商业与初创',
    'Hardware': '前沿硬件',
    'Science': '前沿科学'
  };
  return map[cat] || cat;
}

// Side Drawer Operations
function openDrawer(id) {
  const item = articles.find(x => x.id === id);
  if (!item) return;
  
  activeArticleId = id;
  currentSummaryLang = 'zh'; // default back to Chinese
  
  updateDrawerBookmarkBtnState(id);
  
  const pubDate = new Date(item.publish_time);
  const timeStr = pubDate.toLocaleString('zh-CN', { 
    year: 'numeric', 
    month: '2-digit', 
    day: '2-digit', 
    hour: '2-digit', 
    minute: '2-digit' 
  });
  
  const scoreClass = item.importance_score >= 9.0 ? '' : 'med-score';
  
  // Render Drawer Content
  drawerContent.innerHTML = `
    <div class="drawer-meta-header">
      <div class="drawer-source-score">
        <span class="source-badge">
          <svg viewBox="0 0 24 24" width="12" height="12" stroke="currentColor" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"></circle>
          </svg>
          ${item.source} · ${getCategoryNameZh(item.category)}
        </span>
        <div class="score-badge ${scoreClass}">AI 评分: ${item.importance_score.toFixed(1)}</div>
      </div>
      <h2 class="drawer-title">${item.title}</h2>
      <div class="drawer-time-link">
        <span>发布于: ${timeStr}</span>
        <a href="${item.url}" target="_blank" rel="noopener noreferrer" class="btn-link-out">
          直达原文
          <svg viewBox="0 0 24 24" width="14" height="14" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
            <polyline points="15 3 21 3 21 9"></polyline>
            <line x1="10" y1="14" x2="21" y2="3"></line>
          </svg>
        </a>
      </div>
    </div>
    
    <div class="drawer-divider"></div>
    
    <!-- Takeaways Bullet Points -->
    <div class="takeaways-section">
      <h4>AI 提炼要点</h4>
      <ul class="takeaways-list">
        ${item.takeaways.map(pt => `<li>${pt}</li>`).join('')}
      </ul>
    </div>
    
    <div class="drawer-divider"></div>
    
    <!-- AI Summary Tabs -->
    <div class="summary-section">
      <div class="summary-tabs-header">
        <h4>AI 总结详情</h4>
        <div class="summary-toggle-controls">
          <button class="summary-toggle-btn active" id="tab-lang-zh" data-lang="zh">中文</button>
          <button class="summary-toggle-btn" id="tab-lang-en" data-lang="en">EN</button>
        </div>
      </div>
      
      <div class="summary-text-box">
        <p id="summary-zh-text" class="summary-text-content">${item.summary_zh}</p>
        <p id="summary-en-text" class="summary-text-content hidden">${item.summary_en}</p>
      </div>
    </div>
  `;
  
  // Bind Inner Lang Switchers
  const tabZh = document.getElementById('tab-lang-zh');
  const tabEn = document.getElementById('tab-lang-en');
  const textZh = document.getElementById('summary-zh-text');
  const textEn = document.getElementById('summary-en-text');
  
  tabZh.addEventListener('click', () => {
    currentSummaryLang = 'zh';
    tabZh.classList.add('active');
    tabEn.classList.remove('active');
    textZh.classList.remove('hidden');
    textEn.classList.add('hidden');
  });
  
  tabEn.addEventListener('click', () => {
    currentSummaryLang = 'en';
    tabEn.classList.add('active');
    tabZh.classList.remove('active');
    textEn.classList.remove('hidden');
    textZh.classList.add('hidden');
  });
  
  // Show side drawer
  drawerBackdrop.classList.add('active');
  sideDrawer.classList.add('active');
  document.body.style.overflow = 'hidden'; // Lock main scroll
}

function closeDrawer() {
  drawerBackdrop.classList.remove('active');
  sideDrawer.classList.remove('active');
  document.body.style.overflow = ''; // Unlock main scroll
  activeArticleId = null;
}

// Bookmark filter operations
function toggleBookmarkFilter(active) {
  showOnlyBookmarked = active;
  if (active) {
    bookmarkFilterBtn.classList.add('btn-icon-active');
    bookmarkFilterBtn.style.color = 'var(--accent-pink)';
    bookmarkFilterBtn.style.borderColor = 'rgba(244, 114, 182, 0.3)';
    activeFiltersBar.classList.remove('hidden');
  } else {
    bookmarkFilterBtn.classList.remove('btn-icon-active');
    bookmarkFilterBtn.style.color = '';
    bookmarkFilterBtn.style.borderColor = '';
    activeFiltersBar.classList.add('hidden');
  }
  renderNews();
}

// Copy Summary
function copyCurrentSummaryToClipboard() {
  if (!activeArticleId) return;
  const item = articles.find(x => x.id === activeArticleId);
  if (!item) return;
  
  const copyText = `【Today Tech Top 20 精选】
标题: ${item.title}
评分: ${item.importance_score} (${item.source})
原文链接: ${item.url}

要点提炼:
${item.takeaways.map((pt, idx) => `${idx + 1}. ${pt}`).join('\n')}

AI 总结 (${currentSummaryLang === 'zh' ? '中文' : '英文'}):
${currentSummaryLang === 'zh' ? item.summary_zh : item.summary_en}`;

  navigator.clipboard.writeText(copyText).then(() => {
    // Show copy toast feedback on button
    const originalText = drawerShareBtn.querySelector('span');
    const prevContent = originalText.textContent;
    originalText.textContent = '已复制!';
    drawerShareBtn.style.borderColor = 'var(--accent-teal)';
    drawerShareBtn.style.color = 'var(--accent-teal)';
    
    setTimeout(() => {
      originalText.textContent = prevContent;
      drawerShareBtn.style.borderColor = '';
      drawerShareBtn.style.color = '';
    }, 1500);
  }).catch(err => {
    console.error('复制失败:', err);
    alert('复制失败，请手动选择复制');
  });
}

// Setup Application Event Listeners
function setupEventListeners() {
  // Bookmark button in header
  bookmarkFilterBtn.addEventListener('click', () => {
    toggleBookmarkFilter(!showOnlyBookmarked);
  });
  
  // Clear bookmarks filter bar
  resetFiltersBtn.addEventListener('click', () => {
    toggleBookmarkFilter(false);
  });
  
  // Search events
  searchInput.addEventListener('input', (e) => {
    searchQuery = e.target.value;
    if (searchQuery.trim()) {
      clearSearchBtn.style.display = 'block';
    } else {
      clearSearchBtn.style.display = 'none';
    }
    renderNews();
  });
  
  clearSearchBtn.addEventListener('click', () => {
    searchInput.value = '';
    searchQuery = '';
    clearSearchBtn.style.display = 'none';
    renderNews();
  });
  
  // Category tabs events
  categoriesList.addEventListener('click', (e) => {
    const tab = e.target.closest('.category-tab');
    if (!tab) return;
    
    // Toggle active class
    const tabs = categoriesList.querySelectorAll('.category-tab');
    tabs.forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
    
    currentCategory = tab.dataset.category;
    renderNews();
  });
  
  // Sort actions
  sortScoreBtn.addEventListener('click', () => {
    currentSort = 'score';
    sortScoreBtn.classList.add('active');
    sortTimeBtn.classList.remove('active');
    renderNews();
  });
  
  sortTimeBtn.addEventListener('click', () => {
    currentSort = 'time';
    sortTimeBtn.classList.add('active');
    sortScoreBtn.classList.remove('active');
    renderNews();
  });
  
  // Drawer buttons
  closeDrawerBtn.addEventListener('click', closeDrawer);
  drawerBackdrop.addEventListener('click', closeDrawer);
  
  drawerBookmarkBtn.addEventListener('click', () => {
    if (activeArticleId) {
      toggleBookmark(activeArticleId);
    }
  });
  
  drawerShareBtn.addEventListener('click', () => {
    copyCurrentSummaryToClipboard();
  });
  
  // ESC key to close drawer
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && activeArticleId) {
      closeDrawer();
    }
  });
}
