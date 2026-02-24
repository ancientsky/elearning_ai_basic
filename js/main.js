/**
 * 疾管署第一年基礎班線上自學平台
 * 主要 JavaScript 功能
 */

// ==================== Global State ====================
const APP_STATE = {
    progress: {},
    currentModule: null,
    currentUnit: 0
};

// ==================== LocalStorage Keys ====================
const STORAGE_KEYS = {
    PROGRESS: 'cdc_learning_progress',
    QUIZ_RESULTS: 'cdc_quiz_results',
    CHECKLIST: 'cdc_checklist'
};

// ==================== Initialization ====================
document.addEventListener('DOMContentLoaded', () => {
    loadProgress();
    initMobileMenu();
    initTabs();
    initAccordions();
    initQuizzes();
    initDragDrop();
    initFillBlanks();
    initChecklists();
    initCopyButtons();
    initModuleNavigation();
    initSidebarAutoHide();
    updateProgressDisplay();
    initLearningMap();
});

// ==================== Progress Tracking ====================
function loadProgress() {
    const saved = localStorage.getItem(STORAGE_KEYS.PROGRESS);
    if (saved) {
        APP_STATE.progress = JSON.parse(saved);
    } else {
        // Initialize default progress
        APP_STATE.progress = {
            module0: { completed: false, units: {}, quiz: null },
            module1: { completed: false, units: {}, quiz: null },
            module2: { completed: false, units: {}, quiz: null },
            module3: { completed: false, units: {}, quiz: null },
            module4: { completed: false, units: {}, quiz: null },
            module5: { completed: false, units: {}, quiz: null }
        };
    }
}

function saveProgress() {
    localStorage.setItem(STORAGE_KEYS.PROGRESS, JSON.stringify(APP_STATE.progress));
    updateProgressDisplay();
}

function markUnitComplete(moduleId, unitId) {
    if (!APP_STATE.progress[moduleId]) {
        APP_STATE.progress[moduleId] = { completed: false, units: {}, quiz: null };
    }
    APP_STATE.progress[moduleId].units[unitId] = true;

    // Check if all units in module are complete
    checkModuleCompletion(moduleId);
    saveProgress();
}

function checkModuleCompletion(moduleId) {
    const moduleProgress = APP_STATE.progress[moduleId];
    const totalUnits = document.querySelectorAll(`[data-module="${moduleId}"] .unit-container`).length;
    const completedUnits = Object.keys(moduleProgress.units).filter(k => moduleProgress.units[k]).length;

    if (completedUnits >= totalUnits && moduleProgress.quiz !== null) {
        moduleProgress.completed = true;
    }
}

function getOverallProgress() {
    const modules = Object.keys(APP_STATE.progress);
    const completed = modules.filter(m => APP_STATE.progress[m].completed).length;
    return Math.round((completed / modules.length) * 100);
}

function getModuleProgress(moduleId) {
    const moduleProgress = APP_STATE.progress[moduleId];
    if (!moduleProgress) return 0;

    let totalUnits = 5; // Default

    // In index.html, we can't count .unit-container elements
    const path = window.location.pathname;
    if (path.endsWith('index.html') || path === '/' || !path.includes('/modules/')) {
        // Hardcoded unit counts for each module
        const unitCounts = {
            'module0': 3,
            'module1': 4,
            'module2': 7,
            'module3': 5,
            'module4': 5,
            'module5': 4
        };
        totalUnits = unitCounts[moduleId] || 5;
    } else {
        totalUnits = document.querySelectorAll(`[data-module="${moduleId}"] .unit-container`).length || 5;
    }

    const completedUnits = Object.keys(moduleProgress.units).filter(k => moduleProgress.units[k]).length;

    return Math.round((completedUnits / totalUnits) * 100);
}

