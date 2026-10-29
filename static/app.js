* {
    box-sizing: border-box;
}

:root {
    --bg: #07111f;
    --panel: #101d2d;
    --panel-soft: #14273d;
    --text: #e5edf9;
    --muted: #9fb3c8;
    --primary: #5bc0eb;
    --danger: #ff5d73;
    --warning: #ffb84d;
    --good: #58d68d;
    --border: rgba(255, 255, 255, 0.08);
}

body {
    margin: 0;
    font-family: Arial, Helvetica, sans-serif;
    background: linear-gradient(135deg, #07111f, #0d1d2c 50%, #0e1d2b);
    color: var(--text);
}

.container {
    max-width: 1180px;
    margin: 0 auto;
    padding: 40px 20px 60px;
}

.topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 28px;
}

.eyebrow {
    margin: 0 0 8px;
    font-size: 12px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--primary);
}

h1, h2, h3, p {
    margin-top: 0;
}

h1 {
    margin-bottom: 0;
    font-size: clamp(2rem, 4vw, 3rem);
}

.badge {
    background: rgba(91, 192, 235, 0.1);
    border: 1px solid var(--border);
    color: var(--primary);
    padding: 10px 14px;
    border-radius: 999px;
    font-weight: 600;
}

.layout {
    display: grid;
    grid-template-columns: 1.1fr 1fr;
    gap: 24px;
}

.panel {
    background: rgba(16, 29, 45, 0.9);
    border: 1px solid var(--border);
    border-radius: 18px;
    box-shadow: 0 18px 40px rgba(0, 0, 0, 0.22);
    padding: 22px;
}

textarea {
    width: 100%;
    min-height: 360px;
    resize: vertical;
    border-radius: 12px;
    border: 1px solid var(--border);
    background: var(--panel-soft);
    padding: 16px;
    color: var(--text);
    font-size: 15px;
    line-height: 1.55;
    margin-top: 10px;
    font-family: "SFMono-Regular", Consolas, monospace;
}

textarea::placeholder {
    color: var(--muted);
}

.button-row {
    display: flex;
    gap: 12px;
    margin-top: 18px;
}

button {
    border: none;
    border-radius: 10px;
    background: linear-gradient(135deg, var(--primary), #7ee0ff);
    color: #04111d;
    font-weight: 700;
    padding: 12px 18px;
    cursor: pointer;
    transition: transform 0.15s ease, opacity 0.15s ease;
}

button:hover {
    transform: translateY(-1px);
}

button.secondary {
    background: rgba(255, 255, 255, 0.06);
    color: var(--text);
    border: 1px solid var(--border);
}

.result-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    margin-bottom: 14px;
}

.score-box {
    background: rgba(91, 192, 235, 0.08);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 12px 16px;
    min-width: 118px;
    text-align: center;
}

.score-box span {
    display: block;
    font-size: 12px;
    color: var(--muted);
}

.score-box strong {
    font-size: 2rem;
}

.summary {
    color: var(--muted);
    margin-bottom: 12px;
}

.section {
    margin-top: 18px;
}

.findings-list,
.recommendations-list {
    list-style: none;
    padding: 0;
    margin: 0;
    display: grid;
    gap: 12px;
}

.findings-list li,
.recommendations-list li {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid var(--border);
    border-left: 4px solid var(--primary);
    border-radius: 10px;
    padding: 12px 14px;
}

.findings-list li[data-severity="critical"] {
    border-left-color: var(--danger);
}

.findings-list li[data-severity="high"] {
    border-left-color: #ff6f61;
}

.findings-list li[data-severity="medium"] {
    border-left-color: var(--warning);
}

.findings-list li[data-severity="low"] {
    border-left-color: var(--good);
}

.finding-top {
    display: flex;
    justify-content: space-between;
    gap: 12px;
    margin-bottom: 6px;
}

.severity-tag {
    border-radius: 999px;
    padding: 4px 8px;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-weight: 700;
    background: rgba(255, 255, 255, 0.05);
}

.code-snippet {
    color: #d9e7ff;
    font-family: "SFMono-Regular", Consolas, monospace;
    font-size: 13px;
    margin-top: 6px;
    word-break: break-all;
}

@media (max-width: 850px) {
    .layout {
        grid-template-columns: 1fr;
    }

    .topbar {
        flex-direction: column;
        align-items: flex-start;
        gap: 12px;
    }
}
