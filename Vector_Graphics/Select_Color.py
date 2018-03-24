# Generates a Panel where you can choose a color by clicking
# This python3 script generates a SVG. Open the .svg with a browser to see the panel

with open("Select_Color.svg", "w") as file_svg:
    # SVG headers
    file_svg.write("<!DOCTYPE html>\n" \
                    + "<html>\n" \
                    + "<body>\n" \
                    + "<svg width=\"500\" height=\"500\" xmlns=\"http://www.w3.org/2000/svg\">\n" \
                    + "\t<defs>\n" \
    	            + "\t\t<linearGradient id=\"linear\" x1=\"0%\" y1=\"0%\" x2=\"0%\" y2=\"100%\">\n" \
      		        + "\t\t<stop id=\"s0\" offset=\"0%\"   stop-color=\"#000\"/>\n" \
                    + "\t\t<stop id=\"s50\" offset=\"50%\"   stop-color=\"#5a0\"/>\n" \
                    + "\t\t<stop id=\"s100\" offset=\"100%\" stop-color=\"#fff\"/>\n" \
            	    + "\t\t</linearGradient>\n" \
  	                + "\t</defs>\n")

    # script handling onClick events
    file_svg.write("\t<script type=\"text/JavaScript\">\n" \
                    + "\t\t<![CDATA[\n" \
                    + "\t\tfunction clickEvent(r, g, b) {\n" \
                    + "\t\t\tvar color_50 = \"rgb(\" + r + \",\" + g + \",\" + b + \")\";\n" \
                    + "\t\t\tvar stop_50 = document.getElementById(\"s50\");\n" \
                    + "\t\t\tstop_50.setAttribute(\"stop-color\", color_50);\n" \
                    + "\t\t}]]>\n" \
                    + "\t</script>\n")

    step = 10
    for i in range(0, 255, step):
        for j in range(0, 255, step):
            (r, g, b) = (128, i, j)

            file_svg.write("\t<rect x=\"" + str(j) + "\" y=\"" + str(i) + "\" width=\"" + str(step) + "\" height=\"" + str(step) + "\" fill=\"rgb(" + str(r) + "," + str(g) + "," + str(b) + ")\" onclick=\"clickEvent(" + str(r) + "," + str(g) + "," + str(b) + ")\"/>\n")

    # Rectangular bar presenting the Selected Color
    file_svg.write("<rect x=\"260\" y=\"0\" width=\"20\" height=\"260\" fill=\"url(#linear)\" />")

    file_svg.write("</svg>\n" \
                   + "</body>\n" \
                   + "</html>\n")