function updateProgressDisplay() {
    // Update learning map
    const mapSteps = document.querySelectorAll('.map-step');
    mapSteps.forEach(step => {
        const moduleId = step.dataset.module;
        if (APP_STATE.progress[moduleId]?.completed) {
            step.classList.add('completed');
            step.classList.remove('current');
        }
    });

    // Update module cards
    const moduleCards = document.querySelectorAll('.module-card');
    moduleCards.forEach(card => {
        const moduleId = card.dataset.module;
        const progress = getModuleProgress(moduleId);
        const progressFill = card.querySelector('.progress-fill');
        const progressText = card.querySelector('.progress-text');

        if (progressFill) progressFill.style.width = `${progress}%`;
        if (progressText) progressText.textContent = `${progress}% 完成`;

        if (APP_STATE.progress[moduleId]?.completed) {
            card.classList.add('completed');
        }
    });

    // Update overall progress
    const overallProgress = getOverallProgress();
    const overallDisplay = document.querySelector('.overall-progress h4');
    if (overallDisplay) {
        overallDisplay.textContent = `${overallProgress}%`;
    }

    // Update sidebar navigation
    updateSidebarNavigation();
}

function updateSidebarNavigation() {
    const navLinks = document.querySelectorAll('.module-nav-link');
    navLinks.forEach(link => {
        const unitId = link.dataset.unit;
        const moduleId = APP_STATE.currentModule;

        if (moduleId && APP_STATE.progress[moduleId]?.units[unitId]) {
            link.classList.add('completed');
        }
    });
}

// ==================== Learning Map ====================
function initLearningMap() {
    const mapSteps = document.querySelectorAll('.map-step');
    mapSteps.forEach(step => {
        step.addEventListener('click', () => {
            const moduleId = step.dataset.module;
            if (!step.classList.contains('locked')) {
                window.location.href = `modules/${moduleId}.html`;
            }
        });
    });
}

// ==================== Mobile Menu ====================
function initMobileMenu() {
    const menuBtn = document.querySelector('.mobile-menu-btn');
    const nav = document.querySelector('nav');

    if (menuBtn && nav) {
        menuBtn.addEventListener('click', () => {
            nav.classList.toggle('show');
        });
    }
}

// ==================== Tabs ====================
function initTabs() {
    const tabGroups = document.querySelectorAll('.tabs');

    tabGroups.forEach(tabGroup => {
        const tabs = tabGroup.querySelectorAll('.tab');
        const contents = tabGroup.parentElement.querySelectorAll('.tab-content');

        tabs.forEach(tab => {
            tab.addEventListener('click', () => {
                // Remove active from all
                tabs.forEach(t => t.classList.remove('active'));
                contents.forEach(c => c.classList.remove('active'));

                // Add active to clicked
                tab.classList.add('active');
                const targetId = tab.dataset.tab;
                const targetContent = document.getElementById(targetId);
                if (targetContent) targetContent.classList.add('active');
            });
        });
    });
}

// ==================== Accordions ====================
function initAccordions() {
    const accordionHeaders = document.querySelectorAll('.accordion-header');

    accordionHeaders.forEach(header => {
        header.addEventListener('click', () => {
            const body = header.nextElementSibling;
            const isActive = header.classList.contains('active');

            // Close all others in same accordion
            const accordion = header.closest('.accordion');
            accordion.querySelectorAll('.accordion-header').forEach(h => {
                h.classList.remove('active');
                h.nextElementSibling.classList.remove('show');
            });

            // Toggle clicked
            if (!isActive) {
                header.classList.add('active');
                body.classList.add('show');
            }
        });
    });
}

// ==================== Sound Effects ====================
let _audioCtx = null;

function playSound(isCorrect) {
    try {
        if (!_audioCtx) _audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        const ctx = _audioCtx;
        const now = ctx.currentTime;
        const gain = ctx.createGain();
        gain.connect(ctx.destination);

        if (isCorrect) {
            // Ascending two-note chime
            gain.gain.setValueAtTime(0.18, now);
            gain.gain.exponentialRampToValueAtTime(0.001, now + 0.5);
            const o1 = ctx.createOscillator();
            o1.type = 'sine';
            o1.frequency.value = 523.25; // C5
            o1.connect(gain);
            o1.start(now);
            o1.stop(now + 0.2);

            const gain2 = ctx.createGain();
            gain2.connect(ctx.destination);
            gain2.gain.setValueAtTime(0.18, now + 0.15);
            gain2.gain.exponentialRampToValueAtTime(0.001, now + 0.55);
            const o2 = ctx.createOscillator();
            o2.type = 'sine';
            o2.frequency.value = 659.25; // E5
            o2.connect(gain2);
            o2.start(now + 0.15);
            o2.stop(now + 0.55);
        } else {
            // Short low buzz
            gain.gain.setValueAtTime(0.15, now);
            gain.gain.exponentialRampToValueAtTime(0.001, now + 0.3);
            const o = ctx.createOscillator();
            o.type = 'sine';
            o.frequency.value = 200;
            o.connect(gain);
            o.start(now);
            o.stop(now + 0.3);
        }
    } catch (e) {
        // Silently ignore if AudioContext is unavailable
    }
}

