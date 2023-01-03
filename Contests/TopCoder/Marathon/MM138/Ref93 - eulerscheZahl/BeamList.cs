using System;
using System.Collections.Generic;

public class BeamList
{
    private int BeamOffset = -20;
    private static Random random = new Random(0);
    private List<List<Board>> beam = new List<List<Board>>();

    public BeamList(int beamOffset = -20)
    {
        this.BeamOffset = beamOffset;
    }
    public void Add(Board board)
    {
        if (board.Score < BeamOffset) return;
        while (beam.Count <= board.Score - BeamOffset) beam.Add(new List<Board>());
        beam[board.Score - BeamOffset].Add(board);
    }

    public List<Board> Extract(int beamWidth)
    {
        List<Board> result = new List<Board>();
        for (int i = beam.Count - 1; i >= 0; i--)
        {
            if (result.Count + beam[i].Count <= beamWidth) result.AddRange(beam[i]);
            else
            {
                int take = beamWidth - result.Count;
                for (int j = 0; j < take; j++)
                {
                    int rnd = random.Next(beam[i].Count - j) + j;
                    Board tmp = beam[i][j];
                    beam[i][j] = beam[i][rnd];
                    beam[i][rnd] = tmp;
                    result.Add(beam[i][j]);
                }
            }

            if (result.Count >= beamWidth) return result;
        }
        return result;
    }
}