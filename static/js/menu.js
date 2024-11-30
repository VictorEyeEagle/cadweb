    // Sidebar toggle
    document.getElementById('toggle-sidebar').addEventListener('click', function () {
        document.getElementById('sidebar').classList.toggle('active');
        document.getElementById('content').classList.toggle('active');
    });

    // Submenu toggle
    document.querySelectorAll('.nav-item').forEach(function (item) {
        item.addEventListener('click', function () {
            if (this.classList.contains('open')) {
                this.classList.remove('open');
            } else {
                // Fechar outros menus abertos
                document.querySelectorAll('.nav-item.open').forEach(function (openItem) {
                    openItem.classList.remove('open');
                });
                this.classList.add('open');
            }
        });
    });