# 圖形搜尋
在離散數學、演算法與人工智慧的領域，很多問題可以表示為「節點與連線所形成的圖形」，一個程式要解決某問題其實是在這個圖形裏把目標節點給找出來，於是問題求解就簡化成了圖形的搜尋，我們只要把解答給「找出來」就行了。

圖形搜尋的方法大致可以分為「深度優先搜尋 (Depth-First Search, DFS)、廣度優先搜尋 (Breath-First Search, BFS)、最佳優先搜尋 (Best-First Search, BestFS) 等三類。

然後針對最佳優先搜尋的部份，還有一種具有理論背景，且較為強大好用的 A* 搜尋法可採用。

# 深度優先搜尋法
一種用來遍尋一個樹(tree)或圖(graph)的演算法。由樹的根(或圖的某一點當成 根)來開始探尋，先探尋邊(edge)上未搜尋的一節點(vertex or node)，並儘可能深的搜索，直到該節點的所有邊上節點都已探尋；就回溯(backtracking)到前一個節點，重覆探尋未搜尋的節點，直到找到目 的節點或遍尋全部節點。

深度優先搜尋法屬於盲目搜索(uninformed search)是利用堆疊(Stack)來處理，通常以遞迴的方式呈現。

# 廣度優先搜尋法
是一種圖形(graph)搜索演算法。從圖的某一節點(vertex, node)開始走訪，接著走訪此一節點所有相鄰且未拜訪過的節點，由走訪過的節點繼續進行先廣後深的搜尋。以樹(tree)來說即把同一深度(level)的節點走訪完，再繼續向下一個深度搜尋，直到找到目的節點或遍尋全部節點。

廣度優先搜尋法屬於盲目搜索(uninformed search)是利用佇列(Queue)來處理，通常以迴圈的方式呈現。

# 感想(原創)
深度優先搜尋和廣度優先搜尋常用於路經的縮短，是路徑搜尋的基礎，在很多像是迷宮類的比賽都有人用，也有用於迷宮搜尋的A*演算和洪水演算法

# 参考资料
https://misavo.com/blog/%E9%99%B3%E9%8D%BE%E8%AA%A0/%E6%9B%B8%E7%B1%8D/%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/04-%E5%9C%96%E5%BD%A2%E6%90%9C%E5%B0%8B/A-%E5%9C%96%E5%BD%A2%E7%9A%84%E6%A6%82%E5%BF%B5
http://simonsays-tw.com/web/DFS-BFS/BreadthFirstSearch.html
http://simonsays-tw.com/web/DFS-BFS/DepthFirstSearch.html
