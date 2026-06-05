// 基本的JavaScript功能
document.addEventListener('DOMContentLoaded', function() {
    const apiBtn = document.getElementById('apiBtn');
    const resultDiv = document.getElementById('result');
    
    if (apiBtn) {
        apiBtn.addEventListener('click', function() {
            callApi();
        });
    }
});

// API 呼叫函式
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
            // 顯示緊急告示牌
            showSiteBroken();
        });
}

// 緊急處理函式
function showSiteBroken() {
    document.body.innerHTML = `
    <div style="
    display:flex;
    justify-content:center;
    align-items:center;
    height:100vh;
    font-size:48px;
    background:black;
    color:red;
    ">
    SITE BROKEN
    </div>
    `;
}

