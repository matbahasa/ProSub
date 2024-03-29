# 日本語データについて

## このページで公開するファイルについて
このページではアノテーションファイルのみを公開しています。コーパスデータは国立国語研究所から購入して下さい。[https://www2.ninjal.ac.jp/conversation/cejc/contract.html](https://www2.ninjal.ac.jp/conversation/cejc/contract.html)

- `ver0`フォルダーには、[Nomoto et al. (2023)](https://www.anlp.jp/proceedings/annual_meeting/2023/pdf_dir/P9-4.pdf)で報告した2つのグループに別れ、独立して行ったアノテーションが入っています。アノテーター間不一致があります。
- `ver1`フォルダーには、`ver0`のアノテーター間不一致を確認・検討を行った最終的なアノテーションが入っています。

## アノテーションファイルとコーパスデータの統合法
アノテーションはコーパスの転記テキストから発話IDと話者名および発話を抽出し、タブで区切った形式のファイルに対して行いました。この形式のファイルの作成にはPythonスクリプト`create_annotation_file.py`を用いました。

- 転記テキストの形式（`会話ID-luu.csv`）  
`発話ID,開始時刻,終了時刻,話者ID,発話`

    999,855.867,858.194,IC03_さとし,こっち(D ライ) スーパーと言えばライフだと思ってたけど:。

- アノテーション用に整形した形式（`会話ID-luu-anno.txt`）  
`発話ID [TAB] 話者名 [TAB] 発話`

    999 [TAB] さとし [TAB] こっち(D ライ) スーパーと言えばライフだと思ってたけど:。

- アノテーションファイルと整形した転記テキストのファイルの統合を簡単に行うには[ETA: Easy Text Annotator](https://github.com/matbahasa/ETA)が便利です。

## 謝辞
日本語データのアノテーション作業はJSPS科研費「代名詞代用・呼びかけ表現の通言語学的研究」（課題番号[JP20H01255](https://kaken.nii.ac.jp/ja/grant/KAKENHI-PROJECT-20H01255/)）および国立国語研究所共同利用型共同研究(C)の助成を受けて行いました。
