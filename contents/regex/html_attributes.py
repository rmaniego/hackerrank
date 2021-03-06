import re

web = ["""
<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm" data-hello>Example Link</a></p>
<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples... data-hello="abc"</a></div>
<input autocomplete>
<input data-name>
<input data-type="1">
<h6></h6>
""",
"""
<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>
<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>
""",
"""
<li style="-moz-float-edge: content-box">... that <a href="/wiki/Orval_Overall" title="Orval Overall">Orval Overall</a> <i>(pictured)</i> is the only <b><a href="/wiki/List_of_Major_League_Baseball_pitchers_who_have_struck_out_four_batters_in_one_inning" title="List of Major League Baseball pitchers who have struck out four batters in one inning">Major League Baseball player to strike out four batters in one inning</a></b> in the <a href="/wiki/World_Series" title="World Series">World Series</a>?</li>
<li style="-moz-float-edge: content-box">... that the three cities of the <b><a href="/wiki/West_Triangle_Economic_Zone" title="West Triangle Economic Zone">West Triangle Economic Zone</a></b> contribute 40% of Western China's GDP?</li>
<li style="-moz-float-edge: content-box">... that <i><a href="/wiki/Kismet_(1943_film)" title="Kismet (1943 film)">Kismet</a></i>, directed by <b><a href="/wiki/Gyan_Mukherjee" title="Gyan Mukherjee">Gyan Mukherjee</a></b>, ran at the <a href="/wiki/Roxy_Cinema_(Kolkata)" title="Roxy Cinema (Kolkata)">Roxy, Kolkata</a>, for 3 years and 8 months?</li>
<li style="-moz-float-edge: content-box">... that <a href="/wiki/Vauix_Carter" title="Vauix Carter">Vauix Carter</a> both coached and played for the <b><a href="/wiki/1882_Navy_Midshipmen_football_team" title="1882 Navy Midshipmen football team">1882 Navy Midshipmen football team</a></b>?</li>
<li style="-moz-float-edge: content-box">... that <a href="/wiki/Zhu_Chenhao" title="Zhu Chenhao">Zhu Chenhao</a> was sentenced to <a href="/wiki/Slow_slicing" title="Slow slicing">slow slicing</a> for leading the <b><a href="/wiki/Prince_of_Ning_rebellion" title="Prince of Ning rebellion">Prince of Ning rebellion</a></b> against the <a href="/wiki/Ming_Dynasty" title="Ming Dynasty">Ming Dynasty</a> <a href="/wiki/Zhengde_Emperor" title="Zhengde Emperor">emperor Zhengde</a>?</li>
<li style="-moz-float-edge: content-box">... that <b><a href="/wiki/Mirza_Adeeb" title="Mirza Adeeb">Mirza Adeeb</a></b> was a prominent modern Pakistani <a href="/wiki/Urdu" title="Urdu">Urdu</a> playwright whose later work focuses on social problems and daily life?</li>
<li style="-moz-float-edge: content-box">... that in <i><b><a href="/wiki/La%C3%9Ft_uns_sorgen,_la%C3%9Ft_uns_wachen,_BWV_213" title="Lat uns sorgen, lat uns wachen, BWV 213">Die Wahl des Herkules</a></b></i>, Hercules must choose between the good cop and the bad cop?<br style="clear:both;" />
<div style="text-align: right;" class="noprint"><b><a href="/wiki/Wikipedia:Recent_additions" title="Wikipedia:Recent additions">Archive</a></b>  <b><a href="/wiki/Wikipedia:Your_first_article" title="Wikipedia:Your first article">Start a new article</a></b>  <b><a href="/wiki/Template_talk:Did_you_know" title="Template talk:Did you know">Nominate an article</a></b></div>
</li>
""",
"""
<div class="portal" role="navigation" id='p-tb'>
<h3>Toolbox</h3>
<div class="body">
<ul>
<li id="t-whatlinkshere"><a href="/wiki/Special:WhatLinksHere/Human_trafficking_in_Canada" title="List of all English Wikipedia pages containing links to this page [j]" accesskey="j">What links here</a></li>
<li id="t-recentchangeslinked"><a href="/wiki/Special:RecentChangesLinked/Human_trafficking_in_Canada" title="Recent changes in pages linked from this page [k]" accesskey="k">Related changes</a></li>
<li id="t-upload"><a href="/wiki/Wikipedia:File_Upload_Wizard" title="Upload files [u]" accesskey="u">Upload file</a></li>
<li id="t-specialpages"><a href="/wiki/Special:SpecialPages" title="A list of all special pages [q]" accesskey="q">Special pages</a></li>
<li id="t-permalink"><a href="/w/index.php?title=Human_trafficking_in_Canada&amp;oldid=560794473" title="Permanent link to this revision of the page">Permanent link</a></li>
<li id="t-info"><a href="/w/index.php?title=Human_trafficking_in_Canada&amp;action=info">Page information</a></li>
<li id="t-cite"><a href="/w/index.php?title=Special:Cite&amp;page=Human_trafficking_in_Canada&amp;id=560794473" title="Information on how to cite this page">Cite this page</a></li>	</ul>
</div>
</div>
"""]

pattern_html = r'(?:(?<=\<))([a-z]+[1-6]*)(.*?)(?:(?=\>))'
pattern_attribs = r'( [\w\-]*((?=[\r\n=])|$))'
for html in web:
    tags = {}
    for part in re.findall(pattern_html, html):
        tag = part[0]
        if tag not in tags:
            tags[tag] = []
        for matches in re.findall(pattern_attribs, part[1]):
            attribs = set([x.strip() for x in matches if x.strip() != ""])
            tags[tag].extend(attribs)

    matched = []
    for tag, matches in tags.items():
        attribs = ""
        if len(matches):
            attribs = ",".join(sorted(set(matches)))
        matched.append(":".join((tag, attribs)))
    print("\n".join(sorted(set(matched))))
    print("\n")