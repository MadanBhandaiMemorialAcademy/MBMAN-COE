        // Mobile Menu Toggle
        const btn = document.getElementById('mobile-menu-btn');
        const menu = document.getElementById('mobile-menu');

        btn.addEventListener('click', () => {
            menu.classList.toggle('hidden');
        });

        // Smooth scroll for anchor links in menu
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                menu.classList.add('hidden'); // Close mobile menu on click
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });

        // Tab Switcher for Notices/Events
        function switchTab(tabName) {
            const noticesTab = document.getElementById('tab-notices');
            const eventsTab = document.getElementById('tab-events');
            const btnNotices = document.getElementById('btn-notices');
            const btnEvents = document.getElementById('btn-events');

            if (tabName === 'notices') {
                noticesTab.classList.remove('hidden');
                eventsTab.classList.add('hidden');
                
                btnNotices.classList.add('bg-mbman-blue', 'text-white', 'shadow-md');
                btnNotices.classList.remove('text-gray-600', 'hover:bg-gray-100');
                
                btnEvents.classList.remove('bg-mbman-blue', 'text-white', 'shadow-md');
                btnEvents.classList.add('text-gray-600', 'hover:bg-gray-100');
            } else {
                noticesTab.classList.add('hidden');
                eventsTab.classList.remove('hidden');
                
                btnEvents.classList.add('bg-mbman-blue', 'text-white', 'shadow-md');
                btnEvents.classList.remove('text-gray-600', 'hover:bg-gray-100');
                
                btnNotices.classList.remove('bg-mbman-blue', 'text-white', 'shadow-md');
                btnNotices.classList.add('text-gray-600', 'hover:bg-gray-100');
            }
        }

        // Tab Switcher for Faculty
        function switchFacultyTab(tabName) {
            const bitTab = document.getElementById('tab-faculty-bit');
            const agTab = document.getElementById('tab-faculty-ag');
            const btnBit = document.getElementById('btn-faculty-bit');
            const btnAg = document.getElementById('btn-faculty-ag');

            if (tabName === 'bit') {
                bitTab.classList.remove('hidden');
                agTab.classList.add('hidden');
                
                // Activate BIT button (blue)
                btnBit.classList.add('bg-mbman-blue', 'text-white', 'shadow-sm');
                btnBit.classList.remove('text-gray-600', 'hover:bg-gray-100');
                
                // Deactivate Ag button
                btnAg.classList.remove('bg-green-600', 'text-white', 'shadow-sm');
                btnAg.classList.add('text-gray-600', 'hover:bg-gray-100');
            } else {
                bitTab.classList.add('hidden');
                agTab.classList.remove('hidden');
                
                // Activate Ag button (green for differentiation)
                btnAg.classList.add('bg-green-600', 'text-white', 'shadow-sm');
                btnAg.classList.remove('text-gray-600', 'hover:bg-gray-100');
                
                // Deactivate BIT button
                btnBit.classList.remove('bg-mbman-blue', 'text-white', 'shadow-sm');
                btnBit.classList.add('text-gray-600', 'hover:bg-gray-100');
            }
        }

        // User Dropdown Toggle
        const userDropdownBtn = document.getElementById('user-dropdown-btn');
        const userDropdownMenu = document.getElementById('user-dropdown-menu');
        const userDropdownContainer = document.getElementById('user-dropdown-container');

        if (userDropdownBtn) {
            userDropdownBtn.addEventListener('click', () => {
                userDropdownMenu.classList.toggle('hidden');
            });

            // Close dropdown if clicking outside
            window.addEventListener('click', (e) => {
                if (userDropdownContainer && !userDropdownContainer.contains(e.target)) {
                    if (userDropdownMenu) {
                        userDropdownMenu.classList.add('hidden');
                    }
                }
            });
        }

        // --- REMOVED Authentication UI Toggle Function ---
        