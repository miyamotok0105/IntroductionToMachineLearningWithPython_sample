# 教師あり学習

## アルゴリズム

- [最近傍法](https://github.com/kajyuuen/IntroductionToMachineLearningWithPython/blob/master/ch02/kmeans.ipynb)

  - [最強の当て馬]
  - 利点    
    モデルが単純。    
    パラメータ調整をあまりしなくても精度が高くなる。    
    多くの場合は非常に高速。（特徴量とサンプル個数が多くなると遅くなる）    
  - 欠点<    
    データ前処理が重要。    
    数百以上の特徴量をもつデータではうまく機能しない。    
    疎なデータは特にうまく機能しない。    

  - パラメータ    
    近傍点の数とデータポイント間の距離測度。    
    近傍点の数は３〜５で十分な場合が多いが調整する必要がある。    
    距離測度はユーグリッド距離で多くの場合うまくいく。    

  
- [線形モデル](https://github.com/kajyuuen/IntroductionToMachineLearningWithPython/blob/master/ch02/linear_model.ipynb)

- [最初に試すべきアルゴリズム]
- 利点
線形モデルは訓練，予測ともに高速．サンプル数が10万~100万点のデータに対しては，LinearRegression,Ridgeにsolver='sag'オプションを用いると高速になる場合がある．    
予測手法が理解しやすい    
特徴量の数がサンプル数の個数よりも多いときに性能を発揮する    
- 欠点
係数の意味を理解するのが難しい    
- パラメータ
正則化パラメータ    
線形モデル: alpha, LinearSVC, LinearRegression: C    
alphaが大きいとき, Cが小さい場合は単純なモデルに対応する．    
両方とも対数スケールで値を変更する    

- [ナイーブベイズ](https://github.com/kajyuuen/IntroductionToMachineLearningWithPython/blob/master/ch02/NaiveBayes.ipynb)
  - クラス分類にしか使えない．線形モデルより高速．線形モデルより精度が落ちる．

- [決定木](https://github.com/kajyuuen/IntroductionToMachineLearningWithPython/blob/master/ch02/decision_tree.ipynb)
  - 高速．可視化が可能で説明が容易．

- [ランダムフォレスト](https://github.com/kajyuuen/IntroductionToMachineLearningWithPython/blob/master/ch02/random_forest.ipynb)
  - 単一の決定木より高速で強力．スパースなデータには適さない．

- [勾配ブースティング決定木](https://github.com/kajyuuen/IntroductionToMachineLearningWithPython/blob/master/ch02/boosting_decision_tree.ipynb)
  - ランダムフォレストよりも精度が高いが時間がかかる．パラメータが重要．
  
- [サポートベクターマシン](https://github.com/kajyuuen/IntroductionToMachineLearningWithPython/blob/master/ch02/svm.ipynb)
  - 中規模なデータセットに対して強力．データのスケールを調整する必要がある．パラメータが重要．

- [ニューラルネットワーク](https://github.com/kajyuuen/IntroductionToMachineLearningWithPython/blob/master/ch02/mlp.ipynb)
  - 複雑なモデルを構築出来る．データのスケールを調整する必要がある．パラメータが重要．時間がかかる．
