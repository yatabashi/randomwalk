# randomwalk

いくつかの種類のランダムウォークをTurtle Graphicsで実行するプログラム群

### randomwalk.py
前後左右に進む単純ランダムウォーク。

### randomwalk_360.py
前後左右以外を含めた360方向に進むランダムウォーク。

### randomwalk_unturnbackable.py
前と左右に進むが、後（来た方向）には戻らないランダムウォーク。

### randomwalk_self-avoiding.py
東西南北に進む自己回避ランダムウォーク。

### randomwalk_mutually-avoiding.py
二頭が自身と相手の軌跡を回避しつつ東西南北に進む自己回避ランダムウォーク。  
冗長なコーディングをしているが、敢えて作成時のまま維持している。_evasiveの特殊例としてリファクタリングが可能である。

### randomwalk_evasive.py
複数頭が自身と他者の軌跡を回避しつつ東西南北に進む自己回避ランダムウォーク。

### randomwalk_self-avoiding_endless.py
東西南北に進む自己回避ランダムウォークで、袋小路からの離脱を行う。
