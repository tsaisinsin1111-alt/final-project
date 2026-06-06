document.addEventListener('DOMContentLoaded', function() {
    const apiBtn = document.getElementById('apiBtn');
    const resultDiv = document.getElementById('result');
    const recommendBtn = document.getElementById('recommendBtn');

    if (apiBtn) {
        apiBtn.addEventListener('click', function() {
            callApi();
        });
    }

    if (recommendBtn) {
        recommendBtn.addEventListener('click', function() {
            const budget = document.getElementById('budget').value;
            const type = document.getElementById('type').value;
            callRecommend(budget, type);
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
            showSiteBroken();
        });
}

function callRecommend(budget, type) {
    const recommendResult = document.getElementById('recommendResult');
    fetch('/recommend', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ budget, type })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            recommendResult.innerHTML =
                `<p>推薦商品：${data.brand} - ${data.type}，價格 ${data.price}</p>`;
        } else {
            recommendResult.innerHTML = `<p>${data.message}</p>`;
        }
    })
    .catch(error => {
        console.error('錯誤:', error);
        showSiteBroken();
    });
}

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





