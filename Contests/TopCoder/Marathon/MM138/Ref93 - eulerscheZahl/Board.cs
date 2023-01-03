using System;
using System.Collections.Generic;
using System.Linq;

public class Board
{
    public static int Size;
    public static int Area => Size * Size;
    public static int V;
    public static double Bonus;
    public static int[] Grid;
    public static int StartX;
    public static int StartY;

    private const int TOP = 0;
    public const int BOTTOM = 1;
    private const int FRONT = 2;
    private const int BACK = 3;
    private const int LEFT = 4;
    private const int RIGHT = 5;
    public static int[] dx = { 0, 1, 0, -1 };
    public static int[] dy = { 1, 0, -1, 0 };
    private static int[,] rotate = {
        //{ TOP,BOTTOM,FRONT,BACK,LEFT,RIGHT } // initial
        { BACK,FRONT,TOP,BOTTOM,LEFT,RIGHT }, // down
        { LEFT,RIGHT,FRONT,BACK,BOTTOM,TOP }, // right
        { FRONT,BACK,BOTTOM,TOP,LEFT,RIGHT }, // up
        { RIGHT,LEFT,FRONT,BACK,TOP,BOTTOM }, // left
    };

    public Board() { }

    public static void ReadInput()
    {
        Size = DiceRoller.ReadInt();
        V = DiceRoller.ReadInt();
        Bonus = double.Parse(Console.ReadLine());

        Grid = new int[Size * Size];
        for (int y = 0; y < Size; y++)
        {
            for (int x = 0; x < Size; x++) Grid[x * Size + y] = DiceRoller.ReadInt();
        }
    }

    public List<string> Path()
    {
        List<string> result = new List<string>();
        Board board = this;
        Board start = this;
        while (board != null)
        {
            result.Add(board.DieY + " " + board.DieX);
            board = board.Parent;
            if (board != null) start = board;
        }
        int[] values = new int[6];
        for (int side = 0; side < 6; side++)
        {
            int max = int.MinValue;
            for (int v = 1; v <= V; v++)
            {
                int current = v * array[HitOffset + side + 6 * v];
                if (current > max)
                {
                    max = current;
                    values[side] = v;
                }
            }
        }
        result.Add(string.Join(" ", start.array.Skip(SideOffset).Take(6).Select(s => values[s])));
        result.Reverse();
        return result;
    }

    public int[] array;
    //public int[] visited;
    //public int[] numbersHit;
    public int[] SideValues;
    //public int[] DieSides;
    public static int SideOffset => Size;
    public static int HitOffset => Size + 6;
    public int DieX, DieY;
    public Board Parent;
    public int Score;
    public int ScoreBonus;
    public int Stage;
    public void Init(int x, int y, int[] dieSides = null)
    {
        array = new int[HitOffset + 6 * (1 + V)];
        SideValues = new int[6];
        for (int i = TOP; i <= RIGHT; i++)
        {
            array[SideOffset + i] = i;
            if (dieSides != null) array[SideOffset + i] = dieSides[i];
        }
        DieX = x;
        DieY = y;
        StartX = DieX;
        StartY = DieY;
        array[DieY] |= 1 << DieX;

        UpdateSideValues();
        ComputeScore();
    }

    public Board(Board board, int[] visited, int[] sideValues)
    {
        Parent = board.Parent;
        Stage = board.Stage;
        DieX = board.DieX;
        DieY = board.DieY;
        this.array = (int[])board.array.Clone();
        for (int i = 0; i < Size; i++) array[i] = visited[i];
        ComputeScore(sideValues);
    }

    public Board(Board parent, int dir, int[] sideValues = null)
    {
        Parent = parent;
        Stage = parent.Stage;
        DieX = parent.DieX + dx[dir];
        DieY = parent.DieY + dy[dir];
        array = (int[])parent.array.Clone();
        array[DieY] |= 1 << DieX;

        for (int i = 0; i < 6; i++)
        {
            array[SideOffset + i] = parent.array[SideOffset + rotate[dir, i]];
        }
        if (sideValues == null)
        {
            SideValues = (int[])parent.SideValues.Clone();
            UpdateSideValues();
        }
        else
        {
            if (Grid[DieX * Size + DieY] > 0) array[HitOffset + array[SideOffset + BOTTOM] + 6 * Grid[DieX * Size + DieY]]++;
            else array[HitOffset + array[SideOffset + BOTTOM] + 6 * -Grid[DieX * Size + DieY]]--;
        }

        ComputeScore(sideValues);
    }

