using System;
using System.Collections.Generic;
using System.IO.Ports;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace diskretnaSistema2
{
    public class Reshenie : IEquatable<Reshenie>
    {
        public int id { get; set; }

        public int x { get; set; }
        public int n { get; set; }
        public string formula { get; set; }
        public string result { get; set; }
        public override bool Equals(object obj)
        {
            if (obj == null) return false;
            Reshenie objAsPart = obj as Reshenie;
            if (objAsPart == null) return false;
            else return Equals(objAsPart);
        }
        public override int GetHashCode()
        {
            return id;
        }
        public bool Equals(Reshenie other)
        {
            if (other == null) return false;
            return (this.id.Equals(other.id));
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            List<Reshenie> Resheniq = new List<Reshenie>();

            //Console.WriteLine("Last 3 letters of your facualty number:");
            //int fac = int.Parse(Console.ReadLine());

            Console.WriteLine("How many rows?:");
            int numberRows = int.Parse(Console.ReadLine());

            Console.WriteLine("From where to start?");
            int numberStart = int.Parse(Console.ReadLine());

            int previous = 0;
            for (int i = numberStart; i < numberRows; i++)
            {
                Console.WriteLine($"Value for X={i}");
                int k = int.Parse(Console.ReadLine());


                int l = Resheniq.Count();
                if(i==numberStart)
                {
                    Resheniq.Add(new Reshenie() { id = ++l, x=k, n=i, formula = $"y({i}) = (-1)^{i}*{k} + 2x({i -1}", result=$"y({i}) = Impossible to determine (out of boundries)" });
                }
                else
                {
                    double A = (Math.Pow(-1, i) * k) + (2 * previous);
                    Resheniq.Add(new Reshenie() { id = ++l, x = k, n = i, formula = $"y({i}) = (-1)^{i}*{k} + 2*{previous}", result = $"y({i}) = {A}" });
                }


                previous = k;
            }
            foreach (var m in Resheniq)
            {
                //Console.WriteLine($"y({m.n}) = (-1)^{m.n}*{m.x}");
                Console.WriteLine(m.formula);
                Console.WriteLine(m.result);
                Console.WriteLine();
            }

            Console.ReadLine();
        }
    }
}
