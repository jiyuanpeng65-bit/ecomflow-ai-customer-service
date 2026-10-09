"""Static WorkBuddy package checks; does not execute an Agent or query business data."""

import json
import re
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AGENT = "ecomflow-customer-service"
SKILLS = (
    "ecomflow-product-support",
    "ecomflow-order-logistics",
    "ecomflow-after-sales",
)
HEADINGS = ("【问题类型】", "【中文处理说明】", "【英文客服回复】", "【数据状态】")


def check() -> None:
    manifest = json.loads((ROOT / ".codebuddy-plugin" / "plugin.json").read_text(encoding="utf-8"))
    assert manifest["expertType"] == "agent"
    assert manifest["agentName"] == AGENT
    assert manifest["agents"] == [f"./agents/{AGENT}.md"]
    assert manifest["skills"] == [f"./skills/{name}" for name in SKILLS]
    assert "dependencies" not in manifest, "No data connector is configured in this phase"
    assert manifest["defaultInitPrompt"] == manifest["quickPrompts"][0]
    assert len(manifest["tags"]) == len(manifest["quickPrompts"]) == 3
    assert (ROOT / manifest["avatar"]).is_file()
    with zipfile.ZipFile(ROOT / "dist" / "ecomflow-ai-expert.zip") as package:
        assert ".codebuddy-plugin/plugin.json" in package.namelist()
        assert f"agents/{AGENT}.md" in package.namelist()
        for name in SKILLS:
            assert f"skills/{name}/SKILL.md" in package.namelist()

    agent = (ROOT / "agents" / f"{AGENT}.md").read_text(encoding="utf-8")
    assert re.search(rf"(?m)^name: {AGENT}$", agent)
    for name in SKILLS:
        assert re.search(rf"(?m)^  - {name}$", agent)
        path = ROOT / "skills" / name / "SKILL.md"
        content = path.read_text(encoding="utf-8")
        assert content.startswith("---\n")
        assert re.search(rf"(?m)^name: {name}$", content)
        for field in ("description", "description_zh", "description_en", "version", "author"):
            assert re.search(rf"(?m)^{field}: .+", content), (name, field)
        with zipfile.ZipFile(ROOT / "dist" / f"{name}.zip") as package:
            assert "SKILL.md" in package.namelist()
            assert package.read("SKILL.md").decode("utf-8") == content

    for heading in HEADINGS:
        assert heading in agent
        assert heading in (ROOT / "prompts" / "output-template.md").read_text(encoding="utf-8")
    for phrase in ("尚未连接查询工具", "未找到记录", "需要人工审核", "已通过工具查询"):
        assert phrase in agent
    assert not list(ROOT.glob("*.db"))
    assert not list(ROOT.glob("data/*"))
    print("PASS: expert manifest, 3 Skills, packages, output rules, no data connector")
    print("NOTE: WorkBuddy UI loading and real data lookups are not verified by this test")


if __name__ == "__main__":
    try:
        check()
    except (AssertionError, FileNotFoundError, KeyError, zipfile.BadZipFile) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