// ==================== Quiz System ====================
function initQuizzes() {
    const quizContainers = document.querySelectorAll('.quiz-container');

    quizContainers.forEach(quiz => {
        const options = quiz.querySelectorAll('.quiz-option');
        const submitBtn = quiz.querySelector('.quiz-submit');
        const feedback = quiz.querySelector('.quiz-feedback');
        const isMultiSelect = quiz.classList.contains('multi-select');

        options.forEach(option => {
            const checkbox = option.querySelector('input[type="checkbox"]');
            const radio = option.querySelector('input[type="radio"]');

            if (isMultiSelect && checkbox) {
                // For multi-select with checkboxes
                checkbox.addEventListener('change', () => {
                    option.classList.toggle('selected', checkbox.checked);
                });
                // Also handle label click
                option.addEventListener('click', (e) => {
                    if (e.target !== checkbox) {
                        // Click was on label, checkbox will auto-toggle
                        setTimeout(() => {
                            option.classList.toggle('selected', checkbox.checked);
                        }, 0);
                    }
                });
            } else {
                // For single select (radio or no input)
                option.addEventListener('click', () => {
                    options.forEach(o => o.classList.remove('selected'));
                    option.classList.add('selected');
                    // If there's a radio button, check it
                    if (radio) radio.checked = true;
                });
            }
        });

        if (submitBtn) {
            submitBtn.addEventListener('click', () => checkQuizAnswer(quiz));
        }
    });
}

function checkQuizAnswer(quizContainer) {
    const selected = quizContainer.querySelectorAll('.quiz-option.selected');
    const feedback = quizContainer.querySelector('.quiz-feedback');
    const options = quizContainer.querySelectorAll('.quiz-option');

    if (selected.length === 0) {
        showFeedback(feedback, false, '請選擇一個答案');
        return;
    }

    let isCorrect = true;

    // Check for multi-select quiz
    if (quizContainer.classList.contains('multi-select')) {
        const correctAnswers = quizContainer.dataset.correct.split(',');
        const selectedAnswers = Array.from(selected).map(s => s.dataset.answer);

        isCorrect = correctAnswers.length === selectedAnswers.length &&
            correctAnswers.every(a => selectedAnswers.includes(a));
    } else {
        // Single select
        const correctAnswer = quizContainer.dataset.correct;
        const selectedAnswer = selected[0].dataset.answer;
        isCorrect = selectedAnswer === correctAnswer;
    }

    // Show visual feedback on options
    options.forEach(option => {
        const isOptionCorrect = quizContainer.classList.contains('multi-select')
            ? quizContainer.dataset.correct.split(',').includes(option.dataset.answer)
            : option.dataset.answer === quizContainer.dataset.correct;

        if (isOptionCorrect) {
            option.classList.add('correct');
        } else if (option.classList.contains('selected')) {
            option.classList.add('incorrect');
        }
    });

    // Show feedback
    const feedbackMessage = isCorrect
        ? (quizContainer.dataset.successMsg || '正確！做得好！')
        : (quizContainer.dataset.errorMsg || '不正確，請再試試。');

    showFeedback(feedback, isCorrect, feedbackMessage);
    playSound(isCorrect);

    // Show explanation if exists
    const explanation = quizContainer.querySelector('.quiz-explanation');
    if (explanation) {
        explanation.style.display = 'block';
        // Smooth scroll to explanation
        setTimeout(() => {
            explanation.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }, 100);
    }

    // Record result
    const quizId = quizContainer.dataset.quizId;
    const moduleId = APP_STATE.currentModule;
    if (moduleId && quizId) {
        recordQuizResult(moduleId, quizId, isCorrect);
    }

    // Disable further interaction if correct
    if (isCorrect) {
        options.forEach(o => o.style.pointerEvents = 'none');
        const submitBtn = quizContainer.querySelector('.quiz-submit');
        if (submitBtn) submitBtn.disabled = true;
    }
}

