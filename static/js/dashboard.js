document.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.getElementById('sidebar');
    const closeBtn = document.getElementById('close-sidebar');
    const overlay = document.getElementById('sidebar-overlay');
    const navbar = document.getElementById('navbar');
    const mainContent = document.getElementById('main-content');

    // Not: openBtn (üç çizgi) kaldırıldığı için sadece mobil kapatma ve resize mantığı kaldı.
    
    const toggleSidebar = () => {
        const isHidden = sidebar.classList.contains('-translate-x-full');
        
        if (isHidden) {
            // Aç
            sidebar.classList.remove('-translate-x-full');
            overlay.classList.remove('hidden');
            setTimeout(() => overlay.classList.add('opacity-100'), 0);
            
            if (window.innerWidth >= 1024) {
                navbar.style.left = '288px';
                if (mainContent) mainContent.style.marginLeft = '288px';
            }
        } else {
            // Kapat
            sidebar.classList.add('-translate-x-full');
            overlay.classList.remove('opacity-100');
            setTimeout(() => overlay.classList.add('hidden'), 300);
            
            if (window.innerWidth >= 1024) {
                navbar.style.left = '0';
                if (mainContent) mainContent.style.marginLeft = '0';
            }
        }
    };

    if (closeBtn) closeBtn.addEventListener('click', toggleSidebar);
    if (overlay) overlay.addEventListener('click', toggleSidebar);

    // Pencere boyutu değiştiğinde sidebar durumunu kontrol et
    const handleResize = () => {
        if (window.innerWidth >= 1024) {
            sidebar.classList.remove('-translate-x-full');
            overlay.classList.add('hidden');
            navbar.style.left = '288px';
            if (mainContent) mainContent.style.marginLeft = '288px';
        } else {
            sidebar.classList.add('-translate-x-full');
            overlay.classList.add('hidden');
            navbar.style.left = '0';
            if (mainContent) mainContent.style.marginLeft = '0';
        }
    };

    window.addEventListener('resize', handleResize);
    handleResize(); // İlk yüklemede çalıştır
});
