// --- Initialize AOS ---
AOS.init({
    duration: 800,
    once: true,
    offset: 50,
});

const projects_cart = document.querySelectorAll('.project-card');
const portfolio = document.querySelector('#portfolio');


function closeModal() {
    projects_cart.forEach(p => {
        if (p.classList.contains('active')) {
            p.classList.remove('active');
        }
    });
    document.body.style.overflow = ''; // Re-enable scrolling
    document.body.classList.remove('project-modal-open'); // aos active

    document.removeEventListener('keydown', escHandler);
}

function escHandler(e) {
    if (e.key === 'Escape') closeModal();
}

document.addEventListener('DOMContentLoaded', () => {
    // --- project modal ---

    projects_cart.forEach(project => {
        project.addEventListener('click', () => {
            // Open project modal
            closeModal();

            // aos not active
            document.body.classList.add('project-modal-open');

            // Toggle overlay
            document.body.style.overflow = 'hidden'; // Prevent scrolling

            // Toggle current project
            project.classList.add('active'); // Ensure the active class is added

            // close on Escape
            document.addEventListener('keydown', escHandler);
        }, true);

    });

    // Close project when clicking overlay
    document.querySelectorAll('.overlay').forEach(overlay => {
        overlay.addEventListener('click', () => {
            closeModal();
        }, true);
    });


    // --- Theme Toggler ---
    const themeToggleBtn = document.getElementById('theme-toggle');
    const darkIcon = document.getElementById('theme-toggle-dark-icon');
    const lightIcon = document.getElementById('theme-toggle-light-icon');

    const htmlTag = document.documentElement;

    if (localStorage.getItem('theme') === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        htmlTag.classList.add('dark');
        lightIcon.classList.remove('hidden');
    } else {
        htmlTag.classList.remove('dark');
        darkIcon.classList.remove('hidden');
    }
    themeToggleBtn.addEventListener('click', () => {
        darkIcon.classList.toggle('hidden');
        lightIcon.classList.toggle('hidden');
        if (localStorage.getItem('theme')) {
            if (localStorage.getItem('theme') === 'light') {
                htmlTag.classList.add('dark');
                localStorage.setItem('theme', 'dark');
            } else {
                htmlTag.classList.remove('dark');
                localStorage.setItem('theme', 'light');
            }
        } else {
            if (htmlTag.classList.contains('dark')) {
                htmlTag.classList.remove('dark');
                localStorage.setItem('theme', 'light');
            } else {
                htmlTag.classList.add('dark');
                localStorage.setItem('theme', 'dark');
            }
        }
    });

    // --- Portfolio Filter ---
    const filterBtns = document.querySelectorAll('#portfolio-filters .filter-btn');
    const portfolioGrid = document.getElementById('portfolio-grid');
    const projects = portfolioGrid.querySelectorAll('.project-card');
    function setActiveButton(activeBtn) {
        filterBtns.forEach(btn => {
            btn.classList.remove('active');
        });
        activeBtn.classList.add('active');
    }
    setActiveButton(document.querySelector('.filter-btn[data-filter="all"]'));
    filterBtns.forEach(button => {
        button.addEventListener('click', () => {
            const filter = button.getAttribute('data-filter');
            setActiveButton(button);
            projects.forEach(project => {
                const category = project.getAttribute('data-category');
                if (filter === 'all' || filter === category) {
                    project.style.display = 'block';
                } else {
                    project.style.display = 'none';
                }
            });
        });
    });
    // --- Copy to Clipboard ---
    const copyButtons = document.querySelectorAll('.copy-btn');
    copyButtons.forEach(button => {
        button.addEventListener('click', () => {
            const textToCopy = button.getAttribute('data-copy');
            const textArea = document.createElement('textarea');
            textArea.value = textToCopy;
            document.body.appendChild(textArea);
            textArea.select();
            try {
                document.execCommand('copy');
                const copyIcon = button.querySelector('.copy-icon');
                const copyFeedback = button.querySelector('.copy-feedback');
                copyIcon.classList.add('hidden');
                copyFeedback.classList.remove('hidden');
                setTimeout(() => {
                    copyIcon.classList.remove('hidden');
                    copyFeedback.classList.add('hidden');
                }, 2000);
            } catch (err) {
                console.error('Failed to copy text: ', err);
            }
            document.body.removeChild(textArea);
        });
    });
});