function showFeedback(feedbackElement, isCorrect, message) {
    if (!feedbackElement) return;

    feedbackElement.className = 'quiz-feedback show';
    feedbackElement.classList.add(isCorrect ? 'correct' : 'incorrect');
    feedbackElement.innerHTML = `
        <span class="feedback-icon">${isCorrect ? '✓' : '✗'}</span>
        <span class="feedback-text">${message}</span>
    `;
}

function recordQuizResult(moduleId, quizId, isCorrect) {
    let results = JSON.parse(localStorage.getItem(STORAGE_KEYS.QUIZ_RESULTS) || '{}');
    if (!results[moduleId]) results[moduleId] = {};
    results[moduleId][quizId] = isCorrect;
    localStorage.setItem(STORAGE_KEYS.QUIZ_RESULTS, JSON.stringify(results));

    // Update module progress
    if (isCorrect) {
        APP_STATE.progress[moduleId].quiz = true;
        saveProgress();
    }
}

// ==================== Drag and Drop ====================
function initDragDrop() {
    const dragItems = document.querySelectorAll('.drag-item');
    const dropZones = document.querySelectorAll('.drop-zone');

    dragItems.forEach(item => {
        item.draggable = true;

        item.addEventListener('dragstart', (e) => {
            item.classList.add('dragging');
            e.dataTransfer.setData('text/plain', item.dataset.value || item.textContent);
            e.dataTransfer.setData('element-id', item.id || '');
        });

        item.addEventListener('dragend', () => {
            item.classList.remove('dragging');
        });
    });

    dropZones.forEach(zone => {
        zone.addEventListener('dragover', (e) => {
            e.preventDefault();
            zone.classList.add('over');
        });

        zone.addEventListener('dragleave', () => {
            zone.classList.remove('over');
        });

        zone.addEventListener('drop', (e) => {
            e.preventDefault();
            zone.classList.remove('over');

            const value = e.dataTransfer.getData('text/plain');
            const elementId = e.dataTransfer.getData('element-id');

            // Clear existing content
            zone.innerHTML = '';

            // Create new item in drop zone
            const newItem = document.createElement('span');
            newItem.className = 'drag-item';
            newItem.textContent = value;
            newItem.dataset.value = value;
            zone.appendChild(newItem);
            zone.classList.add('filled');

            // Hide original item
            if (elementId) {
                const originalItem = document.getElementById(elementId);
                if (originalItem) originalItem.style.visibility = 'hidden';
            }

            // Check if all zones are filled
            checkDragDropCompletion(zone.closest('.drag-drop-container'));
        });
    });
}

function checkDragDropCompletion(container) {
    if (!container) return;

    const zones = container.querySelectorAll('.drop-zone');
    const allFilled = Array.from(zones).every(z => z.classList.contains('filled'));

    if (allFilled) {
        const checkBtn = container.querySelector('.check-answer');
        if (checkBtn) checkBtn.disabled = false;
    }
}

function checkDragDropAnswer(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    const zones = container.querySelectorAll('.drop-zone');
    let allCorrect = true;

    zones.forEach(zone => {
        const expected = zone.dataset.expected;
        const actual = zone.querySelector('.drag-item')?.dataset.value;

        if (actual === expected) {
            zone.classList.add('correct');
        } else {
            zone.classList.add('incorrect');
            allCorrect = false;
        }
    });

    const feedback = container.querySelector('.drag-drop-feedback');
    if (feedback) {
        showFeedback(feedback, allCorrect, allCorrect ? '完全正確！' : '有些位置不對，請再試試。');
    }
    playSound(allCorrect);

    return allCorrect;
}

function resetDragDrop(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    // Clear drop zones
    const zones = container.querySelectorAll('.drop-zone');
    zones.forEach(zone => {
        zone.innerHTML = '';
        zone.classList.remove('filled', 'correct', 'incorrect');
    });

    // Show all drag items
    const items = container.querySelectorAll('.drag-item');
    items.forEach(item => {
        item.style.visibility = 'visible';
    });

    // Hide feedback
    const feedback = container.querySelector('.drag-drop-feedback');
    if (feedback) feedback.classList.remove('show');

    // Disable check button
    const checkBtn = container.querySelector('.check-answer');
    if (checkBtn) checkBtn.disabled = true;
}

