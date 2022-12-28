# <|[MADE BY blueTUZZ_01]|>
# <|[THE361 HACKERS TEAM]|>


import shodan
from rich.console import Console
from rich.panel import Panel
from rich import box
from os import system

console = Console()
logo = '''[bold red] .d0000b.  000                    000 Y00b   d00P 
d00P  Y00b 000                    000  Y00b d00P  
Y00b.      000                    000   Y00o00P   
 "Y000b.   00000b.   .d00b.   .d00000    Y000P    
    "Y00b. 000 "00b d00""00b d00" 000     000     
      "000 000  000 000  000 000  000     000     
Y00b  d00P 000  000 Y00..00P Y00b 000     000     
 "Y0000P"  000  000  "Y00P"   "Y00000     000[/] [bold italic green]shodan search tool[/]'''                          

apiFile = open("API_KEY.txt")
KEY = apiFile.read()
if KEY == '':
	console.print("[X]ERROR, PLEASE SET API KEY")
	exit()
else:
	pass
apiFile.close()


shodan = shodan.Shodan(KEY)

console.print(logo)
search = console.input("\n[italic bold green]{$}->[/]")

results = shodan.search(search)
console.print("[*]TOTAL RESULST: "+str(results['total']), style='green')
input('\nPRESS ENTER TO CONTINUE')

i = 1
for result in results['matches']:
	console.print(Panel.fit('[italic bold green]'+result['data']+'[/]', box=box.ASCII, title=result['ip_str'], subtitle="RESULT №"+str(i)), style='bold red')
	console.print("*********************************************************************", justify='center', style='red')
	i+=1