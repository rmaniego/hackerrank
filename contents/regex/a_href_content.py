import re

elements = [
            '<div class="portal" role="navigation" id="p-lang">',
            '<h3>Languages</h3>',
            '<div class="body">',
            '<ul>',
            '<li class="interwiki-simple"><a href="//simple.wikipedia.org/wiki/" title="" lang="simple" hreflang="simple">Simple English</a></li>',
            '<li class="interwiki-ar"><a href="//ar.wikipedia.org/wiki/" title="" lang="ar" hreflang="ar"></a></li>',
            '<li class="interwiki-id"><a href="//id.wikipedia.org/wiki/" title="" lang="id" hreflang="id">Bahasa Indonesia</a></li>',
            '<li class="interwiki-ms"><a href="//ms.wikipedia.org/wiki/" title="" lang="ms" hreflang="ms">Bahasa Melayu</a></li>',
            '<li class="interwiki-bg"><a href="//bg.wikipedia.org/wiki/" title="" lang="bg" hreflang="bg"></a></li>',
            '<li class="interwiki-ca"><a href="//ca.wikipedia.org/wiki/" title="" lang="ca" hreflang="ca">Catal</a></li>',
            '<li class="interwiki-cs"><a href="//cs.wikipedia.org/wiki/" title="" lang="cs" hreflang="cs">esky</a></li>',
            '<li class="interwiki-da"><a href="//da.wikipedia.org/wiki/" title="" lang="da" hreflang="da"><b>Dansk</b></a></li>',
            '<li class="interwiki-de"><a href="//de.wikipedia.org/wiki/" title="" lang="de" hreflang="de">Deutsch</a></li>',
            '<li class="interwiki-et"><a href="//et.wikipedia.org/wiki/" title="" lang="et" hreflang="et">Eesti</a></li>',
            '<li class="interwiki-el"><a href="//el.wikipedia.org/wiki/" title="" lang="el" hreflang="el"></a></li>',
            '<li class="interwiki-es"><a href="//es.wikipedia.org/wiki/" title="" lang="es" hreflang="es">Espaol</a></li>',
            '<li class="interwiki-eo"><a href="//eo.wikipedia.org/wiki/" title="" lang="eo" hreflang="eo">Esperanto</a></li>',
            '<li class="interwiki-eu"><a href="//eu.wikipedia.org/wiki/" title="" lang="eu" hreflang="eu">Euskara</a></li>',
            '<li class="interwiki-fa"><a href="//fa.wikipedia.org/wiki/" title="" lang="fa" hreflang="fa"></a></li>',
            '<li class="interwiki-fr"><a href="//fr.wikipedia.org/wiki/" title="" lang="fr" hreflang="fr">Franais</a></li>',
            '<li class="interwiki-gl"><a href="//gl.wikipedia.org/wiki/" title="" lang="gl" hreflang="gl">Galego</a></li>',
            '<li class="interwiki-ko"><a href="//ko.wikipedia.org/wiki/" title="" lang="ko" hreflang="ko"></a></li>',
            '<li class="interwiki-he"><a href="//he.wikipedia.org/wiki/" title="" lang="he" hreflang="he"></a></li>',
            '<li class="interwiki-hr"><a href="//hr.wikipedia.org/wiki/" title="" lang="hr" hreflang="hr">Hrvatski</a></li>',
            '<li class="interwiki-it"><a href="//it.wikipedia.org/wiki/" title="" lang="it" hreflang="it">Italiano</a></li>',
            '<li class="interwiki-lt"><a href="//lt.wikipedia.org/wiki/" title="" lang="lt" hreflang="lt">Lietuvi</a></li>',
            '<li class="interwiki-hu"><a href="//hu.wikipedia.org/wiki/" title="" lang="hu" hreflang="hu">Magyar</a></li>',
            '<li class="interwiki-nl"><a href="//nl.wikipedia.org/wiki/" title="" lang="nl" hreflang="nl">Nederlands</a></li>',
            '<li class="interwiki-ja"><a href="//ja.wikipedia.org/wiki/" title="" lang="ja" hreflang="ja"></a></li>',
            '<li class="interwiki-no"><a href="//no.wikipedia.org/wiki/" title="" lang="no" hreflang="no">Norsk bokml</a></li>',
            '<li class="interwiki-nn"><a href="//nn.wikipedia.org/wiki/" title="" lang="nn" hreflang="nn">Norsk nynorsk</a></li>',
            '<li class="interwiki-pl"><a href="//pl.wikipedia.org/wiki/" title="" lang="pl" hreflang="pl">Polski</a></li>',
            '<li class="interwiki-pt"><a href="//pt.wikipedia.org/wiki/" title="" lang="pt" hreflang="pt">Portugus</a></li>',
            '<li class="interwiki-ro"><a href="//ro.wikipedia.org/wiki/" title="" lang="ro" hreflang="ro">Romn</a></li>',
            '<li class="interwiki-ru"><a href="//ru.wikipedia.org/wiki/" title="" lang="ru" hreflang="ru"></a></li>',
            '<li class="interwiki-sk"><a href="//sk.wikipedia.org/wiki/" title="" lang="sk" hreflang="sk">Slovenina</a></li>',
            '<li class="interwiki-sl"><a href="//sl.wikipedia.org/wiki/" title="" lang="sl" hreflang="sl">Slovenina</a></li>',
            '<li class="interwiki-sr"><a href="//sr.wikipedia.org/wiki/" title="" lang="sr" hreflang="sr"> / srpski</a></li>',
            '<li class="interwiki-sh"><a href="//sh.wikipedia.org/wiki/" title="" lang="sh" hreflang="sh">Srpskohrvatski / </a></li>',
            '<li class="interwiki-fi"><a href="//fi.wikipedia.org/wiki/" title="" lang="fi" hreflang="fi">Suomi</a></li>',
            '<li class="interwiki-sv"><a href="//sv.wikipedia.org/wiki/" title="" lang="sv" hreflang="sv">Svenska</a></li>',
            '<li class="interwiki-th"><a href="//th.wikipedia.org/wiki/" title="" lang="th" hreflang="th"></a></li>',
            '<li class="interwiki-vi"><a href="//vi.wikipedia.org/wiki/" title="" lang="vi" hreflang="vi">Ting Vit</a></li>',
            '<li class="interwiki-tr"><a href="//tr.wikipedia.org/wiki/" title="" lang="tr" hreflang="tr">Trke</a></li>',
            '<li class="interwiki-uk"><a href="//uk.wikipedia.org/wiki/" title="" lang="uk" hreflang="uk"></a></li>',
            '<li class="interwiki-zh"><a href="//zh.wikipedia.org/wiki/" title="" lang="zh" hreflang="zh"></a></li>',
            '</ul>',
            '</div>',
            '</div>'
        ]