// ==================== Fill in the Blanks ====================
function initFillBlanks() {
    const fillBlankContainers = document.querySelectorAll('.fill-blank-container');

    fillBlankContainers.forEach(container => {
        const inputs = container.querySelectorAll('.fill-blank-input');
        const selects = container.querySelectorAll('.fill-blank-select');

        inputs.forEach(input => {
            input.addEventListener('input', () => {
                input.classList.remove('correct', 'incorrect');
            });
        });

        selects.forEach(select => {
            select.addEventListener('change', () => {
                select.classList.remove('correct', 'incorrect');
            });
        });
    });
}

function checkFillBlankAnswer(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    const inputs = container.querySelectorAll('.fill-blank-input, .fill-blank-select');
    let allCorrect = true;

    inputs.forEach(input => {
        const expected = input.dataset.answer.toLowerCase().trim();
        const actual = input.value.toLowerCase().trim();

        // Support multiple acceptable answers separated by |
        const acceptableAnswers = expected.split('|').map(a => a.trim());

        if (acceptableAnswers.includes(actual)) {
            input.classList.add('correct');
            input.classList.remove('incorrect');
        } else {
            input.classList.add('incorrect');
            input.classList.remove('correct');
            allCorrect = false;
        }
    });

    const feedback = container.querySelector('.fill-blank-feedback');
    if (feedback) {
        showFeedback(feedback, allCorrect, allCorrect ? '全部正確！' : '有些答案不正確，請再檢查。');
    }
    playSound(allCorrect);

    return allCorrect;
}

function showFillBlankAnswers(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    const inputs = container.querySelectorAll('.fill-blank-input, .fill-blank-select');
    inputs.forEach(input => {
        const answer = input.dataset.answer.split('|')[0]; // Show first acceptable answer
        input.value = answer;
        input.classList.add('correct');
    });
}

// ==================== Checklists ====================
function initChecklists() {
    // Load saved checklist state
    const saved = JSON.parse(localStorage.getItem(STORAGE_KEYS.CHECKLIST) || '{}');

    const checkboxes = document.querySelectorAll('.checklist-checkbox');
    checkboxes.forEach(checkbox => {
        const itemId = checkbox.closest('.checklist-item').dataset.itemId;

        // Restore state
        if (saved[itemId]) {
            checkbox.classList.add('checked');
            checkbox.innerHTML = '✓';
            checkbox.closest('.checklist-item').classList.add('checked');
        }

        checkbox.addEventListener('click', () => {
            checkbox.classList.toggle('checked');
            const isChecked = checkbox.classList.contains('checked');
            checkbox.innerHTML = isChecked ? '✓' : '';
            checkbox.closest('.checklist-item').classList.toggle('checked', isChecked);

            // Save state
            saved[itemId] = isChecked;
            localStorage.setItem(STORAGE_KEYS.CHECKLIST, JSON.stringify(saved));
        });
    });
}

// ==================== Copy Buttons ====================
function initCopyButtons() {
    const copyButtons = document.querySelectorAll('.btn-copy, [data-copy]');

    copyButtons.forEach(btn => {
        btn.addEventListener('click', async () => {
            const targetId = btn.dataset.copyTarget;
            const target = targetId ? document.getElementById(targetId) : btn.previousElementSibling;

            if (!target) return;

            let textToCopy = target.textContent || target.value;

            // Clean up the text (remove extra whitespace but preserve structure)
            textToCopy = textToCopy.replace(/^\s+/gm, '').trim();

            try {
                await navigator.clipboard.writeText(textToCopy);

                // Visual feedback
                const originalText = btn.innerHTML;
                btn.innerHTML = '已複製！';
                btn.classList.add('copied');

                setTimeout(() => {
                    btn.innerHTML = originalText;
                    btn.classList.remove('copied');
                }, 2000);
            } catch (err) {
                console.error('Copy failed:', err);
                // Fallback for older browsers
                const textarea = document.createElement('textarea');
                textarea.value = textToCopy;
                document.body.appendChild(textarea);
                textarea.select();
                document.execCommand('copy');
                document.body.removeChild(textarea);

                btn.innerHTML = '已複製！';
                setTimeout(() => {
                    btn.innerHTML = '複製';
                }, 2000);
            }
        });
    });
}

