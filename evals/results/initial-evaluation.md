# Initial evaluation

## Status

Not run. このリポジトリには、LLMを使ったケース実行、人間比較レビュー、性能または安全性の測定結果はまだない。実行時は `evals/protocol.md` に従う。

## 実行時に記録する項目

- 実行日、Git revision、対象スキル、モデル・バージョン、生成パラメータ、入力ケース
- Baseline / Skill condition、反復番号、出力ファイルまたはトランスクリプトへの相対パス
- `evals/rubric.md` の各項目についての、独立レビュアー別判定と根拠
- 合議後の判定、blocker、誤検知、見逃し、残余リスク
- ケース別・条件別の重大見落とし率、誤検知率、レビュー時間
