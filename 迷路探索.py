from time import sleep

#探索様子を追跡する関数（迷路の更新を出力する）
def track(maze, start, depth):
    draw = f"{depth}手目\n"
    for x in range(len(maze)):
        for y in range(len(maze[x])):
            if x == start[0][0] and y == start[0][1]:
                draw += "S "   #スタート位置
            elif maze[x][y] > 2:
                draw += "■ "    #壁
            elif maze[x][y] == 2:
                draw += "* "    #探索済みの道
            elif maze[x][y] == 1:
                draw += "G "   #ゴール位置
            else:
                draw += "  "    #未探索の道

        draw += "\n"
    print(draw)

#探索関数：ゴールしたらそのときの位置・移動数を返す
def Maze(start):
    #スタート位置（x座標, y座標, 移動回数）をセット
    pos = start.copy()

    while len(pos) > 0:#探索可能ならTrue
        x, y, depth = pos.pop(0) #リストから探索する位置を取得
        #ゴールについた時点で終了
        if maze[x][y] == 1:
            return [(x, y), depth]

        #探索済みとしてセット
        maze[x][y] = 2
        #1秒ごとに図の更新
        sleep(1)
        track(maze, start, depth)

        #現在位置の上下左右を探索：〇<2は壁でもなく探索済みでもないものを示す
        if maze[x-1][y] < 2:#左
            pos.append([x-1, y, depth + 1])
        if maze[x+1][y] < 2:#右
            pos.append([x+1, y, depth + 1])
        if maze[x][y-1] < 2:#上
            pos.append([x, y-1, depth + 1])
        if maze[x][y+1] < 2:#下
            pos.append([x, y+1, depth + 1])

    return False


if __name__ == '__main__':
    #迷路作成
    maze = [
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 9],
                [9, 0, 9, 0, 0, 0, 9, 9, 0, 9, 0, 9],
                [9, 0, 9, 9, 0, 9, 0, 0, 0, 9, 0, 9],
                [9, 0, 0, 0, 9, 0, 0, 9, 9, 0, 9, 9],
                [9, 9, 9, 0, 0, 9, 0, 9, 0, 0, 0, 9],
                [9, 0, 0, 0, 9, 0, 9, 0, 0, 9, 1, 9],
                [9, 0, 9, 0, 0, 0, 0, 9, 0, 0, 9, 9],
                [9, 0, 0, 9, 0, 9, 0, 0, 9, 0, 0, 9],
                [9, 0, 9, 0, 9, 0, 9, 0, 0, 9, 0, 9],
                [9, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
            ]
    start = [[1, 1, 0]]     #スタート位置

    result = Maze(start)  #探索

    print(result)