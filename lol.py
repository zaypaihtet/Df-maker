RED = '\033[91m'
Yellow = '\033[93m'
Green = '\033[92m' 
import os
import sys
import time

#Function
def Writertext(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)

#Banner
time.sleep(1)
banner ="""
         
	\033[1;33;40m  ██████   ██████ █████ █████   █████████   ██████   █████ ██████   ██████   █████████   ███████████  
	\033[1;33;40m ░░██████ ██████ ░░███ ░░███   ███░░░░░███ ░░██████ ░░███ ░░██████ ██████   ███░░░░░███ ░░███░░░░░███ 
	\033[1;33;40m  ░███░█████░███  ░░███ ███   ░███    ░███  ░███░███ ░███  ░███░█████░███  ░███    ░███  ░███    ░███ 
	\033[1;32;40m  ░███░░███ ░███   ░░█████    ░███████████  ░███░░███░███  ░███░░███ ░███  ░███████████  ░██████████  
	\033[1;32;40m  ░███ ░░░  ░███    ░░███     ░███░░░░░███  ░███ ░░██████  ░███ ░░░  ░███  ░███░░░░░███  ░███░░░░░███ 
	\033[1;31;40m  ░███      ░███     ░███     ░███    ░███  ░███  ░░█████  ░███      ░███  ░███    ░███  ░███    ░███ 
	\033[1;31;40m  █████     █████    █████    █████   █████ █████  ░░█████ █████     █████ █████   █████ █████   █████
	\033[1;31;40m ░░░░░     ░░░░░    ░░░░░    ░░░░░   ░░░░░ ░░░░░    ░░░░░ ░░░░░     ░░░░░ ░░░░░   ░░░░░ ░░░░░   ░░░░░ 
"""
Writertext(banner)
a = """
	
	\033[1;31;40m Author:RED_Z
	\033[1;34;40m Facebook:www.facebook.com/zaypaihtet
	\033[1;34;40m Date   : 2021-10-5
	\033[1;31;40m Don't Copy My Script!!!! If you copy my script I will come to your home and f**k your ass :)
"""
Writertext(a)

# Input Question
print(" ")
print(" ")
title = input("\033[1;36;40m[+] Enter Deface Page Title : ")
print(" ")
time.sleep(1)
img = input("\033[1;36;40m[+] Enter Image Link (https://.....) : ")
print(" ")
time.sleep(1)
Hacker_CN = input("\033[1;36;40m[+] Enter Your Name : ")
print(" ")
time.sleep(1)
message = input("\033[1;36;40m[+] Enter Your Message On The Website (You Can Use <br> To Step Line Under) : ")
print(" ")
song = input("\033[1;36;40m[+] Enter Your Song link : ")
print(" ")
time.sleep(1)
choice = input("\033[1;36;40m[+] Do You Want To Continue [y/n] : ")

# Source Code
code1 = """<html>
<head>
<title>"""

code2 = title