// ==================== Module Navigation ====================
function initModuleNavigation() {
    // Get current module from page
    const moduleContainer = document.querySelector('[data-module]');
    if (moduleContainer) {
        APP_STATE.currentModule = moduleContainer.dataset.module;
    }

    // Unit navigation
    const navLinks = document.querySelectorAll('.module-nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const unitIndex = parseInt(link.dataset.unit);
            showUnit(unitIndex);

            // Update active state
            navLinks.forEach(l => l.classList.remove('active'));
            link.classList.add('active');
        });
    });

    // Next/Previous buttons
    const prevBtn = document.querySelector('.prev-unit');
    const nextBtn = document.querySelector('.next-unit');

    if (prevBtn) {
        prevBtn.addEventListener('click', () => {
            const current = getCurrentUnitIndex();
            if (current > 0) showUnit(current - 1);
        });
    }

    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            const current = getCurrentUnitIndex();
            const total = document.querySelectorAll('.unit-container').length;
            if (current < total - 1) {
                // Mark current unit as complete
                markUnitComplete(APP_STATE.currentModule, `unit${current}`);
                showUnit(current + 1);
            }
        });
    }

    // Complete module button
    const completeBtn = document.querySelector('.complete-module');
    if (completeBtn) {
        completeBtn.addEventListener('click', (e) => {
            // 防止 a tag 直接跳轉導致還沒存完就不見
            if (completeBtn.tagName.toLowerCase() === 'a') {
                e.preventDefault();
            }

            const moduleId = APP_STATE.currentModule;
            const current = getCurrentUnitIndex();

            // 將最後一個單元也標記為已完成
            markUnitComplete(moduleId, `unit${current}`);

            APP_STATE.progress[moduleId].completed = true;
            saveProgress();

            // Show completion message or navigate
            if (typeof showCompletionModal === 'function') {
                showCompletionModal(moduleId);
            }

            // 如果是 a tag，在存檔完成後手動跳轉
            if (completeBtn.tagName.toLowerCase() === 'a') {
                const href = completeBtn.getAttribute('href');
                if (href && href !== '#') {
                    // 給一點點時間讓 localStorage 確實寫入
                    setTimeout(() => {
                        window.location.href = href;
                    }, 100);
                }
            }
        });
    }

    // 特別處理模組 5 的「前往領取結業證書」大綠色按鈕
    const certBtn = document.querySelector('a[href="../certificate.html"]');
    if (certBtn) {
        certBtn.addEventListener('click', (e) => {
            e.preventDefault();

            const moduleId = APP_STATE.currentModule;
            const current = getCurrentUnitIndex();

            // 將最後一個單元標記為已完成，確保進度 100%
            if (moduleId) {
                markUnitComplete(moduleId, `unit${current}`);
                APP_STATE.progress[moduleId].completed = true;
                saveProgress();
            }

            // 給一點點時間讓 localStorage 確實寫入
            setTimeout(() => {
                window.location.href = certBtn.getAttribute('href');
            }, 100);
        });
    }
}

function getCurrentUnitIndex() {
    const activeUnit = document.querySelector('.unit-container.active');
    if (activeUnit) {
        return parseInt(activeUnit.dataset.unitIndex) || 0;
    }
    return 0;
}

function showUnit(index) {
    // Show sidebar when switching units (may be hidden by scroll)
    const sidebar = document.querySelector('.module-sidebar');
    if (sidebar) sidebar.classList.remove('sidebar-hidden');

    const units = document.querySelectorAll('.unit-container');
    const navLinks = document.querySelectorAll('.module-nav-link');

    units.forEach((unit, i) => {
        unit.classList.toggle('active', i === index);
    });

    navLinks.forEach((link, i) => {
        link.classList.toggle('active', i === index);
    });

    APP_STATE.currentUnit = index;

    // Update navigation buttons
    updateNavigationButtons(index, units.length);

    // Scroll sidebar nav to show active link
    const activeNavLink = navLinks[index];
    if (activeNavLink) {
        // Small delay to ensure DOM is updated
        setTimeout(() => {
            activeNavLink.scrollIntoView({
                behavior: 'smooth',
                inline: 'center',
                block: 'nearest'
            });
        }, 50);
    }

    // Scroll to top of content
    document.querySelector('.module-content')?.scrollIntoView({ behavior: 'smooth' });
}

