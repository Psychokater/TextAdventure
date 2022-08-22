class cl:
    GREEN   =  '\033[92m'
    BLUE    =  '\033[94m'
    YELLOW  =  '\033[93m' 
    RED     =  '\033[91m'
    RESET   =  '\033[0m' #RESET COLOR

from Colors import cl

print(f"""
           ,                        '           .        '        ,                     .        '
   .            .        '       .         ,         
                                                   .       '     +          .        '
       +          {cl.YELLOW}.-'''''-.{cl.RESET}       '     +
                {cl.YELLOW}.'         `.{cl.RESET}    +     .             
       ___     {cl.YELLOW}:             :{cl.RESET}                        .     '                  .    '     +      '
  ____/   \   {cl.YELLOW}:               :{cl.RESET}      .              ||
 /         \  {cl.YELLOW}:      {cl.RESET}_/|{cl.YELLOW}      :{cl.RESET}    `           ,.|| ||             
/  ,   '  . \  {cl.YELLOW}:    {cl.RESET}/_/{cl.YELLOW}      :{cl.RESET}       '           || || ||   .                     .        '
    |        \  {cl.YELLOW}`.{cl.RESET}_/ |{cl.YELLOW}     .'{cl.RESET}                    \\\\ || ||...    ,     '     +
   ;|,   '   (   /  ,|{cl.YELLOW}...-'{cl.RESET}            '   ,      \\\\|| //             
 ___|____     \_/^\/||__             __.________,.  ||//         .  ,  '     +
           _/~  `""~`"` \_           ''(       ..\.,||/       '                         .        '
 ..,...  __/  -'/  `-._ `\_\__          \           ||``\___,.__.____
              '`  `\   \  \-.\          /_:_,..     || ____/         \\________Î.,___________,.
                                            ______/"###""")
########################################################################