code3 = """</title>
</head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <meta name="author" content="RED_Z">
    
	<link rel="SHORTCUT ICON" href="https://i.gifer.com/3O6Ec.gif" />
	<link href="https://fonts.googleapis.com/css2?family=Iceland&display=swap" rel="stylesheet">
<style>
    
    body {
      background: #000;
      padding-bottom: 40px;
      color: #000;
      
      -webkit-transform: rotateX(90deg);
      -moz-transform: rotateX(90deg);
      -ms-transform: rotateX(90deg);
      -o-transform: rotateX(90deg);
      transform: rotateX(90deg);
      -webkit-transform: translateZ(-100px);
      -moz-transform: translateZ(-100px);
      -ms-transform: translateZ(-100px);
      -o-transform: translateZ(-100px);
      transform: translateZ(-100px);
      -webkit-animation: rain 3s infinite linear;
      -moz-animation: rain 3s infinite linear;
      -ms-animation: rain 3s infinite linear;
      -o-animation: rain 3s infinite linear;
      animation: rain 3s infinite linear;
    }
    @-webkit-keyframes rain {
      from { background-position: left 0px, 40px 0px, left 0px; }
      to   { background-position: left 200px, 40px 200px, left 300px; }
    }
    @-moz-keyframes rain {
      from { background-position: left 0px, 40px 0px, left 0px; }
      to   { background-position: left 200px, 40px 200px, left 300px; }
    }
    @-ms-keyframes rain {
      from { background-position: left 0px, 40px 0px, left 0px; }
      to   { background-position: left 200px, 40px 200px, left 300px; }
    }
    @-o-keyframes rain {
      from { background-position: left 0px, 40px 0px, left 0px; }
      to   { background-position: left 200px, 40px 200px, left 300px; }
    }
    @keyframes rain {
      from { background-position: left 0px, 40px 0px, left 0px; }
      to   { background-position: left 200px, 40px 200px, left 300px; }
    }
  
    .featurette-divider {
      margin: 80px 0; /* Space out the Bootstrap <hr> more */
    }
    .featurette {
      padding-top: 0px; /* Vertically center images part 1: add padding above and below text. 
    }
    .featurette-image {
      margin-top: -120px; /* Vertically center images part 3: negative margin up the image the same amount of the padding to center it. */
    }
    /
    .featurette-image.pull-left {
      margin-right: 40px;
    }
    .featurette-image.pull-right {
      display: block;
        float: none;
        max-width: 40%;
        margin: 0 auto 20px;
    }
   
    .featurette-heading {
      font-size: 50px;
      font-weight: 300;
      line-height: 1;
      letter-spacing: -1px;
	  
	  font-family: Verdana, Arial, Helvetica, sans-serif; 
	  color : black;
    }
   
    @media (max-width: 979px) {
      .featurette {
        height: auto;
        padding: 0;
      }
	  
      .featurette-image.pull-left,
      .featurette-image.pull-right {
        display: block;
        float: none;
        max-width: 40%;
        margin: 0 auto 20px;
      }
    }
    @media (max-width: 767px) {
      .featurette-heading {
        font-size: 30px;
      }
      .featurette .lead {
        font-size: 15px;
        line-height: 1.5;
      }
    }
    </style>	
    <body>

	<br><br><div class="featurette">"""
	
code4 = """<center><img src="""

code5 = img

