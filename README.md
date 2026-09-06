# evidence-guardrails

AI駆動開発で、実装前後の根拠不足を検出するための小さなエージェントスキル群です。`skills/` 配下に標準的な `SKILL.md` 構成で配置しています。

## 含まれるスキル

- `evidence-guardrails`: 変更の影響と証拠不足を分類し、必要な下位スキルだけを順序付ける。
- `map-observable-boundaries`: 変更の外部境界、状態、副作用、失敗、所有者を台帳化する。
- `requirements-to-verification`: ニーズ、要求、設計判断、検証証拠を混同せず追跡する。
- `separate-verification-validation`: 仕様への適合確認と、利用・運用目的への適合確認を分離する。

## 利用

```bash
npx skills add 53able/evidence-guardrails --list
npx skills add 53able/evidence-guardrails --skill map-observable-boundaries
```

ローカルでは、対応CLIが利用できる場合に次を実行できます。

```bash
npx skills add ./ --list
```

## 検証

```bash
npm test
```

これは frontmatter、ディレクトリ名、説明文、相対パス、行数を検査し、正常・異常の完成済み証拠表fixtureに対する検査器を実行します。生成済み成果物の内容が真実であることや、LLMによる実案件評価は保証しません。`evals/` は、実案件へ適用する前の評価オラクル、比較プロトコル、ケースを保持します。

## 非対象

このプロジェクトは、SysMLの自動生成、完全な要件管理、または本番変更の自動承認を提供しません。テンプレートが埋まっていることは、利用目的への適合や安全性を保証しません。


