// 基本的JavaScript功能

document.addEventListener('DOMContentLoaded', function() {
    // API按鈕點擊事件
    const apiBtn = document.getElementById('apiBtn');
    const resultDiv = document.getElementById('result');
    
    if (apiBtn) {
        apiBtn.addEventListener('click', function() {
            callApi();
        });
    }
});

function callApi() {
    const resultDiv = document.getElementById('result');
    
    fetch('/api/hello')
        .then(response => response.json())
        .then(data => {
            resultDiv.innerHTML = `<p>${data.message}</p><p>狀態: ${data.status}</p>`;
            resultDiv.style.display = 'block';
        })
        .catch(error => {
            console.error('錯誤:', error);
            resultDiv.innerHTML = '<p style="color: red;">API呼叫失敗</p>';
            resultDiv.style.display = 'block';
        });
}