code6 = """
		</center><center><h2 class="featurette-heading"><b>
		<script> 
		farbbibliothek = new Array(); 
		farbbibliothek[0] = new Array("#FF0000","#FF1100","#FF2200","#FF3300","#FF4400","#FF5500","#FF6600","#FF7700","#FF8800","#FF9900","#FFaa00","#FFbb00","#FFcc00","#FFdd00","#FFee00","#FFff00","#FFee00","#FFdd00","#FFcc00","#FFbb00","#FFaa00","#FF9900","#FF8800","#FF7700","#FF6600","#FF5500","#FF4400","#FF3300","#FF2200","#FF1100"); 
		farbbibliothek[1] = new Array("#00FF00","#000000","#00FF00","#00FF00"); 
		farbbibliothek[2] = new Array("#00FF00","#FF0000","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00","#00FF00"); 
		farbbibliothek[3] = new Array("#FF0000","#FF4000","#FF8000","#FFC000","#FFFF00","#C0FF00","#80FF00","#40FF00","#00FF00","#00FF40","#00FF80","#00FFC0","#00FFFF","#00C0FF","#0080FF","#0040FF","#0000FF","#4000FF","#8000FF","#C000FF","#FF00FF","#FF00C0","#FF0080","#FF0040"); 
		farbbibliothek[4] = new Array("#FF0000","#EE0000","#DD0000","#CC0000","#BB0000","#AA0000","#990000","#880000","#770000","#660000","#550000","#440000","#330000","#220000","#110000","#000000","#110000","#220000","#330000","#440000","#550000","#660000","#770000","#880000","#990000","#AA0000","#BB0000","#CC0000","#DD0000","#EE0000"); 
		farbbibliothek[5] = new Array("#000000","#000000","#000000","#FFFFFF","#FFFFFF","#FFFFFF"); 
		farbbibliothek[6] = new Array("#0000FF","#FFFF00"); 
		farben = farbbibliothek[4];
		function farbschrift() 
		{ 
			for(var i=0 ; i<Buchstabe.length; i++) 
			{ 
				document.all["a"+i].style.color=farben[i]; 
			} 
			farbverlauf(); 
		} 
		function string2array(text) 
		{ 
			Buchstabe = new Array(); 
			while(farben.length<text.length) 
			{ 
				farben = farben.concat(farben); 
			} 
			k=0; 
			while(k<=text.length) 
			{ 
				Buchstabe[k] = text.charAt(k); 
				k++; 
			} 
		} 
		function divserzeugen() 
		{ 
			for(var i=0 ; i<Buchstabe.length; i++) 
			{ 
				document.write("<span id='a"+i+"' class='a"+i+"'>"+Buchstabe[i] + "</span>"); 
			} 
			farbschrift(); 
		} 
		var a=1; 
		function farbverlauf() 
		{ 
			for(var i=0 ; i<farben.length; i++) 
			{ 
				farben[i-1]=farben[i]; 
			} 
			farben[farben.length-1]=farben[-1]; 
 
			setTimeout("farbschrift()",30); 
		} 
		// Zu Demonstrationszwecken***************** 
		var farbsatz=1; 
		function farbtauscher() 
		{ 
			farben = farbbibliothek[farbsatz]; 
			while(farben.length<text.length) 
			{ 
				farben = farben.concat(farben); 
			} 	
			farbsatz=Math.floor(Math.random()*(farbbibliothek.length-0.0001)); 
		} 
		setInterval("farbtauscher()",4500); 
		text=" You Have Been Hacked ";
//h 
		string2array(text);
		divserzeugen(); 
//document.write(text);   
//
/*function expand() {
for(x = 0; x < 50; x++) {
window.moveTo(screen.availWidth * -(x - 50) / 100, screen.availHeight * -(x - 50) / 100);
window.resizeTo(screen.availWidth * x / 50, screen.availHeight * x / 50);
}
window.moveTo(0,0);
window.resizeTo(screen.availWidth, screen.availHeight);
}
expand();*/
	</script>"""

code7 = """</b></h2></center>
		<hr width="80%" style="color:black" />
		<div style="background : black; padding : 10px;">
<b><center>
<font face="Tahoma" size="5" color=red>"""




code8 = """[<marquee style="width:200px;height:24px;"><font face="Iceland" color=white>Hacked By : <font face="Iceland" color=red>"""

code9 = Hacker_CN

code10 = """<font color=red></font></font></marquee>]</font></center></b>
		</div>"""

code11 = """
<p style="font-family: Verdana, Arial, Helvetica, sans-serif; font-size : 16px;" align="center"><font style="font-family: Verdana, Arial, Helvetica, sans-serif; color : red; font-size : 16px;" align="center">Hello <font style="font-family: Verdana, Arial, Helvetica, sans-serif; color : white; font-size : 16px;" align="center">"""

code12 = message 

code13 = """</p>
    </div>
	<br/><br/>"""

code14 ="""<iframe width="0%" height="0" scrolling="no" frameborder="no" allow="autoplay" loop="true" src="""
	
code15 = song

code16 ="""></iframe>"""

code17 ="""
  </body>
</html>"""


if choice == "y":
	time.sleep(3)
	os.system("clear")
	Writertext("\033[1;32;40mGenerating Your Deface Page Please Wait A Second :)")
#Open the index
	fo = open("df.html","w")
	time.sleep(5)
elif choice == "n":
	exit()

fo.write(code1)
fo.write(code2)
fo.write(code3)
fo.write(code4)
fo.write(code5)
fo.write(code6)
fo.write(code7)
fo.write(code8)
fo.write(code9)
fo.write(code10)
fo.write(code11)
fo.write(code12)
fo.write(code13)
fo.write(code14)
fo.write(code15)
fo.write(code16)
fo.write(code17)

print(" ")
print ("""The  df page has been generate as : df.html.
If you don't like You can chain in html editor:)
Change file example : cp -r df.html /sdcard""")

fo.close()
