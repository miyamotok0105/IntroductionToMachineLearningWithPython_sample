# モデルの評価と改良

### [交差検証](https://github.com/kajyuuen/IntroductionToMachineLearningWithPython/blob/master/ch05/cross-validation.ipynb)

交差検証手法

- k分割交差検証
- 層化k分割交差検証
- シャッフル分割交差検証
- グループ付き交差検証

### [グリッドサーチ](https://github.com/kajyuuen/IntroductionToMachineLearningWithPython/blob/master/ch05/grid-search.ipynb)

パラメータのチューニング方法としてグリッドサーチが存在する．またその際パラメータの過剰適合を防ぐ為，データを以下のように分ける

- 訓練セット(train): モデルを構築する
- 検証セット(valid): モデルのパラメータを選択する
- テストセット(test): 選択したパラメータの性能を評価する

### [評価基準とスコア](https://github.com/kajyuuen/IntroductionToMachineLearningWithPython/blob/master/ch05/evaluation-metrics-and-scoring.ipynb)

#### 2クラス分類

２つのクラスを陽性,陰性と呼び，探している物を陽性と呼ぶ．

- 偽陽性(FP): 陰性のものを陽性と間違えること
- 偽陰性(FN): 陽性のものを陰性と間違えること
- 真陽性(TP): 陽性クラスで正しく分類されたサンプル
- 真陰性(TN): 陰性クラスで正しく分類されたサンプル

#### 評価方法

- 精度(Accuracy)
- 適合率(Precision)
- 再現率(Recall)
- F値
