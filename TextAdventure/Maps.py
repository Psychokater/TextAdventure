
def MapFlatlands(startLocation, location):
    flatlandsList = [startLocation, "the town", "the flatlands", "the forest", "the mountains", "the islands", "the castle"]
    
    a = []
    for i in range(0,len(flatlandsList)):
        a.append(" ")
        if location == flatlandsList[i] :
            a[i] = "X" 
        
            

    print (f'''
                       ,-.^._                 _
                     .'The Castel.        ,' ;
          /`-.  ,----'   . {a[6]}   `-.   _  ,-.,'  `
       _.'   `--'         .       `-' '-'      ;
      :                  The Mountens         ;__,-.
      ,'                     {a[5]}.               ;_,-',. ,--.
     :                           .        Islands,--```    `--'
     :                          .     ..{a[4]}   ;
     :                           .   .      :
     ;                            . .       :
    (                         The Forrest    ;
     `-.                       . .{a[3]}      ,'
       ;                    . .             :
     .'                    .         .-._,'
   .'                     .          `.
_.' The Town. . .The FlatLand       .__;
`._     {a[1]}          . {a[2]}            ;
   `.              .               :   
     `.           .    ,..__,---._;   
       `-.__Camp Fire:               
            `.--.{a[0]};             
                                     
                                     
                                     
''') 