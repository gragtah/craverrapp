def printList(listdata):
        print("""
            <style>
            .placesNearYou{
            margin-top:100px;
            text-align:center;
            }
            @media screen and (min-width: 375px) and (max-width:450px) {
                .placesNearYou{
                    margin-top:200px;
                    }
            }
            </style>
        """)
        print("<div class='placesNearYou'>")
        print("<h2>Places Near You!</h2>")
        print("<ol style='list-style:none;margin-left: -60px;'>")
        for x in range(0,len(listdata[0])):
                    print("<li>")
                    print("<b>")
                    print listdata[0][x]
                    print("</b>")
                    print("<ul>")
                    print("<li style='list-style:none;'>")
                    print "Distance from You:",listdata[1][x],"Kilometers"
                    print("</li>")
                    print("</ul>")
                    print("</li>")
        print("</ol>")
        print("</div>")
