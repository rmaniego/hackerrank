import re

stackoverflow = ["""
<!DOCTYPE html>
<html>
<head>

    <title>Newest Questions - Page 2 - Electrical Engineering Stack Exchange</title>
    <link rel="shortcut icon" href="//cdn.sstatic.net/electronics/img/favicon.ico">
    <link rel="apple-touch-icon image_src" href="//cdn.sstatic.net/electronics/img/apple-touch-icon.png">
    <link rel="search" type="application/opensearchdescription+xml" title="Electrical Engineering Stack Exchange" href="/opensearch.xml">

    <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
    <script type="text/javascript" src="//cdn.sstatic.net/js/stub.js?v=5d233283ca8d"></script>
    <link rel="stylesheet" type="text/css" href="//cdn.sstatic.net/electronics/all.css?v=672ddec9ce04">


                <script type="text/x-mathjax-config">
                    MathJax.Hub.Config({"HTML-CSS": { preferredFont: "TeX", availableFonts: ["STIX","TeX"], linebreaks: { automatic:true }, EqnChunk: (MathJax.Hub.Browser.isMobile ? 10 : 50) },
                                        tex2jax: { inlineMath: [ ["\\$", "\\$"] ], displayMath: [ ["$$","$$"], ["\\[", "\\]"] ], processEscapes: true, ignoreClass: "tex2jax_ignore|dno" },
                                        TeX: {  noUndefined: { attributes: { mathcolor: "red", mathbackground: "#FFEEEE", mathsize: "90%" } }, Macros: { href: "{}" } },
                                        messageStyle: "none"
                });
                </script>
                <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML"></script>

    <script type="text/javascript">
        StackExchange.ready(function () {
            StackExchange.realtime.init('sockets.ny.stackexchange.com');
            StackExchange.realtime.subscribeToInboxNotifications();
                    StackExchange.realtime.subscribeToReputationNotifications('135');
                });
    </script>
    <script type="text/javascript">
        StackExchange.init({"stackAuthUrl":"https://stackauth.com","serverTime":1377686462,"styleCode":true,"enableUserHovercards":true,"site":{"name":"Electrical Engineering Stack Exchange","description":"Q&A for electronics and electrical engineering professionals, students, and enthusiasts","isNoticesTabEnabled":true,"recaptchaPublicKey":"6LdsB7sSAAAAAAzjgEF_Hd8vXv-C42sa_KyofaGR","enableSocialMediaInSharePopup":true},"user":{"fkey":"964caaf8350dc8ae69af722ba29b4a1d","isAnonymous":true}});
        StackExchange.using.setCacheBreakers({"js/prettify-full.js":"6c261bebf56a","js/moderator.js":"ed7a8238b2f8","js/full-anon.js":"5f9bf5810297","js/full.js":"027ac5ea264e","js/wmd.js":"cff10cca4fd9","js/third-party/jquery.autocomplete.min.js":"e5f01e97f7c3","js/mobile.js":"82a79dbb7259","js/help.js":"6e6623243cf6","js/tageditor.js":"450c9e8426fc","js/tageditornew.js":"b6c68ad4c7dd","js/inline-tag-editing.js":"8e84e8a137f7","js/revisions.js":"d3e781ee5528","js/review.js":"947758ba83ea","js/tagsuggestions.js":"aa48ef6154df","js/post-validation.js":"bb996020492a","js/explore-qlist.js":"1c5bbd79b562","js/events.js":"27a33f0b2cad"});
        StackExchange.using.setCacheBreakers({"js/mathjax-editing.js":"6da1b6cfe19f","js/external-editor.js":"51c0a8d46d29"});
    </script>
    <script type="text/javascript">
        StackExchange.using("gps", function() {
             StackExchange.gps.init(true);
        });
    </script>

        <script type="text/javascript">
            StackExchange.ready(function () {
                $('#nav-tour').click(function () {
                    StackExchange.using("gps", function() {
                        StackExchange.gps.track("aboutpage.click", { aboutclick_location: "headermain" }, true);
                    });
                });
            });
        </script>
</head>
<body class="questions-page">
    <noscript><div id="noscript-padding"></div></noscript>
    <div id="notify-container"></div>
    <div id="overlay-header"></div>
    <div id="custom-header"></div>

    <div class="container">
        <div id="header" class=headeranon>
            <div id="portalLink">
                <a class="genu" href="http://stackexchange.com" onclick="StackExchange.ready(function(){genuwine.click();});return false;">Stack Exchange</a>
            </div>
            <div id="topbar">
                <div id="hlinks">

<span id="hlinks-user"></span>
<span id="hlinks-nav">                        <a href="/users/login?returnurl=%2fquestions%3fpage%3d2%26sort%3dnewest">sign up</a>

 <span class="lsep">|</span>
                    <a href="/users/login?returnurl=%2fquestions%3fpage%3d2%26sort%3dnewest">log in</a>

 <span class="lsep">|</span>
</span>
<span id="hlinks-custom"></span>
                </div>
                <div id="hsearch">
                    <form id="search" action="/search" method="get" autocomplete="off">
                        <div>
                            <input autocomplete="off" name="q" class="textbox" placeholder="search" tabindex="1" type="text" maxlength="240" size="28" value="">
                        </div>
                    </form>
                </div>
            </div>
            <br class="cbt">
            <div id="hlogo">
                <a href="/">
                    Electrical Engineering
                </a>
            </div>
            <div id="hmenus">
                <div class="nav mainnavs mainnavsanon">
                    <ul>
                            <li class="youarehere"><a id="nav-questions" href="/questions">Questions</a></li>
                            <li><a id="nav-tags" href="/tags">Tags</a></li>
                            <li><a id="nav-tour" href="/about">Tour</a></li>
                            <li><a id="nav-users" href="/users">Users</a></li>
                    </ul>
                </div>
                <div class="nav askquestion">
                    <ul>
                        <li>
                            <a id="nav-askquestion"  href="/questions/ask">Ask Question</a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>




        <div id="content">

<div id="mainbar">
    <div class="subheader">
        <h1 id="h-all-questions">All Questions</h1>
        <div id="tabs">
<a class="youarehere" href="/questions?sort=newest" title="the most recently asked questions">newest</a>
<a href="/questions?sort=featured" title="questions with open bounties"><span class='bounty-indicator-tab'>3</span>featured</a>
<a href="/questions?sort=frequent" title="questions with the most links">frequent</a>
<a href="/questions?sort=votes" title="questions with the most votes">votes</a>
<a href="/questions?sort=active" title="questions that have recent activity">active</a>
<a href="/questions?sort=unanswered" title="questions that have no upvoted answers">unanswered</a>

        </div>
    </div>

    <div id="questions">

<div class="question-summary" id="question-summary-80417">
    <div class="statscontainer">
        <div class="statsarrow"></div>
        <div class="stats">
            <div class="vote">
                <div class="votes">
                    <span class="vote-count-post "><strong>1</strong></span>
                    <div class="viewcount">vote</div>
                </div>
            </div>
            <div class="status answered">
                <strong>2</strong>answers
            </div>
        </div>



<div class="views " title="65 views">
                    65 views
</div>
    </div>
    <div class="summary">
        <h3><a href="/questions/80417/can-i-safely-enclose-battery-powered-electronics-in-an-antistatic-bag-to-protect" class="question-hyperlink">Can I safely enclose battery-powered electronics in an antistatic bag to protect it from static electricity?</a></h3>
        <div class="excerpt">
            I am building an enclosure for a Beaglebone and external circuit that I want to be able to wear, and therefore want to be lightweight and somewhat comfortable. I power the Beaglebone using a battery ...
        </div>

        <div class="tags t-shielding t-antistatic t-static">
            <a href="/questions/tagged/shielding" class="post-tag" title="show questions tagged 'shielding'" rel="tag">shielding</a> <a href="/questions/tagged/antistatic" class="post-tag" title="show questions tagged 'antistatic'" rel="tag">antistatic</a> <a href="/questions/tagged/static" class="post-tag" title="show questions tagged 'static'" rel="tag">static</a>

        </div>
        <div class="started fr">


    <div class="user-info ">
        <div class="user-action-time">


                    asked <span title="2013-08-27 22:47:03Z" class="relativetime">11 hours ago</span>
        </div>
        <div class="user-gravatar32">
            <a href="/users/19783/mokogobo"><div class=""><img src="https://www.gravatar.com/avatar/045025756373a85e8336c8126ee006c6?s=32&d=identicon&r=PG" alt="" width="32" height="32"></div></a>
        </div>
        <div class="user-details">
            <a href="/users/19783/mokogobo">mokogobo</a><br>
            <span class="reputation-score" title="reputation score" dir="ltr">31</span><span title="4 bronze badges"><span class="badge3"></span><span class="badgecount">4</span></span>
        </div>
    </div>

        </div>
    </div>
</div>

<div class="question-summary" id="question-summary-80412">
    <div class="statscontainer">
        <div class="statsarrow"></div>
        <div class="stats">
            <div class="vote">
                <div class="votes">
                    <span class="vote-count-post "><strong>0</strong></span>
                    <div class="viewcount">votes</div>
                </div>
            </div>
            <div class="status answered">
                <strong>1</strong>answer
            </div>
        </div>



<div class="views " title="22 views">
                    22 views
</div>
    </div>
    <div class="summary">
        <h3><a href="/questions/80412/how-to-overwrite-flash-memory-on-stm32l-series" class="question-hyperlink">How to overwrite flash memory on STM32L series</a></h3>
        <div class="excerpt">
            I am trying to write a known pattern (ie 0xFFFFFFFF or 0x00000000) on top of already written flash memory, to invalidate portions of it for a primitive file system. But it doesn't work for me on the ...
        </div>

        <div class="tags t-stm32 t-flash">
            <a href="/questions/tagged/stm32" class="post-tag" title="show questions tagged 'stm32'" rel="tag">stm32</a> <a href="/questions/tagged/flash" class="post-tag" title="show questions tagged 'flash'" rel="tag">flash</a>

        </div>
        <div class="started fr">


    <div class="user-info ">
        <div class="user-action-time">


                    asked <span title="2013-08-27 22:09:01Z" class="relativetime">12 hours ago</span>
        </div>
        <div class="user-gravatar32">
            <a href="/users/15757/mark-lakata"><div class=""><img src="https://www.gravatar.com/avatar/5fd80d98f96f9adbde7876cbda181715?s=32&d=identicon&r=PG" alt="" width="32" height="32"></div></a>
        </div>
        <div class="user-details">
            <a href="/users/15757/mark-lakata">Mark Lakata</a><br>
            <span class="reputation-score" title="reputation score" dir="ltr">111</span><span title="2 bronze badges"><span class="badge3"></span><span class="badgecount">2</span></span>
        </div>
    </div>

        </div>
    </div>
</div>

<div class="question-summary" id="question-summary-80407">
    <div class="statscontainer">
        <div class="statsarrow"></div>
        <div class="stats">
            <div class="vote">
                <div class="votes">
                    <span class="vote-count-post "><strong>2</strong></span>
                    <div class="viewcount">votes</div>
                </div>
            </div>
            <div class="status answered">
                <strong>1</strong>answer
            </div>
        </div>



<div class="views " title="61 views">
                    61 views
</div>
    </div>
    <div class="summary">
        <h3><a href="/questions/80407/about-power-supply-of-opertional-amplifier" class="question-hyperlink">about power supply of opertional amplifier</a></h3>
        <div class="excerpt">
            I am constructing an operational amplifier as shown in the following figure. I use a batter as supplier for the OP Amp and set it up as a non-inverting amp circuit. I saw that the output was clipped ...
        </div>

        <div class="tags t-op-amp">
            <a href="/questions/tagged/op-amp" class="post-tag" title="show questions tagged 'op-amp'" rel="tag">op-amp</a>

        </div>
        <div class="started fr">


    <div class="user-info ">
        <div class="user-action-time">


                    asked <span title="2013-08-27 21:49:14Z" class="relativetime">12 hours ago</span>
        </div>
        <div class="user-gravatar32">
            <a href="/users/17060/user1285419"><div class=""><img src="https://www.gravatar.com/avatar/08ee68b20a4eceff26f7eee99b708c08?s=32&d=identicon&r=PG" alt="" width="32" height="32"></div></a>
        </div>
        <div class="user-details">
            <a href="/users/17060/user1285419">user1285419</a><br>
            <span class="reputation-score" title="reputation score" dir="ltr">165</span><span title="5 bronze badges"><span class="badge3"></span><span class="badgecount">5</span></span>
        </div>
    </div>

        </div>
    </div>
</div>

<div class="question-summary" id="question-summary-80405">
    <div class="statscontainer">
        <div class="statsarrow"></div>
        <div class="stats">
            <div class="vote">
                <div class="votes">
                    <span class="vote-count-post "><strong>4</strong></span>
                    <div class="viewcount">votes</div>
                </div>
            </div>
            <div class="status answered-accepted">
                <strong>2</strong>answers
            </div>
        </div>



<div class="views " title="64 views">
                    64 views
</div>
    </div>
    <div class="summary">
        <h3><a href="/questions/80405/5v-regulator-power-dissipation" class="question-hyperlink">5V Regulator Power Dissipation</a></h3>
        <div class="excerpt">
            I am using a 5V regulator (LP2950) from ON Semiconductor. I am using this for USB power and I'm feeding in 9V from an adapter. USB requires maximum of 500mA right? So the maximum power dissipation in ...
        </div>

        <div class="tags t-voltage-regulator t-surface-mount t-heatsink t-5v t-power-dissipation">
            <a href="/questions/tagged/voltage-regulator" class="post-tag" title="show questions tagged 'voltage-regulator'" rel="tag">voltage-regulator</a> <a href="/questions/tagged/surface-mount" class="post-tag" title="show questions tagged 'surface-mount'" rel="tag">surface-mount</a> <a href="/questions/tagged/heatsink" class="post-tag" title="show questions tagged 'heatsink'" rel="tag">heatsink</a> <a href="/questions/tagged/5v" class="post-tag" title="show questions tagged '5v'" rel="tag">5v</a> <a href="/questions/tagged/power-dissipation" class="post-tag" title="show questions tagged 'power-dissipation'" rel="tag">power-dissipation</a>

        </div>
        <div class="started fr">


    <div class="user-info ">
        <div class="user-action-time">


                    asked <span title="2013-08-27 21:39:31Z" class="relativetime">13 hours ago</span>
        </div>
        <div class="user-gravatar32">
            <a href="/users/10082/david-norman"><div class=""><img src="https://www.gravatar.com/avatar/8b073417e471077280b3fc5ff2eaf1f7?s=32&d=identicon&r=PG" alt="" width="32" height="32"></div></a>
        </div>
        <div class="user-details">
            <a href="/users/10082/david-norman">David Norman</a><br>
            <span class="reputation-score" title="reputation score" dir="ltr">322</span><span title="3 silver badges"><span class="badge2"></span><span class="badgecount">3</span></span><span title="10 bronze badges"><span class="badge3"></span><span class="badgecount">10</span></span>
        </div>
    </div>

        </div>
    </div>
</div>

<div class="question-summary" id="question-summary-80404">
    <div class="statscontainer">
        <div class="statsarrow"></div>
        <div class="stats">
            <div class="vote">
                <div class="votes">
                    <span class="vote-count-post "><strong>0</strong></span>
                    <div class="viewcount">votes</div>
                </div>
            </div>
            <div class="status answered">
                <strong>1</strong>answer
            </div>
        </div>



<div class="views " title="44 views">
                    44 views
</div>
    </div>
    <div class="summary">
        <h3><a href="/questions/80404/how-to-stop-two-dc-motors-simultaneously-using-limit-switches" class="question-hyperlink">How to stop two DC motors simultaneously using limit switches</a></h3>
        <div class="excerpt">
            I need some help - I'm building a machine but I'm not sure of the best way of doing it.

I have three large wire spools. Two empty and one full. The full spool (approx. 500kg) is much larger than the ...
        </div>

        <div class="tags t-dc-motor t-switch-mode-power-supply t-servo t-plc t-toggle-switch">
            <a href="/questions/tagged/dc-motor" class="post-tag" title="show questions tagged 'dc-motor'" rel="tag">dc-motor</a> <a href="/questions/tagged/switch-mode-power-supply" class="post-tag" title="show questions tagged 'switch-mode-power-supply'" rel="tag">switch-mode-power-supply</a> <a href="/questions/tagged/servo" class="post-tag" title="show questions tagged 'servo'" rel="tag">servo</a> <a href="/questions/tagged/plc" class="post-tag" title="show questions tagged 'plc'" rel="tag">plc</a> <a href="/questions/tagged/toggle-switch" class="post-tag" title="show questions tagged 'toggle-switch'" rel="tag">toggle-switch</a>

        </div>
        <div class="started fr">


    <div class="user-info ">
        <div class="user-action-time">


                    asked <span title="2013-08-27 21:29:47Z" class="relativetime">13 hours ago</span>
        </div>
        <div class="user-gravatar32">
            <a href="/users/28090/golden-bucky"><div class=""><img src="https://www.gravatar.com/avatar/0d00cc71566104e18dc131bc7f5b4cf1?s=32&d=identicon&r=PG&f=1" alt="" width="32" height="32"></div></a>
        </div>
        <div class="user-details">
            <a href="/users/28090/golden-bucky">Golden Bucky</a><br>
            <span class="reputation-score" title="reputation score" dir="ltr">1</span>
        </div>
    </div>

        </div>
    </div>
</div>

<div class="question-summary" id="question-summary-80396">
    <div class="statscontainer">
        <div class="statsarrow"></div>
        <div class="stats">
            <div class="vote">
                <div class="votes">
                    <span class="vote-count-post "><strong>1</strong></span>
                    <div class="viewcount">vote</div>
                </div>
            </div>
            <div class="status answered">
                <strong>1</strong>answer
            </div>
        </div>



<div class="views " title="58 views">
                    58 views
</div>
    </div>
    <div class="summary">
        <h3><a href="/questions/80396/logic-level-translator-caveats" class="question-hyperlink">Logic Level Translator caveats</a></h3>
        <div class="excerpt">
            I have a device that runs on 2.5Vcmos logic levels, there are about a half dozen ic's with a mixture of parallel and serial (TWI and I2C) signal lines. Rather than placing my own uC on the board I'd ...
        </div>

        <div class="tags t-level-translation">
            <a href="/questions/tagged/level-translation" class="post-tag" title="show questions tagged 'level-translation'" rel="tag">level-translation</a>

        </div>
        <div class="started fr">


    <div class="user-info ">
        <div class="user-action-time">


                    asked <span title="2013-08-27 20:45:03Z" class="relativetime">13 hours ago</span>
        </div>
        <div class="user-gravatar32">
            <a href="/users/1729/crasic"><div class=""><img src="https://www.gravatar.com/avatar/61084e40f265986dd41136b4f3dc028f?s=32&d=identicon&r=PG" alt="" width="32" height="32"></div></a>
        </div>
        <div class="user-details">
            <a href="/users/1729/crasic">crasic</a><br>
            <span class="reputation-score" title="reputation score" dir="ltr">643</span><span title="2 silver badges"><span class="badge2"></span><span class="badgecount">2</span></span><span title="8 bronze badges"><span class="badge3"></span><span class="badgecount">8</span></span>
        </div>
    </div>

        </div>
    </div>
</div>

<div class="question-summary" id="question-summary-80393">
    <div class="statscontainer">
        <div class="statsarrow"></div>
        <div class="stats">
            <div class="vote">
                <div class="votes">
                    <span class="vote-count-post "><strong>1</strong></span>
                    <div class="viewcount">vote</div>
                </div>
            </div>
            <div class="status answered">
                <strong>1</strong>answer
            </div>
        </div>



<div class="views " title="57 views">
                    57 views
</div>
    </div>
    <div class="summary">
        <h3><a href="/questions/80393/microcontroller-newbe-here-led-color-pattern-controller-for-arcade-machine" class="question-hyperlink">Microcontroller Newbe here. LED color pattern controller for arcade machine [on hold]</a></h3>
        <div class="excerpt">
            I am building an arcade machine and I want to make a cool led light display for the marquee.

You can see pictures of what I'm talking about here.





I want to light up each one of those holes with ...
        </div>

        <div class="tags t-microcontroller t-led">
            <a href="/questions/tagged/microcontroller" class="post-tag" title="show questions tagged 'microcontroller'" rel="tag">microcontroller</a> <a href="/questions/tagged/led" class="post-tag" title="show questions tagged 'led'" rel="tag">led</a>

        </div>
        <div class="started fr">


    <div class="user-info ">
        <div class="user-action-time">


                    asked <span title="2013-08-27 20:34:56Z" class="relativetime">14 hours ago</span>
        </div>
        <div class="user-gravatar32">
            <a href="/users/28086/doug-steinberg"><div class=""><img src="https://www.gravatar.com/avatar/f8a5cf563e719e934263883978ab80f1?s=32&d=identicon&r=PG" alt="" width="32" height="32"></div></a>
        </div>
        <div class="user-details">
            <a href="/users/28086/doug-steinberg">Doug Steinberg</a><br>
            <span class="reputation-score" title="reputation score" dir="ltr">6</span><span title="1 bronze badge"><span class="badge3"></span><span class="badgecount">1</span></span>
        </div>
    </div>

        </div>
    </div>
</div>

<div class="question-summary" id="question-summary-80385">
    <div class="statscontainer">
        <div class="statsarrow"></div>
        <div class="stats">
            <div class="vote">
                <div class="votes">
                    <span class="vote-count-post "><strong>1</strong></span>
                    <div class="viewcount">vote</div>
                </div>
            </div>
            <div class="status answered">
                <strong>2</strong>answers
            </div>
        </div>



<div class="views " title="69 views">
                    69 views
</div>
    </div>
    <div class="summary">
        <h3><a href="/questions/80385/how-to-scale-dynamic-range-voltage-to-1-5-volt" class="question-hyperlink">how to scale dynamic range voltage to 1-5 volt</a></h3>
        <div class="excerpt">
            how can i make circuit that scale input voltage that have dynamic range to 1-5 volt output?



the circuit will have Vref+ and Vref- as maximum and minimum for Vinput and then scale to 1-5 volt output
...
        </div>

        <div class="tags t-voltage t-amplifier">
            <a href="/questions/tagged/voltage" class="post-tag" title="show questions tagged 'voltage'" rel="tag">voltage</a> <a href="/questions/tagged/amplifier" class="post-tag" title="show questions tagged 'amplifier'" rel="tag">amplifier</a>

        </div>
        <div class="started fr">


    <div class="user-info ">
        <div class="user-action-time">


                    asked <span title="2013-08-27 19:30:33Z" class="relativetime">15 hours ago</span>
        </div>
        <div class="user-gravatar32">
            <a href="/users/28084/user28084"><div class=""><img src="https://www.gravatar.com/avatar/2cacd24f99b2bcbd8236d1ce8c3c559f?s=32&d=identicon&r=PG&f=1" alt="" width="32" height="32"></div></a>
        </div>
        <div class="user-details">
            <a href="/users/28084/user28084">user28084</a><br>
            <span class="reputation-score" title="reputation score" dir="ltr">9</span><span title="2 bronze badges"><span class="badge3"></span><span class="badgecount">2</span></span>
        </div>
    </div>

        </div>
    </div>
</div>

<div class="question-summary" id="question-summary-80383">
    <div class="statscontainer">
        <div class="statsarrow"></div>
        <div class="stats">
            <div class="vote">
                <div class="votes">
                    <span class="vote-count-post "><strong>0</strong></span>
                    <div class="viewcount">votes</div>
                </div>
            </div>
            <div class="status answered-accepted">
                <strong>1</strong>answer
            </div>
        </div>



<div class="views " title="38 views">
                    38 views
</div>
    </div>
    <div class="summary">
        <h3><a href="/questions/80383/is-it-the-frequency-that-determines-the-current-in-a-lc-tank-parallel-circuit" class="question-hyperlink">Is it the frequency that determines the current in a LC Tank Parallel Circuit?</a></h3>
        <div class="excerpt">
            Jump a head to the question if you aren't interested in the background of my project

Background of my project

I want to create objects of metal. So I need to be able to cast a metal. Aluminium seems ...
        </div>

        <div class="tags t-current t-frequency t-solenoid t-induction t-rlc">
            <a href="/questions/tagged/current" class="post-tag" title="show questions tagged 'current'" rel="tag">current</a> <a href="/questions/tagged/frequency" class="post-tag" title="show questions tagged 'frequency'" rel="tag">frequency</a> <a href="/questions/tagged/solenoid" class="post-tag" title="show questions tagged 'solenoid'" rel="tag">solenoid</a> <a href="/questions/tagged/induction" class="post-tag" title="show questions tagged 'induction'" rel="tag">induction</a> <a href="/questions/tagged/rlc" class="post-tag" title="show questions tagged 'rlc'" rel="tag">rlc</a>

        </div>
        <div class="started fr">


    <div class="user-info ">
        <div class="user-action-time">


                    asked <span title="2013-08-27 19:29:24Z" class="relativetime">15 hours ago</span>
        </div>
        <div class="user-gravatar32">
            <a href="/users/26135/mike-de-klerk"><div class=""><img src="https://www.gravatar.com/avatar/7c2d61f7fedb644912d1cef5ed0b250a?s=32&d=identicon&r=PG" alt="" width="32" height="32"></div></a>
        </div>
        <div class="user-details">
            <a href="/users/26135/mike-de-klerk">Mike de Klerk</a><br>
            <span class="reputation-score" title="reputation score" dir="ltr">183</span><span title="6 bronze badges"><span class="badge3"></span><span class="badgecount">6</span></span>
        </div>
    </div>

        </div>
    </div>
</div>

<div class="question-summary" id="question-summary-80378">
    <div class="statscontainer">
        <div class="statsarrow"></div>
        <div class="stats">
            <div class="vote">
                <div class="votes">
                    <span class="vote-count-post "><strong>4</strong></span>
                    <div class="viewcount">votes</div>
                </div>
            </div>
            <div class="status answered-accepted">
                <strong>4</strong>answers
            </div>
        </div>



<div class="views " title="54 views">
                    54 views
</div>
    </div>
    <div class="summary">
        <h3><a href="/questions/80378/replacing-resistors-with-equivalent-resistor" class="question-hyperlink">Replacing resistors with equivalent resistor</a></h3>
        <div class="excerpt">
            This is somewhat a homework assignment, but please bear with me. Given the following schematic, I want to know the overall resistance when measured from node A to node B.







simulate this circuit ...
        </div>

        <div class="tags t-resistors t-resistance t-circuit-analysis">
            <a href="/questions/tagged/resistors" class="post-tag" title="show questions tagged 'resistors'" rel="tag">resistors</a> <a href="/questions/tagged/resistance" class="post-tag" title="show questions tagged 'resistance'" rel="tag">resistance</a> <a href="/questions/tagged/circuit-analysis" class="post-tag" title="show questions tagged 'circuit-analysis'" rel="tag">circuit-analysis</a>

        </div>
        <div class="started fr">


    <div class="user-info ">
        <div class="user-action-time">


                    asked <span title="2013-08-27 19:07:14Z" class="relativetime">15 hours ago</span>
        </div>
        <div class="user-gravatar32">
            <a href="/users/9913/nijansen"><div class=""><img src="https://www.gravatar.com/avatar/8250825c174a99613ffeec2ccc085bcf?s=32&d=identicon&r=PG" alt="" width="32" height="32"></div></a>
        </div>
        <div class="user-details">
            <a href="/users/9913/nijansen">nijansen</a><br>
            <span class="reputation-score" title="reputation score" dir="ltr">174</span><span title="8 bronze badges"><span class="badge3"></span><span class="badgecount">8</span></span>
        </div>
    </div>

        </div>
    </div>
</div>

<div class="question-summary" id="question-summary-80371">
    <div class="statscontainer">
        <div class="statsarrow"></div>
        <div class="stats">
            <div class="vote">
                <div class="votes">
                    <span class="vote-count-post "><strong>2</strong></span>
                    <div class="viewcount">votes</div>
                </div>
            </div>
            <div class="status answered">
                <strong>2</strong>answers
            </div>
        </div>



<div class="views " title="32 views">
                    32 views
</div>
    </div>
    <div class="summary">
        <h3><a href="/questions/80371/saturation-current-in-inductor-definition" class="question-hyperlink">Saturation current in inductor - Definition?</a></h3>
        <div class="excerpt">
            Can somebody explain me what actually is a saturation current of an inductor. You may consider one inductor too and explain the things. This is very much confusing for me. Somebody give me a clear cut ...
        </div>

        <div class="tags t-inductor">
            <a href="/questions/tagged/inductor" class="post-tag" title="show questions tagged 'inductor'" rel="tag">inductor</a>

        </div>
        <div class="started fr">


    <div class="user-info ">
        <div class="user-action-time">


                    asked <span title="2013-08-27 18:38:03Z" class="relativetime">16 hours ago</span>
        </div>
        <div class="user-gravatar32">
            <a href="/users/20352/durgaprasad"><div class="gravatar-wrapper-32"><img src="http://i.stack.imgur.com/iQDud.jpg?s=32&g=1" alt=""></div></a>
        </div>
        <div class="user-details">
            <a href="/users/20352/durgaprasad">Durgaprasad</a><br>
            <span class="reputation-score" title="reputation score" dir="ltr">339</span><span title="9 bronze badges"><span class="badge3"></span><span class="badgecount">9</span></span>
        </div>
    </div>

        </div>
    </div>
</div>

<div class="question-summary" id="question-summary-80370">
    <div class="statscontainer">
        <div class="statsarrow"></div>
        <div class="stats">
            <div class="vote">
                <div class="votes">
                    <span class="vote-count-post "><strong>3</strong></span>
                    <div class="viewcount">votes</div>
                </div>
            </div>
            <div class="status answered">
                <strong>2</strong>answers
            </div>
        </div>



<div class="views " title="85 views">
                    85 views
</div>
    </div>
    <div class="summary">
        <h3><a href="/questions/80370/is-it-possible-for-batteries-to-give-a-false-reading-of-being-charged-with-a-mul" class="question-hyperlink">Is it possible for batteries to give a false reading of being charged with a multimeter?</a></h3>
        <div class="excerpt">
            I bought a Stanley SL5W09L spotlight about four years ago and it has performed wonderfully ever since.  Recently however it has stopped working.

I can plug it in, and the charge light will come on ...
        </div>

        <div class="tags t-batteries">
            <a href="/questions/tagged/batteries" class="post-tag" title="show questions tagged 'batteries'" rel="tag">batteries</a>

        </div>
        <div class="started fr">


    <div class="user-info ">
        <div class="user-action-time">


                    asked <span title="2013-08-27 18:36:29Z" class="relativetime">16 hours ago</span>
        </div>
        <div class="user-gravatar32">
            <a href="/users/24413/steve-french"><div class=""><img src="https://www.gravatar.com/avatar/ef46e9c26326bd9d82479c7daf4155a3?s=32&d=identicon&r=PG" alt="" width="32" height="32"></div></a>
        </div>
        <div class="user-details">
            <a href="/users/24413/steve-french">Steve French</a><br>
            <span class="reputation-score" title="reputation score" dir="ltr">119</span><span title="1 bronze badge"><span class="badge3"></span><span class="badgecount">1</span></span>
        </div>
    </div>

        </div>
    </div>
</div>

<div class="question-summary" id="question-summary-80366">
    <div class="statscontainer">
        <div class="statsarrow"></div>
        <div class="stats">
            <div class="vote">
                <div class="votes">
                    <span class="vote-count-post "><strong>0</strong></span>
                    <div class="viewcount">votes</div>
                </div>
            </div>
            <div class="status answered">
                <strong>1</strong>answer
            </div>
        </div>



<div class="views " title="37 views">
                    37 views
</div>
    </div>
    <div class="summary">
        <h3><a href="/questions/80366/arduino-accessing-extra-analog-pins-on-32-pin-smt-package" class="question-hyperlink">Arduino - accessing extra analog pins on 32-pin SMT package</a></h3>
        <div class="excerpt">
            I've got a 32-pin ATMega328 on a breadboard. I have its analog pin #6 as an input pin from another IC on my board. The IC sends data to this analog pin.

Now, the ATMega328 DIP package (used on the ...
        </div>

        <div class="tags t-arduino">
            <a href="/questions/tagged/arduino" class="post-tag" title="show questions tagged 'arduino'" rel="tag">arduino</a>

        </div>
        <div class="started fr">


    <div class="user-info ">
        <div class="user-action-time">


                    asked <span title="2013-08-27 18:07:58Z" class="relativetime">16 hours ago</span>
        </div>
        <div class="user-gravatar32">
            <a href="/users/17082/ryan-tuck"><div class=""><img src="https://www.gravatar.com/avatar/57bb887b039eb0ca9f976210fe821a2a?s=32&d=identicon&r=PG" alt="" width="32" height="32"></div></a>
        </div>
        <div class="user-details">
            <a href="/users/17082/ryan-tuck">Ryan Tuck</a><br>
            <span class="reputation-score" title="reputation score" dir="ltr">114</span><span title="5 bronze badges"><span class="badge3"></span><span class="badgecount">5</span></span>
        </div>
    </div>

        </div>
    </div>
</div>

<div class="question-summary" id="question-summary-80365">
    <div class="statscontainer">
        <div class="statsarrow"></div>
        <div class="stats">
            <div class="vote">
                <div class="votes">
                    <span class="vote-count-post "><strong>6</strong></span>
                    <div class="viewcount">votes</div>
                </div>
            </div>
            <div class="status answered-accepted">
                <strong>4</strong>answers
            </div>
        </div>



<div class="views " title="88 views">
                    88 views
</div>
    </div>
    <div class="summary">
        <h3><a href="/questions/80365/capacitor-inrush-current" class="question-hyperlink">Capacitor Inrush Current</a></h3>
        <div class="excerpt">
            I have to filter a power control circuit and as usual I am using lots of capacitors in parallel. Some of these capacitors are Tantalum or Aluminium Polymer types, with ripple current ratings of 3 amps ...
        </div>

        <div class="tags t-capacitor t-inrush-current">
            <a href="/questions/tagged/capacitor" class="post-tag" title="show questions tagged 'capacitor'" rel="tag">capacitor</a> <a href="/questions/tagged/inrush-current" class="post-tag" title="show questions tagged 'inrush-current'" rel="tag">inrush-current</a>

        </div>
        <div class="started fr">


    <div class="user-info user-hover">
        <div class="user-action-time">


                    asked <span title="2013-08-27 18:04:39Z" class="relativetime">16 hours ago</span>
        </div>
        <div class="user-gravatar32">
            <a href="/users/15955/mfeinstein"><div class=""><img src="https://www.gravatar.com/avatar/86b9f964b2a1d7cc66a78a6199801f71?s=32&d=identicon&r=PG" alt="" width="32" height="32"></div></a>
        </div>
        <div class="user-details">
            <a href="/users/15955/mfeinstein">mFeinstein</a><br>
            <span class="reputation-score" title="reputation score" dir="ltr">1,006</span><span title="11 bronze badges"><span class="badge3"></span><span class="badgecount">11</span></span>
        </div>
    </div>

        </div>
    </div>
</div>

<div class="question-summary" id="question-summary-80360">
    <div class="statscontainer">
        <div class="statsarrow"></div>
        <div class="stats">
            <div class="vote">
                <div class="votes">
                    <span class="vote-count-post "><strong>0</strong></span>
                    <div class="viewcount">votes</div>
                </div>
            </div>
            <div class="status answered">
                <strong>1</strong>answer
            </div>
        </div>



<div class="views " title="28 views">
                    28 views
</div>
    </div>
    <div class="summary">
        <h3><a href="/questions/80360/designing-adc-driver-circuit-using-ltc6406" class="question-hyperlink">Designing ADC driver circuit using LTC6406</a></h3>
        <div class="excerpt">
            I am designing the front end(single ended to differential) for the ADC using LTC6406 to interface with the 20MSPS ADC. My input frequency is 140 MHz.
Simulation Sch is shown below:

L1, L2 and C1 are ...
        </div>

        <div class="tags t-circuit t-adc">
            <a href="/questions/tagged/circuit" class="post-tag" title="show questions tagged 'circuit'" rel="tag">circuit</a> <a href="/questions/tagged/adc" class="post-tag" title="show questions tagged 'adc'" rel="tag">adc</a>

        </div>
        <div class="started fr">


    <div class="user-info ">
        <div class="user-action-time">


                    asked <span title="2013-08-27 17:36:42Z" class="relativetime">17 hours ago</span>
        </div>
        <div class="user-gravatar32">
            <a href="/users/25017/anand-kumar-rai"><div class="gravatar-wrapper-32"><img src="http://i.stack.imgur.com/v6adE.jpg?s=32&g=1" alt=""></div></a>
        </div>
        <div class="user-details">
            <a href="/users/25017/anand-kumar-rai">Anand Kumar Rai</a><br>
            <span class="reputation-score" title="reputation score" dir="ltr">183</span><span title="1 silver badge"><span class="badge2"></span><span class="badgecount">1</span></span><span title="10 bronze badges"><span class="badge3"></span><span class="badgecount">10</span></span>
        </div>
    </div>

        </div>
    </div>
</div>
        </div>

    <br class="cbt">


    <div class="page-sizer fr">
            <a href="/questions?pagesize=15&amp;sort=newest" title="show 15 items per page" class="page-numbers current">15</a>
            <a href="/questions?pagesize=30&amp;sort=newest" title="show 30 items per page" class="page-numbers ">30</a>
            <a href="/questions?pagesize=50&amp;sort=newest" title="show 50 items per page" class="page-numbers ">50</a>
        <span class="page-numbers desc">per page</span>
    </div>
<div class="pager fl" >
<a href="/questions?page=1&amp;sort=newest" title="go to page 1" rel="prev"><span class="page-numbers prev">prev </span></a>
<a href="/questions?page=1&amp;sort=newest" title="go to page 1"><span class="page-numbers">1</span></a>
<span class="page-numbers current">2</span>
<a href="/questions?page=3&amp;sort=newest" title="go to page 3"><span class="page-numbers">3</span></a>
<a href="/questions?page=4&amp;sort=newest" title="go to page 4"><span class="page-numbers">4</span></a>
<a href="/questions?page=5&amp;sort=newest" title="go to page 5"><span class="page-numbers">5</span></a>
<span class="page-numbers dots">&hellip;</span>
<a href="/questions?page=1340&amp;sort=newest" title="go to page 1340"><span class="page-numbers">1340</span></a>
<a href="/questions?page=3&amp;sort=newest" title="go to page 3" rel="next"><span class="page-numbers next"> next</span></a>
</div>

</div>
<div id="sidebar">
    <div class="module" id="questions-count">
        <div class="summarycount al">20,098</div>
        <p>questions</p>
    </div>







    <div class="module" id="related-tags">
    <h4 id="h-related-tags">Related Tags</h4>

            <a href="/questions/tagged/arduino" class="post-tag" title="show questions tagged 'arduino'" rel="tag">arduino</a>&nbsp;<span class="item-multiplier"><span class="item-multiplier-x">&times;</span>&nbsp;<span class="item-multiplier-count">2030</span></span><br>
            <a href="/questions/tagged/microcontroller" class="post-tag" title="show questions tagged 'microcontroller'" rel="tag">microcontroller</a>&nbsp;<span class="item-multiplier"><span class="item-multiplier-x">&times;</span>&nbsp;<span class="item-multiplier-count">1432</span></span><br>
            <a href="/questions/tagged/power-supply" class="post-tag" title="show questions tagged 'power-supply'" rel="tag">power-supply</a>&nbsp;<span class="item-multiplier"><span class="item-multiplier-x">&times;</span>&nbsp;<span class="item-multiplier-count">899</span></span><br>
            <a href="/questions/tagged/led" class="post-tag" title="show questions tagged 'led'" rel="tag">led</a>&nbsp;<span class="item-multiplier"><span class="item-multiplier-x">&times;</span>&nbsp;<span class="item-multiplier-count">789</span></span><br>
            <a href="/questions/tagged/pic" class="post-tag" title="show questions tagged 'pic'" rel="tag">pic</a>&nbsp;<span class="item-multiplier"><span class="item-multiplier-x">&times;</span>&nbsp;<span class="item-multiplier-count">735</span></span><br>
            <a href="/questions/tagged/power" class="post-tag" title="show questions tagged 'power'" rel="tag">power</a>&nbsp;<span class="item-multiplier"><span class="item-multiplier-x">&times;</span>&nbsp;<span class="item-multiplier-count">730</span></span><br>
            <a href="/questions/tagged/voltage" class="post-tag" title="show questions tagged 'voltage'" rel="tag">voltage</a>&nbsp;<span class="item-multiplier"><span class="item-multiplier-x">&times;</span>&nbsp;<span class="item-multiplier-count">608</span></span><br>
            <a href="/questions/tagged/batteries" class="post-tag" title="show questions tagged 'batteries'" rel="tag">batteries</a>&nbsp;<span class="item-multiplier"><span class="item-multiplier-x">&times;</span>&nbsp;<span class="item-multiplier-count">593</span></span><br>
            <a href="/questions/tagged/transistors" class="post-tag" title="show questions tagged 'transistors'" rel="tag">transistors</a>&nbsp;<span class="item-multiplier"><span class="item-multiplier-x">&times;</span>&nbsp;<span class="item-multiplier-count">577</span></span><br>
            <a href="/questions/tagged/pcb" class="post-tag" title="show questions tagged 'pcb'" rel="tag">pcb</a>&nbsp;<span class="item-multiplier"><span class="item-multiplier-x">&times;</span>&nbsp;<span class="item-multiplier-count">570</span></span><br>
            <a href="/questions/tagged/capacitor" class="post-tag" title="show questions tagged 'capacitor'" rel="tag">capacitor</a>&nbsp;<span class="item-multiplier"><span class="item-multiplier-x">&times;</span>&nbsp;<span class="item-multiplier-count">564</span></span><br>
            <a href="/questions/tagged/usb" class="post-tag" title="show questions tagged 'usb'" rel="tag">usb</a>&nbsp;<span class="item-multiplier"><span class="item-multiplier-x">&times;</span>&nbsp;<span class="item-multiplier-count">538</span></span><br>
            <a href="/questions/tagged/digital-logic" class="post-tag" title="show questions tagged 'digital-logic'" rel="tag">digital-logic</a>&nbsp;<span class="item-multiplier"><span class="item-multiplier-x">&times;</span>&nbsp;<span class="item-multiplier-count">522</span></span><br>
            <a href="/questions/tagged/sensor" class="post-tag" title="show questions tagged 'sensor'" rel="tag">sensor</a>&nbsp;<span class="item-multiplier"><span class="item-multiplier-x">&times;</span>&nbsp;<span class="item-multiplier-count">500</span></span><br>
            <a href="/questions/tagged/avr" class="post-tag" title="show questions tagged 'avr'" rel="tag">avr</a>&nbsp;<span class="item-multiplier"><span class="item-multiplier-x">&times;</span>&nbsp;<span class="item-multiplier-count">493</span></span><br>
            <a href="/questions/tagged/op-amp" class="post-tag" title="show questions tagged 'op-amp'" rel="tag">op-amp</a>&nbsp;<span class="item-multiplier"><span class="item-multiplier-x">&times;</span>&nbsp;<span class="item-multiplier-count">447</span></span><br>
            <a href="/questions/tagged/current" class="post-tag" title="show questions tagged 'current'" rel="tag">current</a>&nbsp;<span class="item-multiplier"><span class="item-multiplier-x">&times;</span>&nbsp;<span class="item-multiplier-count">436</span></span><br>
            <a href="/questions/tagged/fpga" class="post-tag" title="show questions tagged 'fpga'" rel="tag">fpga</a>&nbsp;<span class="item-multiplier"><span class="item-multiplier-x">&times;</span>&nbsp;<span class="item-multiplier-count">431</span></span><br>
            <a href="/questions/tagged/circuit" class="post-tag" title="show questions tagged 'circuit'" rel="tag">circuit</a>&nbsp;<span class="item-multiplier"><span class="item-multiplier-x">&times;</span>&nbsp;<span class="item-multiplier-count">423</span></span><br>
            <a href="/questions/tagged/resistors" class="post-tag" title="show questions tagged 'resistors'" rel="tag">resistors</a>&nbsp;<span class="item-multiplier"><span class="item-multiplier-x">&times;</span>&nbsp;<span class="item-multiplier-count">394</span></span><br>
            <a href="/questions/tagged/audio" class="post-tag" title="show questions tagged 'audio'" rel="tag">audio</a>&nbsp;<span class="item-multiplier"><span class="item-multiplier-x">&times;</span>&nbsp;<span class="item-multiplier-count">394</span></span><br>
            <a href="/questions/tagged/motor" class="post-tag" title="show questions tagged 'motor'" rel="tag">motor</a>&nbsp;<span class="item-multiplier"><span class="item-multiplier-x">&times;</span>&nbsp;<span class="item-multiplier-count">384</span></span><br>
            <a href="/questions/tagged/voltage-regulator" class="post-tag" title="show questions tagged 'voltage-regulator'" rel="tag">voltage-regulator</a>&nbsp;<span class="item-multiplier"><span class="item-multiplier-x">&times;</span>&nbsp;<span class="item-multiplier-count">377</span></span><br>
            <a href="/questions/tagged/mosfet" class="post-tag" title="show questions tagged 'mosfet'" rel="tag">mosfet</a>&nbsp;<span class="item-multiplier"><span class="item-multiplier-x">&times;</span>&nbsp;<span class="item-multiplier-count">374</span></span><br>
            <a href="/questions/tagged/switches" class="post-tag" title="show questions tagged 'switches'" rel="tag">switches</a>&nbsp;<span class="item-multiplier"><span class="item-multiplier-x">&times;</span>&nbsp;<span class="item-multiplier-count">344</span></span><br>
    </div>
</div>

        </div>
    </div>
    <div id="footer" class="categories">
        <div class="footerwrap">
            <div id="footer-menu">
                <div class="top-footer-links">
                        <a href="/about">about</a>
                    <a href="/help">help</a>
                        <a href="/help/badges">badges</a>
                    <a href="http://blog.stackexchange.com?blb=1">blog</a>
                        <a href="http://chat.stackexchange.com">chat</a>
                    <a href="http://data.stackexchange.com">data</a>
                    <a href="http://stackexchange.com/legal">legal</a>
                    <a href="http://stackexchange.com/legal/privacy-policy">privacy policy</a>
                    <a href="http://stackexchange.com/about/hiring">jobs</a>
                    <a href="http://stackexchange.com/about/contact">advertising info</a>

                    <a onclick='StackExchange.switchMobile("on", "/questions?page=2&amp;sort=newest")'>mobile</a>
                    <b><a href="/contact">contact us</a></b>
                        <b><a href="http://meta.electronics.stackexchange.com">feedback</a></b>

                </div>
                <div id="footer-sites">
                    <table>
    <tr>
            <th colspan=3>
                Technology
            </th>
            <th >
                Life / Arts
            </th>
            <th >
                Culture / Recreation
            </th>
            <th >
                Science
            </th>
            <th >
                Other
            </th>
    </tr>
    <tr>
            <td>
                <ol>
                        <li><a href="http://stackoverflow.com" title="professional and enthusiast programmers">Stack Overflow</a></li>
                        <li><a href="http://serverfault.com" title="professional system and network administrators">Server Fault</a></li>
                        <li><a href="http://superuser.com" title="computer enthusiasts and power users">Super User</a></li>
                        <li><a href="http://webapps.stackexchange.com" title="power users of web applications">Web Applications</a></li>
                        <li><a href="http://askubuntu.com" title="Ubuntu users and developers">Ask Ubuntu</a></li>
                        <li><a href="http://webmasters.stackexchange.com" title="pro webmasters">Webmasters</a></li>
                        <li><a href="http://gamedev.stackexchange.com" title="professional and independent game developers">Game Development</a></li>
                        <li><a href="http://tex.stackexchange.com" title="users of TeX, LaTeX, ConTeXt, and related typesetting systems">TeX - LaTeX</a></li>
                            </ol></td><td><ol>
                        <li><a href="http://programmers.stackexchange.com" title="professional programmers interested in conceptual questions about software development">Programmers</a></li>
                        <li><a href="http://unix.stackexchange.com" title="users of Linux, FreeBSD and other Un*x-like operating systems.">Unix &amp; Linux</a></li>
                        <li><a href="http://apple.stackexchange.com" title="power users of Apple hardware and software">Ask Different (Apple)</a></li>
                        <li><a href="http://wordpress.stackexchange.com" title="WordPress developers and administrators">WordPress Answers</a></li>
                        <li><a href="http://gis.stackexchange.com" title="cartographers, geographers and GIS professionals">Geographic Information Systems</a></li>
                        <li><a href="http://electronics.stackexchange.com" title="electronics and electrical engineering professionals, students, and enthusiasts">Electrical Engineering</a></li>
                        <li><a href="http://android.stackexchange.com" title="enthusiasts and power users of the Android operating system">Android Enthusiasts</a></li>
                        <li><a href="http://security.stackexchange.com" title="IT security professionals">IT Security</a></li>
                            </ol></td><td><ol>
                        <li><a href="http://dba.stackexchange.com" title="database professionals who wish to improve their database skills and learn from others in the community">Database Administrators</a></li>
                        <li><a href="http://drupal.stackexchange.com" title="Drupal developers and administrators">Drupal Answers</a></li>
                        <li><a href="http://sharepoint.stackexchange.com" title="SharePoint enthusiasts">SharePoint</a></li>
                        <li><a href="http://ux.stackexchange.com" title="user experience researchers and experts">User Experience</a></li>
                        <li><a href="http://mathematica.stackexchange.com" title="users of Mathematica">Mathematica</a></li>

                        <li>
                            <a href="http://stackexchange.com/sites#technology" class="more">
                                more (13)
                            </a>
                        </li>
                </ol>
            </td>
            <td>
                <ol>
                        <li><a href="http://photo.stackexchange.com" title="professional, enthusiast and amateur photographers">Photography</a></li>
                        <li><a href="http://scifi.stackexchange.com" title="science fiction and fantasy enthusiasts">Science Fiction &amp; Fantasy</a></li>
                        <li><a href="http://cooking.stackexchange.com" title="professional and amateur chefs">Seasoned Advice (cooking)</a></li>
                        <li><a href="http://diy.stackexchange.com" title="contractors and serious DIYers">Home Improvement</a></li>

                        <li>
                            <a href="http://stackexchange.com/sites#lifearts" class="more">
                                more (13)
                            </a>
                        </li>
                </ol>
            </td>
            <td>
                <ol>
                        <li><a href="http://english.stackexchange.com" title="linguists, etymologists, and serious English language enthusiasts">English Language &amp; Usage</a></li>
                        <li><a href="http://skeptics.stackexchange.com" title="scientific skepticism">Skeptics</a></li>
                        <li><a href="http://judaism.stackexchange.com" title="those who base their lives on Jewish law and tradition and anyone interested in learning more">Mi Yodeya (Judaism)</a></li>
                        <li><a href="http://travel.stackexchange.com" title="road warriors and seasoned travelers">Travel</a></li>
                        <li><a href="http://christianity.stackexchange.com" title="committed Christians, experts in Christianity and those interested in learning more">Christianity</a></li>
                        <li><a href="http://gaming.stackexchange.com" title="passionate videogamers on all platforms">Arqade (gaming)</a></li>
                        <li><a href="http://bicycles.stackexchange.com" title="people who build and repair bicycles, people who train cycling, or commute on bicycles">Bicycles</a></li>
                        <li><a href="http://rpg.stackexchange.com" title="gamemasters and players of tabletop, paper-and-pencil role-playing games">Role-playing Games</a></li>

                        <li>
                            <a href="http://stackexchange.com/sites#culturerecreation" class="more">
                                more (21)
                            </a>
                        </li>
                </ol>
            </td>
            <td>
                <ol>
                        <li><a href="http://math.stackexchange.com" title="people studying math at any level and professionals in related fields">Mathematics</a></li>
                        <li><a href="http://stats.stackexchange.com" title="statisticians, data analysts, data miners and data visualization experts">Cross Validated (stats)</a></li>
                        <li><a href="http://cstheory.stackexchange.com" title="theoretical computer scientists and researchers in related fields">Theoretical Computer Science</a></li>
                        <li><a href="http://physics.stackexchange.com" title="active researchers, academics and students of physics">Physics</a></li>
                        <li><a href="http://mathoverflow.net" title="professional mathematicians">MathOverflow</a></li>

                        <li>
                            <a href="http://stackexchange.com/sites#science" class="more">
                                more (7)
                            </a>
                        </li>
                </ol>
            </td>
            <td>
                <ol>
                        <li><a href="http://stackapps.com" title="apps, scripts, and development with the Stack Exchange API">Stack Apps</a></li>
                        <li><a href="http://meta.stackoverflow.com" title="meta-discussion of the Stack Exchange family of Q&amp;A websites">Meta Stack Overflow</a></li>
                        <li><a href="http://area51.stackexchange.com" title="proposing new sites in the Stack Exchange network">Area 51</a></li>
                        <li><a href="http://careers.stackoverflow.com">Stack Overflow Careers</a></li>

                </ol>
            </td>
    </tr>
</table>
                </div>
            </div>

            <div id="copyright">
                site design / logo &copy; 2013 stack exchange inc;
                user contributions licensed under <a href="http://creativecommons.org/licenses/by-sa/3.0/" rel="license">cc-wiki</a>
                with <a href="http://blog.stackoverflow.com/2009/06/attribution-required/" rel="license">attribution required</a>
            </div>
            <div id="footer-flair">
                <a href="http://creativecommons.org/licenses/by-sa/3.0/" class="cc-wiki-link"></a>
            </div>
            <div id="svnrev">
                rev 2013.8.28.977
            </div>

        </div>
    </div>
    <noscript>
        <div id="noscript-warning">Electrical Engineering Stack Exchange works best with JavaScript enabled<img src="http://pixel.quantserve.com/pixel/p-c1rF4kxgLUzNc.gif" alt="" class="dno"></div>
    </noscript>

    <script type="text/javascript">var _gaq=_gaq||[];_gaq.push(['_setAccount','UA-5620270-24']);
        _gaq.push(['_setDomainName','.stackexchange.com']);
_gaq.push(['_trackPageview']);
    var _qevents = _qevents || [];
    (function () {
        var ssl='https:'==document.location.protocol,
            s=document.getElementsByTagName('script')[0],
            ga=document.createElement('script');
        ga.type='text/javascript';
        ga.async=true;
        ga.src=(ssl?'https://ssl':'http://www')+'.google-analytics.com/ga.js';
        s.parentNode.insertBefore(ga,s);
        var sc=document.createElement('script');
        sc.type='text/javascript';
        sc.async=true;
        sc.src=(ssl?'https://secure':'http://edge')+'.quantserve.com/quant.js';
        s.parentNode.insertBefore(sc,s);
    })();
    _qevents.push({ qacct: "p-c1rF4kxgLUzNc" });
    </script>

</body>
</html>
"""]

pattern_id = r'(?:(?<=question-summary-)).*?(?:(?="))'
pattern_question = r'(?:(?<=>))([^<>]*[^<>]*)(?:(?=<\/a><\/h3))'
pattern_time = r'(?:(?<="relativetime">))([^<>]*[^<>]*)(?:(?=<\/span))'
for html in stackoverflow:
    ids = re.findall(pattern_id, html)
    questions = re.findall(pattern_question, html)
    times = re.findall(pattern_time, html)
    for i in range(len(ids)):
        print(";".join((ids[i].strip(), questions[i].strip(), times[i].strip())))