// Submit butonu yükleniyor efekti
const loginForm = document.getElementById('loginForm');
const submitBtn = document.getElementById('submitBtn');

if (loginForm && submitBtn) {
    loginForm.addEventListener('submit', () => {
        const btnText = submitBtn.querySelector('.btn-text');
        const btnSpinner = submitBtn.querySelector('.btn-spinner');
        
        // Şablondan (button.html) gelen yükleme metnini çekiyoruz
        const loadingText = submitBtn.getAttribute('data-loading-text');

        // Form gönderildiğinde butonu yükleme moduna al
        submitBtn.disabled = true;
        if (btnText && loadingText) btnText.textContent = loadingText;
        if (btnSpinner) btnSpinner.classList.remove('hidden');
    });
}

// Sayfa geri tuşuyla veya önbellekten yüklendiğinde butonu sıfırla
window.addEventListener('pageshow', (event) => {
    if (submitBtn) {
        const btnText = submitBtn.querySelector('.btn-text');
        const btnSpinner = submitBtn.querySelector('.btn-spinner');
        
        // Şablondan (button.html) gelen orijinal metni geri yüklüyoruz
        const initialText = submitBtn.getAttribute('data-initial-text');

        submitBtn.disabled = false;
        if (btnText && initialText) btnText.textContent = initialText;
        if (btnSpinner) btnSpinner.classList.add('hidden');
    }
});
