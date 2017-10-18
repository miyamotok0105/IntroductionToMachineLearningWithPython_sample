# データの表現と特徴量エンジニアリング

- 連続値特徴量
    - 浮動小数点配列の配列のような形を取る
- 離散値特徴量
    - カテゴリ変数
    
特定のアプリケーションに対して，最良のデータ表現を模索することを`特徴量エンジニアリング`という

### [カテゴリ変数](https://github.com/kajyuuen/IntroductionToMachineLearningWithPython/blob/master/ch04/categorical_variables.ipynb)

- ワンホットエンコーディング(ダミー変数)
    - ダミー変数とは，カテゴリ変数を一つ以上の0と1の値を持つ新しい特徴量で置き換えるもの． 値0と1を使えば，線形ニクラス分類の式が意味を持つので，sklearnの殆どのモデルを利用出来る．

### [ビニング，離散化，線形モデル，決定木](https://github.com/kajyuuen/IntroductionToMachineLearningWithPython/blob/master/ch04/binning.ipynb)

- ビニング, 離散化
    - 連続値を，等間隔な区分に分割する

### [交互作用と多項式](https://github.com/kajyuuen/IntroductionToMachineLearningWithPython/blob/master/ch04/interactions_and_polynomials.ipynb)

- 交互作用特徴量
    - ある特徴量x_1, x_2に対して, x_1 * x_2を考える
- 多項式特徴量
    - ある特徴量xに対して, x^2, x^3と考える

### [単変量非線形変換](https://github.com/kajyuuen/IntroductionToMachineLearningWithPython/blob/master/ch04/univariate_non-linear_transformations.ipynb)

殆どのモデルは，個々の特徴量がおおよそガウス分布に従っているときに最もうまく機能する．
整数のカウントデータに対してlog, expを用いると正規分布になったりする．(この種の変換は決定木ベースのモデルには関係が無い)

### [自動特徴量選択](https://github.com/kajyuuen/IntroductionToMachineLearningWithPython/blob/master/ch04/automatic_feature_selection.ipynb)

よい特徴量を調べるためには

- 単変量統計
    - 変量統計では，個々の特徴量とターゲットの間に統計的に顕著な関係があるかどうかを計算する
- モデルベース選択
    - 全ての特徴量を同時に考慮するので変数間の相互作用を捉える
- 反復選択
    - 異なる特徴量を用いた一連のモデルを作る
の三つがある．これらは教師あり手法であり，特徴量選択時には訓練セットだけを用いて行う必要がある．

### [専門家知識の利用](https://github.com/kajyuuen/IntroductionToMachineLearningWithPython/blob/master/ch04/utilizing_expert_knowledge.ipynb)

### まとめ

- 線形モデル
    - ビニングや多項式特徴量，交互作用特徴量の追加の恩恵を受けやすい
- 非線形モデル(ランダムフォレストやSVM)
    - 明示的に特徴空間を拡張することなく，複雑なタスクを学習出来る
