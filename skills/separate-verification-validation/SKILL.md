---
name: separate-verification-validation
description: 仕様・契約への適合確認と、利用者・運用者の目的への適合確認を別々の証拠表へ記録する。リリース判定、高影響変更、AI生成実装のレビュー、運用シナリオ確認で使う。単体テストだけの実行、利用目的が不要な局所整形、未実施シナリオを合格扱いする作業には使わない。
---

# Verification と Validation を分離する

## 手順

1. 要求追跡表の `R-*` と `V-*`、設計契約、実行済みテスト、代表的な利用・運用シナリオを収集する。要求がない場合は `requirements-to-verification` を先に適用する。
2. `assets/vv-evidence-template.md` を複製する。
3. Verification 欄には、要求・契約・設計に対する適合確認だけを記録する。例は単体、結合、E2E、障害系、性能、静的検査である。
4. Validation 欄には、利用者または運用者の目的を達成できるかを確認するシナリオだけを記録する。例は受入演習、復旧演習、代表タスクの完了、限定利用である。
5. 高影響操作を含む場合は `references/release-gates.md` を読み、未実施の validation、rollback 不在、または承認者不在を停止条件として扱う。
6. テスト成功だけから validation を `passed` としない。validation のシナリオまたは観測結果がなければ `not run` または `blocked` とする。
7. `scripts/validate-vv-evidence.py <証拠表ファイル>` を実行し、二つの証拠レーンと残余リスク欄を検査する。
8. リリース可否ではなく、Verification 状態、Validation 状態、未検査範囲、残余リスク、必要な人間承認を出力する。

## 出力規約

- Verification の合格は「仕様どおり」を示すに留める。
- Validation の合格は、代表シナリオと観測結果を結び付ける。
- `not run`、`blocked`、`failed` を `passed` に要約しない。

## Error Handling

- 利用・運用シナリオを取得できない場合は validation を `not run` とし、代理のユニットテストを validation 証拠として使わない。
- 高影響変更で rollback または承認者が不明な場合は、`references/release-gates.md` に従って停止する。
