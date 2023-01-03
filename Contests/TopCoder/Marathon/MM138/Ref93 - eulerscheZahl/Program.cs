using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

public class DiceRoller
{
    private static Queue<int> queue = new Queue<int>();
    public static int ReadInt()
    {
        while (queue.Count == 0)
        {
            foreach (string s in Console.ReadLine().Split(" ".ToCharArray(), StringSplitOptions.RemoveEmptyEntries)) queue.Enqueue(int.Parse(s));
        }
        return queue.Dequeue();
    }

    static void Main(string[] args)
    {
        Board.ReadInput();

        int timeLimit = 9800;
        int splitCountX = 1, splitCountY = Board.Size / 4;
        if (Board.Size >= 10) splitCountX = 2;
        if (Board.Size >= 16) splitCountX = 4;
        if (Board.Size >= 24) splitCountX = 6;
        //splitCountX=1; splitCountY=1;
        string path = ".";
        for (int i = 4; i <= splitCountX; i += 2)
        {
            path += "R" + new string('D', splitCountY - 2) + "R" + new string('U', splitCountY - 2);
        }
        if (splitCountX > 1) path += "R";
        path += new string('D', splitCountY - 1);
        path += new string('L', splitCountX - 1);
        path += new string('U', splitCountY - 1);

        int splitCount = splitCountX * splitCountY;
        List<int> splitsX = Enumerable.Range(0, 1 + splitCountX).Select(s => s * Board.Size / splitCountX).ToList();
        List<int> splitsY = Enumerable.Range(0, 1 + splitCountY).Select(s => s * Board.Size / splitCountY).ToList();
        int[] rectX = new int[splitCount];
        int[] rectY = new int[splitCount];
        int posX = 0, posY = 0;
        for (int i = 1; i < splitCount; i++)
        {
            if (path[i] == 'R') posX++;
            if (path[i] == 'L') posX--;
            if (path[i] == 'D') posY++;
            if (path[i] == 'U') posY--;
            rectX[i] = posX;
            rectY[i] = posY;
        }

        int[] stage = new int[Board.Size * Board.Size];
        for (int s = 0; s < splitCount; s++)
        {
            int minX = splitsX[rectX[s]], maxX = splitsX[rectX[s] + 1];
            int minY = splitsY[rectY[s]], maxY = splitsY[rectY[s] + 1];
            for (int x = minX; x < maxX; x++)
            {
                for (int y = minY; y < maxY; y++) stage[x * Board.Size + y] = s;
            }
        }

        List<Point> allPoints = new List<Point>();
        for (int x = 0; x < Board.Size; x++)
        {
            for (int y = 0; y < Board.Size; y++) allPoints.Add(new Point(x, y));
        }
        List<Point> currentPoints = allPoints.ToList();
        Random random = new Random(0);

        Board start = new Board();
        if (splitCount > 1) start.Init(2, splitsY[1] - 1);
        else
        {
            Point p = currentPoints[random.Next(currentPoints.Count)];
            currentPoints.Remove(p);
            start.Init(p.X, p.Y);
        }

        int beamWidth = (int)2e5 / Board.Area;
        int nodes = 0;
        Stopwatch sw = Stopwatch.StartNew();
        List<Board> results = new List<Board>();

        int firstTime = splitCount > 2 ? timeLimit * 3 / 4 : timeLimit;
        int secondTime = timeLimit;
        bool flipDirection = false;

        for (int iteration = 0; sw.ElapsedMilliseconds < firstTime; iteration++)
        {
            List<Board> boards = new List<Board> { start };
            Board currentBest = start;
            for (int s = 0; s < splitCount; s++)
            {
                BeamList end = new BeamList(currentBest.Score - 50);
                while (boards.Count > 0)
                {
                    BeamList next = new BeamList(currentBest.Score - 50);
                    foreach (Board b in boards)
                    {
                        foreach (Board b2 in b.Expand())
                        {
                            nodes++;
                            if (nodes % 2048 == 0 && sw.ElapsedMilliseconds > firstTime)
                            {
                                results.Add(currentBest.Unflip());
                                goto noTime1;
                            }
                            if (b2.ScoreBonus > currentBest.ScoreBonus) currentBest = b2;
                            if (stage[b2.DieX * Board.Size + b2.DieY] <= s) next.Add(b2);
                            else if (stage[b2.DieX * Board.Size + b2.DieY] == s + 1)
                            {
                                end.Add(b2);
                                b2.Stage++;
                            }
                        }
                    }
                    boards = next.Extract(beamWidth);
                }
                boards = end.Extract(beamWidth).ToList();
            }
            results.Add(currentBest.Unflip());
            Console.Error.WriteLine("first run: " + currentBest.ScoreBonus);

            if (iteration % 4 == 0)
            {
                flipDirection = !flipDirection;
                for (int x = 0; x < Board.Size; x++)
                {
                    for (int y = 0; y < Board.Size; y++)
                    {
                        stage[x * Board.Size + y] = splitCount - 1 - stage[x * Board.Size + y];
                    }
                }
            }
            if (iteration % 2 == 0) Board.FlipY();
            else Board.FlipX();

            start = new Board();
            if (splitCount > 1) start.Init((3 + iteration / 8) % splitsX[1], flipDirection ? splitsY[1] : splitsY[1] - 1);
            else
            {
                if (currentPoints.Count == 0)
                {
                    currentPoints = allPoints.ToList();
                    beamWidth *= 4;
                }
                Point p = currentPoints[random.Next(currentPoints.Count)];
                currentPoints.Remove(p);
                start.Init(p.X, p.Y);
            }
        }

    noTime1:
        Board.UnflipGrid();

        beamWidth *= 2;
        foreach (Board board in results.OrderByDescending(r => r.ScoreBonus).ToList())
        {
            Console.Error.WriteLine("score: " + board.ScoreBonus);
            Console.Error.WriteLine("nodes: " + nodes);
            if (sw.ElapsedMilliseconds > secondTime) break;

            int[] sideValues = board.SideValues.ToArray();
            Board toScore = board;
            while (toScore != null)
            {
                toScore.ComputeScore(sideValues);
                toScore = toScore.Parent;
            }
            Board currentBest = board;
            for (int rev = 1; rev <= 2; rev++)
            {
                currentBest = currentBest.Reverse(sideValues); // make a copy
                int size = 2;
                for (int s = 0; s + size <= splitCount; s++)
                {
                    List<Board> pathAfter = currentBest.GetPath();
                    Board first = pathAfter.FirstOrDefault(p => p.Stage == s);
                    Board last = pathAfter.LastOrDefault(p => p.Stage == s + size - 1);
                    if (first == null || last == null) continue;
                    pathAfter = pathAfter.Skip(pathAfter.IndexOf(last) + 1).ToList();

                    Board current = last;
                    int[] visited = currentBest.array.Take(Board.Size).ToArray();
                    while (current != first)
                    {
                        visited[current.DieY] ^= 1 << current.DieX;
                        current = current.Parent;
                    }

                    Board final = last;
                    start = new Board(current, visited, sideValues);
                    List<Board> boards = new List<Board> { start };
                    while (boards.Count > 0)
                    {
                        BeamList next = new BeamList(start.Score - 50);
                        foreach (Board b in boards)
                        {
                            foreach (Board b2 in b.Expand(sideValues))
                            {
                                nodes++;
                                if (nodes % 2048 == 0 && sw.ElapsedMilliseconds > timeLimit)
                                {
                                    if (currentBest.ScoreBonus > board.ScoreBonus) results.Add(currentBest);
                                    goto noTime2;
                                }
                                if (b2.DieX == last.DieX && b2.DieY == last.DieY)
                                {
                                    if (b2.array[Board.SideOffset + 0] == last.array[Board.SideOffset + 0] && b2.array[Board.SideOffset + 2] == last.array[Board.SideOffset + 2] && b2.Score > final.Score) final = b2;
                                    else if (s + size == splitCount && b2.Score > final.Score) final = b2;
                                }
                                else next.Add(b2);
                            }
                        }
                        boards = next.Extract(beamWidth);
                    }
                    if (final != last)
                    {
                        Console.Error.WriteLine("    " + last.Score + " => " + final.Score + " @" + s + "/" + (splitCount - size));
                        foreach (Board after in pathAfter)
                        {
                            final.array[after.DieY] ^= 1 << after.DieX;
                            final = final.Expand(sideValues).First(b => b.DieX == after.DieX && b.DieY == after.DieY);
                            final.Stage = after.Stage;
                        }
                        currentBest = final;
                        s++;
                    }
                }

                Console.Error.WriteLine("second run " + rev + ": " + board.ScoreBonus + " => " + currentBest.ScoreBonus);
                results.Add(currentBest);
            }
        }


    noTime2:
        Board best = results.OrderByDescending(b => b.ScoreBonus).First();

        Console.Error.WriteLine($"nodes: {nodes}   score: {best.ScoreBonus}   time: {sw.ElapsedMilliseconds}");
        List<string> solution = best.Path();
        Console.WriteLine(solution[0].Replace(" ", "\n"));
        solution.RemoveAt(0);
        Console.WriteLine(solution.Count);
        foreach (string s in solution) Console.WriteLine(s);
    }
}