function updateNavigationButtons(currentIndex, totalUnits) {
    const prevBtn = document.querySelector('.prev-unit');
    const nextBtn = document.querySelector('.next-unit');
    const completeBtn = document.querySelector('.complete-module');

    if (prevBtn) prevBtn.style.display = currentIndex === 0 ? 'none' : 'inline-flex';

    if (nextBtn && completeBtn) {
        const isLastUnit = currentIndex === totalUnits - 1;
        nextBtn.style.display = isLastUnit ? 'none' : 'inline-flex';
        completeBtn.style.display = isLastUnit ? 'inline-flex' : 'none';
    }
}

// ==================== Sidebar Auto-Hide on Mobile ====================
function initSidebarAutoHide() {
    const sidebar = document.querySelector('.module-sidebar');
    if (!sidebar) return;

    let lastScrollY = window.scrollY;
    let ticking = false;
    const SCROLL_THRESHOLD = 10;

    window.addEventListener('scroll', () => {
        if (ticking) return;
        ticking = true;

        requestAnimationFrame(() => {
            const currentScrollY = window.scrollY;
            const delta = currentScrollY - lastScrollY;
            const isMobile = window.matchMedia('(max-width: 860px)').matches;

            if (isMobile && Math.abs(delta) > SCROLL_THRESHOLD) {
                if (delta > 0 && currentScrollY > 150) {
                    sidebar.classList.add('sidebar-hidden');
                } else if (delta < 0) {
                    sidebar.classList.remove('sidebar-hidden');
                }
            }

            if (!isMobile) {
                sidebar.classList.remove('sidebar-hidden');
            }

            lastScrollY = currentScrollY;
            ticking = false;
        });
    });
}

function showCompletionModal(moduleId) {
    const modal = document.createElement('div');
    modal.className = 'completion-modal';
    modal.innerHTML = `
        <div class="modal-overlay"></div>
        <div class="modal-content">
            <div class="modal-icon">🎉</div>
            <h3>恭喜完成！</h3>
            <p>您已完成本模組的學習。</p>
            <div class="modal-buttons">
                <a href="../index.html" class="btn btn-primary">返回首頁</a>
                <a href="${getNextModuleUrl(moduleId)}" class="btn btn-secondary">下一模組</a>
            </div>
        </div>
    `;

    // Add modal styles
    const style = document.createElement('style');
    style.textContent = `
        .completion-modal {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            z-index: 9999;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .modal-overlay {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0,0,0,0.5);
        }
        .modal-content {
            position: relative;
            background: white;
            padding: 40px;
            border-radius: 16px;
            text-align: center;
            max-width: 400px;
            animation: fadeIn 0.3s ease;
        }
        .modal-icon {
            font-size: 4rem;
            margin-bottom: 16px;
        }
        .modal-content h3 {
            font-size: 1.5rem;
            margin-bottom: 12px;
        }
        .modal-content p {
            color: #666;
            margin-bottom: 24px;
        }
        .modal-buttons {
            display: flex;
            gap: 12px;
            justify-content: center;
        }
    `;

    document.head.appendChild(style);
    document.body.appendChild(modal);

    // Close on overlay click
    modal.querySelector('.modal-overlay').addEventListener('click', () => {
        modal.remove();
    });
}

function getNextModuleUrl(currentModuleId) {
    const modules = ['module0', 'module1', 'module2', 'module3', 'module4', 'module5'];
    const currentIndex = modules.indexOf(currentModuleId);
    if (currentIndex < modules.length - 1) {
        return `${modules[currentIndex + 1]}.html`;
    }
    return '../index.html';
}

// ==================== Scenario Judgment Quiz ====================
function initScenarioQuiz(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    const checkboxes = container.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(cb => {
        cb.addEventListener('change', () => {
            cb.closest('.scenario-option').classList.toggle('selected', cb.checked);
        });
    });
}

