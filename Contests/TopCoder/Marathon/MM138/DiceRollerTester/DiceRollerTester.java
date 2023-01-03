import java.awt.*;
import java.awt.geom.*;
import java.util.*;
import java.io.*;
import javax.imageio.*;
import java.util.List;
import java.util.ArrayList;
import java.awt.image.BufferedImage;

import com.topcoder.marathon.*;

public class DiceRollerTester extends MarathonAnimatedVis {
  // parameter ranges
  private static final int minN = 6, maxN = 30;         // grid size range
  private static final int minV = 3, maxV = 9;          // number of values range
  private static final double minP = 0.05, maxP = 0.3;  // negation probability range
  private static final double minB = 1.00, maxB = 1.2;  // bonus multiplier range

  // Inputs
  private int N;                // grid size
  private int V;                // number of values
  private double P;             // negation probability
  private double B;             // bonus multiplier

  // Derived values

  //Constants
  private static final int INF=-1000;

  // State Control
  private int[][] grid;
  private int[][] visited;
  private List<Integer> path;
  private int R=INF;
  private int C=INF;
  private int prevR=INF;
  private int prevC=INF;    
  private int startR=INF;
  private int startC=INF;      
  private int steps=0;
  private double score = 0;  
  private Dice dice;


  protected void generate() {
    N = randomInt(minN, maxN);
    V = randomInt(minV, maxV);
    P = randomDouble(minP, maxP);
    B = randomDouble(minB, maxB);

    //Special cases
    if (seed == 1)
    {
      N = minN;
      V = minV;
      P = 0.1;      
    }
    else if (seed == 2)
    {
      N = maxN;
      V = maxV;
      P = maxP;
    }

    //User defined parameters
    if (parameters.isDefined("N")) N = randomInt(parameters.getIntRange("N"), minN, maxN);
    if (parameters.isDefined("V")) V = randomInt(parameters.getIntRange("V"), minV, maxV);
    if (parameters.isDefined("P")) P = randomDouble(parameters.getDoubleRange("P"), minP, maxP);
    if (parameters.isDefined("B")) B = randomDouble(parameters.getDoubleRange("B"), minB, maxB);


    grid = new int[N][N];
    visited = new int[N][N];     //0=unvisited, 1=visited, 2=good match
    path = new ArrayList<Integer>();

    //generate the grid
    for (int row = 0; row < N; row++)
      for (int col = 0; col < N; col++)
      {
        grid[row][col] = randomInt(1,V);
        if (randomDouble(0,1) < P) grid[row][col]*=-1;
      }


    if (debug)
    {
      System.out.println("Grid size, N = " + N);
      System.out.println("Number of values, V = " + V);
      System.out.println("Negation probability, P = " + P);
      System.out.println("Bonus multiplier, B = " + B);

      for (int row = 0; row < N; row++)
      {
        for (int col = 0; col < N; col++)
          System.err.print(grid[row][col]+" ");
        System.out.println();
      }
    }
  }

  protected boolean isMaximize() {
      return true;
  }

  protected double run() throws Exception {
    init();
    return runAuto();
  }

  protected double runAuto() throws Exception {
    double score = callSolution();
    if (score < 0) {
      if (!isReadActive()) return getErrorScore();
      return fatalError();
    }
    return score;
  }

  protected void timeout() {
    addInfo("Time", getRunTime());
    update();
  }


  private double callSolution() throws Exception {
    writeLine(N);
    writeLine(V);
    writeLine(""+B);
    // print grid
    for (int row = 0; row < N; row++)
      for (int col = 0; col < N; col++)
        writeLine(grid[row][col]);
    flush();
    if (!isReadActive()) return -1;

    updateState();

    try {
      // Get the solution
      startTime();

      int top = Integer.parseInt(readLine());
      int bottom = Integer.parseInt(readLine());
      int front = Integer.parseInt(readLine());
      int back = Integer.parseInt(readLine());
      int left = Integer.parseInt(readLine());
      int right = Integer.parseInt(readLine());
      if (!correctFaces(new int[]{top,bottom,front,back,left,right}))
        return fatalError("All dice faces must be between 1 and V, inclusive.");        

      dice=new Dice(top, bottom, front, back, left, right);

      int numMoves = Integer.parseInt(readLine());       
      if (numMoves<=0 || numMoves>N*N)
        return fatalError("You must use between 1 and N*N moves, inclusive.");                

      String[] moves = new String[numMoves];
      for (int id = 0; id < numMoves; id++) moves[id] = readLine();

      stopTime();

      score = 0;
      for (int id = 0; id < numMoves; id++)
      {
        String[] move = moves[id].split(" ");
        if (move.length != 2)
          return fatalError("Cannot parse your output. You need to provide the location as Row Col");

        R = Integer.parseInt(move[0]);
        C = Integer.parseInt(move[1]);
        if (id==0)
        {
          startR=R;
          startC=C;
        }

        if (!inGrid(R, C))
          return fatalError("The cell (" + R + ", " + C + ") is outside the grid.");
        if (visited[R][C]>0)
          return fatalError("The cell (" + R + ", " + C + ") has already been visited.");
        if (prevR!=INF && Math.abs(R-prevR)+Math.abs(C-prevC)!=1)
          return fatalError("The path at cell (" + R + ", " + C + ") is disconnected.");
        
        makeMove();
      }

      //add bonus multiplier if path completes a loop
      if (Math.abs(R-startR)+Math.abs(C-startC)==1)
      {
        score*=B;
        if (hasVis())
        {      
          synchronized (updateLock)
          {
            addInfo("Bonus", "yes!");
            addInfo("Score", shorten(score));
          }
        }
        updateDelay();
      }
    }
    catch (Exception e) {
      if (debug) System.out.println(e.toString());
      return fatalError("Cannot parse your output");
    }

    return score;
  }