elements2 = [
            '<center>',
            '<div class="noresize" style="height: 242px; width: 600px; "><map name="ImageMap_1_971996215" id="ImageMap_1_971996215">',
            '<area href="/wiki/File:Pardalotus_punctatus_female_with_nesting_material_-_Risdon_Brook.jpg" shape="rect" coords="3,3,297,238" alt="Female" title="Female" />',
            '<area href="/wiki/File:Pardalotus_punctatus_male_with_nesting_material_-_Risdon_Brook.jpg" shape="rect" coords="302,2,597,238" alt="Male" title="Male" /></map><img alt="Pair of Spotted Pardalotes" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Female_and_male_Pardalotus_punctatus.jpg/600px-Female_and_male_Pardalotus_punctatus.jpg" width="600" height="242" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Female_and_male_Pardalotus_punctatus.jpg/900px-Female_and_male_Pardalotus_punctatus.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Female_and_male_Pardalotus_punctatus.jpg/1200px-Female_and_male_Pardalotus_punctatus.jpg 2x" usemap="#ImageMap_1_971996215" />',
            '<div style="margin-left: 0px; margin-top: -20px; text-align: left;"><a href="/wiki/File:Female_and_male_Pardalotus_punctatus.jpg" title="About this image"><img alt="About this image" src="//bits.wikimedia.org/static-1.22wmf7/extensions/ImageMap/desc-20.png" style="border: none;" /></a></div>',
            '</div>',
            '</center>'
        ]

elements3 = [
            '<ul>',
            '<li style="-moz-float-edge: content-box">Former Italian Prime Minister <a href="/wiki/Silvio_Berlusconi" title="Silvio Berlusconi">Silvio Berlusconi</a> <i>(pictured)</i> is <b><a href="/wiki/Silvio_Berlusconi_underage_prostitution_charges" title="Silvio Berlusconi underage prostitution charges">found guilty</a></b> of paying for sex with an underage prostitute.</li>',
            '<li style="-moz-float-edge: content-box">In sports car racing, the <b><a href="/wiki/2013_24_Hours_of_Le_Mans" title="2013 24 Hours of Le Mans">24 Hours of Le Mans</a></b>, won by <a href="/wiki/Tom_Kristensen" title="Tom Kristensen">Tom Kristensen</a>, <a href="/wiki/Allan_McNish" title="Allan McNish">Allan McNish</a> and <a href="/wiki/Lo%C3%AFc_Duval" title="Loc Duval">Loc Duval</a>, is marred by the death of <b><a href="/wiki/Allan_Simonsen_(racing_driver)" title="Allan Simonsen (racing driver)">Allan Simonsen</a></b>.</li>',
            '<li style="-moz-float-edge: content-box"><b><a href="/wiki/2013_Alberta_floods" title="2013 Alberta floods">Flooding</a></b> in <a href="/wiki/Alberta" title="Alberta">Alberta</a>, Canada, results in at least three deaths and the evacuation of thousands.</li>',
            '<li style="-moz-float-edge: content-box"><b><a href="/wiki/2013_North_India_floods" title="2013 North India floods">Flash floods and landslides</a></b> in <a href="/wiki/Uttarakhand" title="Uttarakhand">Uttarakhand</a> and <a href="/wiki/Himachal_Pradesh" title="Himachal Pradesh">Himachal Pradesh</a> in India kill more than <span class="nowrap">1,000 people</span> and trap more than 20,000.</li>',
            '<li style="-moz-float-edge: content-box">In <a href="/wiki/Basketball" title="Basketball">basketball</a>, the <a href="/wiki/Miami_Heat" title="Miami Heat">Miami Heat</a> defeat the <a href="/wiki/San_Antonio_Spurs" title="San Antonio Spurs">San Antonio Spurs</a> to win the <b><a href="/wiki/2013_NBA_Finals" title="2013 NBA Finals">NBA Finals</a></b>.</li>',
            '</ul>'
        ]

# Enter your code here. Read input from STDIN. Print output to STDOUT
pattern_link = r'((?<=<a href=").+?(?="))'
for element in elements3:
    pattern_text = r'(?<=>)([^<>]*[^<>]*)(?=<\/a)'
    if "</b></a>" in element:
        pattern_text = r'(?<=>)([^<>]*[^<>]*)(?=<\/b)'
    texts = re.findall(pattern_text, element)
    for link in re.findall(pattern_link, element):
        if link.strip() != "":            
            text = texts[0]
            texts.remove(text)
            print(",".join((link,text.strip())))