function checkScenarioAnswer(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    const options = container.querySelectorAll('.scenario-option');
    const correctAnswers = container.dataset.correct.split(',');
    let score = 0;
    let total = correctAnswers.length;

    options.forEach(option => {
        const checkbox = option.querySelector('input[type="checkbox"]');
        const value = checkbox.value;
        const isCorrect = correctAnswers.includes(value);
        const isSelected = checkbox.checked;

        option.classList.remove('correct', 'incorrect');

        if (isCorrect && isSelected) {
            option.classList.add('correct');
            score++;
        } else if (isCorrect && !isSelected) {
            option.classList.add('missed');
        } else if (!isCorrect && isSelected) {
            option.classList.add('incorrect');
        }
    });

    const feedback = container.querySelector('.scenario-feedback');
    const isAllCorrect = score === total &&
        container.querySelectorAll('input:checked').length === total;

    if (feedback) {
        showFeedback(feedback, isAllCorrect,
            isAllCorrect ? '完全正確！' : `答對 ${score}/${total}，請再檢查。`);
    }
    playSound(isAllCorrect);
}

// ==================== Certificate Functions ====================
function getFinalExamScore() {
    const results = JSON.parse(localStorage.getItem(STORAGE_KEYS.QUIZ_RESULTS) || '{}');
    const module5Results = results.module5 || {};
    let correct = 0;
    for (let i = 1; i <= 10; i++) {
        if (module5Results['final-' + i] === true) correct++;
    }
    return { correct: correct, total: 10, percentage: Math.round((correct / 10) * 100) };
}

function isCertificateEligible() {
    const modules = ['module0', 'module1', 'module2', 'module3', 'module4', 'module5'];
    const examScore = getFinalExamScore();
    const examPassed = examScore.percentage >= 80;

    // Auto-fix: if final exam passed, module5 must be completed
    // (user may have clicked "前往領取結業證書" link instead of "Complete Module" button)
    if (examPassed && APP_STATE.progress.module5 && !APP_STATE.progress.module5.completed) {
        APP_STATE.progress.module5.completed = true;
        saveProgress();
    }

    const allModulesCompleted = modules.every(m => APP_STATE.progress[m]?.completed === true);
    return {
        eligible: allModulesCompleted && examPassed,
        details: {
            modules: modules.map(m => ({ id: m, completed: APP_STATE.progress[m]?.completed === true })),
            allModulesCompleted: allModulesCompleted,
            examScore: examScore,
            examPassed: examPassed
        }
    };
}

function generateCertificateId(name, dateStr, score) {
    var str = name + dateStr + score;
    // Two-round hash with different seeds for 8 hex digits (~4 billion combinations)
    var h1 = 5381, h2 = 52711;
    for (var i = 0; i < str.length; i++) {
        var c = str.charCodeAt(i);
        h1 = ((h1 << 5) + h1 + c) | 0;
        h2 = ((h2 << 5) + h2 + c) | 0;
    }
    var hex = (Math.abs(h1) >>> 0).toString(16).toUpperCase().padStart(8, '0').slice(-4) +
        (Math.abs(h2) >>> 0).toString(16).toUpperCase().padStart(8, '0').slice(-4);
    var datePart = dateStr.replace(/\//g, '').replace(/-/g, '');
    return 'TW-CDC-OASIS-' + datePart + '-' + hex;
}

// ==================== Utility Functions ====================
function resetProgress() {
    if (confirm('確定要重設所有學習進度嗎？此操作無法復原。')) {
        localStorage.removeItem(STORAGE_KEYS.PROGRESS);
        localStorage.removeItem(STORAGE_KEYS.QUIZ_RESULTS);
        localStorage.removeItem(STORAGE_KEYS.CHECKLIST);
        location.reload();
    }
}

function formatTime(minutes) {
    if (minutes < 60) return `${minutes} 分鐘`;
    const hours = Math.floor(minutes / 60);
    const mins = minutes % 60;
    return mins > 0 ? `${hours} 小時 ${mins} 分鐘` : `${hours} 小時`;
}

// ==================== Export Functions for Global Use ====================
window.CDC_Learning = {
    markUnitComplete,
    checkQuizAnswer,
    checkDragDropAnswer,
    resetDragDrop,
    checkFillBlankAnswer,
    showFillBlankAnswers,
    checkScenarioAnswer,
    resetProgress,
    getOverallProgress,
    getModuleProgress,
    getFinalExamScore,
    isCertificateEligible,
    generateCertificateId
};