    private void UpdateSideValues()
    {
        int bottom = array[SideOffset + BOTTOM];
        int grid = Grid[DieX * Size + DieY];
        if (grid > 0)
        {
            array[HitOffset + bottom + 6 * grid]++;
            if (array[HitOffset + bottom + 6 * grid] * grid > array[HitOffset + bottom + 6 * SideValues[bottom]] * SideValues[bottom]) SideValues[bottom] = grid;
        }
        else
        {
            array[HitOffset + bottom + 6 * -grid]--;
            int max = int.MinValue;
            for (int v = 1; v <= V; v++)
            {
                if (v * array[HitOffset + bottom + 6 * v] > array[HitOffset + bottom + 6 * SideValues[bottom]] * SideValues[bottom]) SideValues[bottom] = v;
                max = Math.Max(max, v * array[HitOffset + bottom + 6 * v]);
            }
        }
    }

    public IEnumerable<Board> Expand(int[] sideValues = null)
    {
        for (int dir = 0; dir < 4; dir++)
        {
            int x = DieX + dx[dir];
            int y = DieY + dy[dir];
            if (x < 0 || x >= Size || y < 0 || y >= Size || ((array[y] >> x) & 1) == 1) continue;
            yield return new Board(this, dir, sideValues);
        }
    }

    public Board Reverse(int[] sideValues)
    {
        int stage = this.Stage;
        Board result = new Board();
        result.SideValues = sideValues;
        result.Init(this.DieX, this.DieY, array.Skip(SideOffset).Take(6).ToArray());
        result.Stage = 0;

        Board current = this.Parent;
        while (current != null)
        {
            result = result.Expand(sideValues).First(b => b.DieX == current.DieX && b.DieY == current.DieY);
            result.Stage = stage - current.Stage;
            current = current.Parent;
        }
        return result;
    }

    public void ComputeScore(int[] sideValues = null)
    {
        Score = 0;
        for (int side = 0; side < 6; side++)
        {
            if (sideValues == null) Score += SideValues[side] * array[HitOffset + side + 6 * SideValues[side]];
            else Score += sideValues[side] * array[HitOffset + side + 6 * sideValues[side]];
        }
        ScoreBonus = Score;
        if (Math.Abs(DieX - StartX) + Math.Abs(DieY - StartY) == 1) ScoreBonus = (int)(Bonus * Score);
    }

    public override string ToString()
    {
        return DieX + "/" + DieY + ": " + Score + " (" + ScoreBonus + ")";
    }

    private static bool isFlipX, isFlipY;
    public static void FlipX()
    {
        isFlipX = !isFlipX;
        for (int x = 0; x < Board.Size / 2; x++)
        {
            for (int y = 0; y < Board.Size; y++)
            {
                int tmp = Grid[x * Size + y];
                Grid[x * Size + y] = Grid[(Size - 1 - x) * Size + y];
                Grid[(Size - 1 - x) * Size + y] = tmp;
            }
        }
    }

    public static void FlipY()
    {
        isFlipY = !isFlipY;
        for (int x = 0; x < Board.Size; x++)
        {
            for (int y = 0; y < Board.Size / 2; y++)
            {
                int tmp = Grid[x * Size + y];
                Grid[x * Size + y] = Grid[x * Size + (Size - 1 - y)];
                Grid[x * Size + (Size - 1 - y)] = tmp;
            }
        }
    }

    public static void UnflipGrid()
    {
        if (isFlipX) FlipX();
        if (isFlipY) FlipY();
    }

    public Board Unflip()
    {
        bool fx = isFlipX, fy = isFlipY;
        UnflipGrid();
        List<Board> path = new List<Board>();
        Board current = this;
        while (current != null)
        {
            path.Add(current);
            current = current.Parent;
        }

        path.Reverse();
        Board result = new Board();
        result.Init(fx ? Board.Size - 1 - path[0].DieX : path[0].DieX, fy ? Size - 1 - path[0].DieY : path[0].DieY);
        foreach (Board board in path.Skip(1))
        {
            int x = fx ? Board.Size - 1 - board.DieX : board.DieX;
            int y = fy ? Board.Size - 1 - board.DieY : board.DieY;
            result = result.Expand().First(b => b.DieX == x && b.DieY == y);
            result.Stage = board.Stage;
        }

        if (fx) FlipX();
        if (fy) FlipY();
        return result;
    }

    public List<Board> GetPath()
    {
        List<Board> path = new List<Board>();
        Board current = this;
        SideValues = new int[6];
        for (int side = 0; side < 6; side++)
        {
            int max = 0;
            for (int v = 1; v <= V; v++)
            {
                if (v * array[HitOffset + side + 6 * v] > array[HitOffset + side + 6 * SideValues[side]] * SideValues[side]) SideValues[side] = v;
                max = Math.Max(max, v * array[HitOffset + side + 6 * v]);
            }
        }

        while (current != null)
        {
            path.Add(current);
            current.SideValues = SideValues;
            current.ComputeScore();
            current = current.Parent;
        }
        path.Reverse();
        return path;
    }
}