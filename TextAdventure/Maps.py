
from Colors import cl

def MapFlatlands(startLocation, location):
    flatlandsList = [startLocation, "the town", "the flatlands",
    "the forest", "the mountains", "the islands", "mystic ruins", "the castle","green land","the desert","the lake"]
    
    a = []
    for i in range(0,len(flatlandsList)):
        a.append("      ")
        if location == flatlandsList[i] :
            a[i] = f"{cl.RED}  X   {cl.RESET}" 

    print (f'''
                       ,-.^._                 
                     .'The Castle .        
          /`-.  ,----'   {a[7]}.  `-.   _  ,-.,
       _.'   `--'              .       `-' '-'  ;
      :  The Lake        .  .  . The Mountains  ''--.
      ,' .{a[10]}    .            . {a[4]}           ;,--.
     :   .       .              .       . The Islands `--'_  ,-.
     :  The Desert            .       .      . {a[5]},-. `-' '-'
     :    {a[9]}             .      .        .      :'-'
     ;       .               .   .     mystic ruins:
    (         .         The Forest        {a[4]} ;
     `-.       .          {a[3]}             ,'
       ;    Green Land        .              :
     .'       {a[8]}          .       . .-._,'
   .'             .          .        `.
_.' The Town . . The Flatlands       .__;
`._ {a[1]}         {a[2]}             ;
   `.              .              :..'
     `.           .    ,..__,---._;   
       `-._. {startLocation} ;               
            `.-{a[0]}-.;```             

''')


# MAP:
#                                         
#                                                              The Lake        The Castle
#                                  N                               I                I
#                                W + E                             I                I
#                                  S                          The Dessert --- The Mountains
#                                                                  I                I        
#                                                                  I                I
#                                                             Green Land            I
#                                                                  I                I
#                                                                  I                I
#                                                The Town --- The Flatlands --- The Forest --- The Islands
#                                                                  I                               I
#                                                                  I                               I
#                                                             Starting Area                    mystic ruins                    
#                                         
#