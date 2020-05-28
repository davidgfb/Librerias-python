using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;


/* sample program to inspect working variables during SHA-256
msarmento 2015 - msarmento@hotmail.com
*/




namespace sha256_c
{
    public partial class Form1 : Form
    {

        public bool next_flag;
        public static AutoResetEvent click_event  = new AutoResetEvent(false);
        public Form1()
        {
            InitializeComponent();
        }


        public string convert_to_bits(byte input, int size)
        {
            int n = 0;
            byte result = 0;
            string return_string = "";
            for (n = size -1 ; n >= 0; n--)

            {
                result = (byte)Math.Pow(2, n);
                if ((input & result) != 0)

                    return_string = return_string + "1";

                else
                    return_string = return_string + "0";
                                                
            }


            return (return_string);

        }

        public string convert_to_bits64( ulong input, int size)
        {
            int n = 0;
            ulong result = 0;
            string return_string = "";
            for (n = size - 1; n >= 0; n--)

            {
                result = (byte)Math.Pow(2, n);
                if ((input & result) != 0)

                    return_string = return_string + "1";

                else
                    return_string = return_string + "0";

            }


            return (return_string);

        }


        private void textBox1_TextChanged(object sender, EventArgs e)
        {


            int message_len;
            int n,i;
            textBoxbits.Clear();
            byte  hex_byte;
            string bit_string;
            uint[] W;
            uint[] j;
            uint Ch, Maj, Soma0, Soma1, Sigma0,Sigma1;
            uint T1, T2;
            uint H0, H1, H2, H3, H4, H5, H6, H7;

            string string_bits = "";
           


            int posx, posy, current_pos;
            //inicializacao do  bloco 
            //These words were obtained by taking the first thirty-two bits of the fractional parts
            //of the square roots of the first eight prime numbers.




            System.Drawing.SolidBrush myBrush = new System.Drawing.SolidBrush(System.Drawing.Color.White);
            System.Drawing.Graphics formGraphics;
            formGraphics = this.CreateGraphics();

            H0 = 0x6A09E667;
        H1 = 0xBB67AE85;
        H2 = 0x3C6EF372;
        H3 = 0xA54FF53A;
        H4 = 0x510E527F;
        H5 = 0x9B05688C;
        H6 = 0x1F83D9AB;
        H7 = 0x5BE0CD19;



            UInt32 aa, bb, cc, dd, ee, ff, gg, hh;

            j = new uint[64]  {
                0x428A2F98, 0x71374491, 0xB5C0FBCF, 0xE9B5DBA5, 0x3956C25B, 0x59F111F1, 0x923F82A4, 0xAB1C5ED5,
                            0xD807AA98, 0x12835B01, 0x243185BE, 0x550C7DC3, 0x72BE5D74, 0x80DEB1FE, 0x9BDC06A7, 0xC19BF174,
                            0xE49B69C1, 0xEFBE4786, 0x0FC19DC6, 0x240CA1CC, 0x2DE92C6F, 0x4A7484AA, 0x5CB0A9DC, 0x76F988DA,
                            0x983E5152, 0xA831C66D, 0xB00327C8, 0xBF597FC7, 0xC6E00BF3, 0xD5A79147, 0x06CA6351, 0x14292967,
                            0x27B70A85, 0x2E1B2138, 0x4D2C6DFC, 0x53380D13, 0x650A7354, 0x766A0ABB, 0x81C2C92E, 0x92722C85,
                            0xA2BFE8A1, 0xA81A664B, 0xC24B8B70, 0xC76C51A3, 0xD192E819, 0xD6990624, 0xF40E3585, 0x106AA070,
                            0x19A4C116, 0x1E376C08, 0x2748774C, 0x34B0BCB5, 0x391C0CB3, 0x4ED8AA4A, 0x5B9CCA4F, 0x682E6FF3,
                            0x748F82EE, 0x78A5636F, 0x84C87814, 0x8CC70208, 0x90BEFFFA, 0xA4506CEB, 0xBEF9A3F7, 0xC67178F2};







            W = new uint[64];

            message_len = textBox1.Text.Length;
            lbl_message_len.Text = message_len + " bytes (" + message_len * 8 + " bits)";
            lbl_padding.Text = "Padding:" + (448 - ((message_len * 8) + 1));

            for (n = 0; n < message_len; n++)

            {

                hex_byte = (byte) Convert.ToByte ( textBox1.Text.ElementAt(n));


                bit_string = convert_to_bits(hex_byte, 8);
                
                
            textBoxbits.Text = textBoxbits.Text + bit_string;

            }


            //add the 1 bit
        textBoxbits.Text = textBoxbits.Text + "1";


            //padding 
            for (n = 1; n <= 448 - ((message_len * 8) + 1); n++)
            {
                textBoxbits.Text = textBoxbits.Text + "0";
            }

            // add the message size
            bit_string = convert_to_bits64((ulong)(message_len *8), 64);
            textBoxbits.Text = textBoxbits.Text + bit_string;


            //======================================================


          //initialize the W values

            for (n=0; n<16;n++)
            {
                
                bit_string = textBoxbits.Text.Substring(480, 32);

                bit_string = textBoxbits.Text.Substring(n * 32, 32);
                W[n] = Convert.ToUInt32(bit_string,2);

            }


            // initialize the working variables

            aa = H0;
            bb = H1;
            cc = H2;
            dd = H3;
            ee = H4;
            ff = H5;
            gg = H6;
            hh = H7;


            // main loop 

            for (n=0; n < 64; n++)

            {


                Ch = (ee & ff) ^ (~ee & gg);

                Maj = (aa & bb) ^ (aa & cc) ^ (bb & cc);

                Soma0 = ((aa << 30) | (aa >> 2)) ^ ((aa << 19) | (aa >> 13)) ^ ((aa << 10) | (aa >> 22));

                Soma1 = ((ee << 26) | (ee >> 6)) ^ ((ee << 21) | (ee >> 11)) ^ ((ee << 7) | (ee >> 25));


                if (n > 15)
                {

                    Sigma0 = ((W[n - 15] << 25) | (W[n - 15] >> 7)) ^ ((W[n - 15] << 14) | (W[n - 15] >> 18)) ^ (W[n - 15] >> 3);
                    Sigma1 = ((W[n - 2] << 15) | (W[n - 2] >> 17)) ^ ((W[n - 2] << 13) | (W[n - 2] >> 19)) ^ (W[n - 2] >> 10);
                    W[n] = Sigma1 + W[n - 7] + Sigma0 + W[n - 16];

                }


                T1 = hh + Soma1 + Ch + j[n] + W[n];
                T2 = Soma0 + Maj;

                hh = gg;
                gg = ff;
                ff = ee;
                ee = dd + T1;
                dd = cc;
                cc = bb;
                bb = aa;
                aa = T1 + T2;


              

                label_aa.Text = "var a: " + Convert.ToString(aa, 16).PadLeft(8,'0').ToUpper();
                label_bb.Text = "var b: " + Convert.ToString(bb, 16).PadLeft(8, '0').ToUpper(); 
                label_cc.Text = "var c: " + Convert.ToString(cc, 16).PadLeft(8, '0').ToUpper(); 
                label_dd.Text = "var d:" + Convert.ToString(dd, 16).PadLeft(8, '0').ToUpper(); 
                label_ee.Text = "var e:" + Convert.ToString(ee, 16).PadLeft(8, '0').ToUpper(); 
                label_ff.Text = "var f:" + Convert.ToString(ff, 16).PadLeft(8, '0').ToUpper(); 
                label_gg.Text = "var g:" + Convert.ToString(gg, 16).PadLeft(8, '0').ToUpper(); 
                label_hh.Text = "var h:" + Convert.ToString(hh, 16).PadLeft(8, '0').ToUpper();




                //lazy coding ... convert to a function sometime
                string_bits = Convert.ToString(aa, 2).PadLeft(32, '0');
                posy = label_aa.Top + label_aa.Height + 10;
               posx = label_aa.Left;
                current_pos = posx;
                myBrush.Color = Color.Red;
                formGraphics.FillRectangle(myBrush, new Rectangle(current_pos - 10 , posy + n * 3, 6, 2));




                for (i = 0; i < 32; i++)
                {
                   
                    if ( string_bits.Substring(i,1)  == "0")
                       myBrush.Color = Color.Black;
                    else
                      myBrush.Color = Color.White;
                    formGraphics.FillRectangle(myBrush, new Rectangle(posx +i* 3, posy +  n * 3, 2, 2));
                }

                string_bits = Convert.ToString(bb, 2).PadLeft(32, '0');
                posy = label_bb.Top + label_bb.Height + 10;
                posx = label_bb.Left;
                for (i = 0; i < 32; i++)
                {
                    if (string_bits.Substring(i, 1) == "0")
                        myBrush.Color = Color.Black;
                    else
                        myBrush.Color = Color.White;
                    formGraphics.FillRectangle(myBrush, new Rectangle(posx + i * 3, posy + n * 3, 2, 2));
                }

                string_bits = Convert.ToString(cc, 2).PadLeft(32, '0');
                posy = label_cc.Top + label_cc.Height + 10;
                posx = label_cc.Left;
                for (i = 0; i < 32; i++)
                {
                    if (string_bits.Substring(i, 1) == "0")
                        myBrush.Color = Color.Black;
                    else
                        myBrush.Color = Color.White;
                    formGraphics.FillRectangle(myBrush, new Rectangle(posx + i * 3, posy + n * 3, 2, 2));
                }

                string_bits = Convert.ToString(dd, 2).PadLeft(32, '0');
                posy = label_dd.Top + label_dd.Height + 10;
                posx = label_dd.Left;
                for (i = 0; i < 32; i++)
                {
                    if (string_bits.Substring(i, 1) == "0")
                        myBrush.Color = Color.Black;
                    else
                        myBrush.Color = Color.White;
                    formGraphics.FillRectangle(myBrush, new Rectangle(posx + i * 3, posy + n * 3, 2, 2));
                }

                string_bits = Convert.ToString(ee, 2).PadLeft(32, '0');
                posy = label_ee.Top + label_ee.Height + 10;
                posx = label_ee.Left;
                for (i = 0; i < 32; i++)
                {
                    if (string_bits.Substring(i, 1) == "0")
                        myBrush.Color = Color.Black;
                    else
                        myBrush.Color = Color.White;
                    formGraphics.FillRectangle(myBrush, new Rectangle(posx + i * 3, posy + n * 3, 2, 2));
                }

                string_bits = Convert.ToString(ff, 2).PadLeft(32, '0');
                posy = label_ff.Top + label_ff.Height + 10;
                posx = label_ff.Left;
                for (i = 0; i < 32; i++)
                {
                    if (string_bits.Substring(i, 1) == "0")
                        myBrush.Color = Color.Black;
                    else
                        myBrush.Color = Color.White;
                    formGraphics.FillRectangle(myBrush, new Rectangle(posx + i * 3, posy + n * 3, 2, 2));
                }

                string_bits = Convert.ToString(gg, 2).PadLeft(32, '0');
                posy = label_gg.Top + label_gg.Height + 10;
                posx = label_gg.Left;
                for (i = 0; i < 32; i++)
                {
                    if (string_bits.Substring(i, 1) == "0")
                        myBrush.Color = Color.Black;
                    else
                        myBrush.Color = Color.White;
                    formGraphics.FillRectangle(myBrush, new Rectangle(posx + i * 3, posy + n * 3, 2, 2));
                }

                string_bits = Convert.ToString(hh, 2).PadLeft(32, '0');
                posy = label_hh.Top + label_hh.Height + 10;
                posx = label_hh.Left;
                for (i = 0; i < 32; i++)
                {
                    if (string_bits.Substring(i, 1) == "0")
                        myBrush.Color = Color.Black;
                    else
                        myBrush.Color = Color.White;
                    formGraphics.FillRectangle(myBrush, new Rectangle(posx + i * 3, posy + n * 3, 2, 2));
                }

                if (checkStep.Checked == true)
                {
                    while (next_flag == false)
                    {
                        System.Threading.Thread.Sleep(100);
                        Application.DoEvents();
                       
                    }

                    next_flag = false;
                    }

                myBrush.Color = Color.Green;
                formGraphics.FillRectangle(myBrush, new Rectangle(current_pos - 10, posy + n * 3, 6, 2));


                label_step.Text = "Loop step : " +  Convert.ToString(n,10);
 
                this.Update();
            }

            // finaliza o processamento do bloco

            H0 = H0 + aa;
            H1 = H1 + bb;
            H2 = H2 + cc;
            H3 = H3 + dd;
            H4 = H4 + ee;
            H5 = H5 + ff;
            H6 = H6 + gg;
            H7 = H7 + hh;



            //show result SHA

            label1.Text = Convert.ToString(H0, 16).PadLeft(8, '0').ToUpper(); 
            label2.Text = Convert.ToString(H1, 16).PadLeft(8, '0').ToUpper(); 
            label3.Text = Convert.ToString(H2, 16).PadLeft(8, '0').ToUpper(); 
            label4.Text = Convert.ToString(H3, 16).PadLeft(8, '0').ToUpper(); 
            label5.Text = Convert.ToString(H4, 16).PadLeft(8, '0').ToUpper(); 
            label6.Text = Convert.ToString(H5, 16).PadLeft(8, '0').ToUpper(); 
            label7.Text = Convert.ToString(H6, 16).PadLeft(8, '0').ToUpper(); 
            label8.Text = Convert.ToString(H7, 16).PadLeft(8, '0').ToUpper(); 

           

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text = "";
            label2.Text = "";
            label3.Text = "";
            label4.Text = "";
            label5.Text = "";
            label6.Text = "";
            label7.Text = "";
            label8.Text = "";
            
            label_aa.Text = "";
            label_bb.Text = "";
            label_cc.Text = "";
            label_dd.Text = "";
            label_ee.Text = "";
            label_ff.Text = "";
            label_gg.Text = "";
            label_hh.Text = "";

            lbl_message_len.Text = "";
            lbl_padding.Text = "";

            next_flag = false;
        }

        private void button1_Click(object sender, EventArgs e)
        {

            click_event.Set();


        }

        private void checkStep_CheckedChanged(object sender, EventArgs e)
        {
            if (checkStep.Checked == true)
                button1.Enabled = true;
            else
            {
                button1.Enabled = false;
                next_flag = true;
            }
               
        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            next_flag = true;
        }

        private void fileToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void aboutToolStripMenuItem_Click(object sender, EventArgs e)
        {
            AboutBox1 box = new AboutBox1();
            box.ShowDialog();
        }
    }
}
