# class cl:
#     GREEN   =  '\033[92m'
#     BLUE    =  '\033[94m'
#     YELLOW  =  '\033[93m' 
#     RED     =  '\033[91m'
#     WHITE   = "\033[97m"
#     MAGENTA = "\033[95m"
#     CYAN    = "\033[96m"
#     RESET   =  '\033[0m' #RESET COLOR Nice
# from Colors import cl

# print(f"""   
#                      {cl.RED}(            
#                        )          
#                      (  (          
#                          )        
#                    (    ({cl.RESET}       
#                     {cl.RED}){cl.RESET} {cl.YELLOW}/\  {cl.RESET}{cl.RED}({cl.RESET}
#                   {cl.RED}({cl.RESET} {cl.YELLOW} //\  {cl.RESET} {cl.RED}({cl.RESET}     
#                 _ -.;{cl.MAGENTA}_/ \\{cl.RESET}--._    
#                (_;-{cl.MAGENTA}// | \ \{cl.RESET}-'.\   
#                ( `.__ _  ___,')   
#                 `'(_ )_)(_)_)'
# """)

a = ["X","X","X","X","X","X","X","X","X","X","X","X","X",]
startLocation = "test cave"
print (f'''
                       ,-.^._                 _
                     .'The Castle .        ,' ;
          /`-.  ,----'   . {a[6]}   `-.   _  ,-.,
       _.'   `--'         .       `-' '-'      ;
      :  The Lake    . .     The Mountains     ;__,-.
      ,' . {a[10]}      . .        {a[5]} .              ;_,-',. ,--.
     :   .       .               .      . The Islands -```    `--'
     :  The Desert               .     .    {a[4]} ;
     :    {a[9]}                    .   .      :
     ;       .                    . .       :
    (         .               The Forest    ;
     `-.       .               .  {a[3]}      ,'
       ;    Green Land        .              :
     .'       {a[8]}          .         . .-._,'
   .'               .     .          `.
_.' The Town . . The Flatlands       .__;
`._     {a[1]}        . {a[2]}             ;
   `.              .               :..'
     `.           .    ,..__,---._;   
       `-.__{startLocation} ;               
            `.--.{a[0]} ;             

''') 