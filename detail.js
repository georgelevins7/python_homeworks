const loading = document.getElementById('loading');
const errorEl = document.getElementById('error');
const card = document.getElementById('detail-card');

const id = new URLSearchParams(window.location.search).get('id');

async function loadTodo() {
  if (!id) {
    showError('No todo ID provided.');
    loading.classList.add('hidden');
    return;
  }

  try {
    const res = await fetch(`https://jsonplaceholder.typicode.com/todos/${id}`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const todo = await res.json();
    render(todo);
  } catch (err) {
    showError(`Failed to load todo: ${err.message}`);
  } finally {
    loading.classList.add('hidden');
  }
}

function render(todo) {
  document.getElementById('d-id').textContent = todo.id;
  document.getElementById('d-userId').textContent = todo.userId;
  document.getElementById('d-title').textContent = todo.title;

  const statusEl = document.getElementById('d-completed');
  statusEl.textContent = todo.completed ? 'Completed' : 'Not completed';
  statusEl.className = `detail-value status-badge ${todo.completed ? 'status-done' : 'status-pending'}`;

  card.classList.remove('hidden');
}

function showError(msg) {
  errorEl.textContent = msg;
  errorEl.classList.remove('hidden');
}

loadTodo();
