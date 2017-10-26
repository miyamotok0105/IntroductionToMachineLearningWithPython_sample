# アルゴリズムチェーンとパイプライン

Pipelineクラスを用いることでデータ変換とモデル実行のチェーンの構築を簡単に行える．

### [前処理を行う際のパラメータ選択](https://github.com/kajyuuen/IntroductionToMachineLearningWithPython/blob/master/ch06/parameter_selection_with_preprocessing%20.ipynb)

モデルの構築過程において，スケール変換や特徴量抽出を行う際に交差検定の為のデータの分割を怠ると，訓練データセットの情報がテストデータにリークしてしまう．

### [パイプラインの構築](https://github.com/kajyuuen/IntroductionToMachineLearningWithPython/blob/master/ch06/building_pipelines.ipynb)

パイプラインを用いると「前処理+クラス分類」といった一連のプロセスに必要なコードを減らすことが出来る．

### [パイプラインを用いたグリッドサーチ](https://github.com/kajyuuen/IntroductionToMachineLearningWithPython/blob/master/ch06/grid-searching-preprocessing-steps-and-model-parameters.ipynb)

グリッドサーチもパイプラインで扱うことが出来る．

### [汎用パイプラインインターフェース](https://github.com/kajyuuen/IntroductionToMachineLearningWithPython/blob/master/ch06/the-general-pipeline-interface.ipynb)

Pipelineクラスは任意個数のEstimatorを連結することができる．最後以外のステップでは次のステップで使うデータの新しい表現を生成するためにtransformメソッドが定義しなければならないという制約がある．

### [前処理ステップとモデルパラメータに対するグリッドサーチ](https://github.com/kajyuuen/IntroductionToMachineLearningWithPython/blob/master/ch06/grid-searching-preprocessing-steps-and-model-parameters.ipynb)

パイプラインを使うと，機械学習ワークフローの全てのステップを一つのscikit-learn Estimatorにカプセル化することが出来る．そのメリットの一つは，回帰やクラス分類などの教師ありタスクの結果を使った前処理のパラメータの調整を行えるということである．

### [グリッドサーチによるモデルの選択](https://github.com/kajyuuen/IntroductionToMachineLearningWithPython/blob/master/ch06/selection-of-model-by-grid-searching.ipynb)

GridSearchCVとPipelineの組み合わせでは，実際に行われるステップに対してもサーチすることができる
．
