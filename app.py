import re
from flask import Flask, jsonify, render_template, request

app = Flask(__name__, template_folder="templates", static_folder="static")

SEVERITY_SCORES = {
    "critical": 30,
    "high": 20,
    "medium": 12,
    "low": 6,
}

RULES = [
    {
        "id": "unsafe_execution",
        "title": "Dangerous code execution",
        "severity": "critical",
        "description": "Use of eval/exec can allow remote code execution if untrusted input is involved.",
        "patterns": [r"eval\s*\(", r"exec\s*\("],
    },
    {
        "id": "sql_injection",
        "title": "Possible SQL injection pattern",
        "severity": "high",
        "description": "Query strings built with string concatenation may allow SQL injection.",
        "patterns": [
            r"(?i)(SELECT|INSERT|UPDATE|DELETE)\s+.*\+\s*.*",
            r"(?i)(query\s*=\s*f?[\"'][^\"']*\+)",
        ],
    },
    {
        "id": "hardcoded_secret",
        "title": "Hardcoded secret or token",
        "severity": "high",
        "description": "Sensitive credentials embedded directly in source code are risky and should be moved to environment variables.",
        "patterns": [
            r"(?i)(api[_-]?key|access[_-]?token|secret|password)\s*[:=]\s*[\"'][^\"']+[\"']",
            r"(?i)\b(?:AKIA|ASIA|ghp_|github_pat_|sk_live_|xox[baprs]-)[A-Za-z0-9_\-]+",
        ],
    },
    {
        "id": "insecure_deserialization",
        "title": "Unsafe deserialization",
        "severity": "high",
        "description": "Deserializing untrusted data can lead to arbitrary code execution.",
        "patterns": [
            r"pickle\.loads\s*\(",
            r"yaml\.load\s*\(",
            r"marshal\.loads\s*\(",
        ],
    },
    {
        "id": "weak_crypto",
        "title": "Weak cryptographic algorithm",
        "severity": "medium",
        "description": "Weak or legacy hash functions may be vulnerable to brute-force or collision attacks.",
        "patterns": [
            r"(?i)\bmd5\s*\(",
            r"(?i)\bsha1\s*\(",
            r"(?i)\bDES\b",
        ],
    },
    {
        "id": "insecure_auth",
        "title": "Insecure authentication practice",
        "severity": "medium",
        "description": "Authentication logic that bypasses secure password hashing or session verification should be reviewed.",
        "patterns": [
            r"(?i)(password\s*==\s*[\"'][^\"']+[\"'])",
            r"(?i)(session\s*\[.*\]\s*=\s*.*user.*)",
        ],
    },
    {
        "id": "command_injection",
        "title": "Command execution risk",
        "severity": "high",
        "description": "Executing shell commands with user-controlled input can enable command injection.",
        "patterns": [
            r"subprocess\.(call|Popen|run)\s*\(",
            r"os\.system\s*\(",
            r"shell=True",
        ],
    },
]


def get_risk_level(score):
    if score >= 80:
        return "Critical"
    if score >= 55:
        return "High"
    if score >= 25:
        return "Medium"
    if score > 0:
        return "Low"
    return "None"


def build_recommendations(findings):
    recommendations = []
    titles = {item["id"]: item["title"] for item in findings}

    if "unsafe_execution" in titles:
        recommendations.append("Remove dynamic code execution and validate all user input before processing it.")
    if "sql_injection" in titles:
        recommendations.append("Use parameterized queries or prepared statements instead of string concatenation.")
    if "hardcoded_secret" in titles:
        recommendations.append("Move secrets to environment variables or a secure secret manager, and rotate exposed credentials.")
    if "insecure_deserialization" in titles:
        recommendations.append("Avoid deserializing untrusted input. Prefer JSON, schema validation, or safe parsing libraries.")
    if "weak_crypto" in titles:
        recommendations.append("Use modern algorithms such as bcrypt, Argon2, PBKDF2, AES-GCM, or SHA-256 as appropriate.")
    if "insecure_auth" in titles:
        recommendations.append("Enforce secure password hashing and verify sessions with robust authentication checks.")
    if "command_injection" in titles:
        recommendations.append("Avoid shell execution when possible; if required, sanitize arguments and restrict privileges.")

    if not recommendations:
        recommendations.append("No obvious findings were detected in the provided sample. Continue with secure coding review and testing.")

    return recommendations


def analyze_code(code: str):
    text = code or ""
    findings = []

    for rule in RULES:
        for pattern in rule["patterns"]:
            for match in re.finditer(pattern, text, re.IGNORECASE | re.DOTALL):
                line_number = text[: match.start()].count("\n") + 1
                snippet = match.group(0).strip()
                if len(snippet) > 180:
                    snippet = snippet[:177] + "..."

                findings.append(
                    {
                        "id": rule["id"],
                        "title": rule["title"],
                        "severity": rule["severity"],
                        "description": rule["description"],
                        "line": line_number,
                        "snippet": snippet,
                    }
                )

    unique_findings = []
    seen = set()
    for item in findings:
        key = (item["id"], item["line"], item["snippet"])
        if key not in seen:
            seen.add(key)
            unique_findings.append(item)

    total_score = sum(SEVERITY_SCORES[item["severity"]] for item in unique_findings)
    risk_level = get_risk_level(total_score)
    recommendations = build_recommendations(unique_findings)

    return {
        "summary": (
            f"Scanned {len(text.splitlines())} lines. Detected {len(unique_findings)} possible issue(s)."
            if text.strip()
            else "No source code was provided for analysis."
        ),
        "risk_score": min(total_score, 100),
        "risk_level": risk_level,
        "findings": unique_findings,
        "recommendations": recommendations,
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/analyze", methods=["POST"])
def analyze_endpoint():
    payload = request.get_json(silent=True) or {}
    code = payload.get("code", "")
    result = analyze_code(code)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
