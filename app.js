const list = document.getElementById('todo-list');
const loading = document.getElementById('loading');
const errorEl = document.getElementById('error');
const pagination = document.getElementById('pagination');
const pageInfo = document.getElementById('page-info');
const searchInput = document.getElementById('search');
const filterUser = document.getElementById('filter-user');
const filterStatus = document.getElementById('filter-status');

const PER_PAGE = 10;
let allTodos = [];
let currentPage = 1;

async function loadTodos() {
  try {
    const res = await fetch('https://jsonplaceholder.typicode.com/todos');
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    allTodos = await res.json();
    populateUserFilter();
    refresh();
    pagination.classList.remove('hidden');
  } catch (err) {
    showError(`Failed to load todos: ${err.message}`);
  } finally {
    loading.classList.add('hidden');
  }
}

function populateUserFilter() {
  const ids = [...new Set(allTodos.map((t) => t.userId))].sort((a, b) => a - b);
  ids.forEach((id) => {
    const opt = document.createElement('option');
    opt.value = id;
    opt.textContent = `User ${id}`;
    filterUser.appendChild(opt);
  });
}

function getFiltered() {
  const q = searchInput.value.trim().toLowerCase();
  const userId = filterUser.value;
  const status = filterStatus.value;
  return allTodos.filter((t) => {
    if (q && !t.title.toLowerCase().includes(q)) return false;
    if (userId && t.userId !== Number(userId)) return false;
    if (status !== '' && String(t.completed) !== status) return false;
    return true;
  });
}

function renderPage(todos, page) {
  const start = (page - 1) * PER_PAGE;
  const slice = todos.slice(start, start + PER_PAGE);

  list.innerHTML = '';

  if (todos.length === 0) {
    list.innerHTML = '<li class="todo-item todo-empty">No results found</li>';
    pageInfo.textContent = '0 results';
    return;
  }

  slice.forEach((todo) => {
    const li = document.createElement('li');
    li.className = 'todo-item';
    li.innerHTML = `<span class="todo-text">${todo.title}</span>`;
    li.addEventListener('click', () => { window.location.href = `detail.html?id=${todo.id}`; });
    list.appendChild(li);
  });

  pageInfo.textContent = `${start + 1}–${Math.min(start + PER_PAGE, todos.length)} of ${todos.length}`;
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function renderPagination(todos) {
  const totalPages = Math.ceil(todos.length / PER_PAGE);
  pagination.innerHTML = '';

  if (totalPages <= 1) return;

  const prev = btn('← Previous', currentPage === 1);
  prev.addEventListener('click', () => { currentPage--; refresh(); });
  pagination.appendChild(prev);

  for (let p = 1; p <= totalPages; p++) {
    const b = btn(String(p), false);
    if (p === currentPage) b.classList.add('active');
    b.addEventListener('click', () => { currentPage = p; refresh(); });
    pagination.appendChild(b);
  }

  const next = btn('Next →', currentPage === totalPages);
  next.addEventListener('click', () => { currentPage++; refresh(); });
  pagination.appendChild(next);
}

function refresh() {
  const filtered = getFiltered();
  renderPage(filtered, currentPage);
  renderPagination(filtered);
}

function resetAndRefresh() {
  currentPage = 1;
  refresh();
}

searchInput.addEventListener('input', resetAndRefresh);
filterUser.addEventListener('change', resetAndRefresh);
filterStatus.addEventListener('change', resetAndRefresh);

function btn(label, disabled) {
  const b = document.createElement('button');
  b.textContent = label;
  b.disabled = disabled;
  return b;
}

function showError(msg) {
  errorEl.textContent = msg;
  errorEl.classList.remove('hidden');
}

loadTodos();

