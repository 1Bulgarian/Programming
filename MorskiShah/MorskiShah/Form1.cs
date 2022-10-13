using System.Runtime.Intrinsics.X86;

namespace MorskiShah
{
    public partial class Form1 : Form
    {
        string box1;
        string box2;
        string box3;
        string box4;
        string box5;
        string box6;
        string box7;
        string box8;
        string box9;
        int PlayerOneScore = 0;
        int PlayerTwoScore = 0;
        string startingPlayer = "O";
        string CP = "O";
        int currentCount = 0;

        int pointsforX = 0;
        int pointsforO = 0;
        public Form1()
        {
            InitializeComponent();
        }

        
        public string currentPlayer(string curr)
        {
            if (curr == "X")
            {
                pointsforX++;
                curr = "O";
            }
            else
            {
                curr = "X";
                pointsforO++;
            }
            lblCurrentlyPlaying.Text = curr;
            return curr;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            lblCurrentlyPlaying.Text = CP;

        }
        public bool checkDraw()
        {
            if(currentCount < 8)
            {
                return false;
            }
            else
            {
                if (checkwin("X") == false && checkwin("O") == false)
                {
                    string message = "The game ended in a draw. Should we restart the game? YES is for restarting, NO is for new game.";
                    string title = "Draw!";
                    MessageBoxButtons buttons = MessageBoxButtons.YesNo;
                    DialogResult result = MessageBox.Show(message, title, buttons);
                    if (result == DialogResult.Yes)
                    {
                        Application.Restart();
                    }
                    else
                    {
                        newGame();
                    }
                    return true;
                }
                return false;
            }
        }

        public bool swapPlayers()
        {
            if(startingPlayer == "O")
            {
                startingPlayer = "X";
                CP = "X";

            }
            else
            {
                startingPlayer = "O";
                CP = "O";
            }
            return true;
        }
        public bool newGame()
        {
            //Enabling the buttons again
            b1.Enabled = true;
            b2.Enabled = true;
            b3.Enabled = true;
            b4.Enabled = true;
            b5.Enabled = true;
            b6.Enabled = true;
            b7.Enabled = true;
            b8.Enabled = true;
            b9.Enabled = true;

            //Clearing the boxes
            b1.Text = "";
            b2.Text = "";
            b3.Text = "";
            b4.Text = "";
            b5.Text = "";
            b6.Text = "";
            b7.Text = "";
            b8.Text = "";
            b9.Text = "";

            currentCount = 0;
            swapPlayers();

            return true;
        }
        public bool victory(string victor)
        {
            b1.Enabled = false;
            b2.Enabled = false;
            b3.Enabled = false;
            b4.Enabled = false;
            b5.Enabled = false;
            b6.Enabled = false;
            b7.Enabled = false;
            b8.Enabled = false;
            b9.Enabled = false;


            if(victor == startingPlayer)
            {
                PlayerOneScore++;
                lblPlayerOneScore.Text = PlayerOneScore.ToString();
            }
            else
            {
                PlayerTwoScore++;
                lblPlayerTwoScore.Text = PlayerTwoScore.ToString();
            }

            string message = $"Player with '{victor}' won the game! Should we restart the game? YES is for restart, NO is for continuing.";
            string title = $"Victory for {victor}!";
            MessageBoxButtons buttons = MessageBoxButtons.YesNo;
            DialogResult result = MessageBox.Show(message, title, buttons);
            if (result == DialogResult.Yes)
            {
                Application.Restart();
            }
            else
            {
                newGame(); 
            }
            return true;
        }
        public bool checkwin(string current)
        {
            box1 = b1.Text;
            box2 = b2.Text;
            box3 = b3.Text;
            box4 = b4.Text;
            box5 = b5.Text;
            box6 = b6.Text;
            box7 = b7.Text;
            box8 = b8.Text;
            box9 = b9.Text;

            if (box1 == current && box2 == current && box3 == current)
            {
                victory(current);
                return true;
            }
            else if (box4 == current && box5 == current && box6 == current)
            {
                victory(current);
                return true;
            }
            else if (box7 == current && box8 == current && box9 == current)
            {
                victory(current);
                return true;
            }
            else if (box1 == current && box4 == current && box7 == current)
            {
                victory(current);
                return true;
            }
            else if (box2 == current && box5 == current && box8 == current)
            {
                victory(current);
                return true;
            }
            else if (box3 == current && box6 == current && box9 == current)
            {
                victory(current);
                return true;
            }
            else if (box1 == current && box5 == current && box9 == current)
            {
                victory(current);
                return true;
            }
            else if (box7 == current && box5 == current && box3 == current)
            {
                victory(current);
                return true;
            }

            return false;

        }
        private void button2_Click(object sender, EventArgs e)
        {
            b3.Enabled = false;
            b3.Text = CP;
            checkwin(CP);
            checkDraw();
            CP = currentPlayer(CP);
            currentCount += 1;
        }

        private void b1_Click(object sender, EventArgs e)
        {
            b2.Text = "kur";
        }

        private void b1_TextChanged(object sender, EventArgs e)
        {

        }

        private void b2_Click(object sender, EventArgs e)
        {
            b2.Enabled = false;
            b2.Text = CP;
            checkwin(CP);
            checkDraw();
            CP = currentPlayer(CP);
            currentCount += 1;
        }

        private void b1_Click_1(object sender, EventArgs e)
        {
            b1.Enabled = false;
            b1.Text = CP;
            checkwin(CP);
            checkDraw();
            CP = currentPlayer(CP);
            currentCount += 1;
        }

        private void b4_Click(object sender, EventArgs e)
        {
            b4.Enabled = false;
            b4.Text = CP;
            checkwin(CP);
            checkDraw();
            CP = currentPlayer(CP);
            currentCount += 1;
        }

        private void b5_Click(object sender, EventArgs e)
        {
            b5.Enabled = false;
            b5.Text = CP;
            checkwin(CP);
            checkDraw();
            CP = currentPlayer(CP);
            currentCount += 1;
        }

        private void b6_Click(object sender, EventArgs e)
        {
            b6.Enabled = false;
            b6.Text = CP;
            checkwin(CP);
            checkDraw();
            CP = currentPlayer(CP);
            currentCount += 1;
        }

        private void b7_Click(object sender, EventArgs e)
        {
            b7.Enabled = false;
            b7.Text = CP;
            checkwin(CP);
            checkDraw();
            CP = currentPlayer(CP);
            currentCount += 1;
        }

        private void b8_Click(object sender, EventArgs e)
        {
            b8.Enabled = false;
            b8.Text = CP;
            checkwin(CP);
            checkDraw();
            CP = currentPlayer(CP);
            currentCount += 1;
        }

        private void b9_Click(object sender, EventArgs e)
        {
            b9.Enabled = false;
            b9.Text = CP;
            checkwin(CP);
            checkDraw();
            CP = currentPlayer(CP);
            currentCount += 1;
        }
    }
}