  private boolean correctFaces(int[] a)
  {
    for (int i : a)
      if (i<1 || i>V)
        return false;

    return true;
  }

  private void makeMove()    
  {
    //right
    if (C==prevC+1)
    {
      int temp=dice.right;
      dice.right=dice.top;
      dice.top=dice.left;
      dice.left=dice.bottom;
      dice.bottom=temp;
    }
    //left
    else if (C==prevC-1)
    {
      int temp=dice.right;
      dice.right=dice.bottom;
      dice.bottom=dice.left;
      dice.left=dice.top;
      dice.top=temp;
    }
    //up
    else if (R==prevR-1)
    {
      int temp=dice.front;
      dice.front=dice.bottom;
      dice.bottom=dice.back;
      dice.back=dice.top;
      dice.top=temp;
    }
    //down
    else if (R==prevR+1)
    {
      int temp=dice.front;
      dice.front=dice.top;
      dice.top=dice.back;
      dice.back=dice.bottom;
      dice.bottom=temp;
    }
    path.add(R*N+C);
    steps++;

    if (dice.bottom==Math.abs(grid[R][C]))
    {
      score+=grid[R][C];
      if (grid[R][C]>0) visited[R][C]=2;
      else visited[R][C]=1;
    }
    else
    {
      if (grid[R][C]>0) visited[R][C]=1;
      else visited[R][C]=2;
    }
    
    prevR=R;
    prevC=C;

    updateState();
  }

  protected void updateState()
  {
    if (hasVis())
    {      
      synchronized (updateLock) {
        if (dice!=null)
        { 
          addInfo("Top", dice.top);
          addInfo("Bottom", dice.bottom);
          addInfo("Front", dice.front);
          addInfo("Back", dice.back);
          addInfo("Left", dice.left);
          addInfo("Right", dice.right);
        }         
        addInfo("Score", shorten(score));               
        addInfo("Time",  getRunTime());   
      }
      updateDelay();
    }
  }     

  private boolean inGrid(int row, int col) {
    return row >= 0 && row < N && col >= 0 && col < N;
  }


  protected void paintContent(Graphics2D g)
  {
    //draw grid
    adjustFont(g, Font.SANS_SERIF, Font.PLAIN, String.valueOf("1"), new Rectangle2D.Double(0, 0, 0.5, 0.5));
    g.setStroke(new BasicStroke(0.005f, BasicStroke.CAP_ROUND, BasicStroke.JOIN_ROUND));    
    for (int row = 0; row < N; row++)
      for (int col = 0; col < N; col++)
      {          
        if (visited[row][col]==0) g.setColor(Color.white);
        if (visited[row][col]==1) g.setColor(Color.pink);
        if (visited[row][col]==2) g.setColor(Color.green);
        g.fillRect(col, row, 1, 1);

        g.setColor(Color.gray);
        g.drawRect(col, row, 1, 1);          
      }

    //draw path
    if (steps>1)
    {
      GeneralPath gp = new GeneralPath();          

      for (int i=0; i<steps; i++)
      {
        int pos=path.get(i);
        int r=pos/N;
        int c=pos%N;

        if (i==0) gp.moveTo(c+0.5,r+0.5);
        else      gp.lineTo(c+0.5,r+0.5);
      }

      g.setColor(new Color(0,0,255,80));    //transparent blue
      g.setStroke(new BasicStroke(0.05f, BasicStroke.CAP_ROUND, BasicStroke.JOIN_ROUND));
      g.draw(gp);

      g.setColor(Color.blue);
      g.drawRect(startC, startR, 1, 1);     //first square      
      g.drawRect(C, R, 1, 1);               //last square
    }           

    //draw numbers
    for (int row = 0; row < N; row++)
      for (int col = 0; col < N; col++)    
      {
        if (grid[row][col]>0) g.setColor(Color.black);
        else g.setColor(Color.red);
        drawString(g, String.valueOf(grid[row][col]), new Rectangle2D.Double(col + 0.5, row + 0.5, 0, 0));
      }
  }

  private double shorten(double a)
  {
    return (double)Math.round(a * 1000.0) / 1000.0;
  }

  private void init() {
    if (hasVis()) {
      setDefaultDelay(500);
      setContentRect(0, 0, N, N);
      setInfoMaxDimension(20, 15);
      addInfo("Seed", seed);
      addInfo("N", N);
      addInfo("V", V);
      addInfo("P", shorten(P));
      addInfo("B", shorten(B));
      addInfoBreak();
      addInfo("Top", "NA");
      addInfo("Bottom", "NA");
      addInfo("Front", "NA");
      addInfo("Back", "NA");
      addInfo("Left", "NA");
      addInfo("Right", "NA");                
      addInfoBreak();
      addInfo("Score", 0);
      addInfo("Bonus", "no");
      addInfo("Time", 0);
      update();
    }
  }

  public class Dice
  {
    int top, bottom, front, back, left, right;

    public Dice(int t, int bo, int f, int ba, int l, int r)
    {
      top=t;
      bottom=bo;
      front=f;
      back=ba;
      left=l;
      right=r;
    }       
  }    

  public static void main(String[] args) {
      new MarathonController().run(args);